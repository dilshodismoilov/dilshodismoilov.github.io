<?php
require_once '../config.php'; // Include config.php for database connection and BASE_URL
header('Content-Type: application/json');

// Check for required parameters
if (!isset($_GET['station_id'], $_GET['date'], $_GET['transport_type'])) {
    echo json_encode(['success' => false, 'message' => 'Station ID, date are required.']);
    exit;
}

$apikey = '95904d7f-9dba-4bba-bcb1-f80544f60f65';
$station_id = $_GET['station_id'];
$date = $_GET['date'];
$transport_type = $_GET['transport_type'];
$yandex_base_url = 'https://api.rasp.yandex.net/v3.0/';
try {
    $stmt = $pdo->prepare("SELECT number, departure_time, arrival_time FROM train_schedule WHERE station_id = ? AND date = ?");
    $stmt->execute([$station_id, $date]);
    $existingData = $stmt->fetchAll(PDO::FETCH_ASSOC);
    
    $numbers = [];
    //var_dump($existingData);die();
    foreach($existingData as $number) {
        $numbers[$number["number"]] = ["departure_time"=>$number["departure_time"], "arrival_time"=>$number["arrival_time"]];
    }

    //var_dump($numbers); 

    $stmt = $pdo->prepare("SELECT * FROM carrier");
    $stmt->execute();
    $carriers = $stmt->fetchAll(PDO::FETCH_ASSOC);

    $schedule_url = "{$yandex_base_url}schedule/?apikey={$apikey}&station={$station_id}&date={$date}&show_systems=all&transport_types={$transport_type}";

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $schedule_url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $response = curl_exec($ch);
    curl_close($ch);
    //var_dump($response);die();
    $schedule_data = json_decode($response, true);
    //var_dump($schedule_data); die();
    if (!isset($schedule_data['schedule']) || empty($schedule_data['schedule'])) {
        echo json_encode(['success' => false, 'message' => 'No data found for the specified station and date.']);
        exit;
    }
    //var_dump($schedule_data); die();
    //var_dump(($existingData)); die();
  
    foreach ($schedule_data['schedule'] as $train) {
        $uid = $train["thread"]["uid"];
        $carrier_code = $train["thread"]["carrier"]["code"];
        $carrier_title = $train["thread"]["carrier"]["title"];
        $number = $train["thread"]["number"];
        $transport_type = $train["thread"]["transport_type"];
        $transport_subtype = $train["thread"]["transport_subtype"]["title"];
        $carrier_title = $train["thread"]["carrier"]["title"];
        $carrier_code = $train["thread"]["carrier"]["code"];

        $departure_time = $train["departure"];
        $arrival_time = $train["arrival"];
        
        $check = $number;
        if(is_numeric($number)) {
            $check = (int) $number;
        }
        //var_dump($check); 
        if(array_key_exists($check, $numbers)) {
            //echo "hi";
            if($numbers[$check]["departure_time"] == $departure_time && $numbers[$check]["arrival_time"] == $arrival_time) {
                continue;
            }
        }
        //die();
        if ($uid) {
            $thread = getThread($uid);
            
            $duration;
            $thread_start;
            $thread_end;
            if(count($thread) == 0) {
                $search_url = "{$yandex_base_url}thread/?apikey={$apikey}&uid={$uid}&date={$date}";
                $ch = curl_init();
                curl_setopt($ch, CURLOPT_URL, $search_url);
                curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
                $search_response = curl_exec($ch);
                curl_close($ch);

                $search_data = json_decode($search_response, true);
            
                $duration = "N/A";
                $i = 1;
                while(array_key_exists("error", $search_data)) {
                    $temp_date = new DateTime($date);
                    $temp_date->modify("-{$i} day");
                    $search_url = "{$yandex_base_url}thread/?apikey={$apikey}&uid={$uid}&date={$temp_date->format('Y-m-d')}";
                    $ch = curl_init();
                    curl_setopt($ch, CURLOPT_URL, $search_url);
                    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
                    $search_response = curl_exec($ch);
                    curl_close($ch);
                    $i++;
                    $search_data = json_decode($search_response, true);
                }
                //var_dump($search_data); die();
                $duration = gmdate(end($search_data["stops"])["duration"]);
                $thread_start = $search_data["stops"][0]["station"]["title"];
                $thread_end = end($search_data["stops"])["station"]["title"];

                $stmt = $pdo->prepare("INSERT INTO threads (uid, start, end, duration) VALUES (?, ?, ?, ?)");
                $stmt->execute([$uid, $thread_start, $thread_end, $duration]);

            } else {
                $duration = $thread[0]["duration"];
                $thread_start = $thread[0]["start"];
                $thread_end = $thread[0]["end"];
            }
                            
            $carrier = getCarrier($carrier_code);
            if(count($carrier) == 0) {
                
                    $carrier_url = "{$yandex_base_url}carrier/?apikey={$apikey}&code={$carrier_code}";
                    $ch = curl_init();
                    curl_setopt($ch, CURLOPT_URL, $carrier_url);
                    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
                    $carrier_response = curl_exec($ch);
                    curl_close($ch);
                    $carrier_data = json_decode($carrier_response, true);
                    $carrier_logo = $carrier_data["carrier"]["logo"];
                    
                    $stmt = $pdo->prepare("INSERT INTO carrier (code, title, logo) VALUES (?, ?, ?)");
                    $stmt->execute([$carrier_code, $carrier_title, $carrier_data["carrier"]["logo"]]);
                
            } else {
                $carrier_logo = $carrier[0]["logo"];
            }
            
                       
            // Insert into the database
            
            //echo "threads done";
            //var_dump(); die();
            // "carrier done";
            $stmt = $pdo->prepare("
                INSERT INTO train_schedule 
                (uid, carrier_code, number, station_id, departure_time, arrival_time, date, transport_type, transport_subtype) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ");
            
            $stmt->execute([
                $uid,
                $carrier_code,
                $number,
                $station_id,
                $departure_time,
                $arrival_time,
                $date,
                $transport_type,
                $transport_subtype
            ]);
            //echo "train_schedule done";
        }
    
    }
    // Step 4: Return the saved schedule
    $stmt = $pdo->prepare("SELECT * FROM train_schedule WHERE station_id = ? AND date = ?");
    $stmt->execute([$station_id, $date]);
    $savedData = $stmt->fetchAll(PDO::FETCH_ASSOC);
    
    echo json_encode(['success' => true, 'schedule' => $savedData]);
    } catch (Exception $e) {
    echo json_encode(['success' => false, 'message' => 'Error: ' . $e->getMessage()]);
}

function getThread($uid) {
    global $pdo;
    $stmt = $pdo->prepare("SELECT * FROM threads WHERE uid = :uid");
    $stmt->bindParam(":uid", $uid);
    $stmt->execute();
    $threads = $stmt->fetchAll(PDO::FETCH_ASSOC);
    return $threads;
}

function getCarrier($code) {
    global $pdo;
    $stmt = $pdo->prepare("SELECT * FROM carrier WHERE code = :code");
    $stmt->bindParam(":code", $code);
    $stmt->execute();
    $carriers = $stmt->fetchAll(PDO::FETCH_ASSOC);
    return $carriers;
}