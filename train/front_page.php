<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Расписание поездов</title>
    <link rel="stylesheet" href="<?= BASE_URL ?>css/styles.css">
    <script>
        const BASE_URL = '<?php echo BASE_URL; ?>';
    </script>
    <script src="<?= BASE_URL ?>js/scripts.js" defer></script>
</head>
<body>
    <div class="main-container">
        <header class="header">
            <div class="header-content">
                <h1>Расписание поездов</h1>
                <!-- Search Bar -->
                <form id="station-search-form" class="search-bar">
                    <input type="text" id="station-search" name="station" placeholder="Поиск станции..." autocomplete="off">
                    <div id="autocomplete-results"></div>
                </form>
            </div>
        </header>

        <main>
            <section class="station-list-section">
                <h2>Станции</h2>
                <div class="alphabetical-station-list">
                    <?php
                    require_once 'config.php';
                    $db = new PDO('mysql:host=127.0.0.1;dbname=train_schedule', 'root', '');

                    // Fetch stations and group them by the first letter
                    $result = $db->query('SELECT name, code FROM stations WHERE priority > 1 ORDER BY name ASC');
                    $stations = [];
                    while ($row = $result->fetch(PDO::FETCH_ASSOC)) {
                        $firstLetter = mb_substr($row['name'], 0, 1, 'UTF-8');
                        $stations[$firstLetter][] = [
                            'name' => $row['name'],
                            'code' => $row['code']
                        ];
                    }

                    // Render stations grouped by letters
                    foreach ($stations as $letter => $stationGroup) {
                        echo "<div class='letter-group'>";
                        echo "<h3 class='letter-heading'>{$letter}</h3>";
                        echo "<ul class='station-list'>";
                        foreach ($stationGroup as $station) {
                            echo '<li><a href="'.BASE_URL.'stations/' . htmlspecialchars($station['code']) . '">' . htmlspecialchars($station['name']) . '</a></li>';
                        }
                        echo "</ul>";
                        echo "</div>";
                    }
                    ?>
                </div>
            </section>
        </main>

        <footer class="footer">
            <p>&copy; <?= date('Y') ?> Train Schedule. All Rights Reserved.</p>
        </footer>
    </div>
</body>
</html>
