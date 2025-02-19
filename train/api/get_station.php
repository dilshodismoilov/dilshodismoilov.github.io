<?php
require_once '../config.php'; // Include config.php for $pdo and BASE_URL

header('Content-Type: application/json');

if (isset($_GET['station_id'])) {
    $station_id = $_GET['station_id'];

    try {
        // Increment the priority for the clicked station
        // $incrementStmt = $pdo->prepare('UPDATE stations SET priority = priority + 1 WHERE code = :station_id');
        // $incrementStmt->bindParam(':station_id', $station_id);
        // $incrementStmt->execute();

        // Query the station details after incrementing priority
        $stmt = $pdo->prepare('SELECT * FROM stations WHERE code = :station_id');
        $stmt->bindParam(':station_id', $station_id);
        $stmt->execute();
        $station = $stmt->fetch(PDO::FETCH_ASSOC);

        if ($station) {
            echo json_encode([
                'success' => true,
                'station' => $station,
            ]);
        } else {
            echo json_encode([
                'success' => false,
                'message' => 'Station not found.',
            ]);
        }
    } catch (PDOException $e) {
        echo json_encode([
            'success' => false,
            'message' => 'Database error: ' . $e->getMessage(),
        ]);
    }
} else {
    echo json_encode([
        'success' => false,
        'message' => 'Invalid request. Station ID is required.',
    ]);
}
