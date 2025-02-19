<?php
require_once '../config.php';

header('Content-Type: application/json');

$query = $_GET['query'] ?? '';
if (!$query) {
    echo json_encode(['status' => 'error', 'message' => 'No query provided']);
    exit;
}
$query = '%' . $query . '%';
//var_dump($query);die();
$stmt = $pdo->prepare("SELECT name, code FROM stations WHERE name LIKE '{$query}' ORDER BY `priority` DESC LIMIT 20");
//$stmt->bindValue(':query', '%' . $query . '%', PDO::PARAM_STR);
$stmt->execute();

$results = $stmt->fetchAll(PDO::FETCH_ASSOC);
echo json_encode(['status' => 'success', 'results' => $results]);
?>
