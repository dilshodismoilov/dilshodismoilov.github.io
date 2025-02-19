<?php
require_once 'config.php';

$requestUri = $_SERVER['REQUEST_URI'];
$requestPath = parse_url($requestUri, PHP_URL_PATH);

$basePath = dirname($_SERVER['SCRIPT_NAME']);
$requestPath = str_replace($basePath, '', $requestPath);

//$requestPath = trim($requestPath, '/');

// echo '<pre>';
// echo "Request URI: " . htmlspecialchars($requestUri) . "\n";
// echo "Base Path: " . htmlspecialchars($basePath) . "\n";
// echo "Request Path: " . htmlspecialchars($requestPath) . "\n";
// echo '</pre>';

// Routing logic
if ($requestPath === '/' || $requestPath === '/index.php') {
    require 'front_page.php';
} elseif (preg_match('/^\/stations\/([0-9a-zA-Z_-]+)$/', $requestPath, $matches)) {
    $stationCode = $matches[1]; // Extract the station ID
    require 'station.php';
} else {
    http_response_code(404);
    echo '<h1>404 Not Found</h1>';
}
?>
