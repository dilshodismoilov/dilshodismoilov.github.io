<?php
$webhookUrl = "https://b24-u8i9wx.bitrix24.ru/rest/1/0oqwm1oftg1fmgf3/";

// Функция для выполнения запроса к Битрикс24 API
function callBitrix24API($method, $params = array())
{
    global $webhookUrl;
    $url = $webhookUrl . $method;
    $curl = curl_init();
    curl_setopt($curl, CURLOPT_URL, $url);
    curl_setopt($curl, CURLOPT_POST, true);
    curl_setopt($curl, CURLOPT_POSTFIELDS, http_build_query($params));
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
    $response = curl_exec($curl);
    curl_close($curl);
    return json_decode($response, true);
}

// 1. Узнать количество контактов с заполненным полем COMMENTS
$contacts = callBitrix24API('crm.contact.list');
$contactWithCommentsCount = 0;
foreach ($contacts['result'] as $contact) {
    if (!empty($contact['COMMENTS'])) {
        $contactWithCommentsCount++;
    }
}

// 2. Найти все сделки без контактов
$deals = callBitrix24API('crm.deal.list');
$dealsWithoutContacts = [];
foreach ($deals['result'] as $deal) {
    if (empty($deal['CONTACT_ID'])) {
        $dealsWithoutContacts[] = $deal;
    }
}

// 3. Узнать сколько сделок в каждой из существующих Направлений
$dealDirections = [];
foreach ($deals['result'] as $deal) {
    $direction = $deal['CATEGORY_ID'];
    if (!isset($dealDirections[$direction])) {
        $dealDirections[$direction] = 0;
    }
    $dealDirections[$direction]++;
}

// 4. Посчитать сумму значений поля "Баллы" из всех существующих элементов Смарт процесса
$smartProcessElements = callBitrix24API('crm.item.list', ['entityTypeId' => 1038]);
$fieldPointsCode = null;

// Узнать код поля "Баллы"
$fields = callBitrix24API('crm.item.fields', ['entityTypeId' => 1038]);
foreach ($fields['result'] as $code => $field) {
    if ($field['title'] == 'Баллы') {
        $fieldPointsCode = $code;
        break;
    }
}

$pointsSum = 0;
if ($fieldPointsCode) {
    foreach ($smartProcessElements['result'] as $element) {
        if (!empty($element[$fieldPointsCode])) {
            $pointsSum += $element[$fieldPointsCode];
        }
    }
}

// Результаты
echo "Количество контактов с заполненным полем COMMENTS: $contactWithCommentsCount\n";
echo "Сделки без контактов: " . count($dealsWithoutContacts) . "\n";
echo "Направления сделок:\n";
foreach ($dealDirections as $direction => $count) {
    echo " - Направление $direction: $count сделок\n";
}
echo "Сумма значений поля 'Баллы' в Смарт процессе: $pointsSum\n";

// Скриншот результата
file_put_contents('results.txt', ob_get_contents());
