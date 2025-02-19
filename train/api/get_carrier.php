<?php
require_once '../config.php'; // Include config.php for $pdo and BASE_URL

header('Content-Type: application/json');

if (isset($_GET['code'])) {
    $code = $_GET['code'];

    try {
       
        // Query the station details after incrementing priority
        $stmt = $pdo->prepare("SELECT * FROM carrier WHERE code = :code");
        $stmt->bindParam(":code", $code);
        $stmt->execute();
        $carriers = $stmt->fetchAll(PDO::FETCH_ASSOC);

        if ($carriers[0]) {
            echo json_encode([
                'success' => true,
                'carrier' => $carriers[0],
            ]);
        } else {
            echo json_encode([
                'success' => false,
                'message' => 'Carrier not found.',
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
        'message' => 'Invalid request. code is required.',
    ]);
}
