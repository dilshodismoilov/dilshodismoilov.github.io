<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Station Schedule</title>
    <link rel="stylesheet" href="<?= BASE_URL ?>css/station_style.css">
    <script>
        const BASE_URL = '<?php echo BASE_URL; ?>';
    </script>
    
</head>
<body>

<header>
    <div class="header-content">
        <h1 id="station-name">Station Name</h1>
        <a href="<?= BASE_URL ?>" class="back-home">← На главную</a>
    </div>
</header>


    <form id="station-search-form">
                <input type="text" id="station-search" name="station" placeholder="Поиск станции..." autocomplete="off">
                <div id="autocomplete-results"></div>
    </form>

        <!-- Filters -->
    <section id="filters" class="filters">
        <div class="filter-item">
            <label for="transport_type">Тип транспорта:</label>
            <select id="transport_type">
                <option value="train">Поезд</option>
                <option value="suburban">Электричка</option>
            </select>
        </div>

        <div class="filter-item">
            <label for="event_type">Событие:</label>
            <select id="event_type">
                <option value="departure">Отправление</option>
                <option value="arrival">Прибытие</option>
            </select>
        </div>

        <div class="filter-item">
            <label for="date_picker">Дата:</label>
            <input type="date" id="date_picker" value="<?= date('Y-m-d') ?>">
        </div>

        <div class="checkbox-container">
            <input type="checkbox" id="hide_left">
            <label for="hide_left" id="label_hide_left">Скрыть ушедшие</label>
        </div>
    </section>


    <!-- Schedule -->
    <div id="loading-indicator" class="loading-indicator"></div>
    <section id="schedule" class="schedule">
        <p>Loading schedule...</p>
    </section>

    <footer class="yandex-copyright">
    <iframe frameborder="0" style="overflow: hidden; border: 0; width: 740px; height: 51px;" src="//yandex.st/rasp/media/apicc/copyright_horiz_mono.html"></iframe> 
    </footer>

    <script src="<?= BASE_URL ?>js/station.js"></script>
</body>
</html>
