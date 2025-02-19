<?php
require_once '../config.php'; // Include config.php for $pdo and BASE_URL

header('Content-Type: application/json');

if (isset($_GET['uid'])) {
    $uid = $_GET['uid'];

    try {
       
        // Query the station details after incrementing priority
        $stmt = $pdo->prepare("SELECT * FROM threads WHERE uid = :uid");
        $stmt->bindParam(":uid", $uid);
        $stmt->execute();
        $threads = $stmt->fetchAll(PDO::FETCH_ASSOC);

        if ($threads[0]) {
            echo json_encode([
                'success' => true,
                'thread' => $threads[0],
            ]);
        } else {
            echo json_encode([
                'success' => false,
                'message' => 'Thread not found.',
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
        'message' => 'Invalid request. uid is required.',
    ]);
}
