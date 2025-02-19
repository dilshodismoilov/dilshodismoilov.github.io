<?php
// Dynamic base URL based on the server
$base_url = 'http://' . $_SERVER['SERVER_NAME'] . dirname($_SERVER['SCRIPT_NAME']) . '/';
define('BASE_URL', $base_url);

// Database connection (update credentials as needed)
try {
    $pdo = new PDO('mysql:host=127.0.0.1;dbname=train_schedule', 'root', '');
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die('Database connection failed: ' . $e->getMessage());
}
?>
