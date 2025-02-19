<?php
require_once '../config.php';

$stationId = $_GET['station_id'] ?? '';
$transportType = $_GET['transport_type'] ?? 'all';
$event = $_GET['event'] ?? 'departure';
$date = $_GET['date'] ?? date('Y-m-d');
$hideLeft = isset($_GET['hide_left']) && $_GET['hide_left'] == '1';

// Fetch schedule from database or external API
$stmt = $pdo->prepare("
    SELECT * FROM schedule
    WHERE station_id = :station_id
    AND (transport_type = :transport_type OR :transport_type = 'all')
    AND event = :event
    AND DATE(event_time) = :date
    AND (:hide_left = 0 OR event_time >= NOW())
");
$stmt->execute([
    'station_id' => $stationId,
    'transport_type' => $transportType,
    'event' => $event,
    'date' => $date,
    'hide_left' => $hideLeft ? 1 : 0,
]);

echo json_encode($stmt->fetchAll(PDO::FETCH_ASSOC));
