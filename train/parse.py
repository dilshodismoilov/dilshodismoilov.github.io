import requests
url = "https://api.rasp.yandex.net/v3.0/stations_list/?apikey=95904d7f-9dba-4bba-bcb1-f80544f60f65&lang=ru_RU&format=json"
response = requests.get(url, stream=True)

if response.ok:
    with open("./data.txt", "wb") as fd:
        for chunk in response.iter_content(chunk_size=128):
            fd.write(chunk)
else:
    response.raise_for_status()


# from bs4 import BeautifulSoup

# html = '''

# <!doctype html>
# <html>

# <head>
# 	    		<script src="https://ux.tutu.ru/preloader.js?page_name=train_vkz_list" async></script>
# 	<title>Все вокзалы России</title>
# 			<meta name="keywords" content=""/>
# 		<meta name="description" content="Вокзалы России&nbsp;&mdash; в&nbsp;данном разделе вы&nbsp;можете ознакомиться со&nbsp;списком всех вокзалов страны, найти адреса, телефоны, и&nbsp;много другой полезной информации о&nbsp;них."/>
# 	<link rel="apple-touch-icon" sizes="180x180" href="https://cdn1.tu-tu.ru/images2/icons/2023/apple-touch-icon.png">
# 	<link rel="icon" sizes="32x32" href="https://cdn1.tu-tu.ru/images2/icons/2023/favicon.ico">
# 	<link rel="icon" type="image/svg+xml" sizes="any" href="https://cdn1.tu-tu.ru/images2/icons/2023/favicon.svg">

# 	<link rel="manifest" href="https://cdn1.tu-tu.ru/images2/icons/2023/site.webmanifest">
# 	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

	
# 	<noscript><meta http-equiv="refresh" content="0;url=/browser_upgrade/" /></noscript>
# <!--[if lt IE 12]>
# <meta http-equiv="refresh" content="0;url=/browser_upgrade/">
# <![endif]-->
# <script>
# 	if (/MSIE 10|Trident.*rv\:10/.test(navigator.userAgent)) {
# 		window.location.href='/browser_upgrade/';
# 	}
# </script>


# 					<style>
			
# /* File not exists css2/bld/app/train/commons.css! */

# 		</style>
	
# 	<meta name='yandex-verification' content='4494b25130e542f2' />
	

    		

	
# 		<script src="https://cdn1.tu-tu.ru/js4/vendors/raven/3.27.0/raven.min.js" crossorigin="anonymous"></script>
# 		<script>
# 			(function () {
# 				var whitelist = [
# 	"^https?:\/\/.*\.tu-?tu\.ru\/.*$",
# 	"^https?:\/\/.*\.tutu\.travel\/.*$",
# 	"^https?:\/\/.*\.tutu\.pro\/.*$"
# ];
# 				Raven.setTagsContext({
# 					project: 'train',
# 					page: 'vokzal_list'
# 				});
# 				Raven.config('https://8f1da44971f64b64b738cf67dd39081a@sentry.tutu.ru/54', {
# 					whitelistUrls: whitelist.map(function(item){return new RegExp(item)}),
# 					transport: function(options) {
# 						var request = new XMLHttpRequest();
# 						request.onreadystatechange = function (e) {
# 							if (request.readyState !== 4) {
# 								return;
# 							}

# 							if (request.status === 200) {
# 								if (options.onSuccess) {
# 									options.onSuccess();
# 								}
# 							} else {
# 								if (options.onError) {
# 									options.onError();
# 								}
# 							}
# 						};

# 						request.open('POST', 'https://fronterr.tutu.ru/api/v1/errors');
# 						request.setRequestHeader('Content-Type', 'application/json');
# 						request.setRequestHeader('Access-Control-Allow-Origin', '*');
# 						request.send(JSON.stringify(options));
# 					}
# 				}).install();
# 			})();
# 		</script>

	
	
# 	<script>var RM = RM || {}; RM.StaticData = RM.StaticData || {}; RM.StaticData["debug"] = {"levels":{"ERROR":0,"WARNING":1,"INFO":2},"level":0};var RM = RM || {}; RM.StaticData = RM.StaticData || {}; RM.StaticData.isProduction = "1";var RM = RM || {}; RM.StaticData = RM.StaticData || {}; RM.StaticData["session"] = [];var RM = RM || {}; RM.StaticData = RM.StaticData || {}; RM.StaticData["cookiePropagatorConf"] = "need_propagation";RM.StaticData["cookiePropagatorHash"] = "09b0cd4f453f0e2e0e57eac914187d83";var RM = RM || {}; RM.StaticData = RM.StaticData || {}; RM.StaticData["abCampaigns"] = {"avia_offers_longpolling":{"AVIA-5985_longpolling_disabled":0,"AVIA-5985_longpolling_enabled":1},"avia_wizard_auto_complete_hint":{"AVIA-3061_show_hint":0,"AVIA-3061_without_hint":1},"avia_wizard_mobile_change_fare":{"AVIA-10919_show_change_fare":1,"AVIA-10919_without_change_fare":0},"main_page_mobile":{"main_page_mobile_off":0,"main_page_mobile_on":1},"tour_only_hotel_with_photo":{"tour_only_hotel_with_photo_off":1,"tour_only_hotel_with_photo_on":0},"tour_prepayment_rules":{"tour_prepayment_rules_editable":1,"tour_prepayment_rules_fixed":0}};window.AbTestingParams = {"apiUrl":"https:\/\/www.tutu.ru\/ajax\/?Action=analytics_abtesting","campaignsData":{"ab_adv_card_tags":{"id":"ab_adv_card_tags","applied":0,"active":true,"forceVariant":0,"variants":{"ab_adv_card_tags_links_clear":{"assigned":0,"id":"ab_adv_card_tags_links_clear"},"ab_adv_card_tags_links_save":{"assigned":0,"id":"ab_adv_card_tags_links_save"},"ab_adv_card_tags_off":{"assigned":0,"id":"ab_adv_card_tags_off"},"ab_adv_card_tags_text":{"assigned":1,"id":"ab_adv_card_tags_text","versionedId":"ab_adv_card_tags_text_v02"}}},"adv_etrains_direction_link":{"id":"adv_etrains_direction_link","applied":0,"active":true,"forceVariant":0,"variants":{"adv_etrains_direction_link_forei":{"assigned":0,"id":"adv_etrains_direction_link_forei"},"adv_etrains_direction_link_point":{"assigned":0,"id":"adv_etrains_direction_link_point"},"adv_etrains_direction_link_russi":{"assigned":1,"id":"adv_etrains_direction_link_russi","versionedId":"adv_etrains_direction_link_russi_v04"}}},"adv_search_form_showcase_rem":{"id":"adv_search_form_showcase_rem","applied":0,"active":true,"forceVariant":0,"variants":{"adv_search_form_showcase_rem_off":{"assigned":1,"id":"adv_search_form_showcase_rem_off","versionedId":"adv_search_form_showcase_rem_off_v01"},"adv_search_form_showcase_rem_on":{"assigned":0,"id":"adv_search_form_showcase_rem_on"}}},"app_bus_insurances":{"id":"app_bus_insurances","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-3539-no-insurance-selected":{"assigned":1,"id":"MAPP-3539-no-insurance-selected","versionedId":"MAPP-3539-no-insurance-selected"},"MAPP-3539-without-insurance":{"assigned":0,"id":"MAPP-3539-without-insurance"}}},"app_bus_tariff_features":{"id":"app_bus_tariff_features","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-3537-hide-tariff-info":{"assigned":0,"id":"MAPP-3537-hide-tariff-info"},"MAPP-3537-show-tariff-info":{"assigned":1,"id":"MAPP-3537-show-tariff-info","versionedId":"MAPP-3537-show-tariff-info_v01"}}},"app_idfa_requester":{"id":"app_idfa_requester","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-3464_ads":{"assigned":0,"id":"MAPP-3464_ads"},"MAPP-3464_list":{"assigned":1,"id":"MAPP-3464_list","versionedId":"MAPP-3464_list_v04"},"MAPP-3464_off":{"assigned":0,"id":"MAPP-3464_off"}}},"app_ios_hotels_history_2":{"id":"app_ios_hotels_history_2","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-5953_without_hotels_history":{"assigned":0,"id":"MAPP-5953_without_hotels_history"},"MAPP-5953_with_hotels_history":{"assigned":1,"id":"MAPP-5953_with_hotels_history","versionedId":"MAPP-5953_with_hotels_history_v01"}}},"app_mono_train_bdui_banner_android":{"id":"app_mono_train_bdui_banner_android","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-8261-banner-off-android":{"assigned":0,"id":"MAPP-8261-banner-off-android"},"MAPP-8261-banner-on-android":{"assigned":1,"id":"MAPP-8261-banner-on-android","versionedId":"MAPP-8261-banner-on-android_v01"}}},"app_mono_train_bdui_banner_ios":{"id":"app_mono_train_bdui_banner_ios","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-8415-banner-off-ios":{"assigned":0,"id":"MAPP-8415-banner-off-ios"},"MAPP-8415-banner-on-ios":{"assigned":1,"id":"MAPP-8415-banner-on-ios","versionedId":"MAPP-8415-banner-on-ios_v04"}}},"app_ptt_additional_baggage_s7":{"id":"app_ptt_additional_baggage_s7","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-3889_has_baggage":{"assigned":1,"id":"MAPP-3889_has_baggage","versionedId":"MAPP-3889_has_baggage"},"MAPP-3889_no_baggage":{"assigned":0,"id":"MAPP-3889_no_baggage"}}},"app_ptt_bdui_juicy_offers_android":{"id":"app_ptt_bdui_juicy_offers_android","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-8209-android-ptt-hide-juicy-offers":{"assigned":0,"id":"MAPP-8209-android-ptt-hide-juicy-offers"},"MAPP-8209-android-ptt-show-juicy-offers":{"assigned":1,"id":"MAPP-8209-android-ptt-show-juicy-offers","versionedId":"MAPP-8209-android-ptt-show-juicy-offers_v02"}}},"app_ptt_bdui_juicy_offers_ios":{"id":"app_ptt_bdui_juicy_offers_ios","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-8209-ios-ptt-hide-juicy-offers":{"assigned":0,"id":"MAPP-8209-ios-ptt-hide-juicy-offers"},"MAPP-8209-ios-ptt-show-juicy-offers":{"assigned":1,"id":"MAPP-8209-ios-ptt-show-juicy-offers","versionedId":"MAPP-8209-ios-ptt-show-juicy-offers_v03"}}},"app_ptt_bdui_on_main_screen_andr_v2":{"id":"app_ptt_bdui_on_main_screen_andr_v2","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-6104_bdui_v2_off":{"assigned":0,"id":"MAPP-6104_bdui_v2_off"},"MAPP-6104_bdui_v2_on":{"assigned":1,"id":"MAPP-6104_bdui_v2_on","versionedId":"MAPP-6104_bdui_v2_on_v01"}}},"app_ptt_bdui_on_main_screen_ios_3":{"id":"app_ptt_bdui_on_main_screen_ios_3","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-7385_bdui_off_3":{"assigned":0,"id":"MAPP-7385_bdui_off_3"},"MAPP-7385_bdui_on_3":{"assigned":1,"id":"MAPP-7385_bdui_on_3","versionedId":"MAPP-7385_bdui_on_3_v01"}}},"app_ptt_bdui_on_main_screen_ios_v2":{"id":"app_ptt_bdui_on_main_screen_ios_v2","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-6103_bdui_off_v2":{"assigned":0,"id":"MAPP-6103_bdui_off_v2"},"MAPP-6103_bdui_on_v2":{"assigned":1,"id":"MAPP-6103_bdui_on_v2","versionedId":"MAPP-6103_bdui_on_v2_v02"}}},"app_ptt_calendar_prices_android":{"id":"app_ptt_calendar_prices_android","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-5100_hide_prices":{"assigned":0,"id":"MAPP-5100_hide_prices"},"MAPP-5100_show_prices":{"assigned":1,"id":"MAPP-5100_show_prices","versionedId":"MAPP-5100_show_prices_v01"}}},"app_ptt_calendar_prices_ios":{"id":"app_ptt_calendar_prices_ios","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-5101_hide_prices":{"assigned":0,"id":"MAPP-5101_hide_prices"},"MAPP-5101_show_prices":{"assigned":1,"id":"MAPP-5101_show_prices","versionedId":"MAPP-5101_show_prices_v01"}}},"app_ptt_feed_autoswitch_android":{"id":"app_ptt_feed_autoswitch_android","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1570_feed_autoswitch_an_off":{"assigned":0,"id":"VID-1570_feed_autoswitch_an_off"},"VID-1570_feed_autoswitch_an_on":{"assigned":1,"id":"VID-1570_feed_autoswitch_an_on","versionedId":"VID-1570_feed_autoswitch_an_on_v01"}}},"app_ptt_feed_avia_new_design_cell":{"id":"app_ptt_feed_avia_new_design_cell","applied":0,"active":true,"forceVariant":0,"variants":{"VID-2791_new_design":{"assigned":1,"id":"VID-2791_new_design","versionedId":"VID-2791_new_design_v01"},"VID-2791_old_design":{"assigned":0,"id":"VID-2791_old_design"}}},"app_ptt_feed_bus_filters_an":{"id":"app_ptt_feed_bus_filters_an","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1695_feed_bus_fltrs_an_off":{"assigned":0,"id":"VID-1695_feed_bus_fltrs_an_off"},"VID-1695_feed_bus_fltrs_an_on":{"assigned":1,"id":"VID-1695_feed_bus_fltrs_an_on","versionedId":"VID-1695_feed_bus_fltrs_an_on_v01"}}},"app_ptt_feed_bus_new_design_cell":{"id":"app_ptt_feed_bus_new_design_cell","applied":0,"active":true,"forceVariant":0,"variants":{"VID-2536_new_design":{"assigned":1,"id":"VID-2536_new_design","versionedId":"VID-2536_new_design_v01"},"VID-2536_old_design":{"assigned":0,"id":"VID-2536_old_design"}}},"app_ptt_feed_hotel_new_design_cell_v2":{"id":"app_ptt_feed_hotel_new_design_cell_v2","applied":0,"active":true,"forceVariant":0,"variants":{"VID-2304_new_design":{"assigned":1,"id":"VID-2304_new_design","versionedId":"VID-2304_new_design_v02"},"VID-2304_old_design":{"assigned":0,"id":"VID-2304_old_design"}}},"app_ptt_feed_informers_android":{"id":"app_ptt_feed_informers_android","applied":0,"active":true,"forceVariant":0,"variants":{"VID-2375_off":{"assigned":0,"id":"VID-2375_off"},"VID-2375_on":{"assigned":1,"id":"VID-2375_on","versionedId":"VID-2375_on_v01"}}},"app_ptt_feed_informers_ios":{"id":"app_ptt_feed_informers_ios","applied":0,"active":true,"forceVariant":0,"variants":{"INFORM-32_informers_off":{"assigned":0,"id":"INFORM-32_informers_off"},"INFORM-32_informers_on":{"assigned":1,"id":"INFORM-32_informers_on","versionedId":"INFORM-32_informers_on_v02"}}},"app_ptt_feed_map_transition_ios":{"id":"app_ptt_feed_map_transition_ios","applied":0,"active":true,"forceVariant":0,"variants":{"VID-2266_new_transition":{"assigned":1,"id":"VID-2266_new_transition","versionedId":"VID-2266_new_transition_v01"},"VID-2266_old_transition":{"assigned":0,"id":"VID-2266_old_transition"}}},"app_ptt_feed_train_filters_an":{"id":"app_ptt_feed_train_filters_an","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1629_feed_train_fltrs_an_off":{"assigned":0,"id":"VID-1629_feed_train_fltrs_an_off"},"VID-1629_feed_train_fltrs_an_on":{"assigned":1,"id":"VID-1629_feed_train_fltrs_an_on","versionedId":"VID-1629_feed_train_fltrs_an_on_v01"}}},"app_ptt_feed_train_filters_ios":{"id":"app_ptt_feed_train_filters_ios","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1590-train_filters_off":{"assigned":0,"id":"VID-1590-train_filters_off"},"VID-1590-train_filters_on":{"assigned":1,"id":"VID-1590-train_filters_on","versionedId":"VID-1590-train_filters_on_v01"}}},"app_ptt_feed_train_new_design_cell_v2":{"id":"app_ptt_feed_train_new_design_cell_v2","applied":0,"active":true,"forceVariant":0,"variants":{"VID-2881_new_horizontal_design":{"assigned":1,"id":"VID-2881_new_horizontal_design","versionedId":"VID-2881_new_horizontal_design_v02"},"VID-2881_new_vertical_design":{"assigned":0,"id":"VID-2881_new_vertical_design"},"VID-2881_old_design":{"assigned":0,"id":"VID-2881_old_design"}}},"app_ptt_hotels_android_2":{"id":"app_ptt_hotels_android_2","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-4151_android_hotels_off_2":{"assigned":0,"id":"MAPP-4151_android_hotels_off_2"},"MAPP-4151_android_hotels_on_2":{"assigned":1,"id":"MAPP-4151_android_hotels_on_2","versionedId":"MAPP-4151_android_hotels_on_2"}}},"app_ptt_hotels_history_andr_2":{"id":"app_ptt_hotels_history_andr_2","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-5569_hotels_history_off":{"assigned":0,"id":"MAPP-5569_hotels_history_off"},"MAPP-5569_hotels_history_on":{"assigned":1,"id":"MAPP-5569_hotels_history_on","versionedId":"MAPP-5569_hotels_history_on_v01"}}},"app_ptt_hotels_ios_1":{"id":"app_ptt_hotels_ios_1","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-4070_hotels_off":{"assigned":0,"id":"MAPP-4070_hotels_off"},"MAPP-4070_hotels_on":{"assigned":1,"id":"MAPP-4070_hotels_on","versionedId":"MAPP-4070_hotels_on_v01"}}},"app_ptt_hotels_ios_2":{"id":"app_ptt_hotels_ios_2","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-4310_ios_hotels_off_2":{"assigned":0,"id":"MAPP-4310_ios_hotels_off_2"},"MAPP-4310_ios_hotels_on_2":{"assigned":1,"id":"MAPP-4310_ios_hotels_on_2","versionedId":"MAPP-4310_ios_hotels_on_2"}}},"app_ptt_infoservice_android_3":{"id":"app_ptt_infoservice_android_3","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-4465_infoservice_off":{"assigned":0,"id":"MAPP-4465_infoservice_off"},"MAPP-4465_infoservice_on":{"assigned":1,"id":"MAPP-4465_infoservice_on","versionedId":"MAPP-4465_infoservice_on_v01"}}},"app_ptt_infoservice_ios_3":{"id":"app_ptt_infoservice_ios_3","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-4468_ios_infoservice_off":{"assigned":0,"id":"MAPP-4468_ios_infoservice_off"},"MAPP-4468_ios_infoservice_on":{"assigned":1,"id":"MAPP-4468_ios_infoservice_on","versionedId":"MAPP-4468_ios_infoservice_on"}}},"app_ptt_in_app_updates_2":{"id":"app_ptt_in_app_updates_2","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-7640_turn_off_updates_2":{"assigned":0,"id":"MAPP-7640_turn_off_updates_2"},"MAPP-7640_turn_on_updates_2":{"assigned":1,"id":"MAPP-7640_turn_on_updates_2","versionedId":"MAPP-7640_turn_on_updates_2_v02"}}},"app_ptt_main_stories_andr_2":{"id":"app_ptt_main_stories_andr_2","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-5753_stories_off":{"assigned":0,"id":"MAPP-5753_stories_off"},"MAPP-5753_stories_on":{"assigned":1,"id":"MAPP-5753_stories_on","versionedId":"MAPP-5753_stories_on"}}},"app_ptt_main_stories_ios":{"id":"app_ptt_main_stories_ios","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-5626_stories_off":{"assigned":0,"id":"MAPP-5626_stories_off"},"MAPP-5626_stories_on":{"assigned":1,"id":"MAPP-5626_stories_on","versionedId":"MAPP-5626_stories_on_v01"}}},"app_ptt_messages_center":{"id":"app_ptt_messages_center","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-3621_new_messages_center":{"assigned":1,"id":"MAPP-3621_new_messages_center","versionedId":"MAPP-3621_new_messages_center_v01"},"MAPP-3621_old_messages_center":{"assigned":0,"id":"MAPP-3621_old_messages_center"}}},"app_ptt_new_calendar_ios_v3":{"id":"app_ptt_new_calendar_ios_v3","applied":0,"active":true,"forceVariant":0,"variants":{"VID-2850_old_calendar":{"assigned":0,"id":"VID-2850_old_calendar"},"VID-2850_one_way":{"assigned":1,"id":"VID-2850_one_way","versionedId":"VID-2850_one_way_v02"},"VID-2850_sum_calendar":{"assigned":0,"id":"VID-2850_sum_calendar"}}},"app_ptt_new_calendar_v3_android":{"id":"app_ptt_new_calendar_v3_android","applied":0,"active":true,"forceVariant":0,"variants":{"VID-3214_new":{"assigned":1,"id":"VID-3214_new","versionedId":"VID-3214_new_v02"},"VID-3214_old":{"assigned":0,"id":"VID-3214_old"}}},"app_ptt_new_search_ios_abc":{"id":"app_ptt_new_search_ios_abc","applied":0,"active":true,"forceVariant":0,"variants":{"VID-3388_new_all":{"assigned":1,"id":"VID-3388_new_all","versionedId":"VID-3388_new_all_v06"},"VID-3388_new_search_only":{"assigned":0,"id":"VID-3388_new_search_only"},"VID-3388_old_search":{"assigned":0,"id":"VID-3388_old_search"}}},"app_ptt_orders_hotels_promo_andr":{"id":"app_ptt_orders_hotels_promo_andr","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-5751_promo_off":{"assigned":0,"id":"MAPP-5751_promo_off"},"MAPP-5751_promo_on":{"assigned":1,"id":"MAPP-5751_promo_on","versionedId":"MAPP-5751_promo_on"}}},"app_ptt_orders_hotels_promo_ios":{"id":"app_ptt_orders_hotels_promo_ios","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-5743_promo_off":{"assigned":0,"id":"MAPP-5743_promo_off"},"MAPP-5743_promo_on":{"assigned":1,"id":"MAPP-5743_promo_on","versionedId":"MAPP-5743_promo_on"}}},"app_ptt_orders_indicator_2":{"id":"app_ptt_orders_indicator_2","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-3976_hide_indicator":{"assigned":0,"id":"MAPP-3976_hide_indicator"},"MAPP-3976_show_indicator":{"assigned":1,"id":"MAPP-3976_show_indicator","versionedId":"MAPP-3976_show_indicator"}}},"app_ptt_recommended_avia_ios_v2":{"id":"app_ptt_recommended_avia_ios_v2","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1856_recommendations_v2_off":{"assigned":0,"id":"VID-1856_recommendations_v2_off"},"VID-1856_recommendations_v2_on":{"assigned":1,"id":"VID-1856_recommendations_v2_on","versionedId":"VID-1856_recommendations_v2_on_v01"}}},"app_ptt_search_with_return_ios":{"id":"app_ptt_search_with_return_ios","applied":0,"active":true,"forceVariant":0,"variants":{"VID-3928_without_return_date":{"assigned":1,"id":"VID-3928_without_return_date","versionedId":"VID-3928_without_return_date"},"VID-3928_with_return_date":{"assigned":0,"id":"VID-3928_with_return_date"}}},"app_ptt_show_tours_ab":{"id":"app_ptt_show_tours_ab","applied":0,"active":true,"forceVariant":0,"variants":{"VID-3493_hide_tours":{"assigned":0,"id":"VID-3493_hide_tours"},"VID-3493_show_tours":{"assigned":1,"id":"VID-3493_show_tours","versionedId":"VID-3493_show_tours_v01"}}},"app_ptt_train_add_services_ios":{"id":"app_ptt_train_add_services_ios","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-5387_new_design":{"assigned":1,"id":"MAPP-5387_new_design","versionedId":"MAPP-5387_new_design_v01"},"MAPP-5387_old_design":{"assigned":0,"id":"MAPP-5387_old_design"}}},"app_return_ticket_on_success":{"id":"app_return_ticket_on_success","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-3230_without_promocode":{"assigned":1,"id":"MAPP-3230_without_promocode","versionedId":"MAPP-3230_without_promocode_v01"},"MAPP-3230_without_return_ticket":{"assigned":0,"id":"MAPP-3230_without_return_ticket"},"MAPP-3230_with_promocode":{"assigned":0,"id":"MAPP-3230_with_promocode"}}},"app_train_autoselect_ios":{"id":"app_train_autoselect_ios","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-3721-hide-train-autoselect":{"assigned":0,"id":"MAPP-3721-hide-train-autoselect"},"MAPP-3721-show-train-autoselect":{"assigned":1,"id":"MAPP-3721-show-train-autoselect","versionedId":"MAPP-3721-show-train-autoselect_v01"}}},"app_train_car_selection":{"id":"app_train_car_selection","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-2331_new_car_selection_scre":{"assigned":1,"id":"MAPP-2331_new_car_selection_scre","versionedId":"MAPP-2331_new_car_selection_scre_v02"},"MAPP-2331_old_car_selection_scre":{"assigned":0,"id":"MAPP-2331_old_car_selection_scre"}}},"app_train_passengers_autofill":{"id":"app_train_passengers_autofill","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-2237_new_autofill":{"assigned":1,"id":"MAPP-2237_new_autofill","versionedId":"MAPP-2237_new_autofill_v05"},"MAPP-2237_old_autofill":{"assigned":0,"id":"MAPP-2237_old_autofill"}}},"app_train_pricing_strategy":{"id":"app_train_pricing_strategy","applied":0,"active":true,"forceVariant":0,"variants":{"app_train_pricing_strategy_15ai":{"assigned":0,"id":"app_train_pricing_strategy_15ai"},"app_train_pricing_strategy_4438i":{"assigned":0,"id":"app_train_pricing_strategy_4438i"},"app_train_pricing_strategy_5761":{"assigned":0,"id":"app_train_pricing_strategy_5761"},"app_train_pricing_strategy_6011":{"assigned":0,"id":"app_train_pricing_strategy_6011"},"app_train_pricing_strategy_7103":{"assigned":0,"id":"app_train_pricing_strategy_7103"},"app_train_pricing_strategy_7103m":{"assigned":0,"id":"app_train_pricing_strategy_7103m"},"app_train_pricing_strategy_7153":{"assigned":0,"id":"app_train_pricing_strategy_7153"},"app_train_pricing_strategy_ai":{"assigned":0,"id":"app_train_pricing_strategy_ai"},"app_train_pricing_strategy_aic10":{"assigned":0,"id":"app_train_pricing_strategy_aic10"},"app_train_pricing_strategy_aic15":{"assigned":0,"id":"app_train_pricing_strategy_aic15"},"app_train_pricing_strategy_aic5":{"assigned":0,"id":"app_train_pricing_strategy_aic5"},"app_train_pricing_strategy_aii15":{"assigned":0,"id":"app_train_pricing_strategy_aii15"},"app_train_pricing_strategy_aii5":{"assigned":0,"id":"app_train_pricing_strategy_aii5"},"app_train_pricing_strategy_dc005":{"assigned":0,"id":"app_train_pricing_strategy_dc005"},"app_train_pricing_strategy_dc010":{"assigned":0,"id":"app_train_pricing_strategy_dc010"},"app_train_pricing_strategy_defau":{"assigned":0,"id":"app_train_pricing_strategy_defau"},"app_train_pricing_strategy_dwn10":{"assigned":0,"id":"app_train_pricing_strategy_dwn10"},"app_train_pricing_strategy_dwn4":{"assigned":0,"id":"app_train_pricing_strategy_dwn4"},"app_train_pricing_strategy_dwn5":{"assigned":0,"id":"app_train_pricing_strategy_dwn5"},"app_train_pricing_strategy_dwn8":{"assigned":0,"id":"app_train_pricing_strategy_dwn8"},"app_train_pricing_strategy_ic005":{"assigned":0,"id":"app_train_pricing_strategy_ic005"},"app_train_pricing_strategy_ic010":{"assigned":0,"id":"app_train_pricing_strategy_ic010"},"app_train_pricing_strategy_ic025":{"assigned":0,"id":"app_train_pricing_strategy_ic025"},"app_train_pricing_strategy_sup10":{"assigned":1,"id":"app_train_pricing_strategy_sup10","versionedId":"app_train_pricing_strategy_sup10_v26"},"app_train_pricing_strategy_sup5":{"assigned":0,"id":"app_train_pricing_strategy_sup5"},"app_train_pricing_strategy_up10":{"assigned":0,"id":"app_train_pricing_strategy_up10"},"app_train_pricing_strategy_up4":{"assigned":0,"id":"app_train_pricing_strategy_up4"},"app_train_pricing_strategy_up5":{"assigned":0,"id":"app_train_pricing_strategy_up5"},"app_train_pricing_strategy_up8":{"assigned":0,"id":"app_train_pricing_strategy_up8"}}},"AVIA-16083_booking_price":{"id":"AVIA-16083_booking_price","applied":0,"active":true,"forceVariant":0,"variants":{"AVIA-16083_booking_price_199rub":{"assigned":1,"id":"AVIA-16083_booking_price_199rub","versionedId":"AVIA-16083_booking_price_199rub"},"AVIA-16083_booking_price_1rub":{"assigned":0,"id":"AVIA-16083_booking_price_1rub"},"AVIA-16083_booking_price_99rub":{"assigned":0,"id":"AVIA-16083_booking_price_99rub"}}},"AVIA-16128-insurance-description":{"id":"AVIA-16128-insurance-description","applied":0,"active":true,"forceVariant":0,"variants":{"AVIA-16128_new_description":{"assigned":0,"id":"AVIA-16128_new_description"},"AVIA-16128_old_description":{"assigned":1,"id":"AVIA-16128_old_description","versionedId":"AVIA-16128_old_description_v02"}}},"AVIA-16187_search_extension":{"id":"AVIA-16187_search_extension","applied":0,"active":true,"forceVariant":0,"variants":{"AVIA-16187_without_search_extens":{"assigned":0,"id":"AVIA-16187_without_search_extens"},"AVIA-16187_with_search_extension":{"assigned":1,"id":"AVIA-16187_with_search_extension","versionedId":"AVIA-16187_with_search_extension_v01"}}},"AVIA-16244-show-hotels-on-succes":{"id":"AVIA-16244-show-hotels-on-succes","applied":0,"active":true,"forceVariant":0,"variants":{"AVIA-16244_with_cards":{"assigned":0,"id":"AVIA-16244_with_cards"},"AVIA-16244_with_maps":{"assigned":1,"id":"AVIA-16244_with_maps","versionedId":"AVIA-16244_with_maps_v01"}}},"AVIA-16328_gr_double_price":{"id":"AVIA-16328_gr_double_price","applied":0,"active":true,"forceVariant":0,"variants":{"AVIA-16328_doubled_price":{"assigned":1,"id":"AVIA-16328_doubled_price","versionedId":"AVIA-16328_doubled_price_v04"},"AVIA-16328_same_price":{"assigned":0,"id":"AVIA-16328_same_price"}}},"AVIA-16336_offers_tariff_design":{"id":"AVIA-16336_offers_tariff_design","applied":0,"active":true,"forceVariant":0,"variants":{"AVIA-16336_basic_tariff_view":{"assigned":0,"id":"AVIA-16336_basic_tariff_view"},"AVIA-16336_tariff_cards_view":{"assigned":1,"id":"AVIA-16336_tariff_cards_view","versionedId":"AVIA-16336_tariff_cards_view_v01"}}},"AVIA-16572_feed_checkout":{"id":"AVIA-16572_feed_checkout","applied":0,"active":true,"forceVariant":0,"variants":{"AVIA-16572_feed_checkout_new":{"assigned":1,"id":"AVIA-16572_feed_checkout_new","versionedId":"AVIA-16572_feed_checkout_new"},"AVIA-16572_feed_checkout_old":{"assigned":0,"id":"AVIA-16572_feed_checkout_old"}}},"AVIA-16690_feed_checkout":{"id":"AVIA-16690_feed_checkout","applied":0,"active":true,"forceVariant":0,"variants":{"AVIA-16690_feed_checkout_new":{"assigned":1,"id":"AVIA-16690_feed_checkout_new","versionedId":"AVIA-16690_feed_checkout_new"},"AVIA-16690_feed_checkout_old":{"assigned":0,"id":"AVIA-16690_feed_checkout_old"}}},"AVIA-16737-offer-details-tariffs":{"id":"AVIA-16737-offer-details-tariffs","applied":0,"active":true,"forceVariant":0,"variants":{"AVIA-16737-offer-details-tariffs-expander":{"assigned":0,"id":"AVIA-16737-offer-details-tariffs-expander"},"AVIA-16737-offer-details-tariffs-old":{"assigned":0,"id":"AVIA-16737-offer-details-tariffs-old"},"AVIA-16737-offer-details-tariffs-slider":{"assigned":1,"id":"AVIA-16737-offer-details-tariffs-slider","versionedId":"AVIA-16737-offer-details-tariffs-slider"}}},"AVIA-17048_mono_ios_tariffs_on_details":{"id":"AVIA-17048_mono_ios_tariffs_on_details","applied":0,"active":true,"forceVariant":0,"variants":{"AVIA-17048_mono_ios_tariffs_expandable_cards":{"assigned":0,"id":"AVIA-17048_mono_ios_tariffs_expandable_cards"},"AVIA-17048_mono_ios_tariffs_old":{"assigned":0,"id":"AVIA-17048_mono_ios_tariffs_old"},"AVIA-17048_mono_ios_tariffs_scrollable_cards":{"assigned":1,"id":"AVIA-17048_mono_ios_tariffs_scrollable_cards","versionedId":"AVIA-17048_mono_ios_tariffs_scrollable_cards_v02"}}},"avia_8jnf_frjrbir_frgrnfpu":{"id":"avia_8jnf_frjrbir_frgrnfpu","applied":0,"active":true,"forceVariant":0,"variants":{"avia_8jnf_frjrbir_frgrnfpu_above":{"assigned":1,"id":"avia_8jnf_frjrbir_frgrnfpu_above","versionedId":"avia_8jnf_frjrbir_frgrnfpu_above_v01"},"avia_8jnf_frjrbir_frgrnfpu_below":{"assigned":0,"id":"avia_8jnf_frjrbir_frgrnfpu_below"},"avia_8jnf_frjrbir_frgrnfpu_contr":{"assigned":0,"id":"avia_8jnf_frjrbir_frgrnfpu_contr"}}},"avia_flights1_ptt_popup":{"id":"avia_flights1_ptt_popup","applied":0,"active":true,"forceVariant":0,"variants":{"avia_flights1_ptt_popup_off":{"assigned":0,"id":"avia_flights1_ptt_popup_off"},"avia_flights1_ptt_popup_on":{"assigned":1,"id":"avia_flights1_ptt_popup_on","versionedId":"avia_flights1_ptt_popup_on_v02"}}},"avia_form_on_main":{"id":"avia_form_on_main","applied":0,"active":true,"forceVariant":0,"variants":{"AVIA-15755_avia_form_on_main_off":{"assigned":0,"id":"AVIA-15755_avia_form_on_main_off"},"AVIA-15755_avia_form_on_main_on":{"assigned":1,"id":"AVIA-15755_avia_form_on_main_on","versionedId":"AVIA-15755_avia_form_on_main_on_v01"}}},"avia_main_ptt_popup":{"id":"avia_main_ptt_popup","applied":0,"active":true,"forceVariant":0,"variants":{"avia_main_ptt_popup_off":{"assigned":0,"id":"avia_main_ptt_popup_off"},"avia_main_ptt_popup_on":{"assigned":1,"id":"avia_main_ptt_popup_on","versionedId":"avia_main_ptt_popup_on_v05"}}},"avia_revenue_on_offers":{"id":"avia_revenue_on_offers","applied":0,"active":true,"forceVariant":0,"variants":{"avia_revenue_on_offers_above":{"assigned":0,"id":"avia_revenue_on_offers_above"},"avia_revenue_on_offers_below":{"assigned":1,"id":"avia_revenue_on_offers_below","versionedId":"avia_revenue_on_offers_below"},"avia_revenue_on_offers_contr":{"assigned":0,"id":"avia_revenue_on_offers_contr"}}},"avia_rough_exchange_calc":{"id":"avia_rough_exchange_calc","applied":0,"active":true,"forceVariant":0,"variants":{"AVIA-15145_rough_calc_off":{"assigned":0,"id":"AVIA-15145_rough_calc_off"},"AVIA-15145_rough_calc_on":{"assigned":1,"id":"AVIA-15145_rough_calc_on","versionedId":"AVIA-15145_rough_calc_on_v01"}}},"avia_wizard_company_payment":{"id":"avia_wizard_company_payment","applied":0,"active":true,"forceVariant":0,"variants":{"avia_wizard_company_payment_off":{"assigned":0,"id":"avia_wizard_company_payment_off"},"avia_wizard_company_payment_on":{"assigned":1,"id":"avia_wizard_company_payment_on","versionedId":"avia_wizard_company_payment_on_v01"}}},"bus_checkout_app_banner":{"id":"bus_checkout_app_banner","applied":0,"active":true,"forceVariant":0,"variants":{"bus_checkout_app_banner_off":{"assigned":0,"id":"bus_checkout_app_banner_off"},"bus_checkout_app_banner_on":{"assigned":1,"id":"bus_checkout_app_banner_on","versionedId":"bus_checkout_app_banner_on_v01"}}},"bus_checkout_voyager_suggester_ios":{"id":"bus_checkout_voyager_suggester_ios","applied":0,"active":true,"forceVariant":0,"variants":{"bus_checkout_voyager_suggester_ios_off":{"assigned":0,"id":"bus_checkout_voyager_suggester_ios_off"},"bus_checkout_voyager_suggester_ios_on":{"assigned":1,"id":"bus_checkout_voyager_suggester_ios_on","versionedId":"bus_checkout_voyager_suggester_ios_on_v01"}}},"bus_foreign_card":{"id":"bus_foreign_card","applied":0,"active":true,"forceVariant":0,"variants":{"bus_foreign_card_off":{"assigned":0,"id":"bus_foreign_card_off"},"bus_foreign_card_on":{"assigned":1,"id":"bus_foreign_card_on","versionedId":"bus_foreign_card_on_v02"}}},"bus_new_station_page":{"id":"bus_new_station_page","applied":0,"active":true,"forceVariant":0,"variants":{"bus_new_station_page_off":{"assigned":0,"id":"bus_new_station_page_off"},"bus_new_station_page_on":{"assigned":1,"id":"bus_new_station_page_on","versionedId":"bus_new_station_page_on_v03"}}},"bus_refund_form":{"id":"bus_refund_form","applied":0,"active":true,"forceVariant":0,"variants":{"bus_refund_form_off":{"assigned":0,"id":"bus_refund_form_off"},"bus_refund_form_on":{"assigned":1,"id":"bus_refund_form_on","versionedId":"bus_refund_form_on_v08"}}},"bus_schedule_buy_action":{"id":"bus_schedule_buy_action","applied":0,"active":true,"forceVariant":0,"variants":{"bus_schedule_buy_action_date":{"assigned":1,"id":"bus_schedule_buy_action_date","versionedId":"bus_schedule_buy_action_date_v02"},"bus_schedule_buy_action_from":{"assigned":0,"id":"bus_schedule_buy_action_from"},"bus_schedule_buy_action_init":{"assigned":0,"id":"bus_schedule_buy_action_init"}}},"bus_success_app_banner":{"id":"bus_success_app_banner","applied":0,"active":true,"forceVariant":0,"variants":{"bus_success_app_banner_off":{"assigned":0,"id":"bus_success_app_banner_off"},"bus_success_app_banner_on":{"assigned":1,"id":"bus_success_app_banner_on","versionedId":"bus_success_app_banner_on_v01"}}},"bus_supreme_loader":{"id":"bus_supreme_loader","applied":0,"active":true,"forceVariant":0,"variants":{"bus_supreme_loader_off":{"assigned":0,"id":"bus_supreme_loader_off"},"bus_supreme_loader_on":{"assigned":1,"id":"bus_supreme_loader_on","versionedId":"bus_supreme_loader_on_v01"}}},"bus_tickets_buy_action":{"id":"bus_tickets_buy_action","applied":0,"active":true,"forceVariant":0,"variants":{"bus_tickets_buy_action_buy":{"assigned":0,"id":"bus_tickets_buy_action_buy"},"bus_tickets_buy_action_date":{"assigned":1,"id":"bus_tickets_buy_action_date","versionedId":"bus_tickets_buy_action_date_v02"},"bus_tickets_buy_action_init":{"assigned":0,"id":"bus_tickets_buy_action_init"}}},"bus_vid_app_banner":{"id":"bus_vid_app_banner","applied":0,"active":true,"forceVariant":0,"variants":{"bus_vid_app_banner_off":{"assigned":0,"id":"bus_vid_app_banner_off"},"bus_vid_app_banner_on":{"assigned":1,"id":"bus_vid_app_banner_on","versionedId":"bus_vid_app_banner_on_v01"}}},"bus_vid_price_labels":{"id":"bus_vid_price_labels","applied":0,"active":true,"forceVariant":0,"variants":{"bus_vid_price_labels_off":{"assigned":0,"id":"bus_vid_price_labels_off"},"bus_vid_price_labels_on":{"assigned":1,"id":"bus_vid_price_labels_on","versionedId":"bus_vid_price_labels_on_v02"}}},"cf_test_avia_main":{"id":"cf_test_avia_main","applied":0,"active":true,"forceVariant":0,"variants":{"CF-2358-avia_main_a":{"assigned":1,"id":"CF-2358-avia_main_a","versionedId":"CF-2358-avia_main_a"},"CF-2358-avia_main_b":{"assigned":0,"id":"CF-2358-avia_main_b"}}},"checkout_avia_7_android":{"id":"checkout_avia_7_android","applied":0,"active":true,"forceVariant":0,"variants":{"checkout_avia_7_android_off":{"assigned":0,"id":"checkout_avia_7_android_off"},"checkout_avia_7_android_on":{"assigned":1,"id":"checkout_avia_7_android_on","versionedId":"checkout_avia_7_android_on_v02"}}},"checkout_avia_8_ios":{"id":"checkout_avia_8_ios","applied":0,"active":true,"forceVariant":0,"variants":{"checkout_avia_8_ios_off":{"assigned":0,"id":"checkout_avia_8_ios_off"},"checkout_avia_8_ios_on":{"assigned":1,"id":"checkout_avia_8_ios_on","versionedId":"checkout_avia_8_ios_on_v01"}}},"checkout_avia_9_ios":{"id":"checkout_avia_9_ios","applied":0,"active":true,"forceVariant":0,"variants":{"checkout_avia_9_ios_off":{"assigned":0,"id":"checkout_avia_9_ios_off"},"checkout_avia_9_ios_on":{"assigned":1,"id":"checkout_avia_9_ios_on","versionedId":"checkout_avia_9_ios_on_v01"}}},"checkout_bus_1_android":{"id":"checkout_bus_1_android","applied":0,"active":true,"forceVariant":0,"variants":{"checkout_bus_1_android_off":{"assigned":0,"id":"checkout_bus_1_android_off"},"checkout_bus_1_android_on":{"assigned":1,"id":"checkout_bus_1_android_on","versionedId":"checkout_bus_1_android_on_v02"}}},"checkout_bus_1_ios":{"id":"checkout_bus_1_ios","applied":0,"active":true,"forceVariant":0,"variants":{"checkout_bus_1_ios_off":{"assigned":0,"id":"checkout_bus_1_ios_off"},"checkout_bus_1_ios_on":{"assigned":1,"id":"checkout_bus_1_ios_on","versionedId":"checkout_bus_1_ios_on_v02"}}},"checkout_voyager_suggester_ios":{"id":"checkout_voyager_suggester_ios","applied":0,"active":true,"forceVariant":0,"variants":{"checkout_voyager_suggester_ios_off":{"assigned":0,"id":"checkout_voyager_suggester_ios_off"},"checkout_voyager_suggester_ios_on":{"assigned":1,"id":"checkout_voyager_suggester_ios_on","versionedId":"checkout_voyager_suggester_ios_on_v01"}}},"dt_acceptance_test_alfa":{"id":"dt_acceptance_test_alfa","applied":0,"active":true,"forceVariant":0,"variants":{"dt_acceptance_test_alfa_off":{"assigned":0,"id":"dt_acceptance_test_alfa_off"},"dt_acceptance_test_alfa_on":{"assigned":1,"id":"dt_acceptance_test_alfa_on","versionedId":"dt_acceptance_test_alfa_on"}}},"dt_test_variative_router":{"id":"dt_test_variative_router","applied":0,"active":true,"forceVariant":0,"variants":{"dt_test_variative_router_a":{"assigned":1,"id":"dt_test_variative_router_a","versionedId":"dt_test_variative_router_a_v02"},"dt_test_variative_router_b":{"assigned":0,"id":"dt_test_variative_router_b"}}},"eco_wallet_bus_android":{"id":"eco_wallet_bus_android","applied":0,"active":true,"forceVariant":0,"variants":{"eco_wallet_bus_android_off":{"assigned":1,"id":"eco_wallet_bus_android_off","versionedId":"eco_wallet_bus_android_off_v01"},"eco_wallet_bus_android_on":{"assigned":0,"id":"eco_wallet_bus_android_on"}}},"eco_wallet_bus_ios":{"id":"eco_wallet_bus_ios","applied":0,"active":true,"forceVariant":0,"variants":{"eco_wallet_bus_ios_off":{"assigned":1,"id":"eco_wallet_bus_ios_off","versionedId":"eco_wallet_bus_ios_off_v01"},"eco_wallet_bus_ios_on":{"assigned":0,"id":"eco_wallet_bus_ios_on"}}},"eco_wallet_bus_web":{"id":"eco_wallet_bus_web","applied":0,"active":true,"forceVariant":0,"variants":{"eco_wallet_bus_web_off":{"assigned":0,"id":"eco_wallet_bus_web_off"},"eco_wallet_bus_web_on":{"assigned":1,"id":"eco_wallet_bus_web_on","versionedId":"eco_wallet_bus_web_on_v01"}}},"eco_wallet_hotels_android":{"id":"eco_wallet_hotels_android","applied":0,"active":true,"forceVariant":0,"variants":{"eco_wallet_hotels_android_off":{"assigned":0,"id":"eco_wallet_hotels_android_off"},"eco_wallet_hotels_android_on":{"assigned":1,"id":"eco_wallet_hotels_android_on","versionedId":"eco_wallet_hotels_android_on"}}},"eco_wallet_hotels_ios":{"id":"eco_wallet_hotels_ios","applied":0,"active":true,"forceVariant":0,"variants":{"eco_wallet_hotels_ios_off":{"assigned":1,"id":"eco_wallet_hotels_ios_off","versionedId":"eco_wallet_hotels_ios_off"},"eco_wallet_hotels_ios_on":{"assigned":0,"id":"eco_wallet_hotels_ios_on"}}},"eco_wallet_hotels_web":{"id":"eco_wallet_hotels_web","applied":0,"active":true,"forceVariant":0,"variants":{"eco_wallet_hotels_web_off":{"assigned":0,"id":"eco_wallet_hotels_web_off"},"eco_wallet_hotels_web_on":{"assigned":1,"id":"eco_wallet_hotels_web_on","versionedId":"eco_wallet_hotels_web_on_v01"}}},"etrain-1689_mobile_filters":{"id":"etrain-1689_mobile_filters","applied":0,"active":true,"forceVariant":0,"variants":{"etrain-1689_mobile_filters_new":{"assigned":1,"id":"etrain-1689_mobile_filters_new","versionedId":"etrain-1689_mobile_filters_new_v02"},"etrain-1689_mobile_filters_old":{"assigned":0,"id":"etrain-1689_mobile_filters_old"}}},"etrain-1737_mrasp_empty_date":{"id":"etrain-1737_mrasp_empty_date","applied":0,"active":true,"forceVariant":0,"variants":{"etrain-1737_mrasp_empty_date_new":{"assigned":1,"id":"etrain-1737_mrasp_empty_date_new","versionedId":"etrain-1737_mrasp_empty_date_new_v03"},"etrain-1737_mrasp_empty_date_old":{"assigned":0,"id":"etrain-1737_mrasp_empty_date_old"}}},"etrain-1895_sidebar":{"id":"etrain-1895_sidebar","applied":0,"active":true,"forceVariant":0,"variants":{"etrain-1895_sidebar_new":{"assigned":1,"id":"etrain-1895_sidebar_new","versionedId":"etrain-1895_sidebar_new"},"etrain-1895_sidebar_old":{"assigned":0,"id":"etrain-1895_sidebar_old"}}},"etrain-1928_mroute":{"id":"etrain-1928_mroute","applied":0,"active":true,"forceVariant":0,"variants":{"etrain-1928_mroute_new":{"assigned":1,"id":"etrain-1928_mroute_new","versionedId":"etrain-1928_mroute_new_v04"},"etrain-1928_mroute_old":{"assigned":0,"id":"etrain-1928_mroute_old"}}},"etrain-2073-occup-abc":{"id":"etrain-2073-occup-abc","applied":0,"active":true,"forceVariant":0,"variants":{"etrain-2073-occup-abc_off":{"assigned":0,"id":"etrain-2073-occup-abc_off"},"etrain-2073-occup-abc_on_link":{"assigned":1,"id":"etrain-2073-occup-abc_on_link","versionedId":"etrain-2073-occup-abc_on_link_v02"},"etrain-2073-occup-abc_on_popup":{"assigned":0,"id":"etrain-2073-occup-abc_on_popup"}}},"etrain-2076-schedule-aa-test":{"id":"etrain-2076-schedule-aa-test","applied":0,"active":true,"forceVariant":0,"variants":{"etrain-2076-schedule-aa-test_a":{"assigned":1,"id":"etrain-2076-schedule-aa-test_a","versionedId":"etrain-2076-schedule-aa-test_a_v06"},"etrain-2076-schedule-aa-test_b":{"assigned":0,"id":"etrain-2076-schedule-aa-test_b"}}},"etrain-2118_mobile_color":{"id":"etrain-2118_mobile_color","applied":0,"active":true,"forceVariant":0,"variants":{"etrain-2118_mobile_color_new":{"assigned":1,"id":"etrain-2118_mobile_color_new","versionedId":"etrain-2118_mobile_color_new_v04"},"etrain-2118_mobile_color_old":{"assigned":0,"id":"etrain-2118_mobile_color_old"}}},"etrain-2118_rasp_color":{"id":"etrain-2118_rasp_color","applied":0,"active":true,"forceVariant":0,"variants":{"etrain-2118_rasp_color_new":{"assigned":1,"id":"etrain-2118_rasp_color_new","versionedId":"etrain-2118_rasp_color_new_v03"},"etrain-2118_rasp_color_old":{"assigned":0,"id":"etrain-2118_rasp_color_old"}}},"etrain-2420_show_adriver":{"id":"etrain-2420_show_adriver","applied":0,"active":true,"forceVariant":0,"variants":{"etrain-2420_show_adriver_off":{"assigned":0,"id":"etrain-2420_show_adriver_off"},"etrain-2420_show_adriver_on":{"assigned":1,"id":"etrain-2420_show_adriver_on","versionedId":"etrain-2420_show_adriver_on_v05"}}},"etrain-3639_adtech_desktop":{"id":"etrain-3639_adtech_desktop","applied":0,"active":true,"forceVariant":0,"variants":{"etrain-3639_adtech_desktop_off":{"assigned":0,"id":"etrain-3639_adtech_desktop_off"},"etrain-3639_adtech_desktop_on":{"assigned":1,"id":"etrain-3639_adtech_desktop_on","versionedId":"etrain-3639_adtech_desktop_on_v08"}}},"etrain-3639_adtech_mobile":{"id":"etrain-3639_adtech_mobile","applied":0,"active":true,"forceVariant":0,"variants":{"etrain-3639_adtech_mobile_off":{"assigned":0,"id":"etrain-3639_adtech_mobile_off"},"etrain-3639_adtech_mobile_on":{"assigned":1,"id":"etrain-3639_adtech_mobile_on","versionedId":"etrain-3639_adtech_mobile_on_v07"}}},"etrain_app_benefits_main":{"id":"etrain_app_benefits_main","applied":0,"active":true,"forceVariant":0,"variants":{"etrain_app_benefits_main_control":{"assigned":1,"id":"etrain_app_benefits_main_control","versionedId":"etrain_app_benefits_main_control"},"etrain_app_benefits_main_enabled":{"assigned":0,"id":"etrain_app_benefits_main_enabled"}}},"etrain_app_benefits_schedule":{"id":"etrain_app_benefits_schedule","applied":0,"active":true,"forceVariant":0,"variants":{"etrain_app_benefits_schedule_control":{"assigned":0,"id":"etrain_app_benefits_schedule_control"},"etrain_app_benefits_schedule_enabled":{"assigned":1,"id":"etrain_app_benefits_schedule_enabled","versionedId":"etrain_app_benefits_schedule_enabled_v02"}}},"etrain_mobile_app_banners":{"id":"etrain_mobile_app_banners","applied":0,"active":true,"forceVariant":0,"variants":{"etrain_mobile_app_banners_app_icon":{"assigned":1,"id":"etrain_mobile_app_banners_app_icon","versionedId":"etrain_mobile_app_banners_app_icon_v01"},"etrain_mobile_app_banners_lady":{"assigned":0,"id":"etrain_mobile_app_banners_lady"},"etrain_mobile_app_banners_train":{"assigned":0,"id":"etrain_mobile_app_banners_train"}}},"etrain_mobile_footer_ads":{"id":"etrain_mobile_footer_ads","applied":0,"active":true,"forceVariant":0,"variants":{"etrain_mobile_footer_ads_first":{"assigned":0,"id":"etrain_mobile_footer_ads_first"},"etrain_mobile_footer_ads_second":{"assigned":1,"id":"etrain_mobile_footer_ads_second","versionedId":"etrain_mobile_footer_ads_second_v01"}}},"feed_hotels_map_selector_andr":{"id":"feed_hotels_map_selector_andr","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1740_hotels_map_slctr_fab":{"assigned":0,"id":"VID-1740_hotels_map_slctr_fab"},"VID-1740_hotels_map_slctr_hor":{"assigned":1,"id":"VID-1740_hotels_map_slctr_hor","versionedId":"VID-1740_hotels_map_slctr_hor_v01"},"VID-1740_hotels_map_slctr_pic":{"assigned":0,"id":"VID-1740_hotels_map_slctr_pic"}}},"feed_labels_bus_ios":{"id":"feed_labels_bus_ios","applied":0,"active":true,"forceVariant":0,"variants":{"feed_labels_bus_ios_off":{"assigned":1,"id":"feed_labels_bus_ios_off","versionedId":"feed_labels_bus_ios_off_v01"},"feed_labels_bus_ios_on":{"assigned":0,"id":"feed_labels_bus_ios_on"}}},"gladkikh_test":{"id":"gladkikh_test","applied":0,"active":true,"forceVariant":0,"variants":{"off1":{"assigned":0,"id":"off1"},"on1":{"assigned":1,"id":"on1","versionedId":"on1"}}},"hotels-review-web":{"id":"hotels-review-web","applied":0,"active":true,"forceVariant":0,"variants":{"hotels-review-web-new":{"assigned":1,"id":"hotels-review-web-new","versionedId":"hotels-review-web-new_v01"},"hotels-review-web-old":{"assigned":0,"id":"hotels-review-web-old"}}},"hotels_aa_campaign":{"id":"hotels_aa_campaign","applied":0,"active":true,"forceVariant":0,"variants":{"hotels_aa_campaign_a":{"assigned":1,"id":"hotels_aa_campaign_a","versionedId":"hotels_aa_campaign_a"},"hotels_aa_campaign_b":{"assigned":0,"id":"hotels_aa_campaign_b"}}},"hotels_details_redesign":{"id":"hotels_details_redesign","applied":0,"active":true,"forceVariant":0,"variants":{"hotels_details_redesign_off":{"assigned":1,"id":"hotels_details_redesign_off","versionedId":"hotels_details_redesign_off"},"hotels_details_redesign_on":{"assigned":0,"id":"hotels_details_redesign_on"}}},"hotels_details_shortcuts":{"id":"hotels_details_shortcuts","applied":0,"active":true,"forceVariant":0,"variants":{"HOTELS-4145_shortcuts_off":{"assigned":0,"id":"HOTELS-4145_shortcuts_off"},"HOTELS-4145_shortcuts_on":{"assigned":1,"id":"HOTELS-4145_shortcuts_on","versionedId":"HOTELS-4145_shortcuts_on"}}},"hotels_edit_stories":{"id":"hotels_edit_stories","applied":0,"active":true,"forceVariant":0,"variants":{"hotels_edit_stories_off":{"assigned":0,"id":"hotels_edit_stories_off"},"hotels_edit_stories_on":{"assigned":1,"id":"hotels_edit_stories_on","versionedId":"hotels_edit_stories_on_v01"}}},"hotels_payment_on_the_spot":{"id":"hotels_payment_on_the_spot","applied":0,"active":true,"forceVariant":0,"variants":{"hotels_payment_on_the_spot_off":{"assigned":0,"id":"hotels_payment_on_the_spot_off"},"hotels_payment_on_the_spot_on":{"assigned":1,"id":"hotels_payment_on_the_spot_on","versionedId":"hotels_payment_on_the_spot_on_v01"}}},"hotels_pay_later_android":{"id":"hotels_pay_later_android","applied":0,"active":true,"forceVariant":0,"variants":{"hotels_pay_later_android_off":{"assigned":0,"id":"hotels_pay_later_android_off"},"hotels_pay_later_android_on":{"assigned":1,"id":"hotels_pay_later_android_on","versionedId":"hotels_pay_later_android_on_v01"}}},"hotels_pay_later_web":{"id":"hotels_pay_later_web","applied":0,"active":true,"forceVariant":0,"variants":{"hotels_pay_later_web_off":{"assigned":0,"id":"hotels_pay_later_web_off"},"hotels_pay_later_web_on":{"assigned":1,"id":"hotels_pay_later_web_on","versionedId":"hotels_pay_later_web_on_v07"}}},"hotels_pricing_discount":{"id":"hotels_pricing_discount","applied":0,"active":true,"forceVariant":0,"variants":{"HOTELS-3881_without_discount":{"assigned":0,"id":"HOTELS-3881_without_discount"},"HOTELS-3881_with_discount":{"assigned":1,"id":"HOTELS-3881_with_discount","versionedId":"HOTELS-3881_with_discount_v01"}}},"hotels_pricing_ladder":{"id":"hotels_pricing_ladder","applied":0,"active":true,"forceVariant":0,"variants":{"hotels_pricing_ladder_off":{"assigned":0,"id":"hotels_pricing_ladder_off"},"hotels_pricing_ladder_on":{"assigned":1,"id":"hotels_pricing_ladder_on","versionedId":"hotels_pricing_ladder_on_v01"}}},"hotels_promocode":{"id":"hotels_promocode","applied":0,"active":true,"forceVariant":0,"variants":{"hotels_promocode_off":{"assigned":0,"id":"hotels_promocode_off"},"hotels_promocode_on":{"assigned":1,"id":"hotels_promocode_on","versionedId":"hotels_promocode_on_v04"}}},"hotels_recommended_two_models":{"id":"hotels_recommended_two_models","applied":0,"active":true,"forceVariant":0,"variants":{"hotels_recommended_two_models_1":{"assigned":1,"id":"hotels_recommended_two_models_1","versionedId":"hotels_recommended_two_models_1_v01"},"hotels_recommended_two_models_2":{"assigned":0,"id":"hotels_recommended_two_models_2"}}},"hotels_redesign_map":{"id":"hotels_redesign_map","applied":0,"active":true,"forceVariant":0,"variants":{"hotels_redesign_map_off":{"assigned":0,"id":"hotels_redesign_map_off"},"hotels_redesign_map_on":{"assigned":1,"id":"hotels_redesign_map_on","versionedId":"hotels_redesign_map_on_v03"}}},"hotels_use_feauture_store_bookings":{"id":"hotels_use_feauture_store_bookings","applied":0,"active":true,"forceVariant":0,"variants":{"hotels_use_feauture_store_bookings_off":{"assigned":0,"id":"hotels_use_feauture_store_bookings_off"},"hotels_use_feauture_store_bookings_on":{"assigned":1,"id":"hotels_use_feauture_store_bookings_on","versionedId":"hotels_use_feauture_store_bookings_on_v03"}}},"logo_2023_web":{"id":"logo_2023_web","applied":0,"active":true,"forceVariant":0,"variants":{"logo_2023_web_new":{"assigned":1,"id":"logo_2023_web_new","versionedId":"logo_2023_web_new_v01"},"logo_2023_web_old":{"assigned":0,"id":"logo_2023_web_old"}}},"main_hope_button":{"id":"main_hope_button","applied":0,"active":true,"forceVariant":0,"variants":{"main_hope_button_hope":{"assigned":1,"id":"main_hope_button_hope","versionedId":"main_hope_button_hope_v01"},"main_hope_button_map":{"assigned":0,"id":"main_hope_button_map"},"main_hope_button_status":{"assigned":0,"id":"main_hope_button_status"}}},"main_page_ae_tab_desktop":{"id":"main_page_ae_tab_desktop","applied":0,"active":true,"forceVariant":0,"variants":{"main_page_ae_tab_desktop_off":{"assigned":0,"id":"main_page_ae_tab_desktop_off"},"main_page_ae_tab_desktop_on":{"assigned":1,"id":"main_page_ae_tab_desktop_on","versionedId":"main_page_ae_tab_desktop_on_v03"}}},"main_page_ae_tab_mobile":{"id":"main_page_ae_tab_mobile","applied":0,"active":true,"forceVariant":0,"variants":{"main_page_ae_tab_mobile_off":{"assigned":0,"id":"main_page_ae_tab_mobile_off"},"main_page_ae_tab_mobile_on":{"assigned":1,"id":"main_page_ae_tab_mobile_on","versionedId":"main_page_ae_tab_mobile_on_v03"}}},"main_page_big_icon":{"id":"main_page_big_icon","applied":0,"active":true,"forceVariant":0,"variants":{"CF-3786_main_page_big_icon_off":{"assigned":0,"id":"CF-3786_main_page_big_icon_off"},"CF-3786_main_page_big_icon_on":{"assigned":1,"id":"CF-3786_main_page_big_icon_on","versionedId":"CF-3786_main_page_big_icon_on_v01"}}},"main_page_corporate_tab":{"id":"main_page_corporate_tab","applied":0,"active":true,"forceVariant":0,"variants":{"main_page_corporate_tab_off":{"assigned":0,"id":"main_page_corporate_tab_off"},"main_page_corporate_tab_on":{"assigned":1,"id":"main_page_corporate_tab_on","versionedId":"main_page_corporate_tab_on_v01"}}},"main_page_mb_hat_auth_simple":{"id":"main_page_mb_hat_auth_simple","applied":0,"active":true,"forceVariant":0,"variants":{"main_page_mb_hat_auth_simple_off":{"assigned":0,"id":"main_page_mb_hat_auth_simple_off"},"main_page_mb_hat_auth_simple_on":{"assigned":1,"id":"main_page_mb_hat_auth_simple_on","versionedId":"main_page_mb_hat_auth_simple_on_v01"}}},"main_ptt_popup":{"id":"main_ptt_popup","applied":0,"active":true,"forceVariant":0,"variants":{"main_ptt_popup_off":{"assigned":0,"id":"main_ptt_popup_off"},"main_ptt_popup_on":{"assigned":1,"id":"main_ptt_popup_on","versionedId":"main_ptt_popup_on_v01"}}},"main_ptt_popup_test":{"id":"main_ptt_popup_test","applied":0,"active":true,"forceVariant":0,"variants":{"main_ptt_popup_test_off":{"assigned":0,"id":"main_ptt_popup_test_off"},"main_ptt_popup_test_on":{"assigned":1,"id":"main_ptt_popup_test_on","versionedId":"main_ptt_popup_test_on"}}},"MAPP-5290_recommendation_avia":{"id":"MAPP-5290_recommendation_avia","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-5290_rec_avia":{"assigned":0,"id":"MAPP-5290_rec_avia"},"MAPP-5290_rec_nopush_avia":{"assigned":0,"id":"MAPP-5290_rec_nopush_avia"},"MAPP-5290_rec_static_avia":{"assigned":1,"id":"MAPP-5290_rec_static_avia","versionedId":"MAPP-5290_rec_static_avia"}}},"MAPP-5290_recommendation_train":{"id":"MAPP-5290_recommendation_train","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-5290_rec_nopush_train":{"assigned":0,"id":"MAPP-5290_rec_nopush_train"},"MAPP-5290_rec_static_train":{"assigned":0,"id":"MAPP-5290_rec_static_train"},"MAPP-5290_rec_train":{"assigned":1,"id":"MAPP-5290_rec_train","versionedId":"MAPP-5290_rec_train"}}},"MAPP-5942_viewed_hotels":{"id":"MAPP-5942_viewed_hotels","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-5942_viewed_hotels":{"assigned":0,"id":"MAPP-5942_viewed_hotels"},"MAPP-5942_viewed_hotels_nopush":{"assigned":1,"id":"MAPP-5942_viewed_hotels_nopush","versionedId":"MAPP-5942_viewed_hotels_nopush"}}},"MAPP-7241_tariffs_on_details":{"id":"MAPP-7241_tariffs_on_details","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-7241_tariffs_olds":{"assigned":0,"id":"MAPP-7241_tariffs_olds"},"MAPP-7241_tariff_expandable_cards":{"assigned":0,"id":"MAPP-7241_tariff_expandable_cards"},"MAPP-7241_tariff_scrollable_cards":{"assigned":1,"id":"MAPP-7241_tariff_scrollable_cards","versionedId":"MAPP-7241_tariff_scrollable_cards_v01"}}},"MAPP-7378_ios_tariffs_on_details":{"id":"MAPP-7378_ios_tariffs_on_details","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-7378_ios_tariffs_expandable_cards":{"assigned":0,"id":"MAPP-7378_ios_tariffs_expandable_cards"},"MAPP-7378_ios_tariffs_old":{"assigned":0,"id":"MAPP-7378_ios_tariffs_old"},"MAPP-7378_ios_tariffs_scrollable_cards":{"assigned":1,"id":"MAPP-7378_ios_tariffs_scrollable_cards","versionedId":"MAPP-7378_ios_tariffs_scrollable_cards"}}},"MAPP-logo_2023_android":{"id":"MAPP-logo_2023_android","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-logo_2023_android_new":{"assigned":1,"id":"MAPP-logo_2023_android_new","versionedId":"MAPP-logo_2023_android_new_v01"},"MAPP-logo_2023_android_old":{"assigned":0,"id":"MAPP-logo_2023_android_old"}}},"MAPP-logo_2023_ios":{"id":"MAPP-logo_2023_ios","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-logo_2023_ios_new":{"assigned":1,"id":"MAPP-logo_2023_ios_new","versionedId":"MAPP-logo_2023_ios_new_v01"},"MAPP-logo_2023_ios_old":{"assigned":0,"id":"MAPP-logo_2023_ios_old"}}},"martech_mainpage_geo_block":{"id":"martech_mainpage_geo_block","applied":0,"active":true,"forceVariant":0,"variants":{"MARTECH-24_geo":{"assigned":1,"id":"MARTECH-24_geo","versionedId":"MARTECH-24_geo_v01"},"MARTECH-24_stories":{"assigned":0,"id":"MARTECH-24_stories"}}},"mono_avia_android_ptt_banner":{"id":"mono_avia_android_ptt_banner","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-8013-android-ptt-hide-banner":{"assigned":0,"id":"MAPP-8013-android-ptt-hide-banner"},"MAPP-8013-android-ptt-show-banner":{"assigned":1,"id":"MAPP-8013-android-ptt-show-banner","versionedId":"MAPP-8013-android-ptt-show-banner_v02"}}},"mono_avia_ios_ptt_banner":{"id":"mono_avia_ios_ptt_banner","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-7932-ios-ptt-hide-banner":{"assigned":0,"id":"MAPP-7932-ios-ptt-hide-banner"},"MAPP-7932-ios-ptt-show-banner":{"assigned":1,"id":"MAPP-7932-ios-ptt-show-banner","versionedId":"MAPP-7932-ios-ptt-show-banner_v02"}}},"ptt_android_feed_hotels_favourites":{"id":"ptt_android_feed_hotels_favourites","applied":0,"active":true,"forceVariant":0,"variants":{"ptt_android_feed_hotels_favourites_off":{"assigned":0,"id":"ptt_android_feed_hotels_favourites_off"},"ptt_android_feed_hotels_favourites_on":{"assigned":1,"id":"ptt_android_feed_hotels_favourites_on","versionedId":"ptt_android_feed_hotels_favourites_on_v01"}}},"ptt_android_feed_hotels_new_rooms":{"id":"ptt_android_feed_hotels_new_rooms","applied":0,"active":true,"forceVariant":0,"variants":{"ptt_android_feed_hotels_new_rooms_off":{"assigned":1,"id":"ptt_android_feed_hotels_new_rooms_off","versionedId":"ptt_android_feed_hotels_new_rooms_off"},"ptt_android_feed_hotels_new_rooms_on":{"assigned":0,"id":"ptt_android_feed_hotels_new_rooms_on"}}},"ptt_android_feed_hotels_offers":{"id":"ptt_android_feed_hotels_offers","applied":0,"active":true,"forceVariant":0,"variants":{"ptt_android_feed_hotels_offers_off":{"assigned":0,"id":"ptt_android_feed_hotels_offers_off"},"ptt_android_feed_hotels_offers_on":{"assigned":1,"id":"ptt_android_feed_hotels_offers_on","versionedId":"ptt_android_feed_hotels_offers_on_v01"}}},"ptt_android_feed_mtp":{"id":"ptt_android_feed_mtp","applied":0,"active":true,"forceVariant":0,"variants":{"ptt_android_feed_mtp_off":{"assigned":0,"id":"ptt_android_feed_mtp_off"},"ptt_android_feed_mtp_on":{"assigned":1,"id":"ptt_android_feed_mtp_on","versionedId":"ptt_android_feed_mtp_on_v02"}}},"ptt_android_feed_train_price_calculation_for_child":{"id":"ptt_android_feed_train_price_calculation_for_child","applied":0,"active":true,"forceVariant":0,"variants":{"VID-3165_disable":{"assigned":0,"id":"VID-3165_disable"},"VID-3165_enable":{"assigned":1,"id":"VID-3165_enable","versionedId":"VID-3165_enable_v02"}}},"ptt_android_new_search_form_v3":{"id":"ptt_android_new_search_form_v3","applied":0,"active":true,"forceVariant":0,"variants":{"VID-3636_off":{"assigned":0,"id":"VID-3636_off"},"VID-3636_on":{"assigned":1,"id":"VID-3636_on","versionedId":"VID-3636_on_v01"}}},"ptt_android_search_tours":{"id":"ptt_android_search_tours","applied":0,"active":true,"forceVariant":0,"variants":{"VID-3505_off":{"assigned":0,"id":"VID-3505_off"},"VID-3505_on":{"assigned":1,"id":"VID-3505_on","versionedId":"VID-3505_on_v01"}}},"ptt_android_search_with_return":{"id":"ptt_android_search_with_return","applied":0,"active":true,"forceVariant":0,"variants":{"VID-3951_off":{"assigned":0,"id":"VID-3951_off"},"VID-3951_on":{"assigned":1,"id":"VID-3951_on","versionedId":"VID-3951_on"}}},"ptt_feed_cards_spacing_an2":{"id":"ptt_feed_cards_spacing_an2","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1764_cards_spacing_ab2_off":{"assigned":0,"id":"VID-1764_cards_spacing_ab2_off"},"VID-1764_cards_spacing_ab2_on":{"assigned":1,"id":"VID-1764_cards_spacing_ab2_on","versionedId":"VID-1764_cards_spacing_ab2_on_v01"}}},"ptt_feed_htl_fltrs_design_andr":{"id":"ptt_feed_htl_fltrs_design_andr","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1991_off":{"assigned":0,"id":"VID-1991_off"},"VID-1991_on":{"assigned":1,"id":"VID-1991_on","versionedId":"VID-1991_on_v01"}}},"ptt_feed_lazy_hotels_andr2":{"id":"ptt_feed_lazy_hotels_andr2","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1973_off":{"assigned":0,"id":"VID-1973_off"},"VID-1973_on":{"assigned":1,"id":"VID-1973_on","versionedId":"VID-1973_on_v01"}}},"ptt_feed_nearby_dates_andr3":{"id":"ptt_feed_nearby_dates_andr3","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1970_off":{"assigned":0,"id":"VID-1970_off"},"VID-1970_on":{"assigned":1,"id":"VID-1970_on","versionedId":"VID-1970_on_v01"}}},"ptt_feed_nearest_dates_ios_v2":{"id":"ptt_feed_nearest_dates_ios_v2","applied":0,"active":true,"forceVariant":0,"variants":{"VID-2063_dates_off":{"assigned":0,"id":"VID-2063_dates_off"},"VID-2063_dates_on":{"assigned":1,"id":"VID-2063_dates_on","versionedId":"VID-2063_dates_on_v02"}}},"ptt_hotels_checkout_skip_cart_an":{"id":"ptt_hotels_checkout_skip_cart_an","applied":0,"active":true,"forceVariant":0,"variants":{"HOTELS-3912_keep_cart":{"assigned":0,"id":"HOTELS-3912_keep_cart"},"HOTELS-3912_skip_cart":{"assigned":1,"id":"HOTELS-3912_skip_cart","versionedId":"HOTELS-3912_skip_cart"}}},"ptt_hotels_choose_rooms_an":{"id":"ptt_hotels_choose_rooms_an","applied":0,"active":true,"forceVariant":0,"variants":{"HOTELS-3218_new_choose_rooms":{"assigned":1,"id":"HOTELS-3218_new_choose_rooms","versionedId":"HOTELS-3218_new_choose_rooms"},"HOTELS-3218_old_choose_rooms":{"assigned":0,"id":"HOTELS-3218_old_choose_rooms"}}},"ptt_hotels_choose_rooms_ios":{"id":"ptt_hotels_choose_rooms_ios","applied":0,"active":true,"forceVariant":0,"variants":{"HOTELS-3132_new_choose_rooms":{"assigned":1,"id":"HOTELS-3132_new_choose_rooms","versionedId":"HOTELS-3132_new_choose_rooms"},"HOTELS-3132_old_choose_rooms":{"assigned":0,"id":"HOTELS-3132_old_choose_rooms"}}},"ptt_hotel_details_redesign":{"id":"ptt_hotel_details_redesign","applied":0,"active":true,"forceVariant":0,"variants":{"HOTELS-2815_redesign_off":{"assigned":0,"id":"HOTELS-2815_redesign_off"},"HOTELS-2815_redesign_on":{"assigned":1,"id":"HOTELS-2815_redesign_on","versionedId":"HOTELS-2815_redesign_on_v01"}}},"ptt_hotel_details_search_form_v2":{"id":"ptt_hotel_details_search_form_v2","applied":0,"active":true,"forceVariant":0,"variants":{"HOTELS-3154_search_form_off":{"assigned":0,"id":"HOTELS-3154_search_form_off"},"HOTELS-3154_search_form_on":{"assigned":1,"id":"HOTELS-3154_search_form_on","versionedId":"HOTELS-3154_search_form_on_v01"}}},"ptt_hotel_filters_design_ios":{"id":"ptt_hotel_filters_design_ios","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1993_new_design":{"assigned":1,"id":"VID-1993_new_design","versionedId":"VID-1993_new_design_v01"},"VID-1993_old_design":{"assigned":0,"id":"VID-1993_old_design"}}},"ptt_ios_feed_hotels_favourites":{"id":"ptt_ios_feed_hotels_favourites","applied":0,"active":true,"forceVariant":0,"variants":{"ptt_ios_feed_hotels_favourites_off":{"assigned":0,"id":"ptt_ios_feed_hotels_favourites_off"},"ptt_ios_feed_hotels_favourites_on":{"assigned":1,"id":"ptt_ios_feed_hotels_favourites_on","versionedId":"ptt_ios_feed_hotels_favourites_on_v01"}}},"ptt_ios_feed_hotels_new_rooms":{"id":"ptt_ios_feed_hotels_new_rooms","applied":0,"active":true,"forceVariant":0,"variants":{"ptt_ios_feed_hotels_new_rooms_off":{"assigned":0,"id":"ptt_ios_feed_hotels_new_rooms_off"},"ptt_ios_feed_hotels_new_rooms_on":{"assigned":1,"id":"ptt_ios_feed_hotels_new_rooms_on","versionedId":"ptt_ios_feed_hotels_new_rooms_on"}}},"ptt_ios_feed_hotels_offers":{"id":"ptt_ios_feed_hotels_offers","applied":0,"active":true,"forceVariant":0,"variants":{"ptt_ios_feed_hotels_offers_off":{"assigned":0,"id":"ptt_ios_feed_hotels_offers_off"},"ptt_ios_feed_hotels_offers_on":{"assigned":1,"id":"ptt_ios_feed_hotels_offers_on","versionedId":"ptt_ios_feed_hotels_offers_on_v01"}}},"ptt_ios_mtp_feed":{"id":"ptt_ios_mtp_feed","applied":0,"active":true,"forceVariant":0,"variants":{"ptt_ios_mtp_feed_off":{"assigned":0,"id":"ptt_ios_mtp_feed_off"},"ptt_ios_mtp_feed_on":{"assigned":1,"id":"ptt_ios_mtp_feed_on","versionedId":"ptt_ios_mtp_feed_on_v03"}}},"ptt_ios_not_selling_offers_in_filter":{"id":"ptt_ios_not_selling_offers_in_filter","applied":0,"active":true,"forceVariant":0,"variants":{"VID-3414_not_selling_in_filters":{"assigned":1,"id":"VID-3414_not_selling_in_filters","versionedId":"VID-3414_not_selling_in_filters_v01"},"VID-3414_only_selling_in_filters":{"assigned":0,"id":"VID-3414_only_selling_in_filters"}}},"ptt_ios_train_new_prices_for_kids":{"id":"ptt_ios_train_new_prices_for_kids","applied":0,"active":true,"forceVariant":0,"variants":{"VID-3146_prices_new":{"assigned":1,"id":"VID-3146_prices_new","versionedId":"VID-3146_prices_new_v02"},"VID-3146_prices_old":{"assigned":0,"id":"VID-3146_prices_old"}}},"ptt_map_selector_in_header_an":{"id":"ptt_map_selector_in_header_an","applied":0,"active":true,"forceVariant":0,"variants":{"VID-2255_default":{"assigned":0,"id":"VID-2255_default"},"VID-2255_in_header":{"assigned":1,"id":"VID-2255_in_header","versionedId":"VID-2255_in_header_v01"}}},"ptt_new_avia_offer_item_an":{"id":"ptt_new_avia_offer_item_an","applied":0,"active":true,"forceVariant":0,"variants":{"VID-2717_off":{"assigned":0,"id":"VID-2717_off"},"VID-2717_on":{"assigned":1,"id":"VID-2717_on","versionedId":"VID-2717_on_v01"}}},"ptt_new_bus_offer_item_an":{"id":"ptt_new_bus_offer_item_an","applied":0,"active":true,"forceVariant":0,"variants":{"VID-2591_off":{"assigned":0,"id":"VID-2591_off"},"VID-2591_on":{"assigned":1,"id":"VID-2591_on","versionedId":"VID-2591_on_v01"}}},"ptt_new_hotel_offer_item_an":{"id":"ptt_new_hotel_offer_item_an","applied":0,"active":true,"forceVariant":0,"variants":{"VID-2382_off":{"assigned":0,"id":"VID-2382_off"},"VID-2382_on":{"assigned":1,"id":"VID-2382_on","versionedId":"VID-2382_on_v01"}}},"ptt_new_train_offer_item_android2":{"id":"ptt_new_train_offer_item_android2","applied":0,"active":true,"forceVariant":0,"variants":{"VID-2870_new_horizontal2":{"assigned":1,"id":"VID-2870_new_horizontal2","versionedId":"VID-2870_new_horizontal2_v01"},"VID-2870_new_vertical2":{"assigned":0,"id":"VID-2870_new_vertical2"},"VID-2870_old2":{"assigned":0,"id":"VID-2870_old2"}}},"ptt_recomm_avia_offers_andr2":{"id":"ptt_recomm_avia_offers_andr2","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1889_2_off":{"assigned":0,"id":"VID-1889_2_off"},"VID-1889_2_on":{"assigned":1,"id":"VID-1889_2_on","versionedId":"VID-1889_2_on_v01"}}},"SEOTOOLS-309_geocontent_ptt_bann":{"id":"SEOTOOLS-309_geocontent_ptt_bann","applied":0,"active":true,"forceVariant":0,"variants":{"SEOTOOLS-309_without_banner":{"assigned":0,"id":"SEOTOOLS-309_without_banner"},"SEOTOOLS-309_with_banner":{"assigned":1,"id":"SEOTOOLS-309_with_banner","versionedId":"SEOTOOLS-309_with_banner"}}},"SF-545-recommendation-labels":{"id":"SF-545-recommendation-labels","applied":0,"active":true,"forceVariant":0,"variants":{"SF-545-recommendation-labels-off":{"assigned":0,"id":"SF-545-recommendation-labels-off"},"SF-545-recommendation-labels-on":{"assigned":1,"id":"SF-545-recommendation-labels-on","versionedId":"SF-545-recommendation-labels-on_v01"}}},"SF-615-details-price-diff":{"id":"SF-615-details-price-diff","applied":0,"active":true,"forceVariant":0,"variants":{"SF-615-details-price-diff-off":{"assigned":0,"id":"SF-615-details-price-diff-off"},"SF-615-details-price-diff-on":{"assigned":1,"id":"SF-615-details-price-diff-on","versionedId":"SF-615-details-price-diff-on_v01"}}},"sf_show_tariff_cabbin_luggage_info":{"id":"sf_show_tariff_cabbin_luggage_info","applied":0,"active":true,"forceVariant":0,"variants":{"sf_show_tariff_cabbin_luggage_info_hide":{"assigned":0,"id":"sf_show_tariff_cabbin_luggage_info_hide"},"sf_show_tariff_cabbin_luggage_info_show":{"assigned":1,"id":"sf_show_tariff_cabbin_luggage_info_show","versionedId":"sf_show_tariff_cabbin_luggage_info_show_v01"}}},"skip_details_bus_ios":{"id":"skip_details_bus_ios","applied":0,"active":true,"forceVariant":0,"variants":{"skip_details_bus_ios_off":{"assigned":0,"id":"skip_details_bus_ios_off"},"skip_details_bus_ios_on":{"assigned":1,"id":"skip_details_bus_ios_on","versionedId":"skip_details_bus_ios_on_v01"}}},"SPL-243-seats-s7-ios":{"id":"SPL-243-seats-s7-ios","applied":0,"active":true,"forceVariant":0,"variants":{"SPL-243-seats-s7-ios-off":{"assigned":0,"id":"SPL-243-seats-s7-ios-off"},"SPL-243-seats-s7-ios-on":{"assigned":1,"id":"SPL-243-seats-s7-ios-on","versionedId":"SPL-243-seats-s7-ios-on_v05"}}},"SPL-243-seats-s7-web":{"id":"SPL-243-seats-s7-web","applied":0,"active":true,"forceVariant":0,"variants":{"SPL-243-seats-s7-web-off":{"assigned":0,"id":"SPL-243-seats-s7-web-off"},"SPL-243-seats-s7-web-on":{"assigned":1,"id":"SPL-243-seats-s7-web-on","versionedId":"SPL-243-seats-s7-web-on_v04"}}},"SPL-428-s7_seats_prices":{"id":"SPL-428-s7_seats_prices","applied":0,"active":true,"forceVariant":0,"variants":{"SPL-428-s7_seats_prices-50":{"assigned":1,"id":"SPL-428-s7_seats_prices-50","versionedId":"SPL-428-s7_seats_prices-50_v01"},"SPL-428-s7_seats_prices-70":{"assigned":0,"id":"SPL-428-s7_seats_prices-70"},"SPL-428-s7_seats_prices-old":{"assigned":0,"id":"SPL-428-s7_seats_prices-old"}}},"SPL-445-upsale_texts_android":{"id":"SPL-445-upsale_texts_android","applied":0,"active":true,"forceVariant":0,"variants":{"SPL-445-upsale_texts_android_new":{"assigned":1,"id":"SPL-445-upsale_texts_android_new","versionedId":"SPL-445-upsale_texts_android_new_v01"},"SPL-445-upsale_texts_android_old":{"assigned":0,"id":"SPL-445-upsale_texts_android_old"}}},"SPL-445-upsale_texts_ios":{"id":"SPL-445-upsale_texts_ios","applied":0,"active":true,"forceVariant":0,"variants":{"SPL-445-upsale_texts_ios_new":{"assigned":1,"id":"SPL-445-upsale_texts_ios_new","versionedId":"SPL-445-upsale_texts_ios_new_v01"},"SPL-445-upsale_texts_ios_old":{"assigned":0,"id":"SPL-445-upsale_texts_ios_old"}}},"SPL-445-upsale_texts_web":{"id":"SPL-445-upsale_texts_web","applied":0,"active":true,"forceVariant":0,"variants":{"SPL-445-upsale_texts_web_new":{"assigned":1,"id":"SPL-445-upsale_texts_web_new","versionedId":"SPL-445-upsale_texts_web_new_v05"},"SPL-445-upsale_texts_web_old":{"assigned":0,"id":"SPL-445-upsale_texts_web_old"}}},"test_local_net_filter":{"id":"test_local_net_filter","applied":0,"active":true,"forceVariant":0,"variants":{"test_local_net_filter_off_a":{"assigned":1,"id":"test_local_net_filter_off_a","versionedId":"test_local_net_filter_off_a"},"test_local_net_filter_off_b":{"assigned":0,"id":"test_local_net_filter_off_b"}}},"tours_progressbar_buying":{"id":"tours_progressbar_buying","applied":0,"active":true,"forceVariant":0,"variants":{"tours_progressbar_buying_off":{"assigned":0,"id":"tours_progressbar_buying_off"},"tours_progressbar_buying_on":{"assigned":1,"id":"tours_progressbar_buying_on","versionedId":"tours_progressbar_buying_on_v03"}}},"tours_scenario_recommendation":{"id":"tours_scenario_recommendation","applied":0,"active":true,"forceVariant":0,"variants":{"tours_scenario_recommend_card":{"assigned":0,"id":"tours_scenario_recommend_card"},"tours_scenario_recommend_off":{"assigned":0,"id":"tours_scenario_recommend_off"},"tours_scenario_recommend_stamp":{"assigned":1,"id":"tours_scenario_recommend_stamp","versionedId":"tours_scenario_recommend_stamp_v04"},"tours_scenario_recommend_stat":{"assigned":0,"id":"tours_scenario_recommend_stat"}}},"tours_transfer_icon":{"id":"tours_transfer_icon","applied":0,"active":true,"forceVariant":0,"variants":{"tours_transfer_icon_hide":{"assigned":1,"id":"tours_transfer_icon_hide","versionedId":"tours_transfer_icon_hide_v02"},"tours_transfer_icon_new":{"assigned":0,"id":"tours_transfer_icon_new"},"tours_transfer_icon_old":{"assigned":0,"id":"tours_transfer_icon_old"}}},"tour_search_filter_question":{"id":"tour_search_filter_question","applied":0,"active":true,"forceVariant":0,"variants":{"tour_search_filter_question_off":{"assigned":0,"id":"tour_search_filter_question_off"},"tour_search_filter_question_on":{"assigned":1,"id":"tour_search_filter_question_on","versionedId":"tour_search_filter_question_on_v02"}}},"train_adaptive_main_zd":{"id":"train_adaptive_main_zd","applied":0,"active":true,"forceVariant":0,"variants":{"train_adaptive_main_zd_off":{"assigned":0,"id":"train_adaptive_main_zd_off"},"train_adaptive_main_zd_on":{"assigned":1,"id":"train_adaptive_main_zd_on","versionedId":"train_adaptive_main_zd_on_v05"}}},"train_android_scheme_v3":{"id":"train_android_scheme_v3","applied":0,"active":true,"forceVariant":0,"variants":{"train_android_scheme_v3_off":{"assigned":0,"id":"train_android_scheme_v3_off"},"train_android_scheme_v3_on":{"assigned":1,"id":"train_android_scheme_v3_on","versionedId":"train_android_scheme_v3_on_v02"}}},"train_autochoice4":{"id":"train_autochoice4","applied":0,"active":true,"forceVariant":0,"variants":{"train_autochoice4_filter":{"assigned":0,"id":"train_autochoice4_filter"},"train_autochoice4_off":{"assigned":0,"id":"train_autochoice4_off"},"train_autochoice4_old":{"assigned":0,"id":"train_autochoice4_old"},"train_autochoice4_rm_button":{"assigned":1,"id":"train_autochoice4_rm_button","versionedId":"train_autochoice4_rm_button_v01"},"train_autochoice4_single_button":{"assigned":0,"id":"train_autochoice4_single_button"}}},"train_autoticketing_new_wizard":{"id":"train_autoticketing_new_wizard","applied":0,"active":true,"forceVariant":0,"variants":{"train_autoticketing_new_wizard_off":{"assigned":0,"id":"train_autoticketing_new_wizard_off"},"train_autoticketing_new_wizard_on":{"assigned":1,"id":"train_autoticketing_new_wizard_on","versionedId":"train_autoticketing_new_wizard_on_v03"}}},"train_bu_pricing_adr":{"id":"train_bu_pricing_adr","applied":0,"active":true,"forceVariant":0,"variants":{"train_bu_pricing_adr_20220324":{"assigned":1,"id":"train_bu_pricing_adr_20220324","versionedId":"train_bu_pricing_adr_20220324_v02"},"train_bu_pricing_adr_20220607_dn":{"assigned":0,"id":"train_bu_pricing_adr_20220607_dn"},"train_bu_pricing_adr_20220607_up":{"assigned":0,"id":"train_bu_pricing_adr_20220607_up"},"train_bu_pricing_adr_off":{"assigned":0,"id":"train_bu_pricing_adr_off"}}},"train_bu_pricing_ios":{"id":"train_bu_pricing_ios","applied":0,"active":true,"forceVariant":0,"variants":{"train_bu_pricing_ios_20220324":{"assigned":1,"id":"train_bu_pricing_ios_20220324","versionedId":"train_bu_pricing_ios_20220324_v02"},"train_bu_pricing_ios_20220607_dn":{"assigned":0,"id":"train_bu_pricing_ios_20220607_dn"},"train_bu_pricing_ios_20220607_up":{"assigned":0,"id":"train_bu_pricing_ios_20220607_up"},"train_bu_pricing_ios_off":{"assigned":0,"id":"train_bu_pricing_ios_off"}}},"train_bu_pricing_web":{"id":"train_bu_pricing_web","applied":0,"active":true,"forceVariant":0,"variants":{"train_bu_pricing_web_20220324":{"assigned":1,"id":"train_bu_pricing_web_20220324","versionedId":"train_bu_pricing_web_20220324_v02"},"train_bu_pricing_web_20220607_dn":{"assigned":0,"id":"train_bu_pricing_web_20220607_dn"},"train_bu_pricing_web_20220607_up":{"assigned":0,"id":"train_bu_pricing_web_20220607_up"},"train_bu_pricing_web_anl_9819":{"assigned":0,"id":"train_bu_pricing_web_anl_9819"},"train_bu_pricing_web_off":{"assigned":0,"id":"train_bu_pricing_web_off"}}},"train_checkout_seats":{"id":"train_checkout_seats","applied":0,"active":true,"forceVariant":0,"variants":{"train_checkout_seats_off":{"assigned":0,"id":"train_checkout_seats_off"},"train_checkout_seats_on":{"assigned":1,"id":"train_checkout_seats_on","versionedId":"train_checkout_seats_on_v01"}}},"train_form_suggest_history":{"id":"train_form_suggest_history","applied":0,"active":true,"forceVariant":0,"variants":{"train_form_suggest_history_off":{"assigned":0,"id":"train_form_suggest_history_off"},"train_form_suggest_history_on":{"assigned":1,"id":"train_form_suggest_history_on","versionedId":"train_form_suggest_history_on_v01"}}},"train_insurance_description":{"id":"train_insurance_description","applied":0,"active":true,"forceVariant":0,"variants":{"train_insurance_desc_all":{"assigned":0,"id":"train_insurance_desc_all"},"train_insurance_desc_off":{"assigned":0,"id":"train_insurance_desc_off"},"train_insurance_desc_soft":{"assigned":1,"id":"train_insurance_desc_soft","versionedId":"train_insurance_desc_soft_v02"}}},"train_ios_scheme_v3":{"id":"train_ios_scheme_v3","applied":0,"active":true,"forceVariant":0,"variants":{"train_ios_scheme_v3_off":{"assigned":0,"id":"train_ios_scheme_v3_off"},"train_ios_scheme_v3_on":{"assigned":1,"id":"train_ios_scheme_v3_on","versionedId":"train_ios_scheme_v3_on_v01"}}},"train_main_ptt_banner":{"id":"train_main_ptt_banner","applied":0,"active":true,"forceVariant":0,"variants":{"train_main_ptt_banner_autochoose":{"assigned":0,"id":"train_main_ptt_banner_autochoose"},"train_main_ptt_banner_base":{"assigned":1,"id":"train_main_ptt_banner_base","versionedId":"train_main_ptt_banner_base_v01"},"train_main_ptt_banner_calendar":{"assigned":0,"id":"train_main_ptt_banner_calendar"},"train_main_ptt_banner_disabled":{"assigned":0,"id":"train_main_ptt_banner_disabled"},"train_main_ptt_banner_info_service":{"assigned":0,"id":"train_main_ptt_banner_info_service"},"train_main_ptt_banner_offline":{"assigned":0,"id":"train_main_ptt_banner_offline"},"train_main_ptt_banner_refund":{"assigned":0,"id":"train_main_ptt_banner_refund"}}},"train_mini_form_scroll":{"id":"train_mini_form_scroll","applied":0,"active":true,"forceVariant":0,"variants":{"train_mini_form_scroll_off":{"assigned":0,"id":"train_mini_form_scroll_off"},"train_mini_form_scroll_on":{"assigned":1,"id":"train_mini_form_scroll_on","versionedId":"train_mini_form_scroll_on_v01"}}},"train_mono_android_sales_closed_description":{"id":"train_mono_android_sales_closed_description","applied":0,"active":true,"forceVariant":0,"variants":{"train_mono_android_sales_closed_description_off":{"assigned":0,"id":"train_mono_android_sales_closed_description_off"},"train_mono_android_sales_closed_description_on":{"assigned":1,"id":"train_mono_android_sales_closed_description_on","versionedId":"train_mono_android_sales_closed_description_on_v01"}}},"train_mono_checkout_nevsky_android":{"id":"train_mono_checkout_nevsky_android","applied":0,"active":true,"forceVariant":0,"variants":{"train_mono_checkout_nevsky_android_off":{"assigned":0,"id":"train_mono_checkout_nevsky_android_off"},"train_mono_checkout_nevsky_android_on":{"assigned":1,"id":"train_mono_checkout_nevsky_android_on","versionedId":"train_mono_checkout_nevsky_android_on_v01"}}},"train_mono_ios_sales_closed_description":{"id":"train_mono_ios_sales_closed_description","applied":0,"active":true,"forceVariant":0,"variants":{"train_mono_ios_sales_closed_description_off":{"assigned":0,"id":"train_mono_ios_sales_closed_description_off"},"train_mono_ios_sales_closed_description_on":{"assigned":1,"id":"train_mono_ios_sales_closed_description_on","versionedId":"train_mono_ios_sales_closed_description_on_v02"}}},"train_mono_new_schedule_android":{"id":"train_mono_new_schedule_android","applied":0,"active":true,"forceVariant":0,"variants":{"train_mono_new_schedule_android_off":{"assigned":0,"id":"train_mono_new_schedule_android_off"},"train_mono_new_schedule_android_on":{"assigned":1,"id":"train_mono_new_schedule_android_on","versionedId":"train_mono_new_schedule_android_on_v05"}}},"train_mono_new_schedule_ios":{"id":"train_mono_new_schedule_ios","applied":0,"active":true,"forceVariant":0,"variants":{"train_mono_new_schedule_ios_off":{"assigned":0,"id":"train_mono_new_schedule_ios_off"},"train_mono_new_schedule_ios_on":{"assigned":1,"id":"train_mono_new_schedule_ios_on","versionedId":"train_mono_new_schedule_ios_on_v06"}}},"train_new_alfa_insurance_api":{"id":"train_new_alfa_insurance_api","applied":0,"active":true,"forceVariant":0,"variants":{"train_new_alfa_insurance_api_off":{"assigned":0,"id":"train_new_alfa_insurance_api_off"},"train_new_alfa_insurance_api_on":{"assigned":1,"id":"train_new_alfa_insurance_api_on","versionedId":"train_new_alfa_insurance_api_on_v02"}}},"train_passengers_rzd_bonus":{"id":"train_passengers_rzd_bonus","applied":0,"active":true,"forceVariant":0,"variants":{"train_passengers_rzd_bonus_off":{"assigned":0,"id":"train_passengers_rzd_bonus_off"},"train_passengers_rzd_bonus_on":{"assigned":1,"id":"train_passengers_rzd_bonus_on","versionedId":"train_passengers_rzd_bonus_on_v01"}}},"train_pricing_strategy":{"id":"train_pricing_strategy","applied":0,"active":true,"forceVariant":0,"variants":{"train_pricing_strategy_4438aid5":{"assigned":0,"id":"train_pricing_strategy_4438aid5"},"train_pricing_strategy_4438aii10":{"assigned":0,"id":"train_pricing_strategy_4438aii10"},"train_pricing_strategy_4438aii5":{"assigned":0,"id":"train_pricing_strategy_4438aii5"},"train_pricing_strategy_4438dc20":{"assigned":0,"id":"train_pricing_strategy_4438dc20"},"train_pricing_strategy_4438dc23":{"assigned":0,"id":"train_pricing_strategy_4438dc23"},"train_pricing_strategy_4438dd5":{"assigned":0,"id":"train_pricing_strategy_4438dd5"},"train_pricing_strategy_4438depth":{"assigned":0,"id":"train_pricing_strategy_4438depth"},"train_pricing_strategy_4438di10":{"assigned":0,"id":"train_pricing_strategy_4438di10"},"train_pricing_strategy_4438di5":{"assigned":0,"id":"train_pricing_strategy_4438di5"},"train_pricing_strategy_4438dwn10":{"assigned":0,"id":"train_pricing_strategy_4438dwn10"},"train_pricing_strategy_4438dwn4":{"assigned":0,"id":"train_pricing_strategy_4438dwn4"},"train_pricing_strategy_4438dwn5":{"assigned":0,"id":"train_pricing_strategy_4438dwn5"},"train_pricing_strategy_4438dwn8":{"assigned":0,"id":"train_pricing_strategy_4438dwn8"},"train_pricing_strategy_4438up10":{"assigned":1,"id":"train_pricing_strategy_4438up10","versionedId":"train_pricing_strategy_4438up10_v47"},"train_pricing_strategy_4438up4":{"assigned":0,"id":"train_pricing_strategy_4438up4"},"train_pricing_strategy_4438up5":{"assigned":0,"id":"train_pricing_strategy_4438up5"},"train_pricing_strategy_4438up8":{"assigned":0,"id":"train_pricing_strategy_4438up8"},"train_pricing_strategy_dc010":{"assigned":0,"id":"train_pricing_strategy_dc010"},"train_pricing_strategy_dc020":{"assigned":0,"id":"train_pricing_strategy_dc020"},"train_pricing_strategy_depth99":{"assigned":0,"id":"train_pricing_strategy_depth99"},"train_pricing_strategy_dep_1":{"assigned":0,"id":"train_pricing_strategy_dep_1"},"train_pricing_strategy_dep_2":{"assigned":0,"id":"train_pricing_strategy_dep_2"},"train_pricing_strategy_dm1000":{"assigned":0,"id":"train_pricing_strategy_dm1000"},"train_pricing_strategy_dm1433":{"assigned":0,"id":"train_pricing_strategy_dm1433"},"train_pricing_strategy_dm2421":{"assigned":0,"id":"train_pricing_strategy_dm2421"},"train_pricing_strategy_dm2701":{"assigned":0,"id":"train_pricing_strategy_dm2701"},"train_pricing_strategy_dm2805":{"assigned":0,"id":"train_pricing_strategy_dm2805"},"train_pricing_strategy_dm4014":{"assigned":0,"id":"train_pricing_strategy_dm4014"},"train_pricing_strategy_dm4304":{"assigned":0,"id":"train_pricing_strategy_dm4304"},"train_pricing_strategy_dm4438":{"assigned":0,"id":"train_pricing_strategy_dm4438"},"train_pricing_strategy_dm4438a":{"assigned":0,"id":"train_pricing_strategy_dm4438a"},"train_pricing_strategy_dm4438ai":{"assigned":0,"id":"train_pricing_strategy_dm4438ai"},"train_pricing_strategy_dm4804":{"assigned":0,"id":"train_pricing_strategy_dm4804"},"train_pricing_strategy_dm5129":{"assigned":0,"id":"train_pricing_strategy_dm5129"},"train_pricing_strategy_dm5399":{"assigned":0,"id":"train_pricing_strategy_dm5399"},"train_pricing_strategy_dm5643":{"assigned":0,"id":"train_pricing_strategy_dm5643"},"train_pricing_strategy_dm5761":{"assigned":0,"id":"train_pricing_strategy_dm5761"},"train_pricing_strategy_dm836":{"assigned":0,"id":"train_pricing_strategy_dm836"},"train_pricing_strategy_dm914":{"assigned":0,"id":"train_pricing_strategy_dm914"},"train_pricing_strategy_dmai02":{"assigned":0,"id":"train_pricing_strategy_dmai02"},"train_pricing_strategy_dmai04":{"assigned":0,"id":"train_pricing_strategy_dmai04"},"train_pricing_strategy_dp_min10":{"assigned":0,"id":"train_pricing_strategy_dp_min10"},"train_pricing_strategy_ic010":{"assigned":0,"id":"train_pricing_strategy_ic010"},"train_pricing_strategy_ic020":{"assigned":0,"id":"train_pricing_strategy_ic020"},"train_pricing_strategy_ic035":{"assigned":0,"id":"train_pricing_strategy_ic035"},"train_pricing_strategy_mnl99":{"assigned":0,"id":"train_pricing_strategy_mnl99"},"train_pricing_strategy_pelican":{"assigned":0,"id":"train_pricing_strategy_pelican"},"train_pricing_strategy_wide99":{"assigned":0,"id":"train_pricing_strategy_wide99"},"train_pricing_strategy_yaml":{"assigned":0,"id":"train_pricing_strategy_yaml"}}},"train_ptt_android_sales_closed_description":{"id":"train_ptt_android_sales_closed_description","applied":0,"active":true,"forceVariant":0,"variants":{"train_ptt_android_sales_closed_description_off":{"assigned":0,"id":"train_ptt_android_sales_closed_description_off"},"train_ptt_android_sales_closed_description_on":{"assigned":1,"id":"train_ptt_android_sales_closed_description_on","versionedId":"train_ptt_android_sales_closed_description_on_v03"}}},"train_ptt_autoticketing_android_v3":{"id":"train_ptt_autoticketing_android_v3","applied":0,"active":true,"forceVariant":0,"variants":{"train_ptt_autoticketing_android_v3_off":{"assigned":0,"id":"train_ptt_autoticketing_android_v3_off"},"train_ptt_autoticketing_android_v3_on":{"assigned":1,"id":"train_ptt_autoticketing_android_v3_on","versionedId":"train_ptt_autoticketing_android_v3_on_v02"}}},"train_ptt_autoticketing_ios_v3":{"id":"train_ptt_autoticketing_ios_v3","applied":0,"active":true,"forceVariant":0,"variants":{"train_ptt_autoticketing_ios_v3_off":{"assigned":0,"id":"train_ptt_autoticketing_ios_v3_off"},"train_ptt_autoticketing_ios_v3_on":{"assigned":1,"id":"train_ptt_autoticketing_ios_v3_on","versionedId":"train_ptt_autoticketing_ios_v3_on_v02"}}},"train_ptt_checkout_nevsky_android":{"id":"train_ptt_checkout_nevsky_android","applied":0,"active":true,"forceVariant":0,"variants":{"train_ptt_checkout_nevsky_android_off":{"assigned":0,"id":"train_ptt_checkout_nevsky_android_off"},"train_ptt_checkout_nevsky_android_on":{"assigned":1,"id":"train_ptt_checkout_nevsky_android_on","versionedId":"train_ptt_checkout_nevsky_android_on_v01"}}},"train_ptt_ios_sales_closed_description":{"id":"train_ptt_ios_sales_closed_description","applied":0,"active":true,"forceVariant":0,"variants":{"train_ptt_ios_sales_closed_description_off":{"assigned":0,"id":"train_ptt_ios_sales_closed_description_off"},"train_ptt_ios_sales_closed_description_on":{"assigned":1,"id":"train_ptt_ios_sales_closed_description_on","versionedId":"train_ptt_ios_sales_closed_description_on_v02"}}},"train_schedule_without_date_ptt_banner":{"id":"train_schedule_without_date_ptt_banner","applied":0,"active":true,"forceVariant":0,"variants":{"train_schedule_without_date_ptt_banner_autochoose":{"assigned":0,"id":"train_schedule_without_date_ptt_banner_autochoose"},"train_schedule_without_date_ptt_banner_booking_upsale":{"assigned":0,"id":"train_schedule_without_date_ptt_banner_booking_upsale"},"train_schedule_without_date_ptt_banner_calendar":{"assigned":1,"id":"train_schedule_without_date_ptt_banner_calendar","versionedId":"train_schedule_without_date_ptt_banner_calendar_v04"},"train_schedule_without_date_ptt_banner_disabled":{"assigned":0,"id":"train_schedule_without_date_ptt_banner_disabled"},"train_schedule_without_date_ptt_banner_info_service":{"assigned":0,"id":"train_schedule_without_date_ptt_banner_info_service"},"train_schedule_without_date_ptt_banner_offline":{"assigned":0,"id":"train_schedule_without_date_ptt_banner_offline"},"train_schedule_without_date_ptt_banner_promocode":{"assigned":0,"id":"train_schedule_without_date_ptt_banner_promocode"},"train_schedule_without_date_ptt_banner_refund":{"assigned":0,"id":"train_schedule_without_date_ptt_banner_refund"}}},"train_seo_pages_ptt_banner":{"id":"train_seo_pages_ptt_banner","applied":0,"active":true,"forceVariant":0,"variants":{"train_seo_pages_ptt_banner_off":{"assigned":0,"id":"train_seo_pages_ptt_banner_off"},"train_seo_pages_ptt_banner_on":{"assigned":1,"id":"train_seo_pages_ptt_banner_on","versionedId":"train_seo_pages_ptt_banner_on_v02"}}},"train_success_ptt_banner":{"id":"train_success_ptt_banner","applied":0,"active":true,"forceVariant":0,"variants":{"train_success_ptt_banner_calendar":{"assigned":0,"id":"train_success_ptt_banner_calendar"},"train_success_ptt_banner_disabled":{"assigned":0,"id":"train_success_ptt_banner_disabled"},"train_success_ptt_banner_info_service":{"assigned":0,"id":"train_success_ptt_banner_info_service"},"train_success_ptt_banner_offline":{"assigned":1,"id":"train_success_ptt_banner_offline","versionedId":"train_success_ptt_banner_offline_v02"},"train_success_ptt_banner_refund":{"assigned":0,"id":"train_success_ptt_banner_refund"}}},"train_swod_tag_desc":{"id":"train_swod_tag_desc","applied":0,"active":true,"forceVariant":0,"variants":{"train_swod_tag_desc_off":{"assigned":0,"id":"train_swod_tag_desc_off"},"train_swod_tag_desc_on":{"assigned":1,"id":"train_swod_tag_desc_on","versionedId":"train_swod_tag_desc_on_v01"}}},"train_vid_sales_closed_description":{"id":"train_vid_sales_closed_description","applied":0,"active":true,"forceVariant":0,"variants":{"train_vid_sales_closed_description_off":{"assigned":0,"id":"train_vid_sales_closed_description_off"},"train_vid_sales_closed_description_on":{"assigned":1,"id":"train_vid_sales_closed_description_on","versionedId":"train_vid_sales_closed_description_on_v01"}}},"train_wizard_b2b":{"id":"train_wizard_b2b","applied":0,"active":true,"forceVariant":0,"variants":{"train_wizard_b2b_hide":{"assigned":0,"id":"train_wizard_b2b_hide"},"train_wizard_b2b_show":{"assigned":1,"id":"train_wizard_b2b_show","versionedId":"train_wizard_b2b_show"}}},"train_wizard_company_payment":{"id":"train_wizard_company_payment","applied":0,"active":true,"forceVariant":0,"variants":{"train_wizard_company_payment_off":{"assigned":0,"id":"train_wizard_company_payment_off"},"train_wizard_company_payment_on":{"assigned":1,"id":"train_wizard_company_payment_on","versionedId":"train_wizard_company_payment_on_v01"}}},"train_wizard_google_pay":{"id":"train_wizard_google_pay","applied":0,"active":true,"forceVariant":0,"variants":{"train_wizard_google_pay_off":{"assigned":0,"id":"train_wizard_google_pay_off"},"train_wizard_google_pay_on":{"assigned":1,"id":"train_wizard_google_pay_on","versionedId":"train_wizard_google_pay_on_v01"}}},"train_wizard_redesign2":{"id":"train_wizard_redesign2","applied":0,"active":true,"forceVariant":0,"variants":{"train_wizard_redesign2_hide_sf":{"assigned":0,"id":"train_wizard_redesign2_hide_sf"},"train_wizard_redesign2_nocb":{"assigned":1,"id":"train_wizard_redesign2_nocb","versionedId":"train_wizard_redesign2_nocb_v02"},"train_wizard_redesign2_off":{"assigned":0,"id":"train_wizard_redesign2_off"},"train_wizard_redesign2_on":{"assigned":0,"id":"train_wizard_redesign2_on"}}},"USA-3847-checkout":{"id":"USA-3847-checkout","applied":0,"active":true,"forceVariant":0,"variants":{"USA-3847-new-checkout":{"assigned":1,"id":"USA-3847-new-checkout","versionedId":"USA-3847-new-checkout_v07"},"USA-3847-old-wizard":{"assigned":0,"id":"USA-3847-old-wizard"}}},"USA-4245-booking-upsales":{"id":"USA-4245-booking-upsales","applied":0,"active":true,"forceVariant":0,"variants":{"USA-4245-booking-upsale":{"assigned":0,"id":"USA-4245-booking-upsale"},"USA-4245-paylater":{"assigned":1,"id":"USA-4245-paylater","versionedId":"USA-4245-paylater_v03"}}},"VID-1807_remove_hotel_loading":{"id":"VID-1807_remove_hotel_loading","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1807_hotels_unload_off":{"assigned":0,"id":"VID-1807_hotels_unload_off"},"VID-1807_hotels_unload_on":{"assigned":1,"id":"VID-1807_hotels_unload_on","versionedId":"VID-1807_hotels_unload_on_v01"}}},"VID-1945_bronevik":{"id":"VID-1945_bronevik","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1945_bronevik_off":{"assigned":0,"id":"VID-1945_bronevik_off"},"VID-1945_bronevik_on":{"assigned":1,"id":"VID-1945_bronevik_on","versionedId":"VID-1945_bronevik_on_v03"}}},"vid_avia_booking_results":{"id":"vid_avia_booking_results","applied":0,"active":true,"forceVariant":0,"variants":{"vid_avia_booking_results_off":{"assigned":0,"id":"vid_avia_booking_results_off"},"vid_avia_booking_results_on":{"assigned":1,"id":"vid_avia_booking_results_on","versionedId":"vid_avia_booking_results_on_v01"}}},"vid_avia_card_v2":{"id":"vid_avia_card_v2","applied":0,"active":true,"forceVariant":0,"variants":{"vid_avia_card_v2_off":{"assigned":0,"id":"vid_avia_card_v2_off"},"vid_avia_card_v2_on":{"assigned":1,"id":"vid_avia_card_v2_on","versionedId":"vid_avia_card_v2_on_v01"}}},"vid_avia_form_separate_date":{"id":"vid_avia_form_separate_date","applied":0,"active":true,"forceVariant":0,"variants":{"vid_avia_form_separate_date_off":{"assigned":0,"id":"vid_avia_form_separate_date_off"},"vid_avia_form_separate_date_on":{"assigned":1,"id":"vid_avia_form_separate_date_on","versionedId":"vid_avia_form_separate_date_on_v01"}}},"vid_avia_modal_bfr_wizard":{"id":"vid_avia_modal_bfr_wizard","applied":0,"active":true,"forceVariant":0,"variants":{"vid_avia_modal_bfr_wizard_off":{"assigned":0,"id":"vid_avia_modal_bfr_wizard_off"},"vid_avia_modal_bfr_wizard_on":{"assigned":1,"id":"vid_avia_modal_bfr_wizard_on","versionedId":"vid_avia_modal_bfr_wizard_on_v02"}}},"vid_bus_with_improves":{"id":"vid_bus_with_improves","applied":0,"active":true,"forceVariant":0,"variants":{"vid_bus_with_improves_off":{"assigned":0,"id":"vid_bus_with_improves_off"},"vid_bus_with_improves_on":{"assigned":1,"id":"vid_bus_with_improves_on","versionedId":"vid_bus_with_improves_on_v06"},"vid_bus_with_improves_withfeatur":{"assigned":0,"id":"vid_bus_with_improves_withfeatur"}}},"vid_hide_departed_trains":{"id":"vid_hide_departed_trains","applied":0,"active":true,"forceVariant":0,"variants":{"vid_hide_departed_trains_off":{"assigned":0,"id":"vid_hide_departed_trains_off"},"vid_hide_departed_trains_on":{"assigned":1,"id":"vid_hide_departed_trains_on","versionedId":"vid_hide_departed_trains_on_v01"}}},"vid_hotels_bronevik_offers":{"id":"vid_hotels_bronevik_offers","applied":0,"active":true,"forceVariant":0,"variants":{"vid_hotels_bronevik_offers_off":{"assigned":0,"id":"vid_hotels_bronevik_offers_off"},"vid_hotels_bronevik_offers_on":{"assigned":1,"id":"vid_hotels_bronevik_offers_on","versionedId":"vid_hotels_bronevik_offers_on_v06"}}},"vid_hotels_card_v2":{"id":"vid_hotels_card_v2","applied":0,"active":true,"forceVariant":0,"variants":{"vid_hotels_card_v2_off":{"assigned":0,"id":"vid_hotels_card_v2_off"},"vid_hotels_card_v2_on":{"assigned":1,"id":"vid_hotels_card_v2_on","versionedId":"vid_hotels_card_v2_on_v01"}}},"vid_hotels_sutochno":{"id":"vid_hotels_sutochno","applied":0,"active":true,"forceVariant":0,"variants":{"vid_hotels_sutochno_off":{"assigned":0,"id":"vid_hotels_sutochno_off"},"vid_hotels_sutochno_on":{"assigned":1,"id":"vid_hotels_sutochno_on","versionedId":"vid_hotels_sutochno_on_v03"}}},"vid_hotel_map_switch_visible":{"id":"vid_hotel_map_switch_visible","applied":0,"active":true,"forceVariant":0,"variants":{"vid_hotel_map_switch_visible_off":{"assigned":0,"id":"vid_hotel_map_switch_visible_off"},"vid_hotel_map_switch_visible_on":{"assigned":1,"id":"vid_hotel_map_switch_visible_on","versionedId":"vid_hotel_map_switch_visible_on_v01"}}},"vid_impr_unified_search":{"id":"vid_impr_unified_search","applied":0,"active":true,"forceVariant":0,"variants":{"vid_impr_unified_search_check":{"assigned":1,"id":"vid_impr_unified_search_check","versionedId":"vid_impr_unified_search_check_v03"},"vid_impr_unified_search_off":{"assigned":0,"id":"vid_impr_unified_search_off"},"vid_impr_unified_search_on":{"assigned":0,"id":"vid_impr_unified_search_on"}}},"vid_informers":{"id":"vid_informers","applied":0,"active":true,"forceVariant":0,"variants":{"vid_informers_off":{"assigned":0,"id":"vid_informers_off"},"vid_informers_on":{"assigned":1,"id":"vid_informers_on","versionedId":"vid_informers_on"}}},"vid_ptt_ad_train":{"id":"vid_ptt_ad_train","applied":0,"active":true,"forceVariant":0,"variants":{"vid_ptt_ad_train_off":{"assigned":0,"id":"vid_ptt_ad_train_off"},"vid_ptt_ad_train_on":{"assigned":1,"id":"vid_ptt_ad_train_on","versionedId":"vid_ptt_ad_train_on_v02"}}},"vid_simple_unified_search":{"id":"vid_simple_unified_search","applied":0,"active":true,"forceVariant":0,"variants":{"vid_simple_unified_search_off":{"assigned":0,"id":"vid_simple_unified_search_off"},"vid_simple_unified_search_on":{"assigned":1,"id":"vid_simple_unified_search_on","versionedId":"vid_simple_unified_search_on_v02"}}},"vid_sutochno_android":{"id":"vid_sutochno_android","applied":0,"active":true,"forceVariant":0,"variants":{"vid_sutochno_android_off":{"assigned":1,"id":"vid_sutochno_android_off","versionedId":"vid_sutochno_android_off"},"vid_sutochno_android_on":{"assigned":0,"id":"vid_sutochno_android_on"}}},"vid_sutochno_ios":{"id":"vid_sutochno_ios","applied":0,"active":true,"forceVariant":0,"variants":{"vid_sutochno_ios_off":{"assigned":1,"id":"vid_sutochno_ios_off","versionedId":"vid_sutochno_ios_off"},"vid_sutochno_ios_on":{"assigned":0,"id":"vid_sutochno_ios_on"}}},"vid_tours_promotion":{"id":"vid_tours_promotion","applied":0,"active":true,"forceVariant":0,"variants":{"vid_tours_promotion_off":{"assigned":0,"id":"vid_tours_promotion_off"},"vid_tours_promotion_on":{"assigned":1,"id":"vid_tours_promotion_on","versionedId":"vid_tours_promotion_on_v01"}}},"vid_train_card_v2":{"id":"vid_train_card_v2","applied":0,"active":true,"forceVariant":0,"variants":{"vid_train_card_v2_buttons":{"assigned":1,"id":"vid_train_card_v2_buttons","versionedId":"vid_train_card_v2_buttons_v01"},"vid_train_card_v2_off":{"assigned":0,"id":"vid_train_card_v2_off"},"vid_train_card_v2_table":{"assigned":0,"id":"vid_train_card_v2_table"}}},"vid_train_offers":{"id":"vid_train_offers","applied":0,"active":true,"forceVariant":0,"variants":{"vid_train_offers_new_feature":{"assigned":1,"id":"vid_train_offers_new_feature","versionedId":"vid_train_offers_new_feature_v07"},"vid_train_offers_off":{"assigned":0,"id":"vid_train_offers_off"},"vid_train_offers_on":{"assigned":0,"id":"vid_train_offers_on"}}},"vid_train_offers_sorting":{"id":"vid_train_offers_sorting","applied":0,"active":true,"forceVariant":0,"variants":{"vid_train_offers_sorting_off":{"assigned":0,"id":"vid_train_offers_sorting_off"},"vid_train_offers_sorting_on":{"assigned":1,"id":"vid_train_offers_sorting_on","versionedId":"vid_train_offers_sorting_on_v01"}}},"vid_train_othertransport":{"id":"vid_train_othertransport","applied":0,"active":true,"forceVariant":0,"variants":{"vid_train_othertransport_off":{"assigned":0,"id":"vid_train_othertransport_off"},"vid_train_othertransport_on":{"assigned":1,"id":"vid_train_othertransport_on","versionedId":"vid_train_othertransport_on_v03"},"vid_train_othertransport_without":{"assigned":0,"id":"vid_train_othertransport_without"}}},"vid_unified_search_form_tab_hotel":{"id":"vid_unified_search_form_tab_hotel","applied":0,"active":true,"forceVariant":0,"variants":{"vid_unified_search_form_tab_hotel_off":{"assigned":0,"id":"vid_unified_search_form_tab_hotel_off"},"vid_unified_search_form_tab_hotel_on":{"assigned":1,"id":"vid_unified_search_form_tab_hotel_on","versionedId":"vid_unified_search_form_tab_hotel_on_v02"}}},"web_main_middle_bdui_banner":{"id":"web_main_middle_bdui_banner","applied":0,"active":true,"forceVariant":0,"variants":{"web_main_middle_bdui_banner_off":{"assigned":0,"id":"web_main_middle_bdui_banner_off"},"web_main_middle_bdui_banner_on":{"assigned":1,"id":"web_main_middle_bdui_banner_on","versionedId":"web_main_middle_bdui_banner_on_v01"}}},"web_main_top_bdui_banner":{"id":"web_main_top_bdui_banner","applied":0,"active":true,"forceVariant":0,"variants":{"web_main_top_bdui_banner_off":{"assigned":0,"id":"web_main_top_bdui_banner_off"},"web_main_top_bdui_banner_on":{"assigned":1,"id":"web_main_top_bdui_banner_on","versionedId":"web_main_top_bdui_banner_on_v01"}}}},"sessionId":"7b230125-e5ca-4280-b49d-2f328a11d9ae"};var RM = RM || {}; RM.StaticData = RM.StaticData || {}; RM.StaticData["urlConfig"] = {"config":"config\/url.php","default-zone":"main","mobile_supported":"1","zone":{"main":{"common-domain":"tutu.ru","static-domain":"static.tu-tu.ru","default-subdomain":"www"},"ukraine":{"top-level-domain":"tutu.travel","common-domain":"ua.tutu.travel","static-domain":"static.tu-tu.ru","is-forbidden-subdomain":"1"},"belarus":{"top-level-domain":"tutu.travel","common-domain":"by.tutu.travel","static-domain":"static.tu-tu.ru","is-forbidden-subdomain":"1"},"english":{"common-domain":"tutu.travel","static-domain":"static.tu-tu.ru","default-subdomain":"www"}},"cache-enable":"1","host":"www.tutu.ru","https":1,"https_only":0};</script>
# 	<script src="https://cdn1.tu-tu.ru/scripts/build/url.js.983c40d97c7564bfe5c9ee77b3721ace11.js"></script>

# 	<script>window.params = {"componentData":{"vokzalList":[{"name":"\u0410\u0431\u0430\u043a\u0430\u043d","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D0%B1%D0%B0%D0%BA%D0%B0%D0%BD\/"},{"name":"\u0410\u0431\u0434\u0443\u043b\u0438\u043d\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D0%B1%D0%B4%D1%83%D0%BB%D0%B8%D0%BD%D0%BE\/"},{"name":"\u0410\u0433\u0440\u044b\u0437","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D0%B3%D1%80%D1%8B%D0%B7\/"},{"name":"\u0410\u0434\u043b\u0435\u0440","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D0%B4%D0%BB%D0%B5%D1%80\/"},{"name":"\u0410\u043a\u0441\u0430\u043a\u043e\u0432\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D0%BA%D1%81%D0%B0%D0%BA%D0%BE%D0%B2%D0%BE\/"},{"name":"\u0410\u043b\u0435\u0439\u0441\u043a\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D0%BB%D0%B5%D0%B9%D1%81%D0%BA%D0%B0%D1%8F\/"},{"name":"\u0410\u043d\u0430\u043f\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D0%BD%D0%B0%D0%BF%D0%B0\/"},{"name":"\u0410\u043d\u0433\u0430\u0440\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D0%BD%D0%B3%D0%B0%D1%80%D1%81%D0%BA\/"},{"name":"\u0410\u043d\u0436\u0435\u0440\u0441\u043a\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D0%BD%D0%B6%D0%B5%D1%80%D1%81%D0%BA%D0%B0%D1%8F\/"},{"name":"\u0410\u0440\u0437\u0430\u043c\u0430\u0441-1","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D1%80%D0%B7%D0%B0%D0%BC%D0%B0%D1%81-1\/"},{"name":"\u0410\u0440\u0437\u0430\u043c\u0430\u0441-2","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D1%80%D0%B7%D0%B0%D0%BC%D0%B0%D1%81-2\/"},{"name":"\u0410\u0440\u043c\u0430\u0432\u0438\u0440-1","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%80-1\/"},{"name":"\u0410\u0440\u043c\u0430\u0432\u0438\u0440-2","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%80-2\/"},{"name":"\u0410\u0440\u0441\u0435\u043d\u044c\u0435\u0432","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D1%80%D1%81%D0%B5%D0%BD%D1%8C%D0%B5%D0%B2\/"},{"name":"\u0410\u0440\u0445\u0430\u043d\u0433\u0435\u043b\u044c\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D1%80%D1%85%D0%B0%D0%BD%D0%B3%D0%B5%D0%BB%D1%8C%D1%81%D0%BA\/"},{"name":"\u0410\u0440\u0445\u0430\u0440\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D1%80%D1%85%D0%B0%D1%80%D0%B0\/"},{"name":"\u0410\u0441\u0442\u0440\u0430\u0445\u0430\u043d\u044c","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D1%81%D1%82%D1%80%D0%B0%D1%85%D0%B0%D0%BD%D1%8C\/"},{"name":"\u0410\u0442\u043a\u0430\u0440\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D1%82%D0%BA%D0%B0%D1%80%D1%81%D0%BA\/"},{"name":"\u0410\u0447\u0438\u043d\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D1%87%D0%B8%D0%BD%D1%81%D0%BA\/"},{"name":"\u0410\u0448\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D1%88%D0%B0\/"},{"name":"\u0410\u044d\u0440\u043e\u0432\u043e\u043a\u0437\u0430\u043b\u044c\u043d\u044b\u0439 \u041a\u043e\u043c\u043f\u043b\u0435\u043a\u0441 \u0410\u0434\u043b\u0435\u0440","url":"\/poezda\/vkz\/%D0%B0%D1%8D%D1%80%D0%BE%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9_%D0%BA%D0%BE%D0%BC%D0%BF%D0%BB%D0%B5%D0%BA%D1%81_%D0%90%D0%B4%D0%BB%D0%B5%D1%80\/"},{"name":"\u0411\u0430\u043b\u0430\u043a\u043e\u0432\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B0%D0%BB%D0%B0%D0%BA%D0%BE%D0%B2%D0%BE\/"},{"name":"\u0411\u0430\u043b\u0430\u0448\u043e\u0432","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B0%D0%BB%D0%B0%D1%88%D0%BE%D0%B2\/"},{"name":"\u0411\u0430\u043b\u0442\u0438\u0439\u0441\u043a\u0438\u0439 \u0412\u043e\u043a\u0437\u0430\u043b","url":"\/poezda\/vkz\/%D0%91%D0%B0%D0%BB%D1%82%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB\/"},{"name":"\u0411\u0430\u0440\u0430\u0431\u0438\u043d\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B0%D1%80%D0%B0%D0%B1%D0%B8%D0%BD%D1%81%D0%BA\/"},{"name":"\u0411\u0430\u0440\u043d\u0430\u0443\u043b","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B0%D1%80%D0%BD%D0%B0%D1%83%D0%BB\/"},{"name":"\u0411\u0430\u0445\u0447\u0438\u0441\u0430\u0440\u0430\u0439","url":"\/poezda\/vkz\/%D0%91%D0%B0%D1%85%D1%87%D0%B8%D1%81%D0%B0%D1%80%D0%B0%D0%B9\/"},{"name":"\u0411\u0435\u043b\u0430\u044f \u041a\u0430\u043b\u0438\u0442\u0432\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B5%D0%BB%D0%B0%D1%8F_%D0%9A%D0%B0%D0%BB%D0%B8%D1%82%D0%B2%D0%B0\/"},{"name":"\u0411\u0435\u043b\u0433\u043e\u0440\u043e\u0434","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B5%D0%BB%D0%B3%D0%BE%D1%80%D0%BE%D0%B4\/"},{"name":"\u0411\u0435\u043b\u043e\u0432\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B5%D0%BB%D0%BE%D0%B2%D0%BE\/"},{"name":"\u0411\u0435\u043b\u043e\u0433\u043e\u0440\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B5%D0%BB%D0%BE%D0%B3%D0%BE%D1%80%D1%81%D0%BA\/"},{"name":"\u0411\u0435\u043b\u043e\u0440\u0435\u0446\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B5%D0%BB%D0%BE%D1%80%D0%B5%D1%86%D0%BA\/"},{"name":"\u0411\u0435\u043b\u043e\u0440\u0435\u0447\u0435\u043d\u0441\u043a\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B5%D0%BB%D0%BE%D1%80%D0%B5%D1%87%D0%B5%D0%BD%D1%81%D0%BA%D0%B0%D1%8F\/"},{"name":"\u0411\u0435\u043b\u043e\u0440\u0443\u0441\u0441\u043a\u0438\u0439 \u0412\u043e\u043a\u0437\u0430\u043b","url":"\/poezda\/vkz\/%D0%91%D0%B5%D0%BB%D0%BE%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB\/"},{"name":"\u0411\u0435\u0440\u0434\u044f\u0443\u0448","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B5%D1%80%D0%B4%D1%8F%D1%83%D1%88\/"},{"name":"\u0411\u0435\u0440\u0435\u0437\u043d\u0438\u043a\u0438","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B5%D1%80%D0%B5%D0%B7%D0%BD%D0%B8%D0%BA%D0%B8\/"},{"name":"\u0411\u0438\u0439\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B8%D0%B9%D1%81%D0%BA\/"},{"name":"\u0411\u0438\u043a\u0438\u043d","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B8%D0%BA%D0%B8%D0%BD\/"},{"name":"\u0411\u0438\u0440\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B8%D1%80%D0%B0\/"},{"name":"\u0411\u0438\u0440\u043e\u0431\u0438\u0434\u0436\u0430\u043d","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B8%D1%80%D0%BE%D0%B1%D0%B8%D0%B4%D0%B6%D0%B0%D0%BD\/"},{"name":"\u0411\u043b\u0430\u0433\u043e\u0432\u0435\u0449\u0435\u043d\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%BB%D0%B0%D0%B3%D0%BE%D0%B2%D0%B5%D1%89%D0%B5%D0%BD%D1%81%D0%BA\/"},{"name":"\u0411\u043e\u0433\u043e\u0442\u043e\u043b","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%BE%D0%B3%D0%BE%D1%82%D0%BE%D0%BB\/"},{"name":"\u0411\u043e\u0433\u043e\u044f\u0432\u043b\u0435\u043d\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%BE%D0%B3%D0%BE%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D1%81%D0%BA\/"},{"name":"\u0411\u043e\u043b\u043e\u0442\u043d\u043e\u0435","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%BE%D0%BB%D0%BE%D1%82%D0%BD%D0%BE%D0%B5\/"},{"name":"\u0411\u043e\u0440\u0437\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%BE%D1%80%D0%B7%D1%8F\/"},{"name":"\u0411\u043e\u0440\u0438\u0441\u043e\u0433\u043b\u0435\u0431\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B3%D0%BB%D0%B5%D0%B1%D1%81%D0%BA\/"},{"name":"\u0411\u0440\u044f\u043d\u0441\u043a - \u041e\u0440\u043b\u043e\u0432\u0441\u043a\u0438\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D1%80%D1%8F%D0%BD%D1%81%D0%BA-%D0%9E%D1%80%D0%BB%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9\/"},{"name":"\u0411\u0443\u0433\u0443\u043b\u044c\u043c\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D1%83%D0%B3%D1%83%D0%BB%D1%8C%D0%BC%D0%B0\/"},{"name":"\u0411\u0443\u0437\u0443\u043b\u0443\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D1%83%D0%B7%D1%83%D0%BB%D1%83%D0%BA\/"},{"name":"\u0411\u0443\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D1%83%D0%B9\/"},{"name":"\u0411\u0443\u0440\u0435\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D1%83%D1%80%D0%B5%D1%8F\/"},{"name":"\u0412\u0430\u043b\u0443\u0439\u043a\u0438","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%B0%D0%BB%D1%83%D0%B9%D0%BA%D0%B8\/"},{"name":"\u0412\u0430\u043d\u0438\u043d\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%B0%D0%BD%D0%B8%D0%BD%D0%BE\/"},{"name":"\u0412\u0435\u043b\u0438\u043a\u0438\u0435 \u041b\u0443\u043a\u0438","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%B5%D0%BB%D0%B8%D0%BA%D0%B8%D0%B5_%D0%9B%D1%83%D0%BA%D0%B8\/"},{"name":"\u0412\u0435\u043b\u0438\u043a\u0438\u0439 \u0423\u0441\u0442\u044e\u0433","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%B2%D0%B5%D0%BB%D0%B8%D0%BA%D0%B8%D0%B9_%D0%A3%D1%81%D1%82%D1%8E%D0%B3\/"},{"name":"\u0412\u0435\u043b\u044c\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%B5%D0%BB%D1%8C%D1%81%D0%BA\/"},{"name":"\u0412\u0435\u0440\u0445\u043d\u0438\u0439 \u0411\u0430\u0441\u043a\u0443\u043d\u0447\u0430\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%B5%D1%80%D1%85%D0%BD%D0%B8%D0%B9_%D0%91%D0%B0%D1%81%D0%BA%D1%83%D0%BD%D1%87%D0%B0%D0%BA\/"},{"name":"\u0412\u0435\u0440\u0445\u043d\u0438\u0439 \u0423\u0444\u0430\u043b\u0435\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%B5%D1%80%D1%85%D0%BD%D0%B8%D0%B9_%D0%A3%D1%84%D0%B0%D0%BB%D0%B5%D0%B9\/"},{"name":"\u0412\u0435\u0441\u0435\u043b\u043e\u0435","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%B5%D1%81%D0%B5%D0%BB%D0%BE%D0%B5\/"},{"name":"\u0412\u0438\u0442\u0435\u0431\u0441\u043a\u0438\u0439 \u0412\u043e\u043a\u0437\u0430\u043b","url":"\/poezda\/vkz\/%D0%92%D0%B8%D1%82%D0%B5%D0%B1%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB\/"},{"name":"\u0412\u0438\u0445\u043e\u0440\u0435\u0432\u043a\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%B8%D1%85%D0%BE%D1%80%D0%B5%D0%B2%D0%BA%D0%B0\/"},{"name":"\u0412\u043b\u0430\u0434\u0438\u0432\u043e\u0441\u0442\u043e\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%B2%D0%BE%D1%81%D1%82%D0%BE%D0%BA\/"},{"name":"\u0412\u043b\u0430\u0434\u0438\u043a\u0430\u0432\u043a\u0430\u0437","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BA%D0%B0%D0%B2%D0%BA%D0%B0%D0%B7\/"},{"name":"\u0412\u043b\u0430\u0434\u0438\u043c\u0438\u0440","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80\/"},{"name":"\u0412\u043e\u043b\u0433\u043e\u0433\u0440\u0430\u0434","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%BE%D0%BB%D0%B3%D0%BE%D0%B3%D1%80%D0%B0%D0%B4\/"},{"name":"\u0412\u043e\u043b\u0433\u043e\u0434\u043e\u043d\u0441\u043a\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%BE%D0%BB%D0%B3%D0%BE%D0%B4%D0%BE%D0%BD%D1%81%D0%BA%D0%B0%D1%8F\/"},{"name":"\u0412\u043e\u043b\u0436\u0441\u043a\u0438\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%BE%D0%BB%D0%B6%D1%81%D0%BA%D0%B8%D0%B9\/"},{"name":"\u0412\u043e\u043b\u043e\u0433\u0434\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%BE%D0%BB%D0%BE%D0%B3%D0%B4%D0%B0\/"},{"name":"\u0412\u043e\u043b\u0445\u043e\u0432\u0441\u0442\u0440\u043e\u0439-1","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%BE%D0%BB%D1%85%D0%BE%D0%B2%D1%81%D1%82%D1%80%D0%BE%D0%B9-1\/"},{"name":"\u0412\u043e\u0440\u043a\u0443\u0442\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%BE%D1%80%D0%BA%D1%83%D1%82%D0%B0\/"},{"name":"\u0412\u043e\u0440\u043e\u043d\u0435\u0436 I","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%BE%D1%80%D0%BE%D0%BD%D0%B5%D0%B6\/"},{"name":"\u0412\u043e\u0441\u0442\u043e\u0447\u043d\u044b\u0439","url":"\/poezda\/vkz\/moskva_vostochniy\/"},{"name":"\u0412\u044b\u0431\u043e\u0440\u0433","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D1%8B%D0%B1%D0%BE%D1%80%D0%B3\/"},{"name":"\u0412\u044f\u0437\u0435\u043c\u0441\u043a\u0438\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D1%8F%D0%B7%D0%B5%D0%BC%D1%81%D0%BA%D0%B8%D0%B9\/"},{"name":"\u0412\u044f\u0437\u043e\u0432\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D1%8F%D0%B7%D0%BE%D0%B2%D0%B0%D1%8F\/"},{"name":"\u0413\u0430\u043b\u0438\u0447","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%93%D0%B0%D0%BB%D0%B8%D1%87\/"},{"name":"\u0413\u0435\u043e\u0440\u0433\u0438\u0435\u0432\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%93%D0%B5%D0%BE%D1%80%D0%B3%D0%B8%D0%B5%D0%B2%D1%81%D0%BA\/"},{"name":"\u0413\u043b\u0430\u0437\u043e\u0432","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%93%D0%BB%D0%B0%D0%B7%D0%BE%D0%B2\/"},{"name":"\u0413\u043e\u0440\u044f\u0447\u0438\u0439 \u041a\u043b\u044e\u0447","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%93%D0%BE%D1%80%D1%8F%D1%87%D0%B8%D0%B9_%D0%9A%D0%BB%D1%8E%D1%87\/"},{"name":"\u0413\u0440\u043e\u0434\u0435\u043a\u043e\u0432\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%93%D1%80%D0%BE%D0%B4%D0%B5%D0%BA%D0%BE%D0%B2%D0%BE\/"},{"name":"\u0413\u0440\u043e\u0437\u043d\u044b\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%93%D1%80%D0%BE%D0%B7%D0%BD%D1%8B%D0%B9\/"},{"name":"\u0413\u0440\u044f\u0437\u0438-\u0412\u043e\u0440\u043e\u043d\u0435\u0436\u0441\u043a\u0438\u0435","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%93%D1%80%D1%8F%D0%B7%D0%B8_%D0%92%D0%BE%D1%80%D0%BE%D0%BD%D0%B5%D0%B6%D1%81%D0%BA%D0%B8%D0%B5\/"},{"name":"\u0413\u0443\u0434\u0435\u0440\u043c\u0435\u0441","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%93%D1%83%D0%B4%D0%B5%D1%80%D0%BC%D0%B5%D1%81\/"},{"name":"\u0414\u0430\u043b\u044c\u043d\u0435\u0440\u0435\u0447\u0435\u043d\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%94%D0%B0%D0%BB%D1%8C%D0%BD%D0%B5%D1%80%D0%B5%D1%87%D0%B5%D0%BD%D1%81%D0%BA\/"},{"name":"\u0414\u0430\u043d\u0438\u043b\u043e\u0432","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%94%D0%B0%D0%BD%D0%B8%D0%BB%D0%BE%D0%B2\/"},{"name":"\u0414\u0435\u0440\u0431\u0435\u043d\u0442","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%94%D0%B5%D1%80%D0%B1%D0%B5%D0%BD%D1%82\/"},{"name":"\u0414\u0436\u0430\u043d\u043a\u043e\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%B4%D0%B6%D0%B0%D0%BD%D0%BA%D0%BE%D0%B9\/"},{"name":"\u0414\u0437\u0435\u0440\u0436\u0438\u043d\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%94%D0%B7%D0%B5%D1%80%D0%B6%D0%B8%D0%BD%D1%81%D0%BA\/"},{"name":"\u0414\u0438\u043c\u0438\u0442\u0440\u043e\u0432\u0433\u0440\u0430\u0434","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%94%D0%B8%D0%BC%D0%B8%D1%82%D1%80%D0%BE%D0%B2%D0%B3%D1%80%D0%B0%D0%B4\/"},{"name":"\u0415\u0439\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%95%D0%B9%D1%81%D0%BA\/"},{"name":"\u0415\u043a\u0430\u0442\u0435\u0440\u0438\u043d\u0431\u0443\u0440\u0433","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3\/"},{"name":"\u0415\u043b\u0435\u0446","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%95%D0%BB%D0%B5%D1%86\/"},{"name":"\u0415\u0440\u0448\u043e\u0432","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%95%D1%80%D1%88%D0%BE%D0%B2\/"},{"name":"\u0415\u0441\u0441\u0435\u043d\u0442\u0443\u043a\u0438","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%95%D1%81%D1%81%D0%B5%D0%BD%D1%82%D1%83%D0%BA%D0%B8\/"},{"name":"\u0416\u0438\u0433\u0443\u043b\u0435\u0432\u0441\u043a\u043e\u0435 \u041c\u043e\u0440\u0435","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%96%D0%B8%D0%B3%D1%83%D0%BB%D0%B5%D0%B2%D1%81%D0%BA%D0%BE%D0%B5_%D0%9C%D0%BE%D1%80%D0%B5\/"},{"name":"\u0417\u0430\u0431\u0430\u0439\u043a\u0430\u043b\u044c\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%97%D0%B0%D0%B1%D0%B0%D0%B9%D0%BA%D0%B0%D0%BB%D1%8C%D1%81%D0%BA\/"},{"name":"\u0417\u0430\u0432\u0438\u0442\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%97%D0%B0%D0%B2%D0%B8%D1%82%D0%B0%D1%8F\/"},{"name":"\u0417\u0430\u043b\u0430\u0440\u0438","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%97%D0%B0%D0%BB%D0%B0%D1%80%D0%B8\/"},{"name":"\u0417\u0430\u043e\u0437\u0435\u0440\u043d\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%97%D0%B0%D0%BE%D0%B7%D0%B5%D1%80%D0%BD%D0%B0%D1%8F\/"},{"name":"\u0417\u0430\u0440\u0438\u043d\u0441\u043a\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%97%D0%B0%D1%80%D0%B8%D0%BD%D1%81%D0%BA%D0%B0%D1%8F\/"},{"name":"\u0417\u0432\u0435\u0440\u0435\u0432\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%97%D0%B2%D0%B5%D1%80%D0%B5%D0%B2%D0%BE\/"},{"name":"\u0417\u0435\u043b\u0435\u043d\u044b\u0439 \u0414\u043e\u043b","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%97%D0%B5%D0%BB%D0%B5%D0%BD%D1%8B%D0%B9_%D0%94%D0%BE%D0%BB\/"},{"name":"\u0417\u0438\u043c\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%97%D0%B8%D0%BC%D0%B0\/"},{"name":"\u0417\u043b\u0430\u0442\u043e\u0443\u0441\u0442","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%97%D0%BB%D0%B0%D1%82%D0%BE%D1%83%D1%81%D1%82\/"},{"name":"\u0417\u0443\u0431\u043e\u0432\u0430 \u041f\u043e\u043b\u044f\u043d\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%97%D1%83%D0%B1%D0%BE%D0%B2%D0%B0_%D0%9F%D0%BE%D0%BB%D1%8F%D0%BD%D0%B0\/"},{"name":"\u0418\u0432\u0430\u043d\u043e\u0432\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%98%D0%B2%D0%B0%D0%BD%D0%BE%D0%B2%D0%BE\/"},{"name":"\u0418\u0436\u0435\u0432\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%98%D0%B6%D0%B5%D0%B2%D1%81%D0%BA\/"},{"name":"\u0418\u043d\u0437\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%98%D0%BD%D0%B7%D0%B0\/"},{"name":"\u0418\u043d\u0441\u043a\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%98%D0%BD%D1%81%D0%BA%D0%B0%D1%8F\/"},{"name":"\u0418\u043d\u0442\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%98%D0%BD%D1%82%D0%B0\/"},{"name":"\u0418\u0440\u043a\u0443\u0442\u0441\u043a-\u041f\u0430\u0441\u0441\u0430\u0436\u0438\u0440\u0441\u043a\u0438\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%98%D1%80%D0%BA%D1%83%D1%82%D1%81%D0%BA-%D0%9F%D0%B0%D1%81%D1%81%D0%B0%D0%B6%D0%B8%D1%80%D1%81%D0%BA%D0%B8%D0%B9\/"},{"name":"\u0418\u0440\u043a\u0443\u0442\u0441\u043a-\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043e\u0447\u043d\u044b\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%98%D1%80%D0%BA%D1%83%D1%82%D1%81%D0%BA-%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BE%D1%87%D0%BD%D1%8B%D0%B9\/"},{"name":"\u0418\u0441\u0430\u043a\u043e\u0433\u043e\u0440\u043a\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%98%D1%81%D0%B0%D0%BA%D0%BE%D0%B3%D0%BE%D1%80%D0%BA%D0%B0\/"},{"name":"\u0418\u0441\u0438\u043b\u044c\u043a\u0443\u043b\u044c","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%98%D1%81%D0%B8%D0%BB%D1%8C%D0%BA%D1%83%D0%BB%D1%8C\/"},{"name":"\u0418\u0441\u043a\u0438\u0442\u0438\u043c","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%98%D1%81%D0%BA%D0%B8%D1%82%D0%B8%D0%BC\/"},{"name":"\u0419\u043e\u0448\u043a\u0430\u0440-\u041e\u043b\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%99%D0%BE%D1%88%D0%BA%D0%B0%D1%80-%D0%9E%D0%BB%D0%B0\/"},{"name":"\u041a\u0430\u0432\u043a\u0430\u0437\u0441\u043a\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D0%B2%D0%BA%D0%B0%D0%B7%D1%81%D0%BA%D0%B0%D1%8F\/"},{"name":"\u041a\u0430\u0437\u0430\u043d\u0441\u043a\u0438\u0439 \u0412\u043e\u043a\u0437\u0430\u043b","url":"\/poezda\/vkz\/%D0%9A%D0%B0%D0%B7%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB\/"},{"name":"\u041a\u0430\u0437\u0430\u043d\u044c","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D0%B7%D0%B0%D0%BD%D1%8C\/"},{"name":"\u041a\u0430\u043b\u0430\u0447\u0438\u043d\u0441\u043a\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D0%BB%D0%B0%D1%87%D0%B8%D0%BD%D1%81%D0%BA%D0%B0%D1%8F\/"},{"name":"\u041a\u0430\u043b\u0438\u043d\u0438\u043d\u0433\u0440\u0430\u0434-\u042e\u0436\u043d\u044b\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D0%BB%D0%B8%D0%BD%D0%B8%D0%BD%D0%B3%D1%80%D0%B0%D0%B4-%D0%AE%D0%B6%D0%BD%D1%8B%D0%B9\/"},{"name":"\u041a\u0430\u043b\u0443\u0433\u0430-1","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D0%BB%D1%83%D0%B3%D0%B0-1\/"},{"name":"\u041a\u0430\u043c\u0435\u043d\u0441\u043a-\u0423\u0440\u0430\u043b\u044c\u0441\u043a\u0438\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D0%BC%D0%B5%D0%BD%D1%81%D0%BA-%D0%A3%D1%80%D0%B0%D0%BB%D1%8C%D1%81%D0%BA%D0%B8%D0%B9\/"},{"name":"\u041a\u0430\u043c\u0435\u043d\u0441\u043a\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D0%BC%D0%B5%D0%BD%D1%81%D0%BA%D0%B0%D1%8F\/"},{"name":"\u041a\u0430\u043c\u0435\u043d\u044c-\u041d\u0430-\u041e\u0431\u0438","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D0%BC%D0%B5%D0%BD%D1%8C-%D0%9D%D0%B0-%D0%9E%D0%B1%D0%B8\/"},{"name":"\u041a\u0430\u043c\u044b\u0448\u043b\u043e\u0432","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D0%BC%D1%8B%D1%88%D0%BB%D0%BE%D0%B2\/"},{"name":"\u041a\u0430\u043d\u0430\u0448","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D0%BD%D0%B0%D1%88\/"},{"name":"\u041a\u0430\u043d\u0441\u043a-\u0415\u043d\u0438\u0441\u0435\u0439\u0441\u043a\u0438\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D0%BD%D1%81%D0%BA-%D0%95%D0%BD%D0%B8%D1%81%D0%B5%D0%B9%D1%81%D0%BA%D0%B8%D0%B9\/"},{"name":"\u041a\u0430\u0440\u0430\u0441\u0443\u043a-1","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D1%80%D0%B0%D1%81%D1%83%D0%BA-1\/"},{"name":"\u041a\u0430\u0440\u0433\u0430\u0442","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D1%80%D0%B3%D0%B0%D1%82\/"},{"name":"\u041a\u0430\u0440\u0442\u0430\u043b\u044b","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D1%80%D1%82%D0%B0%D0%BB%D1%8B\/"},{"name":"\u041a\u0430\u0440\u044b\u043c\u0441\u043a\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D1%80%D1%8B%D0%BC%D1%81%D0%BA%D0%B0%D1%8F\/"},{"name":"\u041a\u0435\u043c\u0435\u0440\u043e\u0432\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B5%D0%BC%D0%B5%D1%80%D0%BE%D0%B2%D0%BE\/"},{"name":"\u041a\u0435\u0440\u0447\u044c (\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439)","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%BA%D0%B5%D1%80%D1%87%D1%8C\/"},{"name":"\u041a\u0435\u0440\u0447\u044c-\u042e\u0436\u043d\u0430\u044f","url":"\/poezda\/vkz\/%D0%BA%D0%B5%D1%80%D1%87%D1%8C_%D1%8E%D0%B6%D0%BD%D0%B0%D1%8F\/"},{"name":"\u041a\u0438\u0435\u0432\u0441\u043a\u0438\u0439 \u0412\u043e\u043a\u0437\u0430\u043b","url":"\/poezda\/vkz\/%D0%9A%D0%B8%D0%B5%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB\/"},{"name":"\u041a\u0438\u0437\u043b\u044f\u0440","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B8%D0%B7%D0%BB%D1%8F%D1%80\/"},{"name":"\u041a\u0438\u043d\u0435\u043b\u044c","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B8%D0%BD%D0%B5%D0%BB%D1%8C\/"},{"name":"\u041a\u0438\u043d\u0435\u0448\u043c\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B8%D0%BD%D0%B5%D1%88%D0%BC%D0%B0\/"},{"name":"\u041a\u0438\u0440\u043e\u0432","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B8%D1%80%D0%BE%D0%B2\/"},{"name":"\u041a\u0438\u0440\u0441\u0430\u043d\u043e\u0432","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B8%D1%80%D1%81%D0%B0%D0%BD%D0%BE%D0%B2\/"},{"name":"\u041a\u0438\u0441\u0435\u043b\u0435\u0432\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B8%D1%81%D0%B5%D0%BB%D0%B5%D0%B2%D1%81%D0%BA\/"},{"name":"\u041a\u0438\u0441\u043b\u043e\u0432\u043e\u0434\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B8%D1%81%D0%BB%D0%BE%D0%B2%D0%BE%D0%B4%D1%81%D0%BA\/"},{"name":"\u041a\u043d\u044f\u0436\u043f\u043e\u0433\u043e\u0441\u0442","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%BD%D1%8F%D0%B6%D0%BF%D0%BE%D0%B3%D0%BE%D1%81%D1%82\/"},{"name":"\u041a\u043e\u0432\u0440\u043e\u0432","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%BE%D0%B2%D1%80%D0%BE%D0%B2\/"},{"name":"\u041a\u043e\u0433\u0430\u043b\u044b\u043c","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%BE%D0%B3%D0%B0%D0%BB%D1%8B%D0%BC\/"},{"name":"\u041a\u043e\u043c\u0441\u043e\u043c\u043e\u043b\u044c\u0441\u043a-\u041d\u0430-\u0410\u043c\u0443\u0440\u0435","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%BE%D0%BC%D1%81%D0%BE%D0%BC%D0%BE%D0%BB%D1%8C%D1%81%D0%BA-%D0%9D%D0%B0-%D0%90%D0%BC%D1%83%D1%80%D0%B5\/"},{"name":"\u041a\u043e\u043d\u043e\u0448\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%BE%D0%BD%D0%BE%D1%88%D0%B0\/"},{"name":"\u041a\u043e\u0440\u0448\u0443\u043d\u0438\u0445\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%BE%D1%80%D1%88%D1%83%D0%BD%D0%B8%D1%85%D0%B0\/"},{"name":"\u041a\u043e\u0441\u0442\u0440\u043e\u043c\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%BE%D1%81%D1%82%D1%80%D0%BE%D0%BC%D0%B0\/"},{"name":"\u041a\u043e\u0442\u0435\u043b\u044c\u043d\u0438\u043a\u043e\u0432\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D1%81%D1%82_%D0%9A%D0%BE%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2%D0%BE\/"},{"name":"\u041a\u043e\u0442\u0435\u043b\u044c\u043d\u0438\u0447","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%BE%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B8%D1%87\/"},{"name":"\u041a\u043e\u0442\u043b\u0430\u0441-\u042e\u0436\u043d\u044b\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%BE%D1%82%D0%BB%D0%B0%D1%81-%D0%AE%D0%B6%D0%BD%D1%8B%D0%B9\/"},{"name":"\u041a\u0440\u0430\u0441\u043d\u043e\u0434\u0430\u0440-1","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B4%D0%B0%D1%80-1\/"},{"name":"\u041a\u0440\u0430\u0441\u043d\u043e\u0443\u0444\u0438\u043c\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D1%83%D1%84%D0%B8%D0%BC%D1%81%D0%BA\/"},{"name":"\u041a\u0440\u0430\u0441\u043d\u043e\u044f\u0440\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D1%8F%D1%80%D1%81%D0%BA\/"},{"name":"\u041a\u0440\u043e\u043f\u0430\u0447\u0435\u0432\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D1%80%D0%BE%D0%BF%D0%B0%D1%87%D0%B5%D0%B2%D0%BE\/"},{"name":"\u041a\u0440\u044b\u043c\u0441\u043a\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D1%80%D1%8B%D0%BC%D1%81%D0%BA%D0%B0%D1%8F\/"},{"name":"\u041a\u0443\u0437\u043d\u0435\u0446\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D1%83%D0%B7%D0%BD%D0%B5%D1%86%D0%BA\/"},{"name":"\u041a\u0443\u043b\u0443\u043d\u0434\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D1%83%D0%BB%D1%83%D0%BD%D0%B4%D0%B0\/"},{"name":"\u041a\u0443\u043f\u0438\u043d\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D1%83%D0%BF%D0%B8%D0%BD%D0%BE\/"},{"name":"\u041a\u0443\u0440\u0433\u0430\u043d","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D1%83%D1%80%D0%B3%D0%B0%D0%BD\/"},{"name":"\u041a\u0443\u0440\u0433\u0430\u043d\u043d\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D1%83%D1%80%D0%B3%D0%B0%D0%BD%D0%BD%D0%B0%D1%8F\/"},{"name":"\u041a\u0443\u0440\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D1%83%D1%80%D1%81%D0%BA\/"},{"name":"\u041a\u0443\u0440\u0441\u043a\u0438\u0439 \u0412\u043e\u043a\u0437\u0430\u043b","url":"\/poezda\/vkz\/%D0%9A%D1%83%D1%80%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB\/"},{"name":"\u041b\u0430\u0434\u043e\u0436\u0441\u043a\u0438\u0439 \u0412\u043e\u043a\u0437\u0430\u043b","url":"\/poezda\/vkz\/%D0%9B%D0%B0%D0%B4%D0%BE%D0%B6%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB\/"},{"name":"\u041b\u0430\u0437\u0430\u0440\u0435\u0432\u0441\u043a\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9B%D0%B0%D0%B7%D0%B0%D1%80%D0%B5%D0%B2%D1%81%D0%BA%D0%B0%D1%8F\/"},{"name":"\u041b\u0435\u0432 \u0422\u043e\u043b\u0441\u0442\u043e\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9B%D0%B5%D0%B2_%D0%A2%D0%BE%D0%BB%D1%81%D1%82%D0%BE%D0%B9\/"},{"name":"\u041b\u0435\u043d\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9B%D0%B5%D0%BD%D0%B0\/"},{"name":"\u041b\u0435\u043d\u0438\u043d\u0433\u0440\u0430\u0434\u0441\u043a\u0438\u0439 \u0412\u043e\u043a\u0437\u0430\u043b","url":"\/poezda\/vkz\/%D0%9B%D0%B5%D0%BD%D0%B8%D0%BD%D0%B3%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB\/"},{"name":"\u041b\u0435\u043d\u0438\u043d\u0441\u043a-\u041a\u0443\u0437\u043d\u0435\u0446\u043a\u0438\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9B%D0%B5%D0%BD%D0%B8%D0%BD%D1%81%D0%BA-%D0%9A%D1%83%D0%B7%D0%BD%D0%B5%D1%86%D0%BA%D0%B8%D0%B9\/"},{"name":"\u041b\u0438\u043f\u0435\u0446\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9B%D0%B8%D0%BF%D0%B5%D1%86%D0%BA\/"},{"name":"\u041b\u0438\u0441\u043a\u0438","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9B%D0%B8%D1%81%D0%BA%D0%B8\/"},{"name":"\u041b\u0438\u0445\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9B%D0%B8%D1%85%D0%B0%D1%8F\/"},{"name":"\u041b\u043e\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9B%D0%BE%D0%BE\/"},{"name":"\u041c\u0430\u0433\u0434\u0430\u0433\u0430\u0447\u0438","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%B0%D0%B3%D0%B4%D0%B0%D0%B3%D0%B0%D1%87%D0%B8\/"},{"name":"\u041c\u0430\u0433\u043d\u0438\u0442\u043e\u0433\u043e\u0440\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%B0%D0%B3%D0%BD%D0%B8%D1%82%D0%BE%D0%B3%D0%BE%D1%80%D1%81%D0%BA\/"},{"name":"\u041c\u0430\u0439\u043a\u043e\u043f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%B0%D0%B9%D0%BA%D0%BE%D0%BF\/"},{"name":"\u041c\u0430\u043c\u043e\u043d\u043e\u0432\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%B0%D0%BC%D0%BE%D0%BD%D0%BE%D0%B2%D0%BE\/"},{"name":"\u041c\u0430\u043d\u0442\u0443\u0440\u043e\u0432\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%B0%D0%BD%D1%82%D1%83%D1%80%D0%BE%D0%B2%D0%BE\/"},{"name":"\u041c\u0430\u0440\u0438\u0438\u043d\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%B0%D1%80%D0%B8%D0%B8%D0%BD%D1%81%D0%BA\/"},{"name":"\u041c\u0430\u0445\u0430\u0447\u043a\u0430\u043b\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%B0%D1%85%D0%B0%D1%87%D0%BA%D0%B0%D0%BB%D0%B0\/"},{"name":"\u041c\u0435\u0436\u0434\u0443\u0440\u0435\u0447\u0435\u043d\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%B5%D0%B6%D0%B4%D1%83%D1%80%D0%B5%D1%87%D0%B5%D0%BD%D1%81%D0%BA\/"},{"name":"\u041c\u0438\u0430\u0441\u0441","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%B8%D0%B0%D1%81%D1%81\/"},{"name":"\u041c\u0438\u043a\u0443\u043d\u044c","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%B8%D0%BA%D1%83%D0%BD%D1%8C\/"},{"name":"\u041c\u0438\u043b\u043b\u0435\u0440\u043e\u0432\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%B8%D0%BB%D0%BB%D0%B5%D1%80%D0%BE%D0%B2%D0%BE\/"},{"name":"\u041c\u0438\u043d\u0435\u0440\u0430\u043b\u044c\u043d\u044b\u0435 \u0412\u043e\u0434\u044b","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%B8%D0%BD%D0%B5%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5_%D0%92%D0%BE%D0%B4%D1%8B\/"},{"name":"\u041c\u0438\u0447\u0443\u0440\u0438\u043d\u0441\u043a-\u0423\u0440\u0430\u043b\u044c\u0441\u043a\u0438\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%B8%D1%87%D1%83%D1%80%D0%B8%D0%BD%D1%81%D0%BA-%D0%A3%D1%80%D0%B0%D0%BB%D1%8C%D1%81%D0%BA%D0%B8%D0%B9\/"},{"name":"\u041c\u043e\u0433\u043e\u0447\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%BE%D0%B3%D0%BE%D1%87%D0%B0\/"},{"name":"\u041c\u043e\u0441\u043a\u043e\u0432\u0441\u043a\u0438\u0439 \u0412\u043e\u043a\u0437\u0430\u043b","url":"\/poezda\/vkz\/%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB\/"},{"name":"\u041c\u043e\u0448\u043a\u043e\u0432\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%BE%D1%88%D0%BA%D0%BE%D0%B2%D0%BE\/"},{"name":"\u041c\u0443\u0440\u043c\u0430\u043d\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D1%83%D1%80%D0%BC%D0%B0%D0%BD%D1%81%D0%BA\/"},{"name":"\u041c\u0443\u0440\u043e\u043c","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D1%83%D1%80%D0%BE%D0%BC\/"},{"name":"\u041d\u0430\u0431\u0435\u0440\u0435\u0436\u043d\u044b\u0435 \u0427\u0435\u043b\u043d\u044b","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%B0%D0%B1%D0%B5%D1%80%D0%B5%D0%B6%D0%BD%D1%8B%D0%B5_%D0%A7%D0%B5%D0%BB%D0%BD%D1%8B\/"},{"name":"\u041d\u0430\u0432\u0430\u0448\u0438\u043d\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%B0%D0%B2%D0%B0%D1%88%D0%B8%D0%BD%D0%BE\/"},{"name":"\u041d\u0430\u0437\u044b\u0432\u0430\u0435\u0432\u0441\u043a\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%B0%D0%B7%D1%8B%D0%B2%D0%B0%D0%B5%D0%B2%D1%81%D0%BA%D0%B0%D1%8F\/"},{"name":"\u041d\u0430\u043b\u044c\u0447\u0438\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%B0%D0%BB%D1%8C%D1%87%D0%B8%D0%BA\/"},{"name":"\u041d\u0430\u0443\u0448\u043a\u0438","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%B0%D1%83%D1%88%D0%BA%D0%B8\/"},{"name":"\u041d\u0435\u0432\u0438\u043d\u043d\u043e\u043c\u044b\u0441\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%B5%D0%B2%D0%B8%D0%BD%D0%BD%D0%BE%D0%BC%D1%8B%D1%81%D1%81%D0%BA\/"},{"name":"\u041d\u0435\u0440\u044e\u043d\u0433\u0440\u0438","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%B5%D1%80%D1%8E%D0%BD%D0%B3%D1%80%D0%B8\/"},{"name":"\u041d\u0435\u0441\u0442\u0435\u0440\u043e\u0432","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%B5%D1%81%D1%82%D0%B5%D1%80%D0%BE%D0%B2\/"},{"name":"\u041d\u0438\u0436\u043d\u0435\u043a\u0430\u043c\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%B8%D0%B6%D0%BD%D0%B5%D0%BA%D0%B0%D0%BC%D1%81%D0%BA\/"},{"name":"\u041d\u0438\u0436\u043d\u0435\u0443\u0434\u0438\u043d\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%B8%D0%B6%D0%BD%D0%B5%D1%83%D0%B4%D0%B8%D0%BD%D1%81%D0%BA\/"},{"name":"\u041d\u0438\u0436\u043d\u0438\u0439 \u041d\u043e\u0432\u0433\u043e\u0440\u043e\u0434","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9_%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4\/"},{"name":"\u041d\u0438\u0436\u043d\u0438\u0439 \u0422\u0430\u0433\u0438\u043b","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9_%D0%A2%D0%B0%D0%B3%D0%B8%D0%BB\/"},{"name":"\u041d\u0438\u043a\u0435\u043b\u044c","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%B8%D0%BA%D0%B5%D0%BB%D1%8C\/"},{"name":"\u041d\u043e\u0432\u0430\u044f \u0427\u0430\u0440\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D0%B2%D0%B0%D1%8F_%D0%A7%D0%B0%D1%80%D0%B0\/"},{"name":"\u041d\u043e\u0432\u0433\u043e\u0440\u043e\u0434","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4\/"},{"name":"\u041d\u043e\u0432\u043e\u043a\u0443\u0437\u043d\u0435\u0446\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D0%B2%D0%BE%D0%BA%D1%83%D0%B7%D0%BD%D0%B5%D1%86%D0%BA\/"},{"name":"\u041d\u043e\u0432\u043e\u043a\u0443\u0439\u0431\u044b\u0448\u0435\u0432\u0441\u043a\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D0%B2%D0%BE%D0%BA%D1%83%D0%B9%D0%B1%D1%8B%D1%88%D0%B5%D0%B2%D1%81%D0%BA%D0%B0%D1%8F\/"},{"name":"\u041d\u043e\u0432\u043e\u0440\u043e\u0441\u0441\u0438\u0439\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D0%B2%D0%BE%D1%80%D0%BE%D1%81%D1%81%D0%B8%D0%B9%D1%81%D0%BA\/"},{"name":"\u041d\u043e\u0432\u043e\u0441\u0438\u0431\u0438\u0440\u0441\u043a-\u0412\u043e\u0441\u0442\u043e\u0447\u043d\u044b\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA-%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D1%8B%D0%B9\/"},{"name":"\u041d\u043e\u0432\u043e\u0441\u0438\u0431\u0438\u0440\u0441\u043a-\u0413\u043b\u0430\u0432\u043d\u044b\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA-%D0%93%D0%BB%D0%B0%D0%B2%D0%BD%D1%8B%D0%B9\/"},{"name":"\u041d\u043e\u0432\u043e\u0441\u0438\u0431\u0438\u0440\u0441\u043a-\u0417\u0430\u043f\u0430\u0434\u043d\u044b\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA-%D0%97%D0%B0%D0%BF%D0%B0%D0%B4%D0%BD%D1%8B%D0%B9\/"},{"name":"\u041d\u043e\u0432\u043e\u0441\u0438\u0431\u0438\u0440\u0441\u043a-\u042e\u0436\u043d\u044b\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA-%D0%AE%D0%B6%D0%BD%D1%8B%D0%B9\/"},{"name":"\u041d\u043e\u0432\u043e\u0442\u0440\u043e\u0438\u0446\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D0%B2%D0%BE%D1%82%D1%80%D0%BE%D0%B8%D1%86%D0%BA\/"},{"name":"\u041d\u043e\u0432\u043e\u0447\u0435\u0440\u043a\u0430\u0441\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D0%B2%D0%BE%D1%87%D0%B5%D1%80%D0%BA%D0%B0%D1%81%D1%81%D0%BA\/"},{"name":"\u041d\u043e\u0432\u044b\u0439 \u0423\u0440\u0433\u0430\u043b","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D0%B2%D1%8B%D0%B9_%D0%A3%D1%80%D0%B3%D0%B0%D0%BB\/"},{"name":"\u041d\u043e\u044f\u0431\u0440\u044c\u0441\u043a-1","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D1%8F%D0%B1%D1%80%D1%8C%D1%81%D0%BA-1\/"},{"name":"\u041d\u043e\u044f\u0431\u0440\u044c\u0441\u043a-2","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D1%8F%D0%B1%D1%80%D1%8C%D1%81%D0%BA-2\/"},{"name":"\u041d\u0443\u0440\u043b\u0430\u0442","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D1%83%D1%80%D0%BB%D0%B0%D1%82\/"},{"name":"\u041d\u044f\u043d\u0434\u043e\u043c\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D1%8F%D0%BD%D0%B4%D0%BE%D0%BC%D0%B0\/"},{"name":"\u041e\u0431\u043b\u0443\u0447\u044c\u0435","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9E%D0%B1%D0%BB%D1%83%D1%87%D1%8C%D0%B5\/"},{"name":"\u041e\u0437\u0438\u043d\u043a\u0438","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D1%81%D1%82_%D0%9E%D0%B7%D0%B8%D0%BD%D0%BA%D0%B8\/"},{"name":"\u041e\u043b\u0438\u043c\u043f\u0438\u0439\u0441\u043a\u0438\u0439 \u041f\u0430\u0440\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9E%D0%BB%D0%B8%D0%BC%D0%BF%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9_%D0%9F%D0%B0%D1%80%D0%BA\/"},{"name":"\u041e\u043c\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9E%D0%BC%D1%81%D0%BA\/"},{"name":"\u041e\u0440\u0435\u043b","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9E%D1%80%D0%B5%D0%BB\/"},{"name":"\u041e\u0440\u0435\u043d\u0431\u0443\u0440\u0433","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9E%D1%80%D0%B5%D0%BD%D0%B1%D1%83%D1%80%D0%B3\/"},{"name":"\u041e\u0440\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9E%D1%80%D1%81%D0%BA\/"},{"name":"\u041f\u0430\u0432\u0435\u043b\u0435\u0446\u043a\u0438\u0439 \u0412\u043e\u043a\u0437\u0430\u043b","url":"\/poezda\/vkz\/%D0%9F%D0%B0%D0%B2%D0%B5%D0%BB%D0%B5%D1%86%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB\/"},{"name":"\u041f\u0430\u0434\u0443\u043d\u0441\u043a\u0438\u0435 \u041f\u043e\u0440\u043e\u0433\u0438","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D0%B0%D0%B4%D1%83%D0%BD%D1%81%D0%BA%D0%B8%D0%B5_%D0%9F%D0%BE%D1%80%D0%BE%D0%B3%D0%B8\/"},{"name":"\u041f\u0435\u043d\u0437\u0430-1","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D0%B5%D0%BD%D0%B7%D0%B0-1\/"},{"name":"\u041f\u0435\u0440\u0432\u043e\u0443\u0440\u0430\u043b\u044c\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D0%B5%D1%80%D0%B2%D0%BE%D1%83%D1%80%D0%B0%D0%BB%D1%8C%D1%81%D0%BA\/"},{"name":"\u041f\u0435\u0440\u043c\u044c-2","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D0%B5%D1%80%D0%BC%D1%8C-2\/"},{"name":"\u041f\u0435\u0442\u0440\u043e\u0432 \u0412\u0430\u043b","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D1%81%D1%82_%D0%9F%D0%B5%D1%82%D1%80%D0%BE%D0%B2_%D0%92%D0%B0%D0%BB\/"},{"name":"\u041f\u0435\u0442\u0440\u043e\u0432\u0441\u043a\u0438\u0439 \u0417\u0430\u0432\u043e\u0434","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D0%B5%D1%82%D1%80%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D0%97%D0%B0%D0%B2%D0%BE%D0%B4\/"},{"name":"\u041f\u0435\u0442\u0440\u043e\u0437\u0430\u0432\u043e\u0434\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D0%B5%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%B2%D0%BE%D0%B4%D1%81%D0%BA\/"},{"name":"\u041f\u0435\u0447\u043e\u0440\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D0%B5%D1%87%D0%BE%D1%80%D0%B0\/"},{"name":"\u041f\u043b\u0435\u0441\u0435\u0446\u043a\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D0%BB%D0%B5%D1%81%D0%B5%D1%86%D0%BA%D0%B0%D1%8F\/"},{"name":"\u041f\u043e\u0432\u043e\u0440\u0438\u043d\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D0%BE%D0%B2%D0%BE%D1%80%D0%B8%D0%BD%D0%BE\/"},{"name":"\u041f\u043e\u0442\u044c\u043c\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D0%BE%D1%82%D1%8C%D0%BC%D0%B0\/"},{"name":"\u041f\u0440\u043e\u043a\u043e\u043f\u044c\u0435\u0432\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D1%80%D0%BE%D0%BA%D0%BE%D0%BF%D1%8C%D0%B5%D0%B2%D1%81%D0%BA\/"},{"name":"\u041f\u0440\u043e\u0445\u043b\u0430\u0434\u043d\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D1%80%D0%BE%D1%85%D0%BB%D0%B0%D0%B4%D0%BD%D0%B0%D1%8F\/"},{"name":"\u041f\u0441\u043a\u043e\u0432","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D1%81%D0%BA%D0%BE%D0%B2\/"},{"name":"\u041f\u044b\u0442\u044c-\u042f\u0445","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D1%8B%D1%82%D1%8C-%D0%AF%D1%85\/"},{"name":"\u041f\u044f\u0442\u0438\u0433\u043e\u0440\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D1%8F%D1%82%D0%B8%D0%B3%D0%BE%D1%80%D1%81%D0%BA\/"},{"name":"\u0420\u0430\u043d\u0435\u043d\u0431\u0443\u0440\u0433","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A0%D0%B0%D0%BD%D0%B5%D0%BD%D0%B1%D1%83%D1%80%D0%B3\/"},{"name":"\u0420\u0435\u0432\u0434\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A0%D0%B5%D0%B2%D0%B4%D0%B0\/"},{"name":"\u0420\u0438\u0436\u0441\u043a\u0438\u0439 \u0412\u043e\u043a\u0437\u0430\u043b","url":"\/poezda\/vkz\/%D0%A0%D0%B8%D0%B6%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB\/"},{"name":"\u0420\u043e\u0437\u0430 \u0425\u0443\u0442\u043e\u0440","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A0%D0%BE%D0%B7%D0%B0_%D0%A5%D1%83%D1%82%D0%BE%D1%80\/"},{"name":"\u0420\u043e\u0441\u0441\u043e\u0448\u044c","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A0%D0%BE%D1%81%D1%81%D0%BE%D1%88%D1%8C\/"},{"name":"\u0420\u043e\u0441\u0442\u043e\u0432-\u0413\u043b\u0430\u0432\u043d\u044b\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%93%D0%BB%D0%B0%D0%B2%D0%BD%D1%8B%D0%B9\/"},{"name":"\u0420\u043e\u0441\u0442\u043e\u0432-\u042f\u0440\u043e\u0441\u043b\u0430\u0432\u0441\u043a\u0438\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%AF%D1%80%D0%BE%D1%81%D0%BB%D0%B0%D0%B2%D1%81%D0%BA%D0%B8%D0%B9\/"},{"name":"\u0420\u0442\u0438\u0449\u0435\u0432\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A0%D1%82%D0%B8%D1%89%D0%B5%D0%B2%D0%BE\/"},{"name":"\u0420\u0443\u0431\u0446\u043e\u0432\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A0%D1%83%D0%B1%D1%86%D0%BE%D0%B2%D1%81%D0%BA\/"},{"name":"\u0420\u0443\u0436\u0438\u043d\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A0%D1%83%D0%B6%D0%B8%D0%BD%D0%BE\/"},{"name":"\u0420\u0443\u0437\u0430\u0435\u0432\u043a\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A0%D1%83%D0%B7%D0%B0%D0%B5%D0%B2%D0%BA%D0%B0\/"},{"name":"\u0420\u044b\u0431\u0438\u043d\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A0%D1%8B%D0%B1%D0%B8%D0%BD%D1%81%D0%BA\/"},{"name":"\u0420\u044f\u0437\u0430\u043d\u044c-1","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A0%D1%8F%D0%B7%D0%B0%D0%BD%D1%8C-1\/"},{"name":"\u0420\u044f\u0437\u0430\u043d\u044c-2","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A0%D1%8F%D0%B7%D0%B0%D0%BD%D1%8C-2\/"},{"name":"\u0421\u0430\u0432\u0435\u043b\u043e\u0432\u0441\u043a\u0438\u0439 \u0412\u043e\u043a\u0437\u0430\u043b","url":"\/poezda\/vkz\/%D0%A1%D0%B0%D0%B2%D0%B5%D0%BB%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB\/"},{"name":"\u0421\u0430\u043a\u0438","url":"\/poezda\/vkz\/%D0%A1%D0%B0%D0%BA%D0%B8\/"},{"name":"\u0421\u0430\u043b\u0430\u0432\u0430\u0442","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B0%D0%BB%D0%B0%D0%B2%D0%B0%D1%82\/"},{"name":"\u0421\u0430\u043b\u044c\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B0%D0%BB%D1%8C%D1%81%D0%BA\/"},{"name":"\u0421\u0430\u043c\u0430\u0440\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0\/"},{"name":"\u0421\u0430\u0440\u0430\u043d\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B0%D1%80%D0%B0%D0%BD%D1%81%D0%BA\/"},{"name":"\u0421\u0430\u0440\u0430\u043f\u0443\u043b","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B0%D1%80%D0%B0%D0%BF%D1%83%D0%BB\/"},{"name":"\u0421\u0430\u0440\u0430\u0442\u043e\u0432-1","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B0%D1%80%D0%B0%D1%82%D0%BE%D0%B2-1\/"},{"name":"\u0421\u0432\u043e\u0431\u043e\u0434\u043d\u044b\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B2%D0%BE%D0%B1%D0%BE%D0%B4%D0%BD%D1%8B%D0%B9\/"},{"name":"\u0421\u0435\u0432\u0430\u0441\u0442\u043e\u043f\u043e\u043b\u044c","url":"\/poezda\/vkz\/%D1%81%D0%B5%D0%B2%D0%B0%D1%81%D1%82%D0%BE%D0%BF%D0%BE%D0%BB%D1%8C%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB\/"},{"name":"\u0421\u0435\u0432\u0435\u0440\u043e\u0431\u0430\u0439\u043a\u0430\u043b\u044c\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B5%D0%B2%D0%B5%D1%80%D0%BE%D0%B1%D0%B0%D0%B9%D0%BA%D0%B0%D0%BB%D1%8C%D1%81%D0%BA\/"},{"name":"\u0421\u0435\u0432\u0435\u0440\u043e\u0434\u0432\u0438\u043d\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B5%D0%B2%D0%B5%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%BD%D1%81%D0%BA\/"},{"name":"\u0421\u0435\u0440\u0433\u0430\u0447","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B5%D1%80%D0%B3%D0%B0%D1%87\/"},{"name":"\u0421\u0435\u0440\u0434\u043e\u0431\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B5%D1%80%D0%B4%D0%BE%D0%B1%D1%81%D0%BA\/"},{"name":"\u0421\u0435\u0440\u043e\u0432","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B5%D1%80%D0%BE%D0%B2\/"},{"name":"\u0421\u0438\u0431\u0430\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B8%D0%B1%D0%B0%D0%B9\/"},{"name":"\u0421\u0438\u0431\u0438\u0440\u0446\u0435\u0432\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B8%D0%B1%D0%B8%D1%80%D1%86%D0%B5%D0%B2%D0%BE\/"},{"name":"\u0421\u0438\u043c\u0444\u0435\u0440\u043e\u043f\u043e\u043b\u044c ","url":"\/poezda\/vkz\/%D1%81%D0%B8%D0%BC%D1%84%D0%B5%D1%80%D0%BE%D0%BF%D0%BE%D0%BB%D1%8C%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB\/"},{"name":"\u0421\u043a\u043e\u0432\u043e\u0440\u043e\u0434\u0438\u043d\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%BA%D0%BE%D0%B2%D0%BE%D1%80%D0%BE%D0%B4%D0%B8%D0%BD%D0%BE\/"},{"name":"\u0421\u043b\u0430\u0432\u0433\u043e\u0440\u043e\u0434","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%BB%D0%B0%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4\/"},{"name":"\u0421\u043b\u044e\u0434\u044f\u043d\u043a\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%BB%D1%8E%D0%B4%D1%8F%D0%BD%D0%BA%D0%B0\/"},{"name":"\u0421\u043c\u043e\u043b\u0435\u043d\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%BC%D0%BE%D0%BB%D0%B5%D0%BD%D1%81%D0%BA\/"},{"name":"\u0421\u043e\u0441\u043d\u043e\u0433\u043e\u0440\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%BE%D1%81%D0%BD%D0%BE%D0%B3%D0%BE%D1%80%D1%81%D0%BA\/"},{"name":"\u0421\u043e\u0447\u0438","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%BE%D1%87%D0%B8\/"},{"name":"\u0421\u043f\u0430\u0441\u0441\u043a-\u0414\u0430\u043b\u044c\u043d\u0438\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%BF%D0%B0%D1%81%D1%81%D0%BA-%D0%94%D0%B0%D0%BB%D1%8C%D0%BD%D0%B8%D0%B9\/"},{"name":"\u0421\u0442\u0430\u0432\u0440\u043e\u043f\u043e\u043b\u044c","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D1%82%D0%B0%D0%B2%D1%80%D0%BE%D0%BF%D0%BE%D0%BB%D1%8C\/"},{"name":"\u0421\u0442\u0430\u043d\u0446\u0438\u044f \u0410\u0439\u0432\u0430\u0437\u043e\u0432\u0441\u043a\u0430\u044f","url":"\/poezda\/vkz\/%D0%90%D0%B9%D0%B2%D0%B0%D0%B7%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F\/"},{"name":"\u0421\u0442\u0430\u043d\u0446\u0438\u044f \u0412\u043b\u0430\u0434\u0438\u0441\u043b\u0430\u0432\u043e\u0432\u043a\u0430","url":"\/poezda\/vkz\/%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D1%81%D0%BB%D0%B0%D0%B2%D0%BE%D0%B2%D0%BA%D0%B0\/"},{"name":"\u0421\u0442\u0430\u043d\u0446\u0438\u044f \u0415\u0432\u043f\u0430\u0442\u043e\u0440\u0438\u044f-\u041a\u0443\u0440\u043e\u0440\u0442","url":"\/poezda\/vkz\/%D0%95%D0%B2%D0%BF%D0%B0%D1%82%D0%BE%D1%80%D0%B8%D1%8F_%D0%BA%D1%83%D1%80%D0%BE%D1%80%D1%82\/"},{"name":"\u0421\u0442\u0430\u043d\u0446\u0438\u044f \u0418\u043d\u043a\u0435\u0440\u043c\u0430\u043d-1","url":"\/poezda\/vkz\/%D0%98%D0%BD%D0%BA%D0%B5%D1%80%D0%BC%D0%B0%D0%BD\/"},{"name":"\u0421\u0442\u0430\u043d\u0446\u0438\u044f \u041a\u0440\u0430\u0441\u043d\u043e\u043f\u0435\u0440\u0435\u043a\u043e\u043f\u0441\u043a","url":"\/poezda\/vkz\/%D0%BA%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%BF%D0%B5%D1%80%D0%B5%D0%BA%D0%BE%D0%BF%D1%81%D0%BA\/"},{"name":"\u0421\u0442\u0430\u043d\u0446\u0438\u044f \u0421\u0435\u043c\u044c \u041a\u043e\u043b\u043e\u0434\u0435\u0437\u0435\u0439","url":"\/poezda\/vkz\/%D1%81%D0%B5%D0%BC%D1%8C_%D0%BA%D0%BE%D0%BB%D0%BE%D0%B4%D0%B5%D0%B7%D0%B5%D0%B9\/"},{"name":"\u0421\u0442\u0430\u043d\u0446\u0438\u044f \u0427\u0438\u0441\u0442\u043e\u043f\u043e\u043b\u044c\u0435","url":"\/poezda\/vkz\/%D0%A7%D0%B8%D1%81%D1%82%D0%BE%D0%BF%D0%BE%D0%BB%D1%8C%D0%B5\/"},{"name":"\u0421\u0442\u0430\u0440\u043e\u043c\u0438\u043d\u0441\u043a\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D1%82%D0%B0%D1%80%D0%BE%D0%BC%D0%B8%D0%BD%D1%81%D0%BA%D0%B0%D1%8F\/"},{"name":"\u0421\u0442\u0430\u0440\u044b\u0439 \u041e\u0441\u043a\u043e\u043b","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D1%82%D0%B0%D1%80%D1%8B%D0%B9_%D0%9E%D1%81%D0%BA%D0%BE%D0%BB\/"},{"name":"\u0421\u0442\u0435\u0440\u043b\u0438\u0442\u0430\u043c\u0430\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D1%82%D0%B5%D1%80%D0%BB%D0%B8%D1%82%D0%B0%D0%BC%D0%B0%D0%BA\/"},{"name":"\u0421\u0443\u0440\u0433\u0443\u0442","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D1%83%D1%80%D0%B3%D1%83%D1%82\/"},{"name":"\u0421\u044b\u0437\u0440\u0430\u043d\u044c-1","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D1%8B%D0%B7%D1%80%D0%B0%D0%BD%D1%8C-1\/"},{"name":"\u0421\u044b\u0437\u0440\u0430\u043d\u044c-\u0413\u043e\u0440\u043e\u0434","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D1%8B%D0%B7%D1%80%D0%B0%D0%BD%D1%8C-%D0%93%D0%BE%D1%80%D0%BE%D0%B4\/"},{"name":"\u0421\u044b\u043a\u0442\u044b\u0432\u043a\u0430\u0440","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D1%8B%D0%BA%D1%82%D1%8B%D0%B2%D0%BA%D0%B0%D1%80\/"},{"name":"\u0422\u0430\u0433\u0430\u043d\u0440\u043e\u0433","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%B0%D0%B3%D0%B0%D0%BD%D1%80%D0%BE%D0%B3\/"},{"name":"\u0422\u0430\u0439\u0433\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%B0%D0%B9%D0%B3%D0%B0\/"},{"name":"\u0422\u0430\u0439\u0448\u0435\u0442","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%B0%D0%B9%D1%88%D0%B5%D1%82\/"},{"name":"\u0422\u0430\u043a\u0441\u0438\u043c\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%B0%D0%BA%D1%81%D0%B8%D0%BC%D0%BE\/"},{"name":"\u0422\u0430\u043b\u043e\u0432\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%B0%D0%BB%D0%BE%D0%B2%D0%B0%D1%8F\/"},{"name":"\u0422\u0430\u043c\u0431\u043e\u0432","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%B0%D0%BC%D0%B1%D0%BE%D0%B2\/"},{"name":"\u0422\u0430\u0442\u0430\u0440\u0441\u043a\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%B0%D1%82%D0%B0%D1%80%D1%81%D0%BA%D0%B0%D1%8F\/"},{"name":"\u0422\u0432\u0435\u0440\u044c","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%B2%D0%B5%D1%80%D1%8C\/"},{"name":"\u0422\u0438\u043c\u0430\u0448\u0435\u0432\u0441\u043a\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%B8%D0%BC%D0%B0%D1%88%D0%B5%D0%B2%D1%81%D0%BA%D0%B0%D1%8F\/"},{"name":"\u0422\u0438\u0445\u043e\u043e\u043a\u0435\u0430\u043d\u0441\u043a\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%B8%D1%85%D0%BE%D0%BE%D0%BA%D0%B5%D0%B0%D0%BD%D1%81%D0%BA%D0%B0%D1%8F\/"},{"name":"\u0422\u0438\u0445\u043e\u0440\u0435\u0446\u043a\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%B8%D1%85%D0%BE%D1%80%D0%B5%D1%86%D0%BA%D0%B0%D1%8F\/"},{"name":"\u0422\u043e\u0431\u043e\u043b\u044c\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%BE%D0%B1%D0%BE%D0%BB%D1%8C%D1%81%D0%BA\/"},{"name":"\u0422\u043e\u0433\u0443\u0447\u0438\u043d","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%BE%D0%B3%D1%83%D1%87%D0%B8%D0%BD\/"},{"name":"\u0422\u043e\u043b\u044c\u044f\u0442\u0442\u0438","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%BE%D0%BB%D1%8C%D1%8F%D1%82%D1%82%D0%B8\/"},{"name":"\u0422\u043e\u043c\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%BE%D0%BC%D1%81%D0%BA\/"},{"name":"\u0422\u043e\u043d\u043d\u0435\u043b\u044c\u043d\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%BE%D0%BD%D0%BD%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F\/"},{"name":"\u0422\u043e\u043f\u043a\u0438","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%BE%D0%BF%D0%BA%D0%B8\/"},{"name":"\u0422\u0440\u043e\u0438\u0446\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D1%80%D0%BE%D0%B8%D1%86%D0%BA\/"},{"name":"\u0422\u0443\u0430\u043f\u0441\u0435","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D1%83%D0%B0%D0%BF%D1%81%D0%B5\/"},{"name":"\u0422\u0443\u0439\u043c\u0430\u0437\u044b","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D1%83%D0%B9%D0%BC%D0%B0%D0%B7%D1%8B\/"},{"name":"\u0422\u0443\u043b\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D1%83%D0%BB%D0%B0\/"},{"name":"\u0422\u0443\u043b\u0443\u043d","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D1%83%D0%BB%D1%83%D0%BD\/"},{"name":"\u0422\u044b\u043d\u0434\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D1%8B%D0%BD%D0%B4%D0%B0\/"},{"name":"\u0422\u044e\u043c\u0435\u043d\u044c","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D1%8E%D0%BC%D0%B5%D0%BD%D1%8C\/"},{"name":"\u0423\u043b\u0430\u043d-\u0423\u0434\u044d","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A3%D0%BB%D0%B0%D0%BD-%D0%A3%D0%B4%D1%8D\/"},{"name":"\u0423\u043b\u044c\u044f\u043d\u043e\u0432\u0441\u043a-\u0426\u0435\u043d\u0442\u0440\u0430\u043b\u044c\u043d\u044b\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A3%D0%BB%D1%8C%D1%8F%D0%BD%D0%BE%D0%B2%D1%81%D0%BA-%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9\/"},{"name":"\u0423\u0440\u0431\u0430\u0445","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D1%81%D1%82_%D0%A3%D1%80%D0%B1%D0%B0%D1%85\/"},{"name":"\u0423\u0440\u044e\u043f\u0438\u043d\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D1%81%D1%82_%D0%A3%D1%80%D1%8E%D0%BF%D0%B8%D0%BD%D1%81%D0%BA\/"},{"name":"\u0423\u0441\u0438\u043d\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A3%D1%81%D0%B8%D0%BD%D1%81%D0%BA\/"},{"name":"\u0423\u0441\u043e\u043b\u044c\u0435-\u0421\u0438\u0431\u0438\u0440\u0441\u043a\u043e\u0435","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A3%D1%81%D0%BE%D0%BB%D1%8C%D0%B5-%D0%A1%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA%D0%BE%D0%B5\/"},{"name":"\u0423\u0441\u0441\u0443\u0440\u0438\u0439\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A3%D1%81%D1%81%D1%83%D1%80%D0%B8%D0%B9%D1%81%D0%BA\/"},{"name":"\u0423\u0441\u0442\u044c-\u0418\u043b\u0438\u043c\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A3%D1%81%D1%82%D1%8C-%D0%98%D0%BB%D0%B8%D0%BC%D1%81%D0%BA\/"},{"name":"\u0423\u0441\u0442\u044c-\u041a\u0430\u0442\u0430\u0432","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A3%D1%81%D1%82%D1%8C-%D0%9A%D0%B0%D1%82%D0%B0%D0%B2\/"},{"name":"\u0423\u0444\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A3%D1%84%D0%B0\/"},{"name":"\u0423\u0445\u0442\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A3%D1%85%D1%82%D0%B0\/"},{"name":"\u0424\u0435\u043e\u0434\u043e\u0441\u0438\u0438","url":"\/poezda\/vkz\/%D0%A4%D0%B5%D0%BE%D0%B4%D0%BE%D1%81%D0%B8%D1%8F\/"},{"name":"\u0424\u0438\u043d\u043b\u044f\u043d\u0434\u0441\u043a\u0438\u0439 \u0412\u043e\u043a\u0437\u0430\u043b","url":"\/poezda\/vkz\/%D0%A4%D0%B8%D0%BD%D0%BB%D1%8F%D0%BD%D0%B4%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB\/"},{"name":"\u0424\u0440\u043e\u043b\u043e\u0432\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A4%D1%80%D0%BE%D0%BB%D0%BE%D0%B2%D0%BE\/"},{"name":"\u0425\u0430\u0431\u0430\u0440\u043e\u0432\u0441\u043a-1","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A5%D0%B0%D0%B1%D0%B0%D1%80%D0%BE%D0%B2%D1%81%D0%BA-1\/"},{"name":"\u0425\u0430\u0441\u0430\u043d","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A5%D0%B0%D1%81%D0%B0%D0%BD\/"},{"name":"\u0425\u043e\u0441\u0442\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A5%D0%BE%D1%81%D1%82%D0%B0\/"},{"name":"\u0427\u0430\u043d\u044b","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A7%D0%B0%D0%BD%D1%8B\/"},{"name":"\u0427\u0430\u043f\u0430\u0435\u0432\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A7%D0%B0%D0%BF%D0%B0%D0%B5%D0%B2%D1%81%D0%BA\/"},{"name":"\u0427\u0435\u0431\u043e\u043a\u0441\u0430\u0440\u044b","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A7%D0%B5%D0%B1%D0%BE%D0%BA%D1%81%D0%B0%D1%80%D1%8B\/"},{"name":"\u0427\u0435\u043b\u044f\u0431\u0438\u043d\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA\/"},{"name":"\u0427\u0435\u0440\u0435\u043c\u0445\u043e\u0432\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A7%D0%B5%D1%80%D0%B5%D0%BC%D1%85%D0%BE%D0%B2%D0%BE\/"},{"name":"\u0427\u0435\u0440\u0435\u043f\u0430\u043d\u043e\u0432\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A7%D0%B5%D1%80%D0%B5%D0%BF%D0%B0%D0%BD%D0%BE%D0%B2%D0%BE\/"},{"name":"\u0427\u0435\u0440\u0435\u043f\u043e\u0432\u0435\u0446","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A7%D0%B5%D1%80%D0%B5%D0%BF%D0%BE%D0%B2%D0%B5%D1%86\/"},{"name":"\u0427\u0435\u0440\u043a\u0435\u0441\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A7%D0%B5%D1%80%D0%BA%D0%B5%D1%81%D1%81%D0%BA\/"},{"name":"\u0427\u0435\u0440\u0442\u043a\u043e\u0432\u043e","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A7%D0%B5%D1%80%D1%82%D0%BA%D0%BE%D0%B2%D0%BE\/"},{"name":"\u0427\u0438\u0442\u0430-2","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A7%D0%B8%D1%82%D0%B0-2\/"},{"name":"\u0427\u0443\u043b\u044b\u043c\u0441\u043a\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A7%D1%83%D0%BB%D1%8B%D0%BC%D1%81%D0%BA%D0%B0%D1%8F\/"},{"name":"\u0428\u0430\u0434\u0440\u0438\u043d\u0441\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A8%D0%B0%D0%B4%D1%80%D0%B8%D0%BD%D1%81%D0%BA\/"},{"name":"\u0428\u0430\u0440\u044c\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A8%D0%B0%D1%80%D1%8C%D1%8F\/"},{"name":"\u0428\u0430\u0445\u0442\u043d\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A8%D0%B0%D1%85%D1%82%D0%BD%D0%B0%D1%8F\/"},{"name":"\u0428\u0430\u0445\u0443\u043d\u044c\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A8%D0%B0%D1%85%D1%83%D0%BD%D1%8C%D1%8F\/"},{"name":"\u0428\u0435\u043f\u0441\u0438","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A8%D0%B5%D0%BF%D1%81%D0%B8\/"},{"name":"\u0428\u0438\u043b\u043a\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A8%D0%B8%D0%BB%D0%BA%D0%B0\/"},{"name":"\u0428\u0438\u043c\u0430\u043d\u043e\u0432\u0441\u043a\u0430\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A8%D0%B8%D0%BC%D0%B0%D0%BD%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F\/"},{"name":"\u0428\u0443\u043c\u0435\u0440\u043b\u044f","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A8%D1%83%D0%BC%D0%B5%D1%80%D0%BB%D1%8F\/"},{"name":"\u0428\u0443\u043c\u0438\u0445\u0430","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A8%D1%83%D0%BC%D0%B8%D1%85%D0%B0\/"},{"name":"\u042d\u0441\u0442\u043e-\u0421\u0430\u0434\u043e\u043a","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%AD%D1%81%D1%82%D0%BE-%D0%A1%D0%B0%D0%B4%D0%BE%D0%BA\/"},{"name":"\u042e\u0440\u0433\u0430-1","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%AE%D0%B3%D1%80%D0%B0-1\/"},{"name":"\u042f\u043d\u0430\u0443\u043b","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%AF%D0%BD%D0%B0%D1%83%D0%BB\/"},{"name":"\u042f\u0440\u043e\u0441\u043b\u0430\u0432\u043b\u044c-\u0413\u043b\u0430\u0432\u043d\u044b\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%AF%D1%80%D0%BE%D1%81%D0%BB%D0%B0%D0%B2%D0%BB%D1%8C-%D0%93%D0%BB%D0%B0%D0%B2%D0%BD%D1%8B%D0%B9\/"},{"name":"\u042f\u0440\u043e\u0441\u043b\u0430\u0432\u043b\u044c-\u041c\u043e\u0441\u043a\u043e\u0432\u0441\u043a\u0438\u0439","url":"\/poezda\/vkz\/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%AF%D1%80%D0%BE%D1%81%D0%BB%D0%B0%D0%B2%D0%BB%D1%8C-%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9\/"},{"name":"\u042f\u0440\u043e\u0441\u043b\u0430\u0432\u0441\u043a\u0438\u0439 \u0412\u043e\u043a\u0437\u0430\u043b","url":"\/poezda\/vkz\/%D0%AF%D1%80%D0%BE%D1%81%D0%BB%D0%B0%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB\/"}],"metaVokzalList":[{"name":"\u0412\u0441\u0435 \u0432\u043e\u043a\u0437\u0430\u043b\u044b \u041c\u043e\u0441\u043a\u0432\u044b","url":"\/poezda\/vkz\/\u0432\u043e\u043a\u0437\u0430\u043b\u044b_%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D1%8B\/"},{"name":"\u0412\u0441\u0435 \u0432\u043e\u043a\u0437\u0430\u043b\u044b \u0421\u0430\u043d\u043a\u0442-\u041f\u0435\u0442\u0435\u0440\u0431\u0443\u0440\u0433\u0430","url":"\/poezda\/vkz\/\u0432\u043e\u043a\u0437\u0430\u043b\u044b_%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%D0%B0\/"}],"breadcrumbs":[{"url":"\/poezda\/","name":"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u0435\u0437\u0434\u043e\u0432"},{"name":"\u0412\u0441\u0435 \u0432\u043e\u043a\u0437\u0430\u043b\u044b \u0420\u043e\u0441\u0441\u0438\u0438"}],"title":"\u0412\u0441\u0435 \u0432\u043e\u043a\u0437\u0430\u043b\u044b \u0420\u043e\u0441\u0441\u0438\u0438","description":"\u0412\u043e\u043a\u0437\u0430\u043b\u044b \u0420\u043e\u0441\u0441\u0438\u0438&nbsp;&mdash; \u0432&nbsp;\u0434\u0430\u043d\u043d\u043e\u043c \u0440\u0430\u0437\u0434\u0435\u043b\u0435 \u0432\u044b&nbsp;\u043c\u043e\u0436\u0435\u0442\u0435 \u043e\u0437\u043d\u0430\u043a\u043e\u043c\u0438\u0442\u044c\u0441\u044f \u0441\u043e&nbsp;\u0441\u043f\u0438\u0441\u043a\u043e\u043c \u0432\u0441\u0435\u0445 \u0432\u043e\u043a\u0437\u0430\u043b\u043e\u0432 \u0441\u0442\u0440\u0430\u043d\u044b, \u043d\u0430\u0439\u0442\u0438 \u0430\u0434\u0440\u0435\u0441\u0430, \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u044b, \u0438&nbsp;\u043c\u043d\u043e\u0433\u043e \u0434\u0440\u0443\u0433\u043e\u0439 \u043f\u043e\u043b\u0435\u0437\u043d\u043e\u0439 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438 \u043e&nbsp;\u043d\u0438\u0445."},"configData":{"showDisclaimer":true,"showBannerUiUpdate":false}}</script>
# 	<script>window.langLabels = {"bemp.blocks.train.form.calendar.today":"сегодня","bemp.blocks.train.form.calendar.title":"Календарь","train.interval.save":"Сохранить","bemp.blocks.train.form.main.back":"Обратно","common.default_popup_text_wrong":"Поле заполнено некорректно","bemp.blocks.train.form.main.error_blank_station":"Пожалуйста, укажите название станции","bemp.blocks.train.form.main.alertNoDepartureDate":"Пожалуйста, укажите дату поездки","datepicker.close":"Закрыть","datepicker.prev":"&#x3c;Пред","datepicker.next":"След&#x3e;","datepicker.current":"Сегодня","datepicker.today":"Сегодня","datepicker.tomorrow":"Завтра","datepicker.afterTomorrow":"Послезавтра","list.month.1":"Январь","list.month.10":"Октябрь","list.month.11":"Ноябрь","list.month.12":"Декабрь","list.month.2":"Февраль","list.month.3":"Март","list.month.4":"Апрель","list.month.5":"Май","list.month.6":"Июнь","list.month.7":"Июль","list.month.8":"Август","list.month.9":"Сентябрь","list.month_s.1":"Янв","list.month_s.10":"Окт","list.month_s.11":"Нояб","list.month_s.12":"Дек","list.month_s.2":"Фев","list.month_s.3":"Мар","list.month_s.4":"Апр","list.month_s.5":"Май","list.month_s.6":"Июнь","list.month_s.7":"Июль","list.month_s.8":"Авг","list.month_s.9":"Сен","list.weekdays.0":"воскресенье","list.weekdays.1":"понедельник","list.weekdays.2":"вторник","list.weekdays.3":"среда","list.weekdays.4":"четверг","list.weekdays.5":"пятница","list.weekdays.6":"суббота","list.weekdays_mid.0":"вск","list.weekdays_mid.1":"пнд","list.weekdays_mid.2":"втр","list.weekdays_mid.3":"срд","list.weekdays_mid.4":"чтв","list.weekdays_mid.5":"птн","list.weekdays_mid.6":"сбт","list.week_days.0":"Вс","list.week_days.1":"Пн","list.week_days.2":"Вт","list.week_days.3":"Ср","list.week_days.4":"Чт","list.week_days.5":"Пт","list.week_days.6":"Сб"};</script>
    
#     <link rel="stylesheet" href="https://cdn1.tu-tu.ru/static/train/css/desktop/vokzalList.css.419e1f97bd8d71bb88adbcaffb69368b1.css" type="text/css" media="all" />
# 	<link rel="canonical" href="https://www.tutu.ru/poezda/vkz/"/>

# 						<script>Array.isArray||(Array.isArray=function(a){return {}.toString.call(a)=='[object Array]';});</script>			<script>(function () {var cons = (window.console = window.console || {}), dummy = function() {}, empty = {}, key, props = 'memory'.split(','),
# methods = ('assert,clear,count,debug,dir,dirxml,error,exception,group,' +
# 'groupCollapsed,groupEnd,info,log,markTimeline,profile,profiles,profileEnd,show,table,time,timeEnd,timeline,timelineEnd,timeStamp,trace,warn').split(',');
# 	while (key = props.pop()) cons[key] = cons[key]||empty;
# 	while (key = methods.pop()) cons[key] = cons[key]||dummy;
# })();</script>			<!--[if lte IE 8]>
# 			<script src="https://cdn1.tu-tu.ru/js4/vendors/polyfills/es5-shim.min.js"></script>
# <script src="https://cdn1.tu-tu.ru/js4/vendors/polyfills/es5-sham.min.js"></script>			<![endif]-->
					
		
# 	<script>window.logdata = {"page_id": "6b5Zh0RGy6R", "site_version": "full"};</script>


# 									<script src="https://cdn1.tu-tu.ru/js4/vendors/jq/1.10.2.min.js"></script>
# 				<script>window.jQuery||document.write('<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"><\/script>')</script>
# 				<script>window.jQuery||document.write('<script src="/js4/vendors/jq/1.10.2.min.js"><\/script>')</script>
			
# 							<script src="https://cdn1.tu-tu.ru/js4/vendors/jq/ui.1.10.3.min.js"></script>
			
# 							<script src="https://cdn1.tu-tu.ru/js4/vendors/cookie/jquery.cookie.js"></script>
			
# 							<script>/*
#  RequireJS 2.1.15 Copyright (c) 2010-2014, The Dojo Foundation All Rights Reserved.
#  Available via the MIT or new BSD license.
#  see: http://github.com/jrburke/requirejs for details
# */
# var requirejs,require,define;
# (function(ba){function G(b){return"[object Function]"===K.call(b)}function H(b){return"[object Array]"===K.call(b)}function v(b,c){if(b){var d;for(d=0;d<b.length&&(!b[d]||!c(b[d],d,b));d+=1);}}function T(b,c){if(b){var d;for(d=b.length-1;-1<d&&(!b[d]||!c(b[d],d,b));d-=1);}}function t(b,c){return fa.call(b,c)}function m(b,c){return t(b,c)&&b[c]}function B(b,c){for(var d in b)if(t(b,d)&&c(b[d],d))break}function U(b,c,d,e){c&&B(c,function(c,g){if(d||!t(b,g))e&&"object"===typeof c&&c&&!H(c)&&!G(c)&&!(c instanceof
# RegExp)?(b[g]||(b[g]={}),U(b[g],c,d,e)):b[g]=c});return b}function u(b,c){return function(){return c.apply(b,arguments)}}function ca(b){throw b;}function da(b){if(!b)return b;var c=ba;v(b.split("."),function(b){c=c[b]});return c}function C(b,c,d,e){c=Error(c+"\nhttp://requirejs.org/docs/errors.html#"+b);c.requireType=b;c.requireModules=e;d&&(c.originalError=d);return c}function ga(b){function c(a,k,b){var f,l,c,d,e,g,i,p,k=k&&k.split("/"),h=j.map,n=h&&h["*"];if(a){a=a.split("/");l=a.length-1;j.nodeIdCompat&&
# Q.test(a[l])&&(a[l]=a[l].replace(Q,""));"."===a[0].charAt(0)&&k&&(l=k.slice(0,k.length-1),a=l.concat(a));l=a;for(c=0;c<l.length;c++)if(d=l[c],"."===d)l.splice(c,1),c-=1;else if(".."===d&&!(0===c||1==c&&".."===l[2]||".."===l[c-1])&&0<c)l.splice(c-1,2),c-=2;a=a.join("/")}if(b&&h&&(k||n)){l=a.split("/");c=l.length;a:for(;0<c;c-=1){e=l.slice(0,c).join("/");if(k)for(d=k.length;0<d;d-=1)if(b=m(h,k.slice(0,d).join("/")))if(b=m(b,e)){f=b;g=c;break a}!i&&(n&&m(n,e))&&(i=m(n,e),p=c)}!f&&i&&(f=i,g=p);f&&(l.splice(0,
# g,f),a=l.join("/"))}return(f=m(j.pkgs,a))?f:a}function d(a){z&&v(document.getElementsByTagName("script"),function(k){if(k.getAttribute("data-requiremodule")===a&&k.getAttribute("data-requirecontext")===i.contextName)return k.parentNode.removeChild(k),!0})}function e(a){var k=m(j.paths,a);if(k&&H(k)&&1<k.length)return k.shift(),i.require.undef(a),i.makeRequire(null,{skipMap:!0})([a]),!0}function n(a){var k,c=a?a.indexOf("!"):-1;-1<c&&(k=a.substring(0,c),a=a.substring(c+1,a.length));return[k,a]}function p(a,
# k,b,f){var l,d,e=null,g=k?k.name:null,j=a,p=!0,h="";a||(p=!1,a="_@r"+(K+=1));a=n(a);e=a[0];a=a[1];e&&(e=c(e,g,f),d=m(r,e));a&&(e?h=d&&d.normalize?d.normalize(a,function(a){return c(a,g,f)}):-1===a.indexOf("!")?c(a,g,f):a:(h=c(a,g,f),a=n(h),e=a[0],h=a[1],b=!0,l=i.nameToUrl(h)));b=e&&!d&&!b?"_unnormalized"+(O+=1):"";return{prefix:e,name:h,parentMap:k,unnormalized:!!b,url:l,originalName:j,isDefine:p,id:(e?e+"!"+h:h)+b}}function s(a){var k=a.id,b=m(h,k);b||(b=h[k]=new i.Module(a));return b}function q(a,
# k,b){var f=a.id,c=m(h,f);if(t(r,f)&&(!c||c.defineEmitComplete))"defined"===k&&b(r[f]);else if(c=s(a),c.error&&"error"===k)b(c.error);else c.on(k,b)}function w(a,b){var c=a.requireModules,f=!1;if(b)b(a);else if(v(c,function(b){if(b=m(h,b))b.error=a,b.events.error&&(f=!0,b.emit("error",a))}),!f)g.onError(a)}function x(){R.length&&(ha.apply(A,[A.length,0].concat(R)),R=[])}function y(a){delete h[a];delete V[a]}function F(a,b,c){var f=a.map.id;a.error?a.emit("error",a.error):(b[f]=!0,v(a.depMaps,function(f,
# d){var e=f.id,g=m(h,e);g&&(!a.depMatched[d]&&!c[e])&&(m(b,e)?(a.defineDep(d,r[e]),a.check()):F(g,b,c))}),c[f]=!0)}function D(){var a,b,c=(a=1E3*j.waitSeconds)&&i.startTime+a<(new Date).getTime(),f=[],l=[],g=!1,h=!0;if(!W){W=!0;B(V,function(a){var i=a.map,j=i.id;if(a.enabled&&(i.isDefine||l.push(a),!a.error))if(!a.inited&&c)e(j)?g=b=!0:(f.push(j),d(j));else if(!a.inited&&(a.fetched&&i.isDefine)&&(g=!0,!i.prefix))return h=!1});if(c&&f.length)return a=C("timeout","Load timeout for modules: "+f,null,
# f),a.contextName=i.contextName,w(a);h&&v(l,function(a){F(a,{},{})});if((!c||b)&&g)if((z||ea)&&!X)X=setTimeout(function(){X=0;D()},50);W=!1}}function E(a){t(r,a[0])||s(p(a[0],null,!0)).init(a[1],a[2])}function I(a){var a=a.currentTarget||a.srcElement,b=i.onScriptLoad;a.detachEvent&&!Y?a.detachEvent("onreadystatechange",b):a.removeEventListener("load",b,!1);b=i.onScriptError;(!a.detachEvent||Y)&&a.removeEventListener("error",b,!1);return{node:a,id:a&&a.getAttribute("data-requiremodule")}}function J(){var a;
# for(x();A.length;){a=A.shift();if(null===a[0])return w(C("mismatch","Mismatched anonymous define() module: "+a[a.length-1]));E(a)}}var W,Z,i,L,X,j={waitSeconds:7,baseUrl:"./",paths:{},bundles:{},pkgs:{},shim:{},config:{}},h={},V={},$={},A=[],r={},S={},aa={},K=1,O=1;L={require:function(a){return a.require?a.require:a.require=i.makeRequire(a.map)},exports:function(a){a.usingExports=!0;if(a.map.isDefine)return a.exports?r[a.map.id]=a.exports:a.exports=r[a.map.id]={}},module:function(a){return a.module?
# a.module:a.module={id:a.map.id,uri:a.map.url,config:function(){return m(j.config,a.map.id)||{}},exports:a.exports||(a.exports={})}}};Z=function(a){this.events=m($,a.id)||{};this.map=a;this.shim=m(j.shim,a.id);this.depExports=[];this.depMaps=[];this.depMatched=[];this.pluginMaps={};this.depCount=0};Z.prototype={init:function(a,b,c,f){f=f||{};if(!this.inited){this.factory=b;if(c)this.on("error",c);else this.events.error&&(c=u(this,function(a){this.emit("error",a)}));this.depMaps=a&&a.slice(0);this.errback=
# c;this.inited=!0;this.ignore=f.ignore;f.enabled||this.enabled?this.enable():this.check()}},defineDep:function(a,b){this.depMatched[a]||(this.depMatched[a]=!0,this.depCount-=1,this.depExports[a]=b)},fetch:function(){if(!this.fetched){this.fetched=!0;i.startTime=(new Date).getTime();var a=this.map;if(this.shim)i.makeRequire(this.map,{enableBuildCallback:!0})(this.shim.deps||[],u(this,function(){return a.prefix?this.callPlugin():this.load()}));else return a.prefix?this.callPlugin():this.load()}},load:function(){var a=
# this.map.url;S[a]||(S[a]=!0,i.load(this.map.id,a))},check:function(){if(this.enabled&&!this.enabling){var a,b,c=this.map.id;b=this.depExports;var f=this.exports,l=this.factory;if(this.inited)if(this.error)this.emit("error",this.error);else{if(!this.defining){this.defining=!0;if(1>this.depCount&&!this.defined){if(G(l)){if(this.events.error&&this.map.isDefine||g.onError!==ca)try{f=i.execCb(c,l,b,f)}catch(d){a=d}else f=i.execCb(c,l,b,f);this.map.isDefine&&void 0===f&&((b=this.module)?f=b.exports:this.usingExports&&
# (f=this.exports));if(a)return a.requireMap=this.map,a.requireModules=this.map.isDefine?[this.map.id]:null,a.requireType=this.map.isDefine?"define":"require",w(this.error=a)}else f=l;this.exports=f;if(this.map.isDefine&&!this.ignore&&(r[c]=f,g.onResourceLoad))g.onResourceLoad(i,this.map,this.depMaps);y(c);this.defined=!0}this.defining=!1;this.defined&&!this.defineEmitted&&(this.defineEmitted=!0,this.emit("defined",this.exports),this.defineEmitComplete=!0)}}else this.fetch()}},callPlugin:function(){var a=
# this.map,b=a.id,d=p(a.prefix);this.depMaps.push(d);q(d,"defined",u(this,function(f){var l,d;d=m(aa,this.map.id);var e=this.map.name,P=this.map.parentMap?this.map.parentMap.name:null,n=i.makeRequire(a.parentMap,{enableBuildCallback:!0});if(this.map.unnormalized){if(f.normalize&&(e=f.normalize(e,function(a){return c(a,P,!0)})||""),f=p(a.prefix+"!"+e,this.map.parentMap),q(f,"defined",u(this,function(a){this.init([],function(){return a},null,{enabled:!0,ignore:!0})})),d=m(h,f.id)){this.depMaps.push(f);
# if(this.events.error)d.on("error",u(this,function(a){this.emit("error",a)}));d.enable()}}else d?(this.map.url=i.nameToUrl(d),this.load()):(l=u(this,function(a){this.init([],function(){return a},null,{enabled:!0})}),l.error=u(this,function(a){this.inited=!0;this.error=a;a.requireModules=[b];B(h,function(a){0===a.map.id.indexOf(b+"_unnormalized")&&y(a.map.id)});w(a)}),l.fromText=u(this,function(f,c){var d=a.name,e=p(d),P=M;c&&(f=c);P&&(M=!1);s(e);t(j.config,b)&&(j.config[d]=j.config[b]);try{g.exec(f)}catch(h){return w(C("fromtexteval",
# "fromText eval for "+b+" failed: "+h,h,[b]))}P&&(M=!0);this.depMaps.push(e);i.completeLoad(d);n([d],l)}),f.load(a.name,n,l,j))}));i.enable(d,this);this.pluginMaps[d.id]=d},enable:function(){V[this.map.id]=this;this.enabling=this.enabled=!0;v(this.depMaps,u(this,function(a,b){var c,f;if("string"===typeof a){a=p(a,this.map.isDefine?this.map:this.map.parentMap,!1,!this.skipMap);this.depMaps[b]=a;if(c=m(L,a.id)){this.depExports[b]=c(this);return}this.depCount+=1;q(a,"defined",u(this,function(a){this.defineDep(b,
# a);this.check()}));this.errback&&q(a,"error",u(this,this.errback))}c=a.id;f=h[c];!t(L,c)&&(f&&!f.enabled)&&i.enable(a,this)}));B(this.pluginMaps,u(this,function(a){var b=m(h,a.id);b&&!b.enabled&&i.enable(a,this)}));this.enabling=!1;this.check()},on:function(a,b){var c=this.events[a];c||(c=this.events[a]=[]);c.push(b)},emit:function(a,b){v(this.events[a],function(a){a(b)});"error"===a&&delete this.events[a]}};i={config:j,contextName:b,registry:h,defined:r,urlFetched:S,defQueue:A,Module:Z,makeModuleMap:p,
# nextTick:g.nextTick,onError:w,configure:function(a){a.baseUrl&&"/"!==a.baseUrl.charAt(a.baseUrl.length-1)&&(a.baseUrl+="/");var b=j.shim,c={paths:!0,bundles:!0,config:!0,map:!0};B(a,function(a,b){c[b]?(j[b]||(j[b]={}),U(j[b],a,!0,!0)):j[b]=a});a.bundles&&B(a.bundles,function(a,b){v(a,function(a){a!==b&&(aa[a]=b)})});a.shim&&(B(a.shim,function(a,c){H(a)&&(a={deps:a});if((a.exports||a.init)&&!a.exportsFn)a.exportsFn=i.makeShimExports(a);b[c]=a}),j.shim=b);a.packages&&v(a.packages,function(a){var b,
# a="string"===typeof a?{name:a}:a;b=a.name;a.location&&(j.paths[b]=a.location);j.pkgs[b]=a.name+"/"+(a.main||"main").replace(ia,"").replace(Q,"")});B(h,function(a,b){!a.inited&&!a.map.unnormalized&&(a.map=p(b))});if(a.deps||a.callback)i.require(a.deps||[],a.callback)},makeShimExports:function(a){return function(){var b;a.init&&(b=a.init.apply(ba,arguments));return b||a.exports&&da(a.exports)}},makeRequire:function(a,e){function j(c,d,m){var n,q;e.enableBuildCallback&&(d&&G(d))&&(d.__requireJsBuild=
# !0);if("string"===typeof c){if(G(d))return w(C("requireargs","Invalid require call"),m);if(a&&t(L,c))return L[c](h[a.id]);if(g.get)return g.get(i,c,a,j);n=p(c,a,!1,!0);n=n.id;return!t(r,n)?w(C("notloaded",'Module name "'+n+'" has not been loaded yet for context: '+b+(a?"":". Use require([])"))):r[n]}J();i.nextTick(function(){J();q=s(p(null,a));q.skipMap=e.skipMap;q.init(c,d,m,{enabled:!0});D()});return j}e=e||{};U(j,{isBrowser:z,toUrl:function(b){var d,e=b.lastIndexOf("."),k=b.split("/")[0];if(-1!==
# e&&(!("."===k||".."===k)||1<e))d=b.substring(e,b.length),b=b.substring(0,e);return i.nameToUrl(c(b,a&&a.id,!0),d,!0)},defined:function(b){return t(r,p(b,a,!1,!0).id)},specified:function(b){b=p(b,a,!1,!0).id;return t(r,b)||t(h,b)}});a||(j.undef=function(b){x();var c=p(b,a,!0),e=m(h,b);d(b);delete r[b];delete S[c.url];delete $[b];T(A,function(a,c){a[0]===b&&A.splice(c,1)});e&&(e.events.defined&&($[b]=e.events),y(b))});return j},enable:function(a){m(h,a.id)&&s(a).enable()},completeLoad:function(a){var b,
# c,d=m(j.shim,a)||{},g=d.exports;for(x();A.length;){c=A.shift();if(null===c[0]){c[0]=a;if(b)break;b=!0}else c[0]===a&&(b=!0);E(c)}c=m(h,a);if(!b&&!t(r,a)&&c&&!c.inited){if(j.enforceDefine&&(!g||!da(g)))return e(a)?void 0:w(C("nodefine","No define call for "+a,null,[a]));E([a,d.deps||[],d.exportsFn])}D()},nameToUrl:function(a,b,c){var d,e,h;(d=m(j.pkgs,a))&&(a=d);if(d=m(aa,a))return i.nameToUrl(d,b,c);if(g.jsExtRegExp.test(a))d=a+(b||"");else{d=j.paths;a=a.split("/");for(e=a.length;0<e;e-=1)if(h=a.slice(0,
# e).join("/"),h=m(d,h)){H(h)&&(h=h[0]);a.splice(0,e,h);break}d=a.join("/");d+=b||(/^data\:|\?/.test(d)||c?"":".js");d=("/"===d.charAt(0)||d.match(/^[\w\+\.\-]+:/)?"":j.baseUrl)+d}return j.urlArgs?d+((-1===d.indexOf("?")?"?":"&")+j.urlArgs):d},load:function(a,b){g.load(i,a,b)},execCb:function(a,b,c,d){return b.apply(d,c)},onScriptLoad:function(a){if("load"===a.type||ja.test((a.currentTarget||a.srcElement).readyState))N=null,a=I(a),i.completeLoad(a.id)},onScriptError:function(a){var b=I(a);if(!e(b.id))return w(C("scripterror",
# "Script error for: "+b.id,a,[b.id]))}};i.require=i.makeRequire();return i}var g,x,y,D,I,E,N,J,s,O,ka=/(\/\*([\s\S]*?)\*\/|([^:]|^)\/\/(.*)$)/mg,la=/[^.]\s*require\s*\(\s*["']([^'"\s]+)["']\s*\)/g,Q=/\.js$/,ia=/^\.\//;x=Object.prototype;var K=x.toString,fa=x.hasOwnProperty,ha=Array.prototype.splice,z=!!("undefined"!==typeof window&&"undefined"!==typeof navigator&&window.document),ea=!z&&"undefined"!==typeof importScripts,ja=z&&"PLAYSTATION 3"===navigator.platform?/^complete$/:/^(complete|loaded)$/,
# Y="undefined"!==typeof opera&&"[object Opera]"===opera.toString(),F={},q={},R=[],M=!1;if("undefined"===typeof define){if("undefined"!==typeof requirejs){if(G(requirejs))return;q=requirejs;requirejs=void 0}"undefined"!==typeof require&&!G(require)&&(q=require,require=void 0);g=requirejs=function(b,c,d,e){var n,p="_";!H(b)&&"string"!==typeof b&&(n=b,H(c)?(b=c,c=d,d=e):b=[]);n&&n.context&&(p=n.context);(e=m(F,p))||(e=F[p]=g.s.newContext(p));n&&e.configure(n);return e.require(b,c,d)};g.config=function(b){return g(b)};
# g.nextTick="undefined"!==typeof setTimeout?function(b){setTimeout(b,4)}:function(b){b()};require||(require=g);g.version="2.1.15";g.jsExtRegExp=/^\/|:|\?|\.js$/;g.isBrowser=z;x=g.s={contexts:F,newContext:ga};g({});v(["toUrl","undef","defined","specified"],function(b){g[b]=function(){var c=F._;return c.require[b].apply(c,arguments)}});if(z&&(y=x.head=document.getElementsByTagName("head")[0],D=document.getElementsByTagName("base")[0]))y=x.head=D.parentNode;g.onError=ca;g.createNode=function(b){var c=
# b.xhtml?document.createElementNS("http://www.w3.org/1999/xhtml","html:script"):document.createElement("script");c.type=b.scriptType||"text/javascript";c.charset="utf-8";c.async=!0;return c};g.load=function(b,c,d){var e=b&&b.config||{};if(z)return e=g.createNode(e,c,d),e.setAttribute("data-requirecontext",b.contextName),e.setAttribute("data-requiremodule",c),e.attachEvent&&!(e.attachEvent.toString&&0>e.attachEvent.toString().indexOf("[native code"))&&!Y?(M=!0,e.attachEvent("onreadystatechange",b.onScriptLoad)):
# (e.addEventListener("load",b.onScriptLoad,!1),e.addEventListener("error",b.onScriptError,!1)),e.src=d,J=e,D?y.insertBefore(e,D):y.appendChild(e),J=null,e;if(ea)try{importScripts(d),b.completeLoad(c)}catch(m){b.onError(C("importscripts","importScripts failed for "+c+" at "+d,m,[c]))}};z&&!q.skipDataMain&&T(document.getElementsByTagName("script"),function(b){y||(y=b.parentNode);if(I=b.getAttribute("data-main"))return s=I,q.baseUrl||(E=s.split("/"),s=E.pop(),O=E.length?E.join("/")+"/":"./",q.baseUrl=
# O),s=s.replace(Q,""),g.jsExtRegExp.test(s)&&(s=I),q.deps=q.deps?q.deps.concat(s):[s],!0});define=function(b,c,d){var e,g;"string"!==typeof b&&(d=c,c=b,b=null);H(c)||(d=c,c=null);!c&&G(d)&&(c=[],d.length&&(d.toString().replace(ka,"").replace(la,function(b,d){c.push(d)}),c=(1===d.length?["require"]:["require","exports","module"]).concat(c)));if(M){if(!(e=J))N&&"interactive"===N.readyState||T(document.getElementsByTagName("script"),function(b){if("interactive"===b.readyState)return N=b}),e=N;e&&(b||
# (b=e.getAttribute("data-requiremodule")),g=F[e.getAttribute("data-requirecontext")])}(g?g.defQueue:R).push([b,c,d])};define.amd={jQuery:!0};g.exec=function(b){return eval(b)};g(q)}})(this);
# </script>
# 				<script>require.config({baseUrl:"/js4/src",appDir:"",waitSeconds:30,paths:{widgets:"widgets",lib:"lib",trait:"trait",module:"module",template:"template",constant:"constant",legacy:"../legacy",trainStaticData:"app/train/data",vendors:"../vendors",Bloodhound:"../vendors/suggest/bloodhound.min",jquery:"../vendors/jq/1.10.2.min",lodash:"../vendors/lodash/3.9.3.min","lodash.assign":"../../../node_modules/lodash.assign/index","lodash.clone":"../../../node_modules/lodash.clone/index","lodash.isempty":"../../../node_modules/lodash.isempty/index",jqueryui:"../vendors/jq/ui.1.10.3.min",moment:"../vendors/jq/plugin/moment/min","moment-range":"../vendors/jq/plugin/moment/moment-range.min",momentRu:"../vendors/jq/plugin/moment/ru",text:"../vendors/rjs/plugin/text",twig:"../vendors/rjs/plugin/twig.min",twigjs:"../vendors/rjs/plugin/twigjs",json:"../vendors/rjs/plugin/json",backbone:"../vendors/backbone/backbone",react:"../vendors/react/14.8/react-with-addons.min","react-dom":"../vendors/react/14.8/react-dom.min","react-dom-server":"../vendors/react/14.8/react-dom-server.min",params:"empty:",logdata:"empty:",calendarParams:"empty:",php:"empty:",langLabels:"empty:",bemp:"reactjs/bemp",templates:"../../templates/twig","@tutu":"../../../node_modules/@tutu",qs:"../../../node_modules/qs/dist/qs",inputmask:"../../../node_modules/inputmask/dist/min/jquery.inputmask.bundle.min",superagent:"../../../node_modules/superagent/superagent",promise:"../../../node_modules/es6-promise/dist/es6-promise.min"},map:{"*":{underscore:"lodash","react/addons":"react"}},shim:{jqueryui:{exports:"$.ui"},typeahead:["jquery"]},config:{twigjs:{autoescape:!1}}});</script>
# 						</head>

# <body class="" onload="if ((function(){return this;})()[(function(){return 'locat'+'i'+'on'})()].hostname.substr(-7) !== 'tutu.'+'ru') location.assign('//tut'+'u.r'+'u');">
				
# <noscript>
# 	<iframe src="//www.googletagmanager.com/ns.html?id=GTM-PFRF35" height="0" width="0" style="display:none;visibility:hidden"></iframe>
# </noscript>
# <script>
# 	(function (w, d, s, l, i) {
# 		w[l] = w[l] || [];
# 		w[l].push({
# 			'gtm.start': new Date().getTime(), event: 'gtm.js'
# 		});
# 		var f = d.getElementsByTagName(s)[0],
# 			j = d.createElement(s), dl = l != 'dataLayer' ? '&l=' + l : '';
# 		j.async = true;
# 		j.src =
# 			'//www.googletagmanager.com/gtm.js?id=' + i + dl;
# 		f.parentNode.insertBefore(j, f);
# 	})(window, document, 'script', 'dataLayer', 'GTM-PFRF35');
# </script>


# 							<div class="t-txt l-vokzal">
# 					<div id="wrapper" class="l-page_wrapper">
# 					<div class="l-vokzal__header">
# 				<div class="l-header">
# 								<div class="row l-header">
						
# <div class="b-header__standart j-header_container _logo_2018">
# 			<div class="top_links_part">
# 			<div class="links_item">
# 				<div class="j-auth-container">
# 	<div class="b-header__user__auth">
# 		<div class="login_string_wrp s-active j-login-string">
# 			<div class="b-header__user__login">
# 				<div class="user_link_wrapper">
# 					<a class="g-link _pseudo m-user_login j-link-tutuid-login" data-ti="uLoginLink" href="https://id.tutu.ru/login/?back_url=https%3A%2F%2Fwww.tutu.ru%2Fpoezda%2Fvkz%2F">Войти</a>
# 					или					<a class="g-link _pseudo m-user_login j-link-tutuid-register" data-ti="uRegistrationLink" href="https://id.tutu.ru/registration/?back_url=https%3A%2F%2Fwww.tutu.ru%2Fpoezda%2Fvkz%2F" >Зарегистрироваться</a>
# 				</div>
# 			</div>
# 		</div>
# 		<div class="logged_string_wrp  j-logged-string">
# 			<div class="b-header__user__logout">
# 				<div class="user_link_wrapper">
# 					<a href="/user/profile/my_orders/" class="g-link _dark" data-ti="uName"></a>
# 				</div>
# 				<a data-ti="uLogoutLink" href="https://id.tutu.ru/logout/?back_url=https%3A%2F%2Fwww.tutu.ru%2Fpoezda%2Fvkz%2F" class="logout j-link-tutuid-logout"></a>
# 			</div>
# 		</div>
# 	</div>
# </div>
# 			</div>

# 			<div class="links_item">
				
# 			</div>

# 			<div class="links_item links_item_orders j-user-orders ">
# 				<div class="orders_link_wrapper">
# 					<a class="g-link _dark" href="/user/profile/my_orders/">Личные заказы</a>
# 				</div>
# 			</div>

			

# 	<div class="links_item links_item_bonuses">
# 		<div class="orders_link_wrapper">
# 			<a class="g-link _dark links_item_bonuses_link" href="https://bonus.tutu.ru" onclick="var d = document, w = window, i = d.createElement('img'), l = (w || w.__INITIAL_PROPS || {}).logdata || {}, sv = l.site_version, p = l.page, pid = l.page_id, src = 'https://www.tutu.ru/ajax/userway_action/hat_bonuses_click/?params=uri%253D%252Fpoezda%252Fvkz%252F%26site_version=' + (sv || 'full') + '%26page=' + p + '%26page_id=' + pid;i.setAttribute('src', src);d.body.appendChild(i);">Бонусы и скидки</a>
# 		</div>
# 	</div>


			
			
# 			<div class="links_item links_item_history rm-infosearch_link j-search_history_show">
# 				<span class="g-link _pseudo _dark">История поисков</span>
# 			</div>
# 		</div>
	
# 	<div class="logo_part">
# 		<div class="logo_wrp">
# 			<a class="g-link _logo _logo_2018" href="/">
# 				<img class="link_img" width="156" height="60" src="https://cdn1.tu-tu.ru/images2/bemp/svg/logo/2023/logo_tutu_final.svg" alt="Tutu.ru"/>
# 			</a>
# 		</div>
# 					<div class="chapter_wrp">
# 																								<a class="g-link _imaged _chapter _train "  href="/poezda/">
# 							<span class="img"></span>
# 							<span class="text">Ж/д билеты</span>
# 													</a>
# 												</div>
		
# 			</div>

# 			<div class="menu_part j-menu_part">
			
# <div class="b-header__menu__standart j-header-menu  _small_margin">
# 						<div class="menu_item menu_item--avia j-menu_item" data-log="avia">
# 				<a class="g-link _imaged _avia" href="https://avia.tutu.ru/" >
# 					<span class="img"></span><span class="text">Авиабилеты</span>
# 				</a>
# 			</div>
# 											<div class="menu_item menu_item--bus j-menu_item" data-log="bus">
# 				<a class="g-link _imaged _bus" href="https://bus.tutu.ru/" >
# 					<span class="img"></span><span class="text">Автобусы</span>
# 				</a>
# 			</div>
# 								<div class="menu_item menu_item--hotel j-menu_item" data-log="hotel">
# 				<a class="g-link _imaged _hotel" href="https://hotel.tutu.ru/" >
# 					<span class="img"></span><span class="text">Заказ гостиниц</span>
# 				</a>
# 			</div>
# 								<div class="menu_item menu_item--etrain j-menu_item" data-log="etrain">
# 				<a class="g-link _imaged _etrain" href="/prigorod/" >
# 					<span class="img"></span><span class="text">Электрички</span>
# 				</a>
# 			</div>
# 								<div class="menu_item menu_item--tours j-menu_item" data-log="tour">
# 				<a class="g-link _imaged _tours" href="https://tours.tutu.ru/" >
# 					<span class="img"></span><span class="text">Туры</span>
# 				</a>
# 			</div>
# 								<div class="menu_item menu_item--2read j-menu_item" data-log="toread">
# 				<a class="g-link _imaged _2read" href="/2read/poezda/main/" >
# 					<span class="img"></span><span class="text">Справочная</span>
# 				</a>
# 			</div>
			
# 	</div>
# 		</div>
# 	</div>

# 					</div>
				
# 		</div>
				
# 	<div class="l-search_form">
# 		<!--noindex-->
		
		



#     <div class="b-train__form__main j-main_search_form  rm-clock_infoblock">
#     	<form action="/poezda/rasp_d.php" method="get" class="j-form">
    		    		
#     		<div class="form">
#     			<div class="row_line m-main">
#     				<div class="departure field_wrp">
#     					    						<div class="b-train__form__main__suggest j-station_from ">
# 	<div class='j-selector_wrapper selector_wrapper'>
# 		<div class="b-input__form__standart m-train_form j-input_wrapper">
# 	<input class="input_field j-station_input  j-station_input_from"  tabindex="1" autocomplete="off" name="schedule_station_from" placeholder="Откуда">
# 	<div class="img j-input_image">
# 		<div class="line"></div>
# 		<div class="arrow_down"></div>
# 	</div>
# 	</div>
# 		<input type="hidden" name="nnst1" value="" class="j-station_hidden j-station_hidden_from_hidden" autocomplete="off">
# 	</div>

# 						<div class="input_example">
# 									<span class="hint_wrp">
# 						<span class="g-link _pseudo j-pseudo _bottom" data-id="2000000" data-value="Москва" data-type="popular">Москва</span>, 
# 					</span>
# 									<span class="hint_wrp">
# 						<span class="g-link _pseudo j-pseudo _bottom" data-id="2004000" data-value="Санкт-Петербург" data-type="popular">Санкт-Петербург</span>
# 					</span>
# 							</div>
# 			</div>
#     					    				</div>

#     				<div class="swap_wrp">
#     					<div class="swap_button j-swap_button"></div>
#     				</div>

#     				<div class="arrival field_wrp">
#     					    						<div class="b-train__form__main__suggest j-station_to ">
# 	<div class='j-selector_wrapper selector_wrapper'>
# 		<div class="b-input__form__standart m-train_form j-input_wrapper">
# 	<input class="input_field j-station_input  j-station_input_to"  tabindex="1" autocomplete="off" name="schedule_station_to" placeholder="Куда">
# 	<div class="img j-input_image">
# 		<div class="line"></div>
# 		<div class="arrow_down"></div>
# 	</div>
# 	</div>
# 		<input type="hidden" name="nnst2" value="" class="j-station_hidden j-station_hidden_to_hidden" autocomplete="off">
# 	</div>

# 						<div class="input_example">
# 									<span class="hint_wrp">
# 						<span class="g-link _pseudo j-pseudo _bottom" data-id="2004000" data-value="Санкт-Петербург" data-type="popular">Санкт-Петербург</span>, 
# 					</span>
# 									<span class="hint_wrp">
# 						<span class="g-link _pseudo j-pseudo _bottom" data-id="2000000" data-value="Москва" data-type="popular">Москва</span>
# 					</span>
# 							</div>
# 			</div>
#     					    				</div>

#     				                        <div class="date_start field_wrp">
#         					        						<div class="b-train__form__main__date _with_arrows j-travel_date_date">
# 	<div class="wrapper" data-ti="date_arrow_to">
# 	<div class="b-input__form__standart content j-date  m-train_calendar">
# 		<input type="text"
# 			   class="input_field j-permanent_open j-input j-date_to"
# 			   autocomplete="off"
# 			   value=""
# 			   placeholder="Дата"
# 			   tabindex="2"
# 			    />
# 					<div class="input_clear s-hidden j-input_clear"></div>
# 			</div>
# 	<button data-ti="date_arrow_reduce" class="button reduce j-decrease_to" type="button"></button>
# 	<button data-ti="date_arrow_increase" class="button increase j-increase_to" type="button"></button>
# </div>

# 			<input type="text" class="calendar_input j-calendar_input"/>
	
# 			<input type="hidden" name="date" class="j-date_container"/>
	
# 			 			<div class="clock_ico rm-infoblock_toggle rm-clock" rel="interval" style="height: 12px; top: 10px; right: 25px;"></div>
# 	<input type="hidden" name="timeFrom" value="0" autocomplete="off" disabled/>
# 	<input type="hidden" name="timeTo" value="24" autocomplete="off" disabled/>

			
# 						<div class="input_example">
# 									<span class="g-link _pseudo j-pseudo" data-value="23.01.2025">23 января</span>, 
# 									<span class="g-link _pseudo j-pseudo" data-value="24.01.2025">24 января</span>
# 							</div>
# 			</div>
#         					        				</div>

    					                    
    				
#     				    				<div class="button_wrp m-border_inner" tabindex="4">
    					
# <button class="b-button__arrow__button j-button j-button-submit _title j-submit_button _blue" type="button">
# 	<span class="inner_wrapper">
# 		<span class="arrow"></span>
# 		<span class="name">Найти ж/д билеты</span>
# 		<span class="spinner"></span>
# 	</span>
# </button>
#     				</div>
#     				    			</div>
#     		</div>

#     		        </form>

#     	     		<div class="b-quest_popup_position m-interval rm-interval rm-infoblock_more_block rm-infoblock_popup" rel="interval">
# 	<div class="pop_top_arr_shad"><div class="pop_top_arr"></div></div>
# 	<div class="close rm-infoblock_toggle" rel="interval"></div>
# 	<div class="content content-width">
# 		<div class="title">Укажите интервал времени отправления, если требуется</div>
# 		<form class="b-interval_form">
# 			<div class="floatL">
# 				<input type="text" class="rm-clock-timeFrom rm-clock-times" value="0" autocomplete="off"/>&nbsp;ч.&nbsp;&mdash;&nbsp;
# 				<input type="text" class="rm-clock-timeTo rm-clock-times" value="24" autocomplete="off"/>&nbsp;ч.			</div>
# 			<div class="rm-save_clock_button b-decor_button m-interval"></div>
# 		</form>
# 	</div>
# </div>

#     	    </div>
# 		<!--/noindex-->
# 	</div>

# <script>
# 	window.pageParams = {
# 		initData: {"departureDate":"","isFormDateBack":false,"departure":"","arrival":"","profilerInLabelList":["poezda-search","poezda-search-uit","poezda-search-react","poezda-search-react-uit","poezda-search-nodate","poezda-search-nodate-react"]},
# 		abData: null,
# 		configData: null,
# 	};
# </script>


# 		<div class=" t-txt-s l-vokzal__element l-vokzal__breadcrumbs">
# 			<div class="b-train__common__breadcrumbs__top t-gray" itemscope itemtype="http://schema.org/BreadcrumbList">
# 			<span itemprop="itemListElement" itemscope itemtype="http://schema.org/ListItem">
# 							<a class="g-link _inline crumb" href="/poezda/" itemprop="item">
# 					<span itemprop="name">Расписание поездов</span></a>&nbsp;&bull;
# 						<meta itemprop="position" content="1"/>
# 		</span>
# 			<span itemprop="itemListElement" itemscope itemtype="http://schema.org/ListItem">
# 							<span itemprop="name">Все вокзалы России</span>
# 				<link itemprop="item" href=""/>
# 						<meta itemprop="position" content="2"/>
# 		</span>
# 	</div>		</div>
# 	</div>

# 					<div class="l-vokzal__row">
# 		<div class="l-vokzal__content">

# 			<div class="l-vokzal__element">
# 				<h1 class="l-vokzal__title">Все вокзалы России</h1>
# 				<div>Вокзалы России&nbsp;&mdash; в&nbsp;данном разделе вы&nbsp;можете ознакомиться со&nbsp;списком всех вокзалов страны, найти адреса, телефоны, и&nbsp;много другой полезной информации о&nbsp;них.</div>
# 			</div>


# 			<div class="l-vokzal__element">
# 									<div class="l-vokzal__meta-link-wrapper">
# 						<a class="l-vokzal__meta-link" href="/poezda/vkz/вокзалы_%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D1%8B/">Все вокзалы Москвы</a><br>
# 					</div>
# 									<div class="l-vokzal__meta-link-wrapper">
# 						<a class="l-vokzal__meta-link" href="/poezda/vkz/вокзалы_%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%D0%B0/">Все вокзалы Санкт-Петербурга</a><br>
# 					</div>
# 							</div>
		

# 			<div class="l-vokzal__element">
# 				<div class="b-train--vokzal_list--links">

            
        
        

#     <div class="b-train--vokzal_list--links__row">
#         <div class="b-train--vokzal_list--links__column">
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">А</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D0%B1%D0%B0%D0%BA%D0%B0%D0%BD/" class="b-train--vokzal_list--links__link">Абакан</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D0%B1%D0%B4%D1%83%D0%BB%D0%B8%D0%BD%D0%BE/" class="b-train--vokzal_list--links__link">Абдулино</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D0%B3%D1%80%D1%8B%D0%B7/" class="b-train--vokzal_list--links__link">Агрыз</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D0%B4%D0%BB%D0%B5%D1%80/" class="b-train--vokzal_list--links__link">Адлер</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D0%BA%D1%81%D0%B0%D0%BA%D0%BE%D0%B2%D0%BE/" class="b-train--vokzal_list--links__link">Аксаково</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D0%BB%D0%B5%D0%B9%D1%81%D0%BA%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Алейская</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D0%BD%D0%B0%D0%BF%D0%B0/" class="b-train--vokzal_list--links__link">Анапа</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D0%BD%D0%B3%D0%B0%D1%80%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Ангарск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D0%BD%D0%B6%D0%B5%D1%80%D1%81%D0%BA%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Анжерская</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D1%80%D0%B7%D0%B0%D0%BC%D0%B0%D1%81-1/" class="b-train--vokzal_list--links__link">Арзамас-1</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D1%80%D0%B7%D0%B0%D0%BC%D0%B0%D1%81-2/" class="b-train--vokzal_list--links__link">Арзамас-2</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%80-1/" class="b-train--vokzal_list--links__link">Армавир-1</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D1%80%D0%BC%D0%B0%D0%B2%D0%B8%D1%80-2/" class="b-train--vokzal_list--links__link">Армавир-2</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D1%80%D1%81%D0%B5%D0%BD%D1%8C%D0%B5%D0%B2/" class="b-train--vokzal_list--links__link">Арсеньев</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D1%80%D1%85%D0%B0%D0%BD%D0%B3%D0%B5%D0%BB%D1%8C%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Архангельск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D1%80%D1%85%D0%B0%D1%80%D0%B0/" class="b-train--vokzal_list--links__link">Архара</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D1%81%D1%82%D1%80%D0%B0%D1%85%D0%B0%D0%BD%D1%8C/" class="b-train--vokzal_list--links__link">Астрахань</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D1%82%D0%BA%D0%B0%D1%80%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Аткарск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D1%87%D0%B8%D0%BD%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Ачинск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%90%D1%88%D0%B0/" class="b-train--vokzal_list--links__link">Аша</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B0%D1%8D%D1%80%D0%BE%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9_%D0%BA%D0%BE%D0%BC%D0%BF%D0%BB%D0%B5%D0%BA%D1%81_%D0%90%D0%B4%D0%BB%D0%B5%D1%80/" class="b-train--vokzal_list--links__link">Аэровокзальный Комплекс Адлер</a>
#         </div>
    
# </div>
                                    
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">Б</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B0%D0%BB%D0%B0%D0%BA%D0%BE%D0%B2%D0%BE/" class="b-train--vokzal_list--links__link">Балаково</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B0%D0%BB%D0%B0%D1%88%D0%BE%D0%B2/" class="b-train--vokzal_list--links__link">Балашов</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%91%D0%B0%D0%BB%D1%82%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB/" class="b-train--vokzal_list--links__link">Балтийский Вокзал</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B0%D1%80%D0%B0%D0%B1%D0%B8%D0%BD%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Барабинск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B0%D1%80%D0%BD%D0%B0%D1%83%D0%BB/" class="b-train--vokzal_list--links__link">Барнаул</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%91%D0%B0%D1%85%D1%87%D0%B8%D1%81%D0%B0%D1%80%D0%B0%D0%B9/" class="b-train--vokzal_list--links__link">Бахчисарай</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B5%D0%BB%D0%B0%D1%8F_%D0%9A%D0%B0%D0%BB%D0%B8%D1%82%D0%B2%D0%B0/" class="b-train--vokzal_list--links__link">Белая Калитва</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B5%D0%BB%D0%B3%D0%BE%D1%80%D0%BE%D0%B4/" class="b-train--vokzal_list--links__link">Белгород</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B5%D0%BB%D0%BE%D0%B2%D0%BE/" class="b-train--vokzal_list--links__link">Белово</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B5%D0%BB%D0%BE%D0%B3%D0%BE%D1%80%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Белогорск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B5%D0%BB%D0%BE%D1%80%D0%B5%D1%86%D0%BA/" class="b-train--vokzal_list--links__link">Белорецк</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B5%D0%BB%D0%BE%D1%80%D0%B5%D1%87%D0%B5%D0%BD%D1%81%D0%BA%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Белореченская</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%91%D0%B5%D0%BB%D0%BE%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB/" class="b-train--vokzal_list--links__link">Белорусский Вокзал</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B5%D1%80%D0%B4%D1%8F%D1%83%D1%88/" class="b-train--vokzal_list--links__link">Бердяуш</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B5%D1%80%D0%B5%D0%B7%D0%BD%D0%B8%D0%BA%D0%B8/" class="b-train--vokzal_list--links__link">Березники</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B8%D0%B9%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Бийск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B8%D0%BA%D0%B8%D0%BD/" class="b-train--vokzal_list--links__link">Бикин</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B8%D1%80%D0%B0/" class="b-train--vokzal_list--links__link">Бира</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%B8%D1%80%D0%BE%D0%B1%D0%B8%D0%B4%D0%B6%D0%B0%D0%BD/" class="b-train--vokzal_list--links__link">Биробиджан</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%BB%D0%B0%D0%B3%D0%BE%D0%B2%D0%B5%D1%89%D0%B5%D0%BD%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Благовещенск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%BE%D0%B3%D0%BE%D1%82%D0%BE%D0%BB/" class="b-train--vokzal_list--links__link">Боготол</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%BE%D0%B3%D0%BE%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Богоявленск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%BE%D0%BB%D0%BE%D1%82%D0%BD%D0%BE%D0%B5/" class="b-train--vokzal_list--links__link">Болотное</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%BE%D1%80%D0%B7%D1%8F/" class="b-train--vokzal_list--links__link">Борзя</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B3%D0%BB%D0%B5%D0%B1%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Борисоглебск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D1%80%D1%8F%D0%BD%D1%81%D0%BA-%D0%9E%D1%80%D0%BB%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9/" class="b-train--vokzal_list--links__link">Брянск - Орловский</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D1%83%D0%B3%D1%83%D0%BB%D1%8C%D0%BC%D0%B0/" class="b-train--vokzal_list--links__link">Бугульма</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D1%83%D0%B7%D1%83%D0%BB%D1%83%D0%BA/" class="b-train--vokzal_list--links__link">Бузулук</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D1%83%D0%B9/" class="b-train--vokzal_list--links__link">Буй</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%91%D1%83%D1%80%D0%B5%D1%8F/" class="b-train--vokzal_list--links__link">Бурея</a>
#         </div>
    
# </div>
                                    
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">В</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%B0%D0%BB%D1%83%D0%B9%D0%BA%D0%B8/" class="b-train--vokzal_list--links__link">Валуйки</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%B0%D0%BD%D0%B8%D0%BD%D0%BE/" class="b-train--vokzal_list--links__link">Ванино</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%B5%D0%BB%D0%B8%D0%BA%D0%B8%D0%B5_%D0%9B%D1%83%D0%BA%D0%B8/" class="b-train--vokzal_list--links__link">Великие Луки</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%B2%D0%B5%D0%BB%D0%B8%D0%BA%D0%B8%D0%B9_%D0%A3%D1%81%D1%82%D1%8E%D0%B3/" class="b-train--vokzal_list--links__link">Великий Устюг</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%B5%D0%BB%D1%8C%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Вельск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%B5%D1%80%D1%85%D0%BD%D0%B8%D0%B9_%D0%91%D0%B0%D1%81%D0%BA%D1%83%D0%BD%D1%87%D0%B0%D0%BA/" class="b-train--vokzal_list--links__link">Верхний Баскунчак</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%B5%D1%80%D1%85%D0%BD%D0%B8%D0%B9_%D0%A3%D1%84%D0%B0%D0%BB%D0%B5%D0%B9/" class="b-train--vokzal_list--links__link">Верхний Уфалей</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%B5%D1%81%D0%B5%D0%BB%D0%BE%D0%B5/" class="b-train--vokzal_list--links__link">Веселое</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%92%D0%B8%D1%82%D0%B5%D0%B1%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB/" class="b-train--vokzal_list--links__link">Витебский Вокзал</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%B8%D1%85%D0%BE%D1%80%D0%B5%D0%B2%D0%BA%D0%B0/" class="b-train--vokzal_list--links__link">Вихоревка</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%B2%D0%BE%D1%81%D1%82%D0%BE%D0%BA/" class="b-train--vokzal_list--links__link">Владивосток</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BA%D0%B0%D0%B2%D0%BA%D0%B0%D0%B7/" class="b-train--vokzal_list--links__link">Владикавказ</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80/" class="b-train--vokzal_list--links__link">Владимир</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%BE%D0%BB%D0%B3%D0%BE%D0%B3%D1%80%D0%B0%D0%B4/" class="b-train--vokzal_list--links__link">Волгоград</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%BE%D0%BB%D0%B3%D0%BE%D0%B4%D0%BE%D0%BD%D1%81%D0%BA%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Волгодонская</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%BE%D0%BB%D0%B6%D1%81%D0%BA%D0%B8%D0%B9/" class="b-train--vokzal_list--links__link">Волжский</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%BE%D0%BB%D0%BE%D0%B3%D0%B4%D0%B0/" class="b-train--vokzal_list--links__link">Вологда</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%BE%D0%BB%D1%85%D0%BE%D0%B2%D1%81%D1%82%D1%80%D0%BE%D0%B9-1/" class="b-train--vokzal_list--links__link">Волховстрой-1</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%BE%D1%80%D0%BA%D1%83%D1%82%D0%B0/" class="b-train--vokzal_list--links__link">Воркута</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D0%BE%D1%80%D0%BE%D0%BD%D0%B5%D0%B6/" class="b-train--vokzal_list--links__link">Воронеж I</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/moskva_vostochniy/" class="b-train--vokzal_list--links__link">Восточный</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D1%8B%D0%B1%D0%BE%D1%80%D0%B3/" class="b-train--vokzal_list--links__link">Выборг</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D1%8F%D0%B7%D0%B5%D0%BC%D1%81%D0%BA%D0%B8%D0%B9/" class="b-train--vokzal_list--links__link">Вяземский</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%92%D1%8F%D0%B7%D0%BE%D0%B2%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Вязовая</a>
#         </div>
    
# </div>
                                    
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">Г</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%93%D0%B0%D0%BB%D0%B8%D1%87/" class="b-train--vokzal_list--links__link">Галич</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%93%D0%B5%D0%BE%D1%80%D0%B3%D0%B8%D0%B5%D0%B2%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Георгиевск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%93%D0%BB%D0%B0%D0%B7%D0%BE%D0%B2/" class="b-train--vokzal_list--links__link">Глазов</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%93%D0%BE%D1%80%D1%8F%D1%87%D0%B8%D0%B9_%D0%9A%D0%BB%D1%8E%D1%87/" class="b-train--vokzal_list--links__link">Горячий Ключ</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%93%D1%80%D0%BE%D0%B4%D0%B5%D0%BA%D0%BE%D0%B2%D0%BE/" class="b-train--vokzal_list--links__link">Гродеково</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%93%D1%80%D0%BE%D0%B7%D0%BD%D1%8B%D0%B9/" class="b-train--vokzal_list--links__link">Грозный</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%93%D1%80%D1%8F%D0%B7%D0%B8_%D0%92%D0%BE%D1%80%D0%BE%D0%BD%D0%B5%D0%B6%D1%81%D0%BA%D0%B8%D0%B5/" class="b-train--vokzal_list--links__link">Грязи-Воронежские</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%93%D1%83%D0%B4%D0%B5%D1%80%D0%BC%D0%B5%D1%81/" class="b-train--vokzal_list--links__link">Гудермес</a>
#         </div>
    
# </div>
                                    
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">Д</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%94%D0%B0%D0%BB%D1%8C%D0%BD%D0%B5%D1%80%D0%B5%D1%87%D0%B5%D0%BD%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Дальнереченск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%94%D0%B0%D0%BD%D0%B8%D0%BB%D0%BE%D0%B2/" class="b-train--vokzal_list--links__link">Данилов</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%94%D0%B5%D1%80%D0%B1%D0%B5%D0%BD%D1%82/" class="b-train--vokzal_list--links__link">Дербент</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%B4%D0%B6%D0%B0%D0%BD%D0%BA%D0%BE%D0%B9/" class="b-train--vokzal_list--links__link">Джанкой</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%94%D0%B7%D0%B5%D1%80%D0%B6%D0%B8%D0%BD%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Дзержинск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%94%D0%B8%D0%BC%D0%B8%D1%82%D1%80%D0%BE%D0%B2%D0%B3%D1%80%D0%B0%D0%B4/" class="b-train--vokzal_list--links__link">Димитровград</a>
#         </div>
    
# </div>
                                    
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">Е</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%95%D0%B9%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Ейск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3/" class="b-train--vokzal_list--links__link">Екатеринбург</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%95%D0%BB%D0%B5%D1%86/" class="b-train--vokzal_list--links__link">Елец</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%95%D1%80%D1%88%D0%BE%D0%B2/" class="b-train--vokzal_list--links__link">Ершов</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%95%D1%81%D1%81%D0%B5%D0%BD%D1%82%D1%83%D0%BA%D0%B8/" class="b-train--vokzal_list--links__link">Ессентуки</a>
#         </div>
    
# </div>
                                    
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">Ж</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%96%D0%B8%D0%B3%D1%83%D0%BB%D0%B5%D0%B2%D1%81%D0%BA%D0%BE%D0%B5_%D0%9C%D0%BE%D1%80%D0%B5/" class="b-train--vokzal_list--links__link">Жигулевское Море</a>
#         </div>
    
# </div>
                                    
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

#                                                     </div>
#                     <div class="b-train--vokzal_list--links__column">
                                    
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">З</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%97%D0%B0%D0%B1%D0%B0%D0%B9%D0%BA%D0%B0%D0%BB%D1%8C%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Забайкальск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%97%D0%B0%D0%B2%D0%B8%D1%82%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Завитая</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%97%D0%B0%D0%BB%D0%B0%D1%80%D0%B8/" class="b-train--vokzal_list--links__link">Залари</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%97%D0%B0%D0%BE%D0%B7%D0%B5%D1%80%D0%BD%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Заозерная</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%97%D0%B0%D1%80%D0%B8%D0%BD%D1%81%D0%BA%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Заринская</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%97%D0%B2%D0%B5%D1%80%D0%B5%D0%B2%D0%BE/" class="b-train--vokzal_list--links__link">Зверево</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%97%D0%B5%D0%BB%D0%B5%D0%BD%D1%8B%D0%B9_%D0%94%D0%BE%D0%BB/" class="b-train--vokzal_list--links__link">Зеленый Дол</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%97%D0%B8%D0%BC%D0%B0/" class="b-train--vokzal_list--links__link">Зима</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%97%D0%BB%D0%B0%D1%82%D0%BE%D1%83%D1%81%D1%82/" class="b-train--vokzal_list--links__link">Златоуст</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%97%D1%83%D0%B1%D0%BE%D0%B2%D0%B0_%D0%9F%D0%BE%D0%BB%D1%8F%D0%BD%D0%B0/" class="b-train--vokzal_list--links__link">Зубова Поляна</a>
#         </div>
    
# </div>
                                    
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">И</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%98%D0%B2%D0%B0%D0%BD%D0%BE%D0%B2%D0%BE/" class="b-train--vokzal_list--links__link">Иваново</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%98%D0%B6%D0%B5%D0%B2%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Ижевск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%98%D0%BD%D0%B7%D0%B0/" class="b-train--vokzal_list--links__link">Инза</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%98%D0%BD%D1%81%D0%BA%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Инская</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%98%D0%BD%D1%82%D0%B0/" class="b-train--vokzal_list--links__link">Инта</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%98%D1%80%D0%BA%D1%83%D1%82%D1%81%D0%BA-%D0%9F%D0%B0%D1%81%D1%81%D0%B0%D0%B6%D0%B8%D1%80%D1%81%D0%BA%D0%B8%D0%B9/" class="b-train--vokzal_list--links__link">Иркутск-Пассажирский</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%98%D1%80%D0%BA%D1%83%D1%82%D1%81%D0%BA-%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BE%D1%87%D0%BD%D1%8B%D0%B9/" class="b-train--vokzal_list--links__link">Иркутск-Сортировочный</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%98%D1%81%D0%B0%D0%BA%D0%BE%D0%B3%D0%BE%D1%80%D0%BA%D0%B0/" class="b-train--vokzal_list--links__link">Исакогорка</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%98%D1%81%D0%B8%D0%BB%D1%8C%D0%BA%D1%83%D0%BB%D1%8C/" class="b-train--vokzal_list--links__link">Исилькуль</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%98%D1%81%D0%BA%D0%B8%D1%82%D0%B8%D0%BC/" class="b-train--vokzal_list--links__link">Искитим</a>
#         </div>
    
# </div>
                                    
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">Й</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%99%D0%BE%D1%88%D0%BA%D0%B0%D1%80-%D0%9E%D0%BB%D0%B0/" class="b-train--vokzal_list--links__link">Йошкар-Ола</a>
#         </div>
    
# </div>
                                    
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">К</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D0%B2%D0%BA%D0%B0%D0%B7%D1%81%D0%BA%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Кавказская</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%9A%D0%B0%D0%B7%D0%B0%D0%BD%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB/" class="b-train--vokzal_list--links__link">Казанский Вокзал</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D0%B7%D0%B0%D0%BD%D1%8C/" class="b-train--vokzal_list--links__link">Казань</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D0%BB%D0%B0%D1%87%D0%B8%D0%BD%D1%81%D0%BA%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Калачинская</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D0%BB%D0%B8%D0%BD%D0%B8%D0%BD%D0%B3%D1%80%D0%B0%D0%B4-%D0%AE%D0%B6%D0%BD%D1%8B%D0%B9/" class="b-train--vokzal_list--links__link">Калининград-Южный</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D0%BB%D1%83%D0%B3%D0%B0-1/" class="b-train--vokzal_list--links__link">Калуга-1</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D0%BC%D0%B5%D0%BD%D1%81%D0%BA-%D0%A3%D1%80%D0%B0%D0%BB%D1%8C%D1%81%D0%BA%D0%B8%D0%B9/" class="b-train--vokzal_list--links__link">Каменск-Уральский</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D0%BC%D0%B5%D0%BD%D1%81%D0%BA%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Каменская</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D0%BC%D0%B5%D0%BD%D1%8C-%D0%9D%D0%B0-%D0%9E%D0%B1%D0%B8/" class="b-train--vokzal_list--links__link">Камень-На-Оби</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D0%BC%D1%8B%D1%88%D0%BB%D0%BE%D0%B2/" class="b-train--vokzal_list--links__link">Камышлов</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D0%BD%D0%B0%D1%88/" class="b-train--vokzal_list--links__link">Канаш</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D0%BD%D1%81%D0%BA-%D0%95%D0%BD%D0%B8%D1%81%D0%B5%D0%B9%D1%81%D0%BA%D0%B8%D0%B9/" class="b-train--vokzal_list--links__link">Канск-Енисейский</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D1%80%D0%B0%D1%81%D1%83%D0%BA-1/" class="b-train--vokzal_list--links__link">Карасук-1</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D1%80%D0%B3%D0%B0%D1%82/" class="b-train--vokzal_list--links__link">Каргат</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D1%80%D1%82%D0%B0%D0%BB%D1%8B/" class="b-train--vokzal_list--links__link">Карталы</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B0%D1%80%D1%8B%D0%BC%D1%81%D0%BA%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Карымская</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B5%D0%BC%D0%B5%D1%80%D0%BE%D0%B2%D0%BE/" class="b-train--vokzal_list--links__link">Кемерово</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%BA%D0%B5%D1%80%D1%87%D1%8C/" class="b-train--vokzal_list--links__link">Керчь (Основной)</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%BA%D0%B5%D1%80%D1%87%D1%8C_%D1%8E%D0%B6%D0%BD%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Керчь-Южная</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%9A%D0%B8%D0%B5%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB/" class="b-train--vokzal_list--links__link">Киевский Вокзал</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B8%D0%B7%D0%BB%D1%8F%D1%80/" class="b-train--vokzal_list--links__link">Кизляр</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B8%D0%BD%D0%B5%D0%BB%D1%8C/" class="b-train--vokzal_list--links__link">Кинель</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B8%D0%BD%D0%B5%D1%88%D0%BC%D0%B0/" class="b-train--vokzal_list--links__link">Кинешма</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B8%D1%80%D0%BE%D0%B2/" class="b-train--vokzal_list--links__link">Киров</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B8%D1%80%D1%81%D0%B0%D0%BD%D0%BE%D0%B2/" class="b-train--vokzal_list--links__link">Кирсанов</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B8%D1%81%D0%B5%D0%BB%D0%B5%D0%B2%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Киселевск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%B8%D1%81%D0%BB%D0%BE%D0%B2%D0%BE%D0%B4%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Кисловодск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%BD%D1%8F%D0%B6%D0%BF%D0%BE%D0%B3%D0%BE%D1%81%D1%82/" class="b-train--vokzal_list--links__link">Княжпогост</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%BE%D0%B2%D1%80%D0%BE%D0%B2/" class="b-train--vokzal_list--links__link">Ковров</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%BE%D0%B3%D0%B0%D0%BB%D1%8B%D0%BC/" class="b-train--vokzal_list--links__link">Когалым</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%BE%D0%BC%D1%81%D0%BE%D0%BC%D0%BE%D0%BB%D1%8C%D1%81%D0%BA-%D0%9D%D0%B0-%D0%90%D0%BC%D1%83%D1%80%D0%B5/" class="b-train--vokzal_list--links__link">Комсомольск-На-Амуре</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%BE%D0%BD%D0%BE%D1%88%D0%B0/" class="b-train--vokzal_list--links__link">Коноша</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%BE%D1%80%D1%88%D1%83%D0%BD%D0%B8%D1%85%D0%B0/" class="b-train--vokzal_list--links__link">Коршуниха</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%BE%D1%81%D1%82%D1%80%D0%BE%D0%BC%D0%B0/" class="b-train--vokzal_list--links__link">Кострома</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D1%81%D1%82_%D0%9A%D0%BE%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2%D0%BE/" class="b-train--vokzal_list--links__link">Котельниково</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%BE%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B8%D1%87/" class="b-train--vokzal_list--links__link">Котельнич</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D0%BE%D1%82%D0%BB%D0%B0%D1%81-%D0%AE%D0%B6%D0%BD%D1%8B%D0%B9/" class="b-train--vokzal_list--links__link">Котлас-Южный</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B4%D0%B0%D1%80-1/" class="b-train--vokzal_list--links__link">Краснодар-1</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D1%83%D1%84%D0%B8%D0%BC%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Красноуфимск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D1%8F%D1%80%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Красноярск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D1%80%D0%BE%D0%BF%D0%B0%D1%87%D0%B5%D0%B2%D0%BE/" class="b-train--vokzal_list--links__link">Кропачево</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D1%80%D1%8B%D0%BC%D1%81%D0%BA%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Крымская</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D1%83%D0%B7%D0%BD%D0%B5%D1%86%D0%BA/" class="b-train--vokzal_list--links__link">Кузнецк</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D1%83%D0%BB%D1%83%D0%BD%D0%B4%D0%B0/" class="b-train--vokzal_list--links__link">Кулунда</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D1%83%D0%BF%D0%B8%D0%BD%D0%BE/" class="b-train--vokzal_list--links__link">Купино</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D1%83%D1%80%D0%B3%D0%B0%D0%BD/" class="b-train--vokzal_list--links__link">Курган</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D1%83%D1%80%D0%B3%D0%B0%D0%BD%D0%BD%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Курганная</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9A%D1%83%D1%80%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Курск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%9A%D1%83%D1%80%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB/" class="b-train--vokzal_list--links__link">Курский Вокзал</a>
#         </div>
    
# </div>
                                    
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">Л</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%9B%D0%B0%D0%B4%D0%BE%D0%B6%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB/" class="b-train--vokzal_list--links__link">Ладожский Вокзал</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9B%D0%B0%D0%B7%D0%B0%D1%80%D0%B5%D0%B2%D1%81%D0%BA%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Лазаревская</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9B%D0%B5%D0%B2_%D0%A2%D0%BE%D0%BB%D1%81%D1%82%D0%BE%D0%B9/" class="b-train--vokzal_list--links__link">Лев Толстой</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9B%D0%B5%D0%BD%D0%B0/" class="b-train--vokzal_list--links__link">Лена</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%9B%D0%B5%D0%BD%D0%B8%D0%BD%D0%B3%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB/" class="b-train--vokzal_list--links__link">Ленинградский Вокзал</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9B%D0%B5%D0%BD%D0%B8%D0%BD%D1%81%D0%BA-%D0%9A%D1%83%D0%B7%D0%BD%D0%B5%D1%86%D0%BA%D0%B8%D0%B9/" class="b-train--vokzal_list--links__link">Ленинск-Кузнецкий</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9B%D0%B8%D0%BF%D0%B5%D1%86%D0%BA/" class="b-train--vokzal_list--links__link">Липецк</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9B%D0%B8%D1%81%D0%BA%D0%B8/" class="b-train--vokzal_list--links__link">Лиски</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9B%D0%B8%D1%85%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Лихая</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9B%D0%BE%D0%BE/" class="b-train--vokzal_list--links__link">Лоо</a>
#         </div>
    
# </div>
                                    
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">М</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%B0%D0%B3%D0%B4%D0%B0%D0%B3%D0%B0%D1%87%D0%B8/" class="b-train--vokzal_list--links__link">Магдагачи</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%B0%D0%B3%D0%BD%D0%B8%D1%82%D0%BE%D0%B3%D0%BE%D1%80%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Магнитогорск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%B0%D0%B9%D0%BA%D0%BE%D0%BF/" class="b-train--vokzal_list--links__link">Майкоп</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%B0%D0%BC%D0%BE%D0%BD%D0%BE%D0%B2%D0%BE/" class="b-train--vokzal_list--links__link">Мамоново</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%B0%D0%BD%D1%82%D1%83%D1%80%D0%BE%D0%B2%D0%BE/" class="b-train--vokzal_list--links__link">Мантурово</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%B0%D1%80%D0%B8%D0%B8%D0%BD%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Мариинск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%B0%D1%85%D0%B0%D1%87%D0%BA%D0%B0%D0%BB%D0%B0/" class="b-train--vokzal_list--links__link">Махачкала</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%B5%D0%B6%D0%B4%D1%83%D1%80%D0%B5%D1%87%D0%B5%D0%BD%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Междуреченск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%B8%D0%B0%D1%81%D1%81/" class="b-train--vokzal_list--links__link">Миасс</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%B8%D0%BA%D1%83%D0%BD%D1%8C/" class="b-train--vokzal_list--links__link">Микунь</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%B8%D0%BB%D0%BB%D0%B5%D1%80%D0%BE%D0%B2%D0%BE/" class="b-train--vokzal_list--links__link">Миллерово</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%B8%D0%BD%D0%B5%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5_%D0%92%D0%BE%D0%B4%D1%8B/" class="b-train--vokzal_list--links__link">Минеральные Воды</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%B8%D1%87%D1%83%D1%80%D0%B8%D0%BD%D1%81%D0%BA-%D0%A3%D1%80%D0%B0%D0%BB%D1%8C%D1%81%D0%BA%D0%B8%D0%B9/" class="b-train--vokzal_list--links__link">Мичуринск-Уральский</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%BE%D0%B3%D0%BE%D1%87%D0%B0/" class="b-train--vokzal_list--links__link">Могоча</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB/" class="b-train--vokzal_list--links__link">Московский Вокзал</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D0%BE%D1%88%D0%BA%D0%BE%D0%B2%D0%BE/" class="b-train--vokzal_list--links__link">Мошково</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D1%83%D1%80%D0%BC%D0%B0%D0%BD%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Мурманск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9C%D1%83%D1%80%D0%BE%D0%BC/" class="b-train--vokzal_list--links__link">Муром</a>
#         </div>
    
# </div>
                                    
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

#                                                     </div>
#                     <div class="b-train--vokzal_list--links__column">
                                    
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">Н</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%B0%D0%B1%D0%B5%D1%80%D0%B5%D0%B6%D0%BD%D1%8B%D0%B5_%D0%A7%D0%B5%D0%BB%D0%BD%D1%8B/" class="b-train--vokzal_list--links__link">Набережные Челны</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%B0%D0%B2%D0%B0%D1%88%D0%B8%D0%BD%D0%BE/" class="b-train--vokzal_list--links__link">Навашино</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%B0%D0%B7%D1%8B%D0%B2%D0%B0%D0%B5%D0%B2%D1%81%D0%BA%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Называевская</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%B0%D0%BB%D1%8C%D1%87%D0%B8%D0%BA/" class="b-train--vokzal_list--links__link">Нальчик</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%B0%D1%83%D1%88%D0%BA%D0%B8/" class="b-train--vokzal_list--links__link">Наушки</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%B5%D0%B2%D0%B8%D0%BD%D0%BD%D0%BE%D0%BC%D1%8B%D1%81%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Невинномысск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%B5%D1%80%D1%8E%D0%BD%D0%B3%D1%80%D0%B8/" class="b-train--vokzal_list--links__link">Нерюнгри</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%B5%D1%81%D1%82%D0%B5%D1%80%D0%BE%D0%B2/" class="b-train--vokzal_list--links__link">Нестеров</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%B8%D0%B6%D0%BD%D0%B5%D0%BA%D0%B0%D0%BC%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Нижнекамск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%B8%D0%B6%D0%BD%D0%B5%D1%83%D0%B4%D0%B8%D0%BD%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Нижнеудинск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9_%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4/" class="b-train--vokzal_list--links__link">Нижний Новгород</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9_%D0%A2%D0%B0%D0%B3%D0%B8%D0%BB/" class="b-train--vokzal_list--links__link">Нижний Тагил</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%B8%D0%BA%D0%B5%D0%BB%D1%8C/" class="b-train--vokzal_list--links__link">Никель</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D0%B2%D0%B0%D1%8F_%D0%A7%D0%B0%D1%80%D0%B0/" class="b-train--vokzal_list--links__link">Новая Чара</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4/" class="b-train--vokzal_list--links__link">Новгород</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D0%B2%D0%BE%D0%BA%D1%83%D0%B7%D0%BD%D0%B5%D1%86%D0%BA/" class="b-train--vokzal_list--links__link">Новокузнецк</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D0%B2%D0%BE%D0%BA%D1%83%D0%B9%D0%B1%D1%8B%D1%88%D0%B5%D0%B2%D1%81%D0%BA%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Новокуйбышевская</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D0%B2%D0%BE%D1%80%D0%BE%D1%81%D1%81%D0%B8%D0%B9%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Новороссийск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA-%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D1%8B%D0%B9/" class="b-train--vokzal_list--links__link">Новосибирск-Восточный</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA-%D0%93%D0%BB%D0%B0%D0%B2%D0%BD%D1%8B%D0%B9/" class="b-train--vokzal_list--links__link">Новосибирск-Главный</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA-%D0%97%D0%B0%D0%BF%D0%B0%D0%B4%D0%BD%D1%8B%D0%B9/" class="b-train--vokzal_list--links__link">Новосибирск-Западный</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA-%D0%AE%D0%B6%D0%BD%D1%8B%D0%B9/" class="b-train--vokzal_list--links__link">Новосибирск-Южный</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D0%B2%D0%BE%D1%82%D1%80%D0%BE%D0%B8%D1%86%D0%BA/" class="b-train--vokzal_list--links__link">Новотроицк</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D0%B2%D0%BE%D1%87%D0%B5%D1%80%D0%BA%D0%B0%D1%81%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Новочеркасск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D0%B2%D1%8B%D0%B9_%D0%A3%D1%80%D0%B3%D0%B0%D0%BB/" class="b-train--vokzal_list--links__link">Новый Ургал</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D1%8F%D0%B1%D1%80%D1%8C%D1%81%D0%BA-1/" class="b-train--vokzal_list--links__link">Ноябрьск-1</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D0%BE%D1%8F%D0%B1%D1%80%D1%8C%D1%81%D0%BA-2/" class="b-train--vokzal_list--links__link">Ноябрьск-2</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D1%83%D1%80%D0%BB%D0%B0%D1%82/" class="b-train--vokzal_list--links__link">Нурлат</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9D%D1%8F%D0%BD%D0%B4%D0%BE%D0%BC%D0%B0/" class="b-train--vokzal_list--links__link">Няндома</a>
#         </div>
    
# </div>
                                    
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">О</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9E%D0%B1%D0%BB%D1%83%D1%87%D1%8C%D0%B5/" class="b-train--vokzal_list--links__link">Облучье</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D1%81%D1%82_%D0%9E%D0%B7%D0%B8%D0%BD%D0%BA%D0%B8/" class="b-train--vokzal_list--links__link">Озинки</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9E%D0%BB%D0%B8%D0%BC%D0%BF%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9_%D0%9F%D0%B0%D1%80%D0%BA/" class="b-train--vokzal_list--links__link">Олимпийский Парк</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9E%D0%BC%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Омск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9E%D1%80%D0%B5%D0%BB/" class="b-train--vokzal_list--links__link">Орел</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9E%D1%80%D0%B5%D0%BD%D0%B1%D1%83%D1%80%D0%B3/" class="b-train--vokzal_list--links__link">Оренбург</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9E%D1%80%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Орск</a>
#         </div>
    
# </div>
                                    
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">П</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%9F%D0%B0%D0%B2%D0%B5%D0%BB%D0%B5%D1%86%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB/" class="b-train--vokzal_list--links__link">Павелецкий Вокзал</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D0%B0%D0%B4%D1%83%D0%BD%D1%81%D0%BA%D0%B8%D0%B5_%D0%9F%D0%BE%D1%80%D0%BE%D0%B3%D0%B8/" class="b-train--vokzal_list--links__link">Падунские Пороги</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D0%B5%D0%BD%D0%B7%D0%B0-1/" class="b-train--vokzal_list--links__link">Пенза-1</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D0%B5%D1%80%D0%B2%D0%BE%D1%83%D1%80%D0%B0%D0%BB%D1%8C%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Первоуральск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D0%B5%D1%80%D0%BC%D1%8C-2/" class="b-train--vokzal_list--links__link">Пермь-2</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D1%81%D1%82_%D0%9F%D0%B5%D1%82%D1%80%D0%BE%D0%B2_%D0%92%D0%B0%D0%BB/" class="b-train--vokzal_list--links__link">Петров Вал</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D0%B5%D1%82%D1%80%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D0%97%D0%B0%D0%B2%D0%BE%D0%B4/" class="b-train--vokzal_list--links__link">Петровский Завод</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D0%B5%D1%82%D1%80%D0%BE%D0%B7%D0%B0%D0%B2%D0%BE%D0%B4%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Петрозаводск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D0%B5%D1%87%D0%BE%D1%80%D0%B0/" class="b-train--vokzal_list--links__link">Печора</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D0%BB%D0%B5%D1%81%D0%B5%D1%86%D0%BA%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Плесецкая</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D0%BE%D0%B2%D0%BE%D1%80%D0%B8%D0%BD%D0%BE/" class="b-train--vokzal_list--links__link">Поворино</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D0%BE%D1%82%D1%8C%D0%BC%D0%B0/" class="b-train--vokzal_list--links__link">Потьма</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D1%80%D0%BE%D0%BA%D0%BE%D0%BF%D1%8C%D0%B5%D0%B2%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Прокопьевск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D1%80%D0%BE%D1%85%D0%BB%D0%B0%D0%B4%D0%BD%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Прохладная</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D1%81%D0%BA%D0%BE%D0%B2/" class="b-train--vokzal_list--links__link">Псков</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D1%8B%D1%82%D1%8C-%D0%AF%D1%85/" class="b-train--vokzal_list--links__link">Пыть-Ях</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%9F%D1%8F%D1%82%D0%B8%D0%B3%D0%BE%D1%80%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Пятигорск</a>
#         </div>
    
# </div>
                                    
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">Р</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A0%D0%B0%D0%BD%D0%B5%D0%BD%D0%B1%D1%83%D1%80%D0%B3/" class="b-train--vokzal_list--links__link">Раненбург</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A0%D0%B5%D0%B2%D0%B4%D0%B0/" class="b-train--vokzal_list--links__link">Ревда</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%A0%D0%B8%D0%B6%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB/" class="b-train--vokzal_list--links__link">Рижский Вокзал</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A0%D0%BE%D0%B7%D0%B0_%D0%A5%D1%83%D1%82%D0%BE%D1%80/" class="b-train--vokzal_list--links__link">Роза Хутор</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A0%D0%BE%D1%81%D1%81%D0%BE%D1%88%D1%8C/" class="b-train--vokzal_list--links__link">Россошь</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%93%D0%BB%D0%B0%D0%B2%D0%BD%D1%8B%D0%B9/" class="b-train--vokzal_list--links__link">Ростов-Главный</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%AF%D1%80%D0%BE%D1%81%D0%BB%D0%B0%D0%B2%D1%81%D0%BA%D0%B8%D0%B9/" class="b-train--vokzal_list--links__link">Ростов-Ярославский</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A0%D1%82%D0%B8%D1%89%D0%B5%D0%B2%D0%BE/" class="b-train--vokzal_list--links__link">Ртищево</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A0%D1%83%D0%B1%D1%86%D0%BE%D0%B2%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Рубцовск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A0%D1%83%D0%B6%D0%B8%D0%BD%D0%BE/" class="b-train--vokzal_list--links__link">Ружино</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A0%D1%83%D0%B7%D0%B0%D0%B5%D0%B2%D0%BA%D0%B0/" class="b-train--vokzal_list--links__link">Рузаевка</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A0%D1%8B%D0%B1%D0%B8%D0%BD%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Рыбинск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A0%D1%8F%D0%B7%D0%B0%D0%BD%D1%8C-1/" class="b-train--vokzal_list--links__link">Рязань-1</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A0%D1%8F%D0%B7%D0%B0%D0%BD%D1%8C-2/" class="b-train--vokzal_list--links__link">Рязань-2</a>
#         </div>
    
# </div>
                                    
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">С</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%A1%D0%B0%D0%B2%D0%B5%D0%BB%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB/" class="b-train--vokzal_list--links__link">Савеловский Вокзал</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%A1%D0%B0%D0%BA%D0%B8/" class="b-train--vokzal_list--links__link">Саки</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B0%D0%BB%D0%B0%D0%B2%D0%B0%D1%82/" class="b-train--vokzal_list--links__link">Салават</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B0%D0%BB%D1%8C%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Сальск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B0%D0%BC%D0%B0%D1%80%D0%B0/" class="b-train--vokzal_list--links__link">Самара</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B0%D1%80%D0%B0%D0%BD%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Саранск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B0%D1%80%D0%B0%D0%BF%D1%83%D0%BB/" class="b-train--vokzal_list--links__link">Сарапул</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B0%D1%80%D0%B0%D1%82%D0%BE%D0%B2-1/" class="b-train--vokzal_list--links__link">Саратов-1</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B2%D0%BE%D0%B1%D0%BE%D0%B4%D0%BD%D1%8B%D0%B9/" class="b-train--vokzal_list--links__link">Свободный</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D1%81%D0%B5%D0%B2%D0%B0%D1%81%D1%82%D0%BE%D0%BF%D0%BE%D0%BB%D1%8C%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB/" class="b-train--vokzal_list--links__link">Севастополь</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B5%D0%B2%D0%B5%D1%80%D0%BE%D0%B1%D0%B0%D0%B9%D0%BA%D0%B0%D0%BB%D1%8C%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Северобайкальск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B5%D0%B2%D0%B5%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%BD%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Северодвинск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B5%D1%80%D0%B3%D0%B0%D1%87/" class="b-train--vokzal_list--links__link">Сергач</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B5%D1%80%D0%B4%D0%BE%D0%B1%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Сердобск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B5%D1%80%D0%BE%D0%B2/" class="b-train--vokzal_list--links__link">Серов</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B8%D0%B1%D0%B0%D0%B9/" class="b-train--vokzal_list--links__link">Сибай</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%B8%D0%B1%D0%B8%D1%80%D1%86%D0%B5%D0%B2%D0%BE/" class="b-train--vokzal_list--links__link">Сибирцево</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D1%81%D0%B8%D0%BC%D1%84%D0%B5%D1%80%D0%BE%D0%BF%D0%BE%D0%BB%D1%8C%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB/" class="b-train--vokzal_list--links__link">Симферополь </a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%BA%D0%BE%D0%B2%D0%BE%D1%80%D0%BE%D0%B4%D0%B8%D0%BD%D0%BE/" class="b-train--vokzal_list--links__link">Сковородино</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%BB%D0%B0%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4/" class="b-train--vokzal_list--links__link">Славгород</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%BB%D1%8E%D0%B4%D1%8F%D0%BD%D0%BA%D0%B0/" class="b-train--vokzal_list--links__link">Слюдянка</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%BC%D0%BE%D0%BB%D0%B5%D0%BD%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Смоленск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%BE%D1%81%D0%BD%D0%BE%D0%B3%D0%BE%D1%80%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Сосногорск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%BE%D1%87%D0%B8/" class="b-train--vokzal_list--links__link">Сочи</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D0%BF%D0%B0%D1%81%D1%81%D0%BA-%D0%94%D0%B0%D0%BB%D1%8C%D0%BD%D0%B8%D0%B9/" class="b-train--vokzal_list--links__link">Спасск-Дальний</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D1%82%D0%B0%D0%B2%D1%80%D0%BE%D0%BF%D0%BE%D0%BB%D1%8C/" class="b-train--vokzal_list--links__link">Ставрополь</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%90%D0%B9%D0%B2%D0%B0%D0%B7%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Станция Айвазовская</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D1%81%D0%BB%D0%B0%D0%B2%D0%BE%D0%B2%D0%BA%D0%B0/" class="b-train--vokzal_list--links__link">Станция Владиславовка</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%95%D0%B2%D0%BF%D0%B0%D1%82%D0%BE%D1%80%D0%B8%D1%8F_%D0%BA%D1%83%D1%80%D0%BE%D1%80%D1%82/" class="b-train--vokzal_list--links__link">Станция Евпатория-Курорт</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%98%D0%BD%D0%BA%D0%B5%D1%80%D0%BC%D0%B0%D0%BD/" class="b-train--vokzal_list--links__link">Станция Инкерман-1</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%BA%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%BF%D0%B5%D1%80%D0%B5%D0%BA%D0%BE%D0%BF%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Станция Красноперекопск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D1%81%D0%B5%D0%BC%D1%8C_%D0%BA%D0%BE%D0%BB%D0%BE%D0%B4%D0%B5%D0%B7%D0%B5%D0%B9/" class="b-train--vokzal_list--links__link">Станция Семь Колодезей</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%A7%D0%B8%D1%81%D1%82%D0%BE%D0%BF%D0%BE%D0%BB%D1%8C%D0%B5/" class="b-train--vokzal_list--links__link">Станция Чистополье</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D1%82%D0%B0%D1%80%D0%BE%D0%BC%D0%B8%D0%BD%D1%81%D0%BA%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Староминская</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D1%82%D0%B0%D1%80%D1%8B%D0%B9_%D0%9E%D1%81%D0%BA%D0%BE%D0%BB/" class="b-train--vokzal_list--links__link">Старый Оскол</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D1%82%D0%B5%D1%80%D0%BB%D0%B8%D1%82%D0%B0%D0%BC%D0%B0%D0%BA/" class="b-train--vokzal_list--links__link">Стерлитамак</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D1%83%D1%80%D0%B3%D1%83%D1%82/" class="b-train--vokzal_list--links__link">Сургут</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D1%8B%D0%B7%D1%80%D0%B0%D0%BD%D1%8C-1/" class="b-train--vokzal_list--links__link">Сызрань-1</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D1%8B%D0%B7%D1%80%D0%B0%D0%BD%D1%8C-%D0%93%D0%BE%D1%80%D0%BE%D0%B4/" class="b-train--vokzal_list--links__link">Сызрань-Город</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A1%D1%8B%D0%BA%D1%82%D1%8B%D0%B2%D0%BA%D0%B0%D1%80/" class="b-train--vokzal_list--links__link">Сыктывкар</a>
#         </div>
    
# </div>
                                    
               

#                                                     </div>
#                     <div class="b-train--vokzal_list--links__column">
                                    
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">Т</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%B0%D0%B3%D0%B0%D0%BD%D1%80%D0%BE%D0%B3/" class="b-train--vokzal_list--links__link">Таганрог</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%B0%D0%B9%D0%B3%D0%B0/" class="b-train--vokzal_list--links__link">Тайга</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%B0%D0%B9%D1%88%D0%B5%D1%82/" class="b-train--vokzal_list--links__link">Тайшет</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%B0%D0%BA%D1%81%D0%B8%D0%BC%D0%BE/" class="b-train--vokzal_list--links__link">Таксимо</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%B0%D0%BB%D0%BE%D0%B2%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Таловая</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%B0%D0%BC%D0%B1%D0%BE%D0%B2/" class="b-train--vokzal_list--links__link">Тамбов</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%B0%D1%82%D0%B0%D1%80%D1%81%D0%BA%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Татарская</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%B2%D0%B5%D1%80%D1%8C/" class="b-train--vokzal_list--links__link">Тверь</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%B8%D0%BC%D0%B0%D1%88%D0%B5%D0%B2%D1%81%D0%BA%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Тимашевская</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%B8%D1%85%D0%BE%D0%BE%D0%BA%D0%B5%D0%B0%D0%BD%D1%81%D0%BA%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Тихоокеанская</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%B8%D1%85%D0%BE%D1%80%D0%B5%D1%86%D0%BA%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Тихорецкая</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%BE%D0%B1%D0%BE%D0%BB%D1%8C%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Тобольск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%BE%D0%B3%D1%83%D1%87%D0%B8%D0%BD/" class="b-train--vokzal_list--links__link">Тогучин</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%BE%D0%BB%D1%8C%D1%8F%D1%82%D1%82%D0%B8/" class="b-train--vokzal_list--links__link">Тольятти</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%BE%D0%BC%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Томск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%BE%D0%BD%D0%BD%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Тоннельная</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D0%BE%D0%BF%D0%BA%D0%B8/" class="b-train--vokzal_list--links__link">Топки</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D1%80%D0%BE%D0%B8%D1%86%D0%BA/" class="b-train--vokzal_list--links__link">Троицк</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D1%83%D0%B0%D0%BF%D1%81%D0%B5/" class="b-train--vokzal_list--links__link">Туапсе</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D1%83%D0%B9%D0%BC%D0%B0%D0%B7%D1%8B/" class="b-train--vokzal_list--links__link">Туймазы</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D1%83%D0%BB%D0%B0/" class="b-train--vokzal_list--links__link">Тула</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D1%83%D0%BB%D1%83%D0%BD/" class="b-train--vokzal_list--links__link">Тулун</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D1%8B%D0%BD%D0%B4%D0%B0/" class="b-train--vokzal_list--links__link">Тында</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A2%D1%8E%D0%BC%D0%B5%D0%BD%D1%8C/" class="b-train--vokzal_list--links__link">Тюмень</a>
#         </div>
    
# </div>
                                    
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">У</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A3%D0%BB%D0%B0%D0%BD-%D0%A3%D0%B4%D1%8D/" class="b-train--vokzal_list--links__link">Улан-Удэ</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A3%D0%BB%D1%8C%D1%8F%D0%BD%D0%BE%D0%B2%D1%81%D0%BA-%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9/" class="b-train--vokzal_list--links__link">Ульяновск-Центральный</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D1%81%D1%82_%D0%A3%D1%80%D0%B1%D0%B0%D1%85/" class="b-train--vokzal_list--links__link">Урбах</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D1%81%D1%82_%D0%A3%D1%80%D1%8E%D0%BF%D0%B8%D0%BD%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Урюпинск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A3%D1%81%D0%B8%D0%BD%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Усинск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A3%D1%81%D0%BE%D0%BB%D1%8C%D0%B5-%D0%A1%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA%D0%BE%D0%B5/" class="b-train--vokzal_list--links__link">Усолье-Сибирское</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A3%D1%81%D1%81%D1%83%D1%80%D0%B8%D0%B9%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Уссурийск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A3%D1%81%D1%82%D1%8C-%D0%98%D0%BB%D0%B8%D0%BC%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Усть-Илимск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A3%D1%81%D1%82%D1%8C-%D0%9A%D0%B0%D1%82%D0%B0%D0%B2/" class="b-train--vokzal_list--links__link">Усть-Катав</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A3%D1%84%D0%B0/" class="b-train--vokzal_list--links__link">Уфа</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A3%D1%85%D1%82%D0%B0/" class="b-train--vokzal_list--links__link">Ухта</a>
#         </div>
    
# </div>
                                    
               

                                
                                
               

                                
                                
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">Ф</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%A4%D0%B5%D0%BE%D0%B4%D0%BE%D1%81%D0%B8%D1%8F/" class="b-train--vokzal_list--links__link">Феодосии</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%A4%D0%B8%D0%BD%D0%BB%D1%8F%D0%BD%D0%B4%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB/" class="b-train--vokzal_list--links__link">Финляндский Вокзал</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A4%D1%80%D0%BE%D0%BB%D0%BE%D0%B2%D0%BE/" class="b-train--vokzal_list--links__link">Фролово</a>
#         </div>
    
# </div>
                                    
               

                                
                                
               

                                
                                
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">Х</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A5%D0%B0%D0%B1%D0%B0%D1%80%D0%BE%D0%B2%D1%81%D0%BA-1/" class="b-train--vokzal_list--links__link">Хабаровск-1</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A5%D0%B0%D1%81%D0%B0%D0%BD/" class="b-train--vokzal_list--links__link">Хасан</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A5%D0%BE%D1%81%D1%82%D0%B0/" class="b-train--vokzal_list--links__link">Хоста</a>
#         </div>
    
# </div>
                                    
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">Ч</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A7%D0%B0%D0%BD%D1%8B/" class="b-train--vokzal_list--links__link">Чаны</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A7%D0%B0%D0%BF%D0%B0%D0%B5%D0%B2%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Чапаевск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A7%D0%B5%D0%B1%D0%BE%D0%BA%D1%81%D0%B0%D1%80%D1%8B/" class="b-train--vokzal_list--links__link">Чебоксары</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Челябинск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A7%D0%B5%D1%80%D0%B5%D0%BC%D1%85%D0%BE%D0%B2%D0%BE/" class="b-train--vokzal_list--links__link">Черемхово</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A7%D0%B5%D1%80%D0%B5%D0%BF%D0%B0%D0%BD%D0%BE%D0%B2%D0%BE/" class="b-train--vokzal_list--links__link">Черепаново</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A7%D0%B5%D1%80%D0%B5%D0%BF%D0%BE%D0%B2%D0%B5%D1%86/" class="b-train--vokzal_list--links__link">Череповец</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A7%D0%B5%D1%80%D0%BA%D0%B5%D1%81%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Черкесск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A7%D0%B5%D1%80%D1%82%D0%BA%D0%BE%D0%B2%D0%BE/" class="b-train--vokzal_list--links__link">Чертково</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A7%D0%B8%D1%82%D0%B0-2/" class="b-train--vokzal_list--links__link">Чита-2</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A7%D1%83%D0%BB%D1%8B%D0%BC%D1%81%D0%BA%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Чулымская</a>
#         </div>
    
# </div>
                                    
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">Ш</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A8%D0%B0%D0%B4%D1%80%D0%B8%D0%BD%D1%81%D0%BA/" class="b-train--vokzal_list--links__link">Шадринск</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A8%D0%B0%D1%80%D1%8C%D1%8F/" class="b-train--vokzal_list--links__link">Шарья</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A8%D0%B0%D1%85%D1%82%D0%BD%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Шахтная</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A8%D0%B0%D1%85%D1%83%D0%BD%D1%8C%D1%8F/" class="b-train--vokzal_list--links__link">Шахунья</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A8%D0%B5%D0%BF%D1%81%D0%B8/" class="b-train--vokzal_list--links__link">Шепси</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A8%D0%B8%D0%BB%D0%BA%D0%B0/" class="b-train--vokzal_list--links__link">Шилка</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A8%D0%B8%D0%BC%D0%B0%D0%BD%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F/" class="b-train--vokzal_list--links__link">Шимановская</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A8%D1%83%D0%BC%D0%B5%D1%80%D0%BB%D1%8F/" class="b-train--vokzal_list--links__link">Шумерля</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%A8%D1%83%D0%BC%D0%B8%D1%85%D0%B0/" class="b-train--vokzal_list--links__link">Шумиха</a>
#         </div>
    
# </div>
                                    
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">Э</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%AD%D1%81%D1%82%D0%BE-%D0%A1%D0%B0%D0%B4%D0%BE%D0%BA/" class="b-train--vokzal_list--links__link">Эсто-Садок</a>
#         </div>
    
# </div>
                                    
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">Ю</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%AE%D0%B3%D1%80%D0%B0-1/" class="b-train--vokzal_list--links__link">Юрга-1</a>
#         </div>
    
# </div>
                                    
               

                                
                                
               

                                
                                
               

                                
                                
                                        
#                     <div class="b-train--vokzal_list--links__group-wrapper">

#         <div class="b-train--vokzal_list--links__capital">Я</div>

#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%AF%D0%BD%D0%B0%D1%83%D0%BB/" class="b-train--vokzal_list--links__link">Янаул</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%AF%D1%80%D0%BE%D1%81%D0%BB%D0%B0%D0%B2%D0%BB%D1%8C-%D0%93%D0%BB%D0%B0%D0%B2%D0%BD%D1%8B%D0%B9/" class="b-train--vokzal_list--links__link">Ярославль-Главный</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB_%D0%AF%D1%80%D0%BE%D1%81%D0%BB%D0%B0%D0%B2%D0%BB%D1%8C-%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9/" class="b-train--vokzal_list--links__link">Ярославль-Московский</a>
#         </div>
#             <div class="b-train--vokzal_list--links__link-wrapper">
#             <a href="/poezda/vkz/%D0%AF%D1%80%D0%BE%D1%81%D0%BB%D0%B0%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB/" class="b-train--vokzal_list--links__link">Ярославский Вокзал</a>
#         </div>
    
# </div>
                                    
#                     </div>

#     </div>

# </div>			</div>
			

# 		</div>
# 		<div class="l-vokzal__sidebar">
# 			<script type="text/javascript" src="https://cdn1.tu-tu.ru/js2/rm.banner.rotate_comp.js.a6bba43feeae05ae9769c5c28092b7a41.js"></script>	
	
# 			<div class="l-payways_nodate j-secure_pay_container">
			
# <div class="b-info__secure_pay__column _train m-right j-secure_pay_block">
# 			<div class="payway_title">Способы оплаты</div>
# 		<div class="icons_wrp">
# 		<div class="b-info__payway__icons_column _train">
# 			<div class="b-train__common__paylogo _visa"></div>
# 			<div class="b-train__common__paylogo _mastercard"></div>
# 			<div class="b-train__common__paylogo _visaelectron"></div>
# 			<div class="b-train__common__paylogo _maestro"></div>
# 			<div class="b-train__common__paylogo _mir"></div>
# 	</div>	</div>
# 			<div class="info_wrp">
# 			<div class="b-info__secure_pay _train">
# 	<div class="info">
# 					<span class="lock"></span>
# 					<span class="pseudo _green j-secure j-log-reason-secure_payment">
# 				Безопасная оплата			</span>
# 		<div class="popup_wrp">
# 			<div class="b-popup__container__standart _close j-popup ">
# 				<div class="popup_close j-popup_close"></div>
# 				<div class="hint_content">
# 					<p class="article">Ваши платежные и&nbsp;личные данные надежно защищены.</p>
# 					<p class="article">Платежные шлюзы партнеров Туту.ру соответствуют международным стандартам безопасности систем Visa и&nbsp;MasterCard, стандарту повышенной надежности PCI&nbsp;DSS&nbsp;3.2.</p>
# 					<div class="secure_image secure_image_pci"></div>
# 					<div class="secure_image secure_image_visa"></div>
# 					<div class="secure_image secure_image_mc"></div>
# 				</div>
# 			</div>
# 		</div>
# 	</div>
# 			<div class="secure_data_text">
# 			Ваши данные защищены		</div>
# 	</div>		</div>
# 	</div>		</div>
	
# 			<div class="l-reasons_to_buy_nodate">
# 			<div class="b-train__info__reasons_to_buy">
# 	<div class="reasons_title t-ttl_third _p">6 причин купить ж/д билеты именно здесь</div>
# 	<div class="reason_to_buy t-txt-s fast">Онлайн-покупка за&nbsp;4&nbsp;минуты</div>
# 	<div class="reason_to_buy t-txt-s refund">Онлайн-возврат<br />билетов без&nbsp;очереди<br />в&nbsp;кассу</div>
# 	<div class="reason_to_buy t-txt-s favourite_places">Выбор любимых мест на&nbsp;схемах вагонов</div>
# 	<div class="reason_to_buy t-txt-s sms">СМС-сопровождение до&nbsp;посадки в&nbsp;поезд</div>
# 	<div class="reason_to_buy t-txt-s answers">Подробные ответы на&nbsp;вопросы о&nbsp;поездке или покупке</div>
# 	<div class="reason_to_buy t-txt-s no_registration">Оформление <nobr>без регистрации на&nbsp;сайте</nobr></div>
# </div>
# 		</div>
	
# 	<noindex>
				
# 				<div class="j-tutu_advantages"></div>
		
# 	<div class="right_block_turn b-fast_infoblock">
# 		<h2 class="title">
# 					Частые вопросы				</h2>
# 		<ul class="accordion_list">
# 			<li class="fast_item">
# 				<h3 class="item_title">
# 					<span class="item_link_dashed">
# 													Как купить ж/д&nbsp;билет?											</span>
# 					<div class="talk-corner"></div>
# 				</h3>
# 				<div class="item_content">
# 					<div class="item_close"></div><div class="talk-corner"></div>
# 											<ul>
# 												<li>Укажите маршрут и&nbsp;дату. В&nbsp;ответ мы&nbsp;найдем информацию РЖД о&nbsp;наличии билетов и&nbsp;их&nbsp;стоимости.</li>
# 												<li>Выберите подходящий поезд и&nbsp;места.</li>
# 												<li>Оплатите билет одним из&nbsp;предложенных способов.</li>
# 												<li>Информация об&nbsp;оплате будет моментально передана в&nbsp;РЖД и&nbsp;Ваш билет будет оформлен.</li>
# 											</ul>									</div>
# 			</li>
			
						
# 			<li class="fast_item">
# 				<h3 class="item_title">
# 					<span class="item_link_dashed">
# 													Как вернуть купленный <span class="nowrap">ж/д</span>&nbsp;билет?											</span>
# 					<div class="talk-corner"></div>
# 				</h3>
# 				<div class="item_content">
# 					<div class="item_close"></div><div class="talk-corner"></div>
# 											<p>Любой купленный на&nbsp;<a href="/">tutu.ru</a> <span class="nowrap">ж/д</span>&nbsp;билет можно сдать в&nbsp;соответствии с&nbsp;правилами&nbsp;РЖД.</p>
# 											<p>Возврат осуществляется прямо в&nbsp;личном кабинете Туту.ру или в&nbsp;железнодорожных кассах.</p>
# 											<p>Если вы&nbsp;оплатили электронный <span class="nowrap">ж/д</span> билет банковской картой, деньги вернут на&nbsp;ту&nbsp;же карту.</p>
# 											<p>При сдаче купленного билета не&nbsp;возвращаются сервисные сборы и&nbsp;комиссии, дополнительно РЖД взимает рекламационный сбор.</p>
# 											<p>Общие потери при сдаче билета зависят от&nbsp;суммы и&nbsp;способа оплаты. За&nbsp;один сданный билет в&nbsp;среднем удерживается около 500&nbsp;рублей.</p>
# 											<p>При возврате билета менее чем за&nbsp;8&nbsp;часов до&nbsp;отправления поезда штрафы РЖД существенно увеличиваются.</p>									</div>
# 			</li>
# 			<li class="fast_item">
# 				<h3 class="item_title">
# 					<span class="item_link_dashed">
# 													Можно&nbsp;ли оплатить билет картой? А&nbsp;это&nbsp;безопасно?											</span>
# 					<div class="talk-corner"></div>
# 				</h3>
# 				<div class="item_content">
# 					<div class="item_close"></div><div class="talk-corner"></div>
# 											<p>
# 											Да, конечно. Оплата происходит через платежный шлюз процессингового центра Gateline.net. Все данные передаются по&nbsp;защищенному каналу.
# 											</p>
# 											<p>								
# 											Шлюз Gateline.net был разработан в&nbsp;соответствии с&nbsp;учетом требований международного стандарта безопасности PCI&nbsp;DSS. Программное обеспечение шлюза успешно прошло аудит по&nbsp;версии 3.1.
# 											</p>
# 											<p>
# 											Система Gateline.net позволяет принимать оплату картами Visa и&nbsp;MasterCard, в&nbsp;том числе с&nbsp;использованием <span class="nowrap">3D-Secure</span>: Verified by&nbsp;Visa и&nbsp;MasterCard SecureCode.
# 											</p>
# 											<p>
# 											Платежная форма Gateline.net оптимизирована под различные браузеры и&nbsp;платформы, в&nbsp;том числе и&nbsp;для мобильных устройств.
# 											</p>
# 											<p>
# 											Почти все ЖД&nbsp;агентства в&nbsp;интернете работают через данный шлюз.
# 											</p>									</div>
# 			</li>
# 			<li class="fast_item">
# 				<h3 class="item_title">
# 					<span class="item_link_dashed">
# 													Что такое электронный билет и&nbsp;электронная регистрация?											</span>
# 					<div class="talk-corner"></div>
# 				</h3>
# 				<div class="item_content">
# 					<div class="item_close"></div><div class="talk-corner"></div>
# 											<p>Покупка электронного билета на Tutu.ru&nbsp;&mdash; современный и&nbsp;быстрый способ оформления проездного документа без&nbsp;участия кассира или&nbsp;оператора.</p>
# 											<p>При покупке электронного <span class="nowrap">ж/д&nbsp;билета</span> места выкупаются сразу, в&nbsp;момент оплаты.</p>
# 											<p>После оплаты для&nbsp;посадки в&nbsp;поезд нужно:</p>
# 											<ul>
# 											<li>либо пройти электронную регистрацию;</li>
# 											<li>либо распечатать билет на&nbsp;вокзале.</li>
# 											</ul>
# 											<p><b>Электронная регистрация</b> доступна не&nbsp;для&nbsp;всех заказов. 
# 											Если регистрация доступна, ее&nbsp;можно пройти, нажав на&nbsp;нашем сайте соответствующую кнопку. Эту кнопку вы&nbsp;увидите сразу после оплаты.
# 											Затем для посадки в&nbsp;поезд понадобится оригинал удостоверения личности и&nbsp;распечатка посадочного купона.
# 											Некоторые проводники распечатку не&nbsp;требуют, но&nbsp;лучше не&nbsp;рисковать.</p>
# 											<p><b>Распечатать электронный билет</b> можно в&nbsp;любое время до&nbsp;отправления поезда в&nbsp;кассе на&nbsp;вокзале либо в&nbsp;терминале саморегистрации.
# 											Для этого нужен 14-значный код заказа (вы&nbsp;получите его по&nbsp;СМС после оплаты) и&nbsp;оригинал удостоверения личности.</p>				</div>
# 			</li>
# 			<li class="fast_item">
# 				<h3 class="item_title">
# 					<span class="item_link_dashed">
# 													Актуальна&nbsp;ли информация на&nbsp;сайте?											</span>
# 					<div class="talk-corner"></div>
# 				</h3>
# 				<div class="item_content">
# 					<div class="item_close"></div><div class="talk-corner"></div>
# 											<p>Мы&nbsp;уверены в&nbsp;точности нашей информации, потому что эти&nbsp;же данные из&nbsp;АСУ &laquo;Экспресс-3&raquo; сейчас видит кассир на&nbsp;вокзале.</p>									</div>
# 			</li>
# 					</ul>
# 	</div>

# 	<script>
# 	$(document).ready(function () {
# 		$('.fast_item .item_title').on("click", function(){
# 			$(this).parent('.fast_item').toggleClass('selected');
# 			return false;
# 		});
# 		$('.fast_item .item_close').on("click", function(){
# 			$('.fast_item.selected').removeClass('selected');
# 			return false;
# 		});
# 	});
# 	</script>	</noindex>


#     <div class="b-promo b-promo-rb_banner">
#         <script type="text/javascript">
#             var bannerRotate = new RM_Banner_Rotate( [{"content":"<script type=\"text\/javascript\"><!--\ngoogle_ad_client = \"ca-pub-7637691783555529\";\n\/* Банер 200 на 200 *\/\ngoogle_ad_slot = \"2609769617\";\ngoogle_ad_width = 200;\ngoogle_ad_height = 200;\n\/\/-->\n<\/script>\n<script type=\"text\/javascript\"\nsrc=\"http:\/\/pagead2.googlesyndication.com\/pagead\/show_ads.js\">\n<\/script>","rating":0},{"content":"<!-- Yandex.RTB R-A-10552-4 -->\n<div id=\"yandex_rtb_R-A-10552-4\"><\/div>\n<script type=\"text\/javascript\">\n    (function(w, d, n, s, t) {\n        w[n] = w[n] || [];\n        w[n].push(function() {\n            Ya.Context.AdvManager.render({\n                blockId: \"R-A-10552-4\",\n                renderTo: \"yandex_rtb_R-A-10552-4\",\n                async: true\n            });\n        });\n        t = d.getElementsByTagName(\"script\")[0];\n        s = d.createElement(\"script\");\n        s.type = \"text\/javascript\";\n        s.src = \"\/\/an.yandex.ru\/system\/context.js\";\n        s.async = true;\n        t.parentNode.insertBefore(s, t);\n    })(this, this.document, \"yandexContextAsyncCallbacks\");\n<\/script>","rating":100}] );
#             document.write( bannerRotate.getRandomBanner() );
#         </script>
#     </div>

# 		</div>
# 	</div>
# 			</div>
		
# 	</div>
# 			<footer>
		
		
# <script type="text/javascript" src="//static.criteo.net/js/ld/ld.js" async="true"></script>
# <script type="text/javascript">
# 	window.criteo_q = window.criteo_q || [];
# 	window.criteo_q.push(
# 		{"event":"setAccount","account":27857},{"event":"setHashedEmail","email":""},{"event":"setSiteType","type":"d"},{"event":"viewHome","nbra":"1","nbrc":"0","numi":"0"}	);
# </script>


# 			<div class="b-train__common__footer__schedule _desktop l-footer_wrapper t-txt-s">
# 					<div class="l-footer t-gray footer_breadcrumbs j-breadcrumbs">
# 				<div class="l-footer_content">
# 									</div>
# 			</div>
		
# 		<div class="l-footer">
# 			<div class="l-footer_content">
# 				<!--noindex-->
# 				<div class="footer_main">
# 					<ul class="footer_column">
# 						<li class="list_item">
# 							<a href="/feedback_bilet.php" class="g-link _inline">
# 								Обратная связь
# 							</a>
# 						</li>
# 						<li class="list_item">
# 															<a href="/2read/poezda/main/" class="g-link _inline">
# 									Справочная
# 								</a>
# 													</li>
# 						<li class="list_item">
# 							<a href="/opros/" class="g-link _inline">
# 								Результаты опросов
# 							</a>
# 						</li>
# 					</ul>&nbsp;<!-- don't remove -->
# 					<ul class="footer_column">
# 						<li class="list_item">
# 							<a href="https://company.tutu.ru/" class="g-link _inline">
# 								О&nbsp;компании
# 							</a>
# 						</li>
# 						<li class="list_item">
# 							<a href="https://company.tutu.ru/vacancy/" class="g-link _inline">
# 								Наши вакансии
# 							</a>
# 						</li>
# 						<li class="list_item">
# 							<a href="/geo/" class="g-link _inline">
# 								Путеводитель по&nbsp;странам
# 							</a>
# 						</li>
# 					</ul>&nbsp;<!-- don't remove -->
# 					<ul class="footer_column">
# 						<li class="list_item">
# 							<a href="/2read/advert/advert/" class="g-link _inline">
# 								Реклама на&nbsp;Туту.ру
# 							</a>
# 						</li>
# 						<li class="list_item">
# 							<a href="https://company.tutu.ru/contacts/" class="g-link _inline">
# 								Контакты
# 							</a>
# 						</li>
# 											</ul>
# 				</div>
# 				<!--/noindex-->

# 				<div class="footer_right">
# 														</div>
# 			</div>
# 		</div>
# 	</div>


# <div class="l-footer_wrapper">
# 	<div class="b-train__common__footer m-schedule l-footer l-footer m-with-upper-block _desktop" data-ti="footer">
# 		<div class="l-footer_content">
# 			<div>
# 				<!--noindex-->
# 								<div class="left_block">
# 					<div class="copyright">
# 						<div class="t-txt-s"></div>
# 												<div style="margin-top:10px">
# 							<a class="b-roskachestvo" data-seo-url="/geo/" rel="nofollow" target="_blank">
# 	<img class="b-roskachestvo__img" title="Максимальный рейтинг по данным Роскачества, ноябрь 2019" width="86" height="43" src="data:image/svg+xml,%3csvg width='557' height='279' viewBox='0 0 557 279' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M99.8 248.1C95.6 248.1 91.5 245.8 89.5 241.8C84.3 231.8 72.6 204.5 62.5 177.7C42.7 124.7 43.9 113.4 44.3 109.2C44.8 104.9 45.6 97.5004 86.7 67.6004C126.8 38.4004 136 38.4004 139 38.4004C142.3 38.4004 151.1 38.4004 190.7 67.6004C230.1 96.6004 232.4 104.2 233.3 107.1C234.2 110.1 236.2 117.1 220.7 164.4C205.3 211.6 199.9 215.6 197.3 217.5C194.6 219.5 184.7 224.8 133.8 222.5C127.4 222.2 122.4 216.8 122.7 210.4C123 204 128.4 199 134.8 199.3C151.9 200.1 175.7 199.9 183 198.5C190.3 185.2 208.8 128.3 210.6 114C200.8 103 152.2 66.8004 139 61.9004C126.2 66.6004 76.8 102.3 67.5 113.5C67.8 118 70.3 132 84.3 169.5C94.6 197 105.9 223 110.1 231.2C113.1 236.9 110.8 243.9 105.1 246.8C103.4 247.7 101.6 248.1 99.8 248.1Z' fill='%23AEAEB1'/%3e%3cpath d='M183.4 123.8C184.8 128.4 169.8 173.3 166.7 175.4C163.6 177.4 115.5 178.2 112.4 175.4C109.3 172.6 94.1 128.1 95.6 123.8C97.2 119.4 133.6 91.9004 139.5 91.9004C145.5 91.9004 182 119.1 183.4 123.8Z' fill='%23AEAEB1'/%3e%3cpath d='M424.1 254.4L426.1 260.4H421.9L424 254.4H424.1Z' fill='%23AEAEB1'/%3e%3cpath d='M376.4 256.5C376.6 257.167 376.7 257.867 376.7 258.6C376.7 259.333 376.6 260 376.4 260.6C376.267 261.267 376 261.867 375.6 262.4C375.267 262.933 374.833 263.367 374.3 263.7C373.7 263.967 373 264.1 372.2 264.1C371.4 264.1 370.7 263.967 370.1 263.7C369.567 263.367 369.133 262.933 368.8 262.4C368.4 261.867 368.133 261.267 368 260.6C367.8 260 367.7 259.333 367.7 258.6C367.7 257.867 367.8 257.167 368 256.5C368.133 255.833 368.4 255.233 368.8 254.7C369.133 254.167 369.567 253.767 370.1 253.5C370.7 253.167 371.4 253 372.2 253C373 253 373.7 253.167 374.3 253.5C374.833 253.767 375.267 254.167 375.6 254.7C376 255.233 376.267 255.833 376.4 256.5Z' fill='%23AEAEB1'/%3e%3cpath d='M358.4 254.4C358.533 254.667 358.6 255.067 358.6 255.6C358.6 256.133 358.533 256.567 358.4 256.9C358.2 257.234 357.967 257.467 357.7 257.6C357.367 257.8 357.033 257.934 356.7 258C356.3 258.067 355.9 258.1 355.5 258.1H352.7V253.2H355.5C355.9 253.2 356.3 253.2 356.7 253.2C357.033 253.267 357.367 253.4 357.7 253.6C357.967 253.8 358.2 254.067 358.4 254.4Z' fill='%23AEAEB1'/%3e%3cpath d='M506.8 260C507.267 260.333 507.5 260.933 507.5 261.8C507.5 262.2 507.433 262.567 507.3 262.9C507.167 263.167 506.967 263.367 506.7 263.5C506.433 263.7 506.167 263.833 505.9 263.9C505.567 263.967 505.2 264 504.8 264H501V259.5H504.9C505.7 259.5 506.333 259.667 506.8 260Z' fill='%23AEAEB1'/%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M556.3 0V278.4H0V0H556.3ZM551.7 61.3H278.1V4.5H4.5V273.9H278.1V207.6H551.7V61.3ZM450.9 26.5L460 33.4L456.5 44.2L465.8 37.7L475.1 44.4L471.7 33.5L480.9 26.7L469.5 26.5L466 15.7L462.3 26.5H450.9ZM402.5 26.5L411.6 33.4L408.1 44.2L417.5 37.6L426.7 44.3L423.3 33.4L432.6 26.7L421.2 26.5L417.6 15.7L413.9 26.5H402.5ZM354.2 26.5L363.3 33.3L359.7 44.2L369.1 37.6L378.3 44.3L375 33.4L384.2 26.7L372.8 26.5L369.3 15.7L365.5 26.5H354.2ZM305.9 26.4L315 33.3L311.5 44.1L320.8 37.6L330 44.3L326.7 33.4L335.9 26.7L324.5 26.5L321 15.6L317.3 26.4H305.9ZM336.3 222.7H292.4V266.7H336.3V222.7ZM362.2 255.5C362.2 254.833 362.1 254.2 361.9 253.6C361.7 252.933 361.367 252.367 360.9 251.9C360.433 251.433 359.833 251.033 359.1 250.7C358.433 250.433 357.567 250.3 356.5 250.3H349.1V266.7H352.7V260.8H356.5C357.567 260.8 358.433 260.667 359.1 260.4C359.833 260.067 360.433 259.667 360.9 259.2C361.367 258.667 361.7 258.1 361.9 257.5C362.1 256.833 362.2 256.167 362.2 255.5ZM362.2 228C362.2 227.333 362.1 226.667 361.9 226C361.7 225.4 361.367 224.833 360.9 224.3C360.433 223.833 359.833 223.433 359.1 223.1C358.433 222.833 357.567 222.7 356.5 222.7H349.1V239.1H352.7V233.2H356.5C357.567 233.2 358.433 233.067 359.1 232.8C359.833 232.467 360.433 232.067 360.9 231.6C361.367 231.067 361.7 230.5 361.9 229.9C362.1 229.3 362.2 228.667 362.2 228ZM380.3 258.5C380.3 257.3 380.133 256.167 379.8 255.1C379.4 254.1 378.867 253.2 378.2 252.4C377.533 251.6 376.7 250.967 375.7 250.5C374.7 250.1 373.567 249.9 372.3 249.9C371.033 249.9 369.9 250.1 368.9 250.5C367.9 250.967 367.033 251.6 366.3 252.4C365.633 253.2 365.133 254.1 364.8 255.1C364.4 256.167 364.2 257.3 364.2 258.5C364.2 259.7 364.4 260.833 364.8 261.9C365.133 262.9 365.633 263.8 366.3 264.6C367.033 265.333 367.9 265.933 368.9 266.4C369.9 266.8 371.033 267 372.3 267C373.567 267 374.7 266.8 375.7 266.4C376.7 265.933 377.533 265.333 378.2 264.6C378.867 263.8 379.4 262.9 379.8 261.9C380.133 260.833 380.3 259.7 380.3 258.5ZM368.5 229.2V225.7H377.2V222.7H364.9V239.1H377.4V236.1H368.5V232H376.5V229.2H368.5ZM380.2 222.7V239.1H384.3L390.5 227.7H390.6V239.1H394.2V222.7H390.1L383.9 234.1H383.8V222.7H380.2ZM387.4 221.3C390.4 221.3 391.9 220.1 391.9 217.7H389.2C389.2 218.233 389.067 218.633 388.8 218.9C388.533 219.233 388.067 219.4 387.4 219.4C386.8 219.4 386.367 219.233 386.1 218.9C385.833 218.633 385.7 218.233 385.7 217.7H383C383 220.1 384.467 221.3 387.4 221.3ZM397.8 260.4H394.3C394.167 261.467 393.8 262.333 393.2 263C392.533 263.667 391.667 264 390.6 264C389.8 264 389.1 263.867 388.5 263.6C387.967 263.267 387.5 262.833 387.1 262.3C386.767 261.767 386.5 261.2 386.3 260.6C386.167 259.933 386.1 259.233 386.1 258.5C386.1 257.833 386.167 257.167 386.3 256.5C386.5 255.767 386.767 255.133 387.1 254.6C387.5 254.133 387.967 253.733 388.5 253.4C389.1 253.067 389.8 252.9 390.6 252.9C391 252.9 391.4 252.967 391.8 253.1C392.267 253.233 392.633 253.433 392.9 253.7C393.233 253.967 393.5 254.267 393.7 254.6C393.967 255 394.133 255.4 394.2 255.8H397.6C397.533 254.867 397.3 254.033 396.9 253.3C396.433 252.567 395.9 251.933 395.3 251.4C394.633 250.933 393.9 250.567 393.1 250.3C392.3 250.033 391.467 249.9 390.6 249.9C389.333 249.9 388.2 250.1 387.2 250.5C386.2 250.967 385.333 251.6 384.6 252.4C383.933 253.2 383.433 254.1 383.1 255.1C382.7 256.167 382.5 257.3 382.5 258.5C382.5 259.7 382.7 260.833 383.1 261.9C383.433 262.9 383.933 263.8 384.6 264.6C385.333 265.333 386.2 265.933 387.2 266.4C388.2 266.8 389.333 267 390.6 267C391.6 267 392.5 266.867 393.3 266.6C394.167 266.267 394.933 265.833 395.6 265.3C396.2 264.7 396.7 264 397.1 263.2C397.433 262.333 397.667 261.4 397.8 260.4ZM401.4 225.7V239.1H405V225.7H410V222.7H396.5V225.7H401.4ZM415.8 266.7L408.1 257.1L415.2 250.3H410.7L404.3 256.8V250.3H400.7V266.7H404.3V260.7L405.5 259.4L411.3 266.7H415.8ZM415.9 234.1V222.7H412.3V239.1H416.3L422.6 227.7V239.1H426.2V222.7H422.2L415.9 234.1ZM432.1 266.7L426 250.3H422.3L416.1 266.7H419.7L421 263H427.1L428.4 266.7H432.1ZM433.5 229V222.7H429.9V239.1H433.5V232H440.1V239.1H443.7V222.7H440.1V229H433.5ZM446.4 250.3H442.8V257.6C442.533 257.6 442.167 257.667 441.7 257.8C441.167 257.867 440.6 257.9 440 257.9C439.133 257.9 438.433 257.7 437.9 257.3C437.3 256.9 437 256.2 437 255.2V250.3H433.4V255.2C433.4 256.267 433.533 257.167 433.8 257.9C434.067 258.633 434.467 259.2 435 259.6C435.533 260.067 436.167 260.4 436.9 260.6C437.7 260.8 438.6 260.9 439.6 260.9C440.2 260.9 440.8 260.867 441.4 260.8C441.933 260.667 442.4 260.567 442.8 260.5V266.7H446.4V250.3ZM462.5 263.7H453.7V259.6H461.6V256.8H453.7V253.3H462.3V250.3H450.1V266.7H462.5V263.7ZM451.1 239.1V225.8H458.9V222.7H447.5V239.1H451.1ZM480 260.4H476.5C476.367 261.533 476 262.433 475.4 263.1C474.733 263.767 473.867 264.1 472.8 264.1C471.933 264.1 471.233 263.933 470.7 263.6C470.1 263.267 469.633 262.867 469.3 262.4C468.967 261.867 468.733 261.267 468.6 260.6C468.4 259.933 468.3 259.267 468.3 258.6C468.3 257.867 468.4 257.167 468.6 256.5C468.733 255.833 468.967 255.233 469.3 254.7C469.633 254.167 470.1 253.733 470.7 253.4C471.233 253.133 471.933 253 472.8 253C473.2 253 473.6 253.067 474 253.2C474.467 253.333 474.833 253.533 475.1 253.8C475.433 254.067 475.7 254.367 475.9 254.7C476.167 255.033 476.333 255.4 476.4 255.8H479.8C479.733 254.867 479.5 254.033 479.1 253.3C478.633 252.567 478.1 251.967 477.5 251.5C476.833 250.967 476.1 250.567 475.3 250.3C474.5 250.033 473.667 249.9 472.8 249.9C471.533 249.9 470.4 250.133 469.4 250.6C468.4 251.067 467.533 251.667 466.8 252.4C466.133 253.2 465.633 254.133 465.3 255.2C464.9 256.267 464.7 257.4 464.7 258.6C464.7 259.8 464.9 260.9 465.3 261.9C465.633 262.967 466.133 263.867 466.8 264.6C467.533 265.4 468.4 266 469.4 266.4C470.4 266.867 471.533 267.1 472.8 267.1C473.8 267.1 474.7 266.933 475.5 266.6C476.367 266.333 477.133 265.9 477.8 265.3C478.4 264.7 478.9 264 479.3 263.2C479.633 262.4 479.867 261.467 480 260.4ZM495.1 250.3H481.6V253.4H486.5V266.7H490.1V253.4H495.1V250.3ZM511.2 261.9C511.133 260.9 510.867 260.033 510.4 259.3C509.933 258.567 509.167 258.033 508.1 257.7C508.833 257.367 509.4 256.933 509.8 256.4C510.2 255.867 510.4 255.167 510.4 254.3C510.4 253.567 510.267 252.933 510 252.4C509.733 251.867 509.367 251.433 508.9 251.1C508.433 250.833 507.9 250.633 507.3 250.5C506.633 250.367 505.9 250.3 505.1 250.3H497.4V266.7H505.4C506.133 266.7 506.833 266.6 507.5 266.4C508.233 266.2 508.867 265.9 509.4 265.5C509.933 265.167 510.367 264.7 510.7 264.1C511.033 263.433 511.2 262.7 511.2 261.9ZM528.4 266.7L522.2 250.3H518.5L512.3 266.7H516L517.2 263H523.4L524.6 266.7H528.4ZM499.4 26.4L508.5 33.2L505 44.1L514.3 37.5L523.5 44.2L520.2 33.3L529.4 26.6L518 26.4L514.5 15.6L510.8 26.4H499.4Z' fill='%23AEAEB1'/%3e%3cpath d='M504.6 257H501V253.2H504.4C504.667 253.2 504.967 253.2 505.3 253.2C505.567 253.267 505.833 253.367 506.1 253.5C506.3 253.634 506.467 253.833 506.6 254.1C506.733 254.367 506.8 254.667 506.8 255C506.8 255.734 506.6 256.234 506.2 256.5C505.8 256.834 505.267 257 504.6 257Z' fill='%23AEAEB1'/%3e%3cpath d='M358.4 226.8C358.533 227.133 358.6 227.533 358.6 228C358.6 228.533 358.533 228.966 358.4 229.3C358.2 229.633 357.967 229.866 357.7 230C357.367 230.2 357.033 230.333 356.7 230.4C356.3 230.466 355.9 230.5 355.5 230.5H352.7V225.6H355.5C355.9 225.6 356.3 225.633 356.7 225.7C357.033 225.766 357.367 225.866 357.7 226C357.967 226.2 358.2 226.466 358.4 226.8Z' fill='%23AEAEB1'/%3e%3cpath d='M520.3 254.4L522.4 260.4H518.1L520.3 254.4Z' fill='%23AEAEB1'/%3e%3cpath d='M348.5 98.7002L344.1 123.1L344.5 123.4C347.433 120.467 350.6 118.367 354 117.1C357.4 115.767 361.233 115.1 365.5 115.1C370.833 115.1 375.567 116.1 379.7 118.1C383.833 120.034 387.3 122.634 390.1 125.9C392.9 129.167 395.067 133.034 396.6 137.5C398.067 141.967 398.8 146.734 398.8 151.8C398.8 157.334 397.733 162.467 395.6 167.2C393.4 172 390.5 176.134 386.9 179.6C383.233 183.134 379 185.834 374.2 187.7C369.333 189.634 364.2 190.534 358.8 190.4C353.533 190.4 348.533 189.7 343.8 188.3C339 186.9 334.767 184.767 331.1 181.9C327.367 179.034 324.4 175.467 322.2 171.2C320 167 318.867 162.067 318.8 156.4H340.6C341.133 161.334 343 165.267 346.2 168.2C349.333 171.067 353.367 172.5 358.3 172.5C361.167 172.5 363.767 171.934 366.1 170.8C368.367 169.6 370.3 168.067 371.9 166.2C373.5 164.267 374.733 162.034 375.6 159.5C376.467 157.034 376.9 154.467 376.9 151.8C376.9 149 376.5 146.367 375.7 143.9C374.9 141.434 373.667 139.3 372 137.5C370.333 135.634 368.4 134.167 366.2 133.1C363.933 132.1 361.3 131.6 358.3 131.6C354.433 131.6 351.267 132.3 348.8 133.7C346.333 135.1 344 137.267 341.8 140.2H322.1L332.8 80.7002H392.9V98.7002H348.5Z' fill='%23AEAEB1'/%3e%3cpath d='M426 171.1V188.4H408.3V171.1H426Z' fill='%23AEAEB1'/%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M439.2 107.7C441.333 100.567 444.2 94.8333 447.8 90.5C451.4 86.1667 455.567 83.1 460.3 81.3C465.1 79.4333 470.167 78.5 475.5 78.5C480.967 78.5 486.067 79.4333 490.8 81.3C495.6 83.1 499.8 86.1667 503.4 90.5C507.067 94.8333 509.967 100.567 512.1 107.7C514.167 114.833 515.2 123.633 515.2 134.1C515.2 144.833 514.167 153.833 512.1 161.1C509.967 168.3 507.067 174.067 503.4 178.4C499.8 182.733 495.6 185.8 490.8 187.6C486.067 189.467 480.967 190.4 475.5 190.4C470.167 190.4 465.1 189.467 460.3 187.6C455.567 185.8 451.4 182.733 447.8 178.4C444.2 174.067 441.333 168.3 439.2 161.1C437.133 153.833 436.1 144.833 436.1 134.1C436.1 123.633 437.133 114.833 439.2 107.7ZM458.3 145.2C458.5 149.6 459.133 153.8 460.2 157.8C461.267 161.867 462.967 165.333 465.3 168.2C467.7 171.067 471.1 172.5 475.5 172.5C480.033 172.5 483.5 171.067 485.9 168.2C488.3 165.333 490.033 161.867 491.1 157.8C492.167 153.8 492.8 149.6 493 145.2C493.2 140.867 493.333 137.167 493.4 134.1C493.333 132.233 493.3 130 493.3 127.4C493.233 124.733 493.033 122.033 492.7 119.3C492.3 116.5 491.767 113.767 491.1 111.1C490.433 108.367 489.433 105.9 488.1 103.7C486.767 101.567 485.067 99.8333 483 98.5C481 97.1667 478.5 96.5 475.5 96.5C472.5 96.5 470 97.1667 468 98.5C466 99.8333 464.367 101.567 463.1 103.7C461.833 105.9 460.833 108.367 460.1 111.1C459.367 113.767 458.867 116.5 458.6 119.3C458.267 122.033 458.067 124.733 458 127.4C457.933 130 457.9 132.233 457.9 134.1C457.9 137.167 458.033 140.867 458.3 145.2Z' fill='%23AEAEB1'/%3e%3crect x='288' y='220' width='50' height='51' fill='%23AEAEB1'/%3e%3c/svg%3e" onmouseover="this.style.opacity=0.5" onmouseout="this.style.opacity=1"/>
# </a>
# 						</div>
# 					</div>
# 					<div class="agreement t-gray t-txt-s">		Данные, используемые на&nbsp;сайте Туту.ру, включая стоимость электронных авиа- и&nbsp;ж/д билетов, электронных билетов на&nbsp;автобусы и&nbsp;туристского продукта, а&nbsp;также расписание самолетов, поездов, электропоездов и&nbsp;автобусов взяты из&nbsp;официальных источников. Электронные авиа- и&nbsp;ж/д билеты, электронные билеты на&nbsp;автобусы предоставляются партнерами Туту.ру и&nbsp;их&nbsp;стоимость указана с&nbsp;учетом сервисного сбора Туту.ру. Окончательную сумму можно увидеть на&nbsp;шаге подтверждения заказа. При использовании материалов ссылка на&nbsp;сайт Туту.ру обязательна.
# 	<!--noindex-->
# 		<a 
# 			class="g-link _grey"
# 			rel="nofollow"
# 			data-seo-url="https://www.tutu.ru/2read/legal_information/legal_personal/"
# 		>
# 			Политика ООО «НТТ» в отношении обработки персональных данных
# 		</a>
# 	<!--/noindex-->
# 	<script src="https://cdn1.tu-tu.ru/js4/src/module/seoHiddenLink/m.js?1683197592"></script>

# 	</div>
# 				</div>
# 			</div>
# 			<div class="m-appstore_links right_block">
# 															</div>
# 			<!--/noindex-->
# 		</div>
# 	</div>
# </div>
# 	</footer>
# 				<!-- Rating@Mail.ru counter -->
# <script type="text/javascript">
# 	var _tmr = window._tmr || (window._tmr = []);
# 	_tmr.push({id: "2846485", type: "pageView", start: (new Date()).getTime()});
# 	(function (d, w, id) {
# 		if (d.getElementById(id)) return;
# 		var ts = d.createElement("script"); ts.type = "text/javascript"; ts.async = true; ts.id = id;
# 		ts.src = (d.location.protocol == "https:" ? "https:" : "http:") + "//top-fwz1.mail.ru/js/code.js";
# 		var f = function () {var s = d.getElementsByTagName("script")[0]; s.parentNode.insertBefore(ts, s);};
# 		if (w.opera == "[object Opera]") { d.addEventListener("DOMContentLoaded", f, false); } else { f(); }
# 	})(document, window, "topmailru-code");
# </script>
# <noscript><div style="position:absolute;left:-10000px;">
# <img src="//top-fwz1.mail.ru/counter?id=2846485;js=na" style="border:0;" height="1" width="1" alt="Рейтинг@Mail.ru" />
# </div></noscript>
# <!-- //Rating@Mail.ru counter -->

# <script type="text/javascript">
# 	var _tmr = _tmr || [];
# 	_tmr.push({"type":"itemView","productid":"","pagetype":"other","totalvalue":"","list":1});
# </script><noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-PD5PQQD"
# height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
# <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
# new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
# j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
# 'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
# })(window,document,'script','dataLayer','GTM-PD5PQQD');</script>
# <script>
# 	window.advcake_push_data = window.advcake_push_data || function(advcake_data_array){};
# 	window.advcake_data = {"pageType":0};
# 	window.advcake_push_data(window.advcake_data);
# </script>

		
# 			<script>var RM = RM || {}; RM.StaticData = RM.StaticData || {}; RM.StaticData["debug"] = {"levels":{"ERROR":0,"WARNING":1,"INFO":2},"level":0};var RM = RM || {}; RM.StaticData = RM.StaticData || {}; RM.StaticData.isProduction = "1";var RM = RM || {}; RM.StaticData = RM.StaticData || {}; RM.StaticData["session"] = [];var RM = RM || {}; RM.StaticData = RM.StaticData || {}; RM.StaticData["cookiePropagatorConf"] = "need_propagation";RM.StaticData["cookiePropagatorHash"] = "09b0cd4f453f0e2e0e57eac914187d83";var RM = RM || {}; RM.StaticData = RM.StaticData || {}; RM.StaticData["abCampaigns"] = {"avia_offers_longpolling":{"AVIA-5985_longpolling_disabled":0,"AVIA-5985_longpolling_enabled":1},"avia_wizard_auto_complete_hint":{"AVIA-3061_show_hint":0,"AVIA-3061_without_hint":1},"avia_wizard_mobile_change_fare":{"AVIA-10919_show_change_fare":1,"AVIA-10919_without_change_fare":0},"main_page_mobile":{"main_page_mobile_off":0,"main_page_mobile_on":1},"tour_only_hotel_with_photo":{"tour_only_hotel_with_photo_off":1,"tour_only_hotel_with_photo_on":0},"tour_prepayment_rules":{"tour_prepayment_rules_editable":1,"tour_prepayment_rules_fixed":0}};window.AbTestingParams = {"apiUrl":"https:\/\/www.tutu.ru\/ajax\/?Action=analytics_abtesting","campaignsData":{"ab_adv_card_tags":{"id":"ab_adv_card_tags","applied":0,"active":true,"forceVariant":0,"variants":{"ab_adv_card_tags_links_clear":{"assigned":0,"id":"ab_adv_card_tags_links_clear"},"ab_adv_card_tags_links_save":{"assigned":0,"id":"ab_adv_card_tags_links_save"},"ab_adv_card_tags_off":{"assigned":0,"id":"ab_adv_card_tags_off"},"ab_adv_card_tags_text":{"assigned":1,"id":"ab_adv_card_tags_text","versionedId":"ab_adv_card_tags_text_v02"}}},"adv_etrains_direction_link":{"id":"adv_etrains_direction_link","applied":0,"active":true,"forceVariant":0,"variants":{"adv_etrains_direction_link_forei":{"assigned":0,"id":"adv_etrains_direction_link_forei"},"adv_etrains_direction_link_point":{"assigned":0,"id":"adv_etrains_direction_link_point"},"adv_etrains_direction_link_russi":{"assigned":1,"id":"adv_etrains_direction_link_russi","versionedId":"adv_etrains_direction_link_russi_v04"}}},"adv_search_form_showcase_rem":{"id":"adv_search_form_showcase_rem","applied":0,"active":true,"forceVariant":0,"variants":{"adv_search_form_showcase_rem_off":{"assigned":1,"id":"adv_search_form_showcase_rem_off","versionedId":"adv_search_form_showcase_rem_off_v01"},"adv_search_form_showcase_rem_on":{"assigned":0,"id":"adv_search_form_showcase_rem_on"}}},"app_bus_insurances":{"id":"app_bus_insurances","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-3539-no-insurance-selected":{"assigned":1,"id":"MAPP-3539-no-insurance-selected","versionedId":"MAPP-3539-no-insurance-selected"},"MAPP-3539-without-insurance":{"assigned":0,"id":"MAPP-3539-without-insurance"}}},"app_bus_tariff_features":{"id":"app_bus_tariff_features","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-3537-hide-tariff-info":{"assigned":0,"id":"MAPP-3537-hide-tariff-info"},"MAPP-3537-show-tariff-info":{"assigned":1,"id":"MAPP-3537-show-tariff-info","versionedId":"MAPP-3537-show-tariff-info_v01"}}},"app_idfa_requester":{"id":"app_idfa_requester","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-3464_ads":{"assigned":0,"id":"MAPP-3464_ads"},"MAPP-3464_list":{"assigned":1,"id":"MAPP-3464_list","versionedId":"MAPP-3464_list_v04"},"MAPP-3464_off":{"assigned":0,"id":"MAPP-3464_off"}}},"app_ios_hotels_history_2":{"id":"app_ios_hotels_history_2","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-5953_without_hotels_history":{"assigned":0,"id":"MAPP-5953_without_hotels_history"},"MAPP-5953_with_hotels_history":{"assigned":1,"id":"MAPP-5953_with_hotels_history","versionedId":"MAPP-5953_with_hotels_history_v01"}}},"app_mono_train_bdui_banner_android":{"id":"app_mono_train_bdui_banner_android","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-8261-banner-off-android":{"assigned":0,"id":"MAPP-8261-banner-off-android"},"MAPP-8261-banner-on-android":{"assigned":1,"id":"MAPP-8261-banner-on-android","versionedId":"MAPP-8261-banner-on-android_v01"}}},"app_mono_train_bdui_banner_ios":{"id":"app_mono_train_bdui_banner_ios","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-8415-banner-off-ios":{"assigned":0,"id":"MAPP-8415-banner-off-ios"},"MAPP-8415-banner-on-ios":{"assigned":1,"id":"MAPP-8415-banner-on-ios","versionedId":"MAPP-8415-banner-on-ios_v04"}}},"app_ptt_additional_baggage_s7":{"id":"app_ptt_additional_baggage_s7","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-3889_has_baggage":{"assigned":1,"id":"MAPP-3889_has_baggage","versionedId":"MAPP-3889_has_baggage"},"MAPP-3889_no_baggage":{"assigned":0,"id":"MAPP-3889_no_baggage"}}},"app_ptt_bdui_juicy_offers_android":{"id":"app_ptt_bdui_juicy_offers_android","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-8209-android-ptt-hide-juicy-offers":{"assigned":0,"id":"MAPP-8209-android-ptt-hide-juicy-offers"},"MAPP-8209-android-ptt-show-juicy-offers":{"assigned":1,"id":"MAPP-8209-android-ptt-show-juicy-offers","versionedId":"MAPP-8209-android-ptt-show-juicy-offers_v02"}}},"app_ptt_bdui_juicy_offers_ios":{"id":"app_ptt_bdui_juicy_offers_ios","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-8209-ios-ptt-hide-juicy-offers":{"assigned":0,"id":"MAPP-8209-ios-ptt-hide-juicy-offers"},"MAPP-8209-ios-ptt-show-juicy-offers":{"assigned":1,"id":"MAPP-8209-ios-ptt-show-juicy-offers","versionedId":"MAPP-8209-ios-ptt-show-juicy-offers_v03"}}},"app_ptt_bdui_on_main_screen_andr_v2":{"id":"app_ptt_bdui_on_main_screen_andr_v2","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-6104_bdui_v2_off":{"assigned":0,"id":"MAPP-6104_bdui_v2_off"},"MAPP-6104_bdui_v2_on":{"assigned":1,"id":"MAPP-6104_bdui_v2_on","versionedId":"MAPP-6104_bdui_v2_on_v01"}}},"app_ptt_bdui_on_main_screen_ios_3":{"id":"app_ptt_bdui_on_main_screen_ios_3","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-7385_bdui_off_3":{"assigned":0,"id":"MAPP-7385_bdui_off_3"},"MAPP-7385_bdui_on_3":{"assigned":1,"id":"MAPP-7385_bdui_on_3","versionedId":"MAPP-7385_bdui_on_3_v01"}}},"app_ptt_bdui_on_main_screen_ios_v2":{"id":"app_ptt_bdui_on_main_screen_ios_v2","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-6103_bdui_off_v2":{"assigned":0,"id":"MAPP-6103_bdui_off_v2"},"MAPP-6103_bdui_on_v2":{"assigned":1,"id":"MAPP-6103_bdui_on_v2","versionedId":"MAPP-6103_bdui_on_v2_v02"}}},"app_ptt_calendar_prices_android":{"id":"app_ptt_calendar_prices_android","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-5100_hide_prices":{"assigned":0,"id":"MAPP-5100_hide_prices"},"MAPP-5100_show_prices":{"assigned":1,"id":"MAPP-5100_show_prices","versionedId":"MAPP-5100_show_prices_v01"}}},"app_ptt_calendar_prices_ios":{"id":"app_ptt_calendar_prices_ios","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-5101_hide_prices":{"assigned":0,"id":"MAPP-5101_hide_prices"},"MAPP-5101_show_prices":{"assigned":1,"id":"MAPP-5101_show_prices","versionedId":"MAPP-5101_show_prices_v01"}}},"app_ptt_feed_autoswitch_android":{"id":"app_ptt_feed_autoswitch_android","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1570_feed_autoswitch_an_off":{"assigned":0,"id":"VID-1570_feed_autoswitch_an_off"},"VID-1570_feed_autoswitch_an_on":{"assigned":1,"id":"VID-1570_feed_autoswitch_an_on","versionedId":"VID-1570_feed_autoswitch_an_on_v01"}}},"app_ptt_feed_avia_new_design_cell":{"id":"app_ptt_feed_avia_new_design_cell","applied":0,"active":true,"forceVariant":0,"variants":{"VID-2791_new_design":{"assigned":1,"id":"VID-2791_new_design","versionedId":"VID-2791_new_design_v01"},"VID-2791_old_design":{"assigned":0,"id":"VID-2791_old_design"}}},"app_ptt_feed_bus_filters_an":{"id":"app_ptt_feed_bus_filters_an","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1695_feed_bus_fltrs_an_off":{"assigned":0,"id":"VID-1695_feed_bus_fltrs_an_off"},"VID-1695_feed_bus_fltrs_an_on":{"assigned":1,"id":"VID-1695_feed_bus_fltrs_an_on","versionedId":"VID-1695_feed_bus_fltrs_an_on_v01"}}},"app_ptt_feed_bus_new_design_cell":{"id":"app_ptt_feed_bus_new_design_cell","applied":0,"active":true,"forceVariant":0,"variants":{"VID-2536_new_design":{"assigned":1,"id":"VID-2536_new_design","versionedId":"VID-2536_new_design_v01"},"VID-2536_old_design":{"assigned":0,"id":"VID-2536_old_design"}}},"app_ptt_feed_hotel_new_design_cell_v2":{"id":"app_ptt_feed_hotel_new_design_cell_v2","applied":0,"active":true,"forceVariant":0,"variants":{"VID-2304_new_design":{"assigned":1,"id":"VID-2304_new_design","versionedId":"VID-2304_new_design_v02"},"VID-2304_old_design":{"assigned":0,"id":"VID-2304_old_design"}}},"app_ptt_feed_informers_android":{"id":"app_ptt_feed_informers_android","applied":0,"active":true,"forceVariant":0,"variants":{"VID-2375_off":{"assigned":0,"id":"VID-2375_off"},"VID-2375_on":{"assigned":1,"id":"VID-2375_on","versionedId":"VID-2375_on_v01"}}},"app_ptt_feed_informers_ios":{"id":"app_ptt_feed_informers_ios","applied":0,"active":true,"forceVariant":0,"variants":{"INFORM-32_informers_off":{"assigned":0,"id":"INFORM-32_informers_off"},"INFORM-32_informers_on":{"assigned":1,"id":"INFORM-32_informers_on","versionedId":"INFORM-32_informers_on_v02"}}},"app_ptt_feed_map_transition_ios":{"id":"app_ptt_feed_map_transition_ios","applied":0,"active":true,"forceVariant":0,"variants":{"VID-2266_new_transition":{"assigned":1,"id":"VID-2266_new_transition","versionedId":"VID-2266_new_transition_v01"},"VID-2266_old_transition":{"assigned":0,"id":"VID-2266_old_transition"}}},"app_ptt_feed_train_filters_an":{"id":"app_ptt_feed_train_filters_an","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1629_feed_train_fltrs_an_off":{"assigned":0,"id":"VID-1629_feed_train_fltrs_an_off"},"VID-1629_feed_train_fltrs_an_on":{"assigned":1,"id":"VID-1629_feed_train_fltrs_an_on","versionedId":"VID-1629_feed_train_fltrs_an_on_v01"}}},"app_ptt_feed_train_filters_ios":{"id":"app_ptt_feed_train_filters_ios","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1590-train_filters_off":{"assigned":0,"id":"VID-1590-train_filters_off"},"VID-1590-train_filters_on":{"assigned":1,"id":"VID-1590-train_filters_on","versionedId":"VID-1590-train_filters_on_v01"}}},"app_ptt_feed_train_new_design_cell_v2":{"id":"app_ptt_feed_train_new_design_cell_v2","applied":0,"active":true,"forceVariant":0,"variants":{"VID-2881_new_horizontal_design":{"assigned":1,"id":"VID-2881_new_horizontal_design","versionedId":"VID-2881_new_horizontal_design_v02"},"VID-2881_new_vertical_design":{"assigned":0,"id":"VID-2881_new_vertical_design"},"VID-2881_old_design":{"assigned":0,"id":"VID-2881_old_design"}}},"app_ptt_hotels_android_2":{"id":"app_ptt_hotels_android_2","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-4151_android_hotels_off_2":{"assigned":0,"id":"MAPP-4151_android_hotels_off_2"},"MAPP-4151_android_hotels_on_2":{"assigned":1,"id":"MAPP-4151_android_hotels_on_2","versionedId":"MAPP-4151_android_hotels_on_2"}}},"app_ptt_hotels_history_andr_2":{"id":"app_ptt_hotels_history_andr_2","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-5569_hotels_history_off":{"assigned":0,"id":"MAPP-5569_hotels_history_off"},"MAPP-5569_hotels_history_on":{"assigned":1,"id":"MAPP-5569_hotels_history_on","versionedId":"MAPP-5569_hotels_history_on_v01"}}},"app_ptt_hotels_ios_1":{"id":"app_ptt_hotels_ios_1","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-4070_hotels_off":{"assigned":0,"id":"MAPP-4070_hotels_off"},"MAPP-4070_hotels_on":{"assigned":1,"id":"MAPP-4070_hotels_on","versionedId":"MAPP-4070_hotels_on_v01"}}},"app_ptt_hotels_ios_2":{"id":"app_ptt_hotels_ios_2","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-4310_ios_hotels_off_2":{"assigned":0,"id":"MAPP-4310_ios_hotels_off_2"},"MAPP-4310_ios_hotels_on_2":{"assigned":1,"id":"MAPP-4310_ios_hotels_on_2","versionedId":"MAPP-4310_ios_hotels_on_2"}}},"app_ptt_infoservice_android_3":{"id":"app_ptt_infoservice_android_3","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-4465_infoservice_off":{"assigned":0,"id":"MAPP-4465_infoservice_off"},"MAPP-4465_infoservice_on":{"assigned":1,"id":"MAPP-4465_infoservice_on","versionedId":"MAPP-4465_infoservice_on_v01"}}},"app_ptt_infoservice_ios_3":{"id":"app_ptt_infoservice_ios_3","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-4468_ios_infoservice_off":{"assigned":0,"id":"MAPP-4468_ios_infoservice_off"},"MAPP-4468_ios_infoservice_on":{"assigned":1,"id":"MAPP-4468_ios_infoservice_on","versionedId":"MAPP-4468_ios_infoservice_on"}}},"app_ptt_in_app_updates_2":{"id":"app_ptt_in_app_updates_2","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-7640_turn_off_updates_2":{"assigned":0,"id":"MAPP-7640_turn_off_updates_2"},"MAPP-7640_turn_on_updates_2":{"assigned":1,"id":"MAPP-7640_turn_on_updates_2","versionedId":"MAPP-7640_turn_on_updates_2_v02"}}},"app_ptt_main_stories_andr_2":{"id":"app_ptt_main_stories_andr_2","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-5753_stories_off":{"assigned":0,"id":"MAPP-5753_stories_off"},"MAPP-5753_stories_on":{"assigned":1,"id":"MAPP-5753_stories_on","versionedId":"MAPP-5753_stories_on"}}},"app_ptt_main_stories_ios":{"id":"app_ptt_main_stories_ios","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-5626_stories_off":{"assigned":0,"id":"MAPP-5626_stories_off"},"MAPP-5626_stories_on":{"assigned":1,"id":"MAPP-5626_stories_on","versionedId":"MAPP-5626_stories_on_v01"}}},"app_ptt_messages_center":{"id":"app_ptt_messages_center","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-3621_new_messages_center":{"assigned":1,"id":"MAPP-3621_new_messages_center","versionedId":"MAPP-3621_new_messages_center_v01"},"MAPP-3621_old_messages_center":{"assigned":0,"id":"MAPP-3621_old_messages_center"}}},"app_ptt_new_calendar_ios_v3":{"id":"app_ptt_new_calendar_ios_v3","applied":0,"active":true,"forceVariant":0,"variants":{"VID-2850_old_calendar":{"assigned":0,"id":"VID-2850_old_calendar"},"VID-2850_one_way":{"assigned":1,"id":"VID-2850_one_way","versionedId":"VID-2850_one_way_v02"},"VID-2850_sum_calendar":{"assigned":0,"id":"VID-2850_sum_calendar"}}},"app_ptt_new_calendar_v3_android":{"id":"app_ptt_new_calendar_v3_android","applied":0,"active":true,"forceVariant":0,"variants":{"VID-3214_new":{"assigned":1,"id":"VID-3214_new","versionedId":"VID-3214_new_v02"},"VID-3214_old":{"assigned":0,"id":"VID-3214_old"}}},"app_ptt_new_search_ios_abc":{"id":"app_ptt_new_search_ios_abc","applied":0,"active":true,"forceVariant":0,"variants":{"VID-3388_new_all":{"assigned":1,"id":"VID-3388_new_all","versionedId":"VID-3388_new_all_v06"},"VID-3388_new_search_only":{"assigned":0,"id":"VID-3388_new_search_only"},"VID-3388_old_search":{"assigned":0,"id":"VID-3388_old_search"}}},"app_ptt_orders_hotels_promo_andr":{"id":"app_ptt_orders_hotels_promo_andr","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-5751_promo_off":{"assigned":0,"id":"MAPP-5751_promo_off"},"MAPP-5751_promo_on":{"assigned":1,"id":"MAPP-5751_promo_on","versionedId":"MAPP-5751_promo_on"}}},"app_ptt_orders_hotels_promo_ios":{"id":"app_ptt_orders_hotels_promo_ios","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-5743_promo_off":{"assigned":0,"id":"MAPP-5743_promo_off"},"MAPP-5743_promo_on":{"assigned":1,"id":"MAPP-5743_promo_on","versionedId":"MAPP-5743_promo_on"}}},"app_ptt_orders_indicator_2":{"id":"app_ptt_orders_indicator_2","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-3976_hide_indicator":{"assigned":0,"id":"MAPP-3976_hide_indicator"},"MAPP-3976_show_indicator":{"assigned":1,"id":"MAPP-3976_show_indicator","versionedId":"MAPP-3976_show_indicator"}}},"app_ptt_recommended_avia_ios_v2":{"id":"app_ptt_recommended_avia_ios_v2","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1856_recommendations_v2_off":{"assigned":0,"id":"VID-1856_recommendations_v2_off"},"VID-1856_recommendations_v2_on":{"assigned":1,"id":"VID-1856_recommendations_v2_on","versionedId":"VID-1856_recommendations_v2_on_v01"}}},"app_ptt_search_with_return_ios":{"id":"app_ptt_search_with_return_ios","applied":0,"active":true,"forceVariant":0,"variants":{"VID-3928_without_return_date":{"assigned":1,"id":"VID-3928_without_return_date","versionedId":"VID-3928_without_return_date"},"VID-3928_with_return_date":{"assigned":0,"id":"VID-3928_with_return_date"}}},"app_ptt_show_tours_ab":{"id":"app_ptt_show_tours_ab","applied":0,"active":true,"forceVariant":0,"variants":{"VID-3493_hide_tours":{"assigned":0,"id":"VID-3493_hide_tours"},"VID-3493_show_tours":{"assigned":1,"id":"VID-3493_show_tours","versionedId":"VID-3493_show_tours_v01"}}},"app_ptt_train_add_services_ios":{"id":"app_ptt_train_add_services_ios","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-5387_new_design":{"assigned":1,"id":"MAPP-5387_new_design","versionedId":"MAPP-5387_new_design_v01"},"MAPP-5387_old_design":{"assigned":0,"id":"MAPP-5387_old_design"}}},"app_return_ticket_on_success":{"id":"app_return_ticket_on_success","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-3230_without_promocode":{"assigned":1,"id":"MAPP-3230_without_promocode","versionedId":"MAPP-3230_without_promocode_v01"},"MAPP-3230_without_return_ticket":{"assigned":0,"id":"MAPP-3230_without_return_ticket"},"MAPP-3230_with_promocode":{"assigned":0,"id":"MAPP-3230_with_promocode"}}},"app_train_autoselect_ios":{"id":"app_train_autoselect_ios","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-3721-hide-train-autoselect":{"assigned":0,"id":"MAPP-3721-hide-train-autoselect"},"MAPP-3721-show-train-autoselect":{"assigned":1,"id":"MAPP-3721-show-train-autoselect","versionedId":"MAPP-3721-show-train-autoselect_v01"}}},"app_train_car_selection":{"id":"app_train_car_selection","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-2331_new_car_selection_scre":{"assigned":1,"id":"MAPP-2331_new_car_selection_scre","versionedId":"MAPP-2331_new_car_selection_scre_v02"},"MAPP-2331_old_car_selection_scre":{"assigned":0,"id":"MAPP-2331_old_car_selection_scre"}}},"app_train_passengers_autofill":{"id":"app_train_passengers_autofill","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-2237_new_autofill":{"assigned":1,"id":"MAPP-2237_new_autofill","versionedId":"MAPP-2237_new_autofill_v05"},"MAPP-2237_old_autofill":{"assigned":0,"id":"MAPP-2237_old_autofill"}}},"app_train_pricing_strategy":{"id":"app_train_pricing_strategy","applied":0,"active":true,"forceVariant":0,"variants":{"app_train_pricing_strategy_15ai":{"assigned":0,"id":"app_train_pricing_strategy_15ai"},"app_train_pricing_strategy_4438i":{"assigned":0,"id":"app_train_pricing_strategy_4438i"},"app_train_pricing_strategy_5761":{"assigned":0,"id":"app_train_pricing_strategy_5761"},"app_train_pricing_strategy_6011":{"assigned":0,"id":"app_train_pricing_strategy_6011"},"app_train_pricing_strategy_7103":{"assigned":0,"id":"app_train_pricing_strategy_7103"},"app_train_pricing_strategy_7103m":{"assigned":0,"id":"app_train_pricing_strategy_7103m"},"app_train_pricing_strategy_7153":{"assigned":0,"id":"app_train_pricing_strategy_7153"},"app_train_pricing_strategy_ai":{"assigned":0,"id":"app_train_pricing_strategy_ai"},"app_train_pricing_strategy_aic10":{"assigned":0,"id":"app_train_pricing_strategy_aic10"},"app_train_pricing_strategy_aic15":{"assigned":0,"id":"app_train_pricing_strategy_aic15"},"app_train_pricing_strategy_aic5":{"assigned":0,"id":"app_train_pricing_strategy_aic5"},"app_train_pricing_strategy_aii15":{"assigned":0,"id":"app_train_pricing_strategy_aii15"},"app_train_pricing_strategy_aii5":{"assigned":0,"id":"app_train_pricing_strategy_aii5"},"app_train_pricing_strategy_dc005":{"assigned":0,"id":"app_train_pricing_strategy_dc005"},"app_train_pricing_strategy_dc010":{"assigned":0,"id":"app_train_pricing_strategy_dc010"},"app_train_pricing_strategy_defau":{"assigned":0,"id":"app_train_pricing_strategy_defau"},"app_train_pricing_strategy_dwn10":{"assigned":0,"id":"app_train_pricing_strategy_dwn10"},"app_train_pricing_strategy_dwn4":{"assigned":0,"id":"app_train_pricing_strategy_dwn4"},"app_train_pricing_strategy_dwn5":{"assigned":0,"id":"app_train_pricing_strategy_dwn5"},"app_train_pricing_strategy_dwn8":{"assigned":0,"id":"app_train_pricing_strategy_dwn8"},"app_train_pricing_strategy_ic005":{"assigned":0,"id":"app_train_pricing_strategy_ic005"},"app_train_pricing_strategy_ic010":{"assigned":0,"id":"app_train_pricing_strategy_ic010"},"app_train_pricing_strategy_ic025":{"assigned":0,"id":"app_train_pricing_strategy_ic025"},"app_train_pricing_strategy_sup10":{"assigned":1,"id":"app_train_pricing_strategy_sup10","versionedId":"app_train_pricing_strategy_sup10_v26"},"app_train_pricing_strategy_sup5":{"assigned":0,"id":"app_train_pricing_strategy_sup5"},"app_train_pricing_strategy_up10":{"assigned":0,"id":"app_train_pricing_strategy_up10"},"app_train_pricing_strategy_up4":{"assigned":0,"id":"app_train_pricing_strategy_up4"},"app_train_pricing_strategy_up5":{"assigned":0,"id":"app_train_pricing_strategy_up5"},"app_train_pricing_strategy_up8":{"assigned":0,"id":"app_train_pricing_strategy_up8"}}},"AVIA-16083_booking_price":{"id":"AVIA-16083_booking_price","applied":0,"active":true,"forceVariant":0,"variants":{"AVIA-16083_booking_price_199rub":{"assigned":1,"id":"AVIA-16083_booking_price_199rub","versionedId":"AVIA-16083_booking_price_199rub"},"AVIA-16083_booking_price_1rub":{"assigned":0,"id":"AVIA-16083_booking_price_1rub"},"AVIA-16083_booking_price_99rub":{"assigned":0,"id":"AVIA-16083_booking_price_99rub"}}},"AVIA-16128-insurance-description":{"id":"AVIA-16128-insurance-description","applied":0,"active":true,"forceVariant":0,"variants":{"AVIA-16128_new_description":{"assigned":0,"id":"AVIA-16128_new_description"},"AVIA-16128_old_description":{"assigned":1,"id":"AVIA-16128_old_description","versionedId":"AVIA-16128_old_description_v02"}}},"AVIA-16187_search_extension":{"id":"AVIA-16187_search_extension","applied":0,"active":true,"forceVariant":0,"variants":{"AVIA-16187_without_search_extens":{"assigned":0,"id":"AVIA-16187_without_search_extens"},"AVIA-16187_with_search_extension":{"assigned":1,"id":"AVIA-16187_with_search_extension","versionedId":"AVIA-16187_with_search_extension_v01"}}},"AVIA-16244-show-hotels-on-succes":{"id":"AVIA-16244-show-hotels-on-succes","applied":0,"active":true,"forceVariant":0,"variants":{"AVIA-16244_with_cards":{"assigned":0,"id":"AVIA-16244_with_cards"},"AVIA-16244_with_maps":{"assigned":1,"id":"AVIA-16244_with_maps","versionedId":"AVIA-16244_with_maps_v01"}}},"AVIA-16328_gr_double_price":{"id":"AVIA-16328_gr_double_price","applied":0,"active":true,"forceVariant":0,"variants":{"AVIA-16328_doubled_price":{"assigned":1,"id":"AVIA-16328_doubled_price","versionedId":"AVIA-16328_doubled_price_v04"},"AVIA-16328_same_price":{"assigned":0,"id":"AVIA-16328_same_price"}}},"AVIA-16336_offers_tariff_design":{"id":"AVIA-16336_offers_tariff_design","applied":0,"active":true,"forceVariant":0,"variants":{"AVIA-16336_basic_tariff_view":{"assigned":0,"id":"AVIA-16336_basic_tariff_view"},"AVIA-16336_tariff_cards_view":{"assigned":1,"id":"AVIA-16336_tariff_cards_view","versionedId":"AVIA-16336_tariff_cards_view_v01"}}},"AVIA-16572_feed_checkout":{"id":"AVIA-16572_feed_checkout","applied":0,"active":true,"forceVariant":0,"variants":{"AVIA-16572_feed_checkout_new":{"assigned":1,"id":"AVIA-16572_feed_checkout_new","versionedId":"AVIA-16572_feed_checkout_new"},"AVIA-16572_feed_checkout_old":{"assigned":0,"id":"AVIA-16572_feed_checkout_old"}}},"AVIA-16690_feed_checkout":{"id":"AVIA-16690_feed_checkout","applied":0,"active":true,"forceVariant":0,"variants":{"AVIA-16690_feed_checkout_new":{"assigned":1,"id":"AVIA-16690_feed_checkout_new","versionedId":"AVIA-16690_feed_checkout_new"},"AVIA-16690_feed_checkout_old":{"assigned":0,"id":"AVIA-16690_feed_checkout_old"}}},"AVIA-16737-offer-details-tariffs":{"id":"AVIA-16737-offer-details-tariffs","applied":0,"active":true,"forceVariant":0,"variants":{"AVIA-16737-offer-details-tariffs-expander":{"assigned":0,"id":"AVIA-16737-offer-details-tariffs-expander"},"AVIA-16737-offer-details-tariffs-old":{"assigned":0,"id":"AVIA-16737-offer-details-tariffs-old"},"AVIA-16737-offer-details-tariffs-slider":{"assigned":1,"id":"AVIA-16737-offer-details-tariffs-slider","versionedId":"AVIA-16737-offer-details-tariffs-slider"}}},"AVIA-17048_mono_ios_tariffs_on_details":{"id":"AVIA-17048_mono_ios_tariffs_on_details","applied":0,"active":true,"forceVariant":0,"variants":{"AVIA-17048_mono_ios_tariffs_expandable_cards":{"assigned":0,"id":"AVIA-17048_mono_ios_tariffs_expandable_cards"},"AVIA-17048_mono_ios_tariffs_old":{"assigned":0,"id":"AVIA-17048_mono_ios_tariffs_old"},"AVIA-17048_mono_ios_tariffs_scrollable_cards":{"assigned":1,"id":"AVIA-17048_mono_ios_tariffs_scrollable_cards","versionedId":"AVIA-17048_mono_ios_tariffs_scrollable_cards_v02"}}},"avia_8jnf_frjrbir_frgrnfpu":{"id":"avia_8jnf_frjrbir_frgrnfpu","applied":0,"active":true,"forceVariant":0,"variants":{"avia_8jnf_frjrbir_frgrnfpu_above":{"assigned":1,"id":"avia_8jnf_frjrbir_frgrnfpu_above","versionedId":"avia_8jnf_frjrbir_frgrnfpu_above_v01"},"avia_8jnf_frjrbir_frgrnfpu_below":{"assigned":0,"id":"avia_8jnf_frjrbir_frgrnfpu_below"},"avia_8jnf_frjrbir_frgrnfpu_contr":{"assigned":0,"id":"avia_8jnf_frjrbir_frgrnfpu_contr"}}},"avia_flights1_ptt_popup":{"id":"avia_flights1_ptt_popup","applied":0,"active":true,"forceVariant":0,"variants":{"avia_flights1_ptt_popup_off":{"assigned":0,"id":"avia_flights1_ptt_popup_off"},"avia_flights1_ptt_popup_on":{"assigned":1,"id":"avia_flights1_ptt_popup_on","versionedId":"avia_flights1_ptt_popup_on_v02"}}},"avia_form_on_main":{"id":"avia_form_on_main","applied":0,"active":true,"forceVariant":0,"variants":{"AVIA-15755_avia_form_on_main_off":{"assigned":0,"id":"AVIA-15755_avia_form_on_main_off"},"AVIA-15755_avia_form_on_main_on":{"assigned":1,"id":"AVIA-15755_avia_form_on_main_on","versionedId":"AVIA-15755_avia_form_on_main_on_v01"}}},"avia_main_ptt_popup":{"id":"avia_main_ptt_popup","applied":0,"active":true,"forceVariant":0,"variants":{"avia_main_ptt_popup_off":{"assigned":0,"id":"avia_main_ptt_popup_off"},"avia_main_ptt_popup_on":{"assigned":1,"id":"avia_main_ptt_popup_on","versionedId":"avia_main_ptt_popup_on_v05"}}},"avia_revenue_on_offers":{"id":"avia_revenue_on_offers","applied":0,"active":true,"forceVariant":0,"variants":{"avia_revenue_on_offers_above":{"assigned":0,"id":"avia_revenue_on_offers_above"},"avia_revenue_on_offers_below":{"assigned":1,"id":"avia_revenue_on_offers_below","versionedId":"avia_revenue_on_offers_below"},"avia_revenue_on_offers_contr":{"assigned":0,"id":"avia_revenue_on_offers_contr"}}},"avia_rough_exchange_calc":{"id":"avia_rough_exchange_calc","applied":0,"active":true,"forceVariant":0,"variants":{"AVIA-15145_rough_calc_off":{"assigned":0,"id":"AVIA-15145_rough_calc_off"},"AVIA-15145_rough_calc_on":{"assigned":1,"id":"AVIA-15145_rough_calc_on","versionedId":"AVIA-15145_rough_calc_on_v01"}}},"avia_wizard_company_payment":{"id":"avia_wizard_company_payment","applied":0,"active":true,"forceVariant":0,"variants":{"avia_wizard_company_payment_off":{"assigned":0,"id":"avia_wizard_company_payment_off"},"avia_wizard_company_payment_on":{"assigned":1,"id":"avia_wizard_company_payment_on","versionedId":"avia_wizard_company_payment_on_v01"}}},"bus_checkout_app_banner":{"id":"bus_checkout_app_banner","applied":0,"active":true,"forceVariant":0,"variants":{"bus_checkout_app_banner_off":{"assigned":0,"id":"bus_checkout_app_banner_off"},"bus_checkout_app_banner_on":{"assigned":1,"id":"bus_checkout_app_banner_on","versionedId":"bus_checkout_app_banner_on_v01"}}},"bus_checkout_voyager_suggester_ios":{"id":"bus_checkout_voyager_suggester_ios","applied":0,"active":true,"forceVariant":0,"variants":{"bus_checkout_voyager_suggester_ios_off":{"assigned":0,"id":"bus_checkout_voyager_suggester_ios_off"},"bus_checkout_voyager_suggester_ios_on":{"assigned":1,"id":"bus_checkout_voyager_suggester_ios_on","versionedId":"bus_checkout_voyager_suggester_ios_on_v01"}}},"bus_foreign_card":{"id":"bus_foreign_card","applied":0,"active":true,"forceVariant":0,"variants":{"bus_foreign_card_off":{"assigned":0,"id":"bus_foreign_card_off"},"bus_foreign_card_on":{"assigned":1,"id":"bus_foreign_card_on","versionedId":"bus_foreign_card_on_v02"}}},"bus_new_station_page":{"id":"bus_new_station_page","applied":0,"active":true,"forceVariant":0,"variants":{"bus_new_station_page_off":{"assigned":0,"id":"bus_new_station_page_off"},"bus_new_station_page_on":{"assigned":1,"id":"bus_new_station_page_on","versionedId":"bus_new_station_page_on_v03"}}},"bus_refund_form":{"id":"bus_refund_form","applied":0,"active":true,"forceVariant":0,"variants":{"bus_refund_form_off":{"assigned":0,"id":"bus_refund_form_off"},"bus_refund_form_on":{"assigned":1,"id":"bus_refund_form_on","versionedId":"bus_refund_form_on_v08"}}},"bus_schedule_buy_action":{"id":"bus_schedule_buy_action","applied":0,"active":true,"forceVariant":0,"variants":{"bus_schedule_buy_action_date":{"assigned":1,"id":"bus_schedule_buy_action_date","versionedId":"bus_schedule_buy_action_date_v02"},"bus_schedule_buy_action_from":{"assigned":0,"id":"bus_schedule_buy_action_from"},"bus_schedule_buy_action_init":{"assigned":0,"id":"bus_schedule_buy_action_init"}}},"bus_success_app_banner":{"id":"bus_success_app_banner","applied":0,"active":true,"forceVariant":0,"variants":{"bus_success_app_banner_off":{"assigned":0,"id":"bus_success_app_banner_off"},"bus_success_app_banner_on":{"assigned":1,"id":"bus_success_app_banner_on","versionedId":"bus_success_app_banner_on_v01"}}},"bus_supreme_loader":{"id":"bus_supreme_loader","applied":0,"active":true,"forceVariant":0,"variants":{"bus_supreme_loader_off":{"assigned":0,"id":"bus_supreme_loader_off"},"bus_supreme_loader_on":{"assigned":1,"id":"bus_supreme_loader_on","versionedId":"bus_supreme_loader_on_v01"}}},"bus_tickets_buy_action":{"id":"bus_tickets_buy_action","applied":0,"active":true,"forceVariant":0,"variants":{"bus_tickets_buy_action_buy":{"assigned":0,"id":"bus_tickets_buy_action_buy"},"bus_tickets_buy_action_date":{"assigned":1,"id":"bus_tickets_buy_action_date","versionedId":"bus_tickets_buy_action_date_v02"},"bus_tickets_buy_action_init":{"assigned":0,"id":"bus_tickets_buy_action_init"}}},"bus_vid_app_banner":{"id":"bus_vid_app_banner","applied":0,"active":true,"forceVariant":0,"variants":{"bus_vid_app_banner_off":{"assigned":0,"id":"bus_vid_app_banner_off"},"bus_vid_app_banner_on":{"assigned":1,"id":"bus_vid_app_banner_on","versionedId":"bus_vid_app_banner_on_v01"}}},"bus_vid_price_labels":{"id":"bus_vid_price_labels","applied":0,"active":true,"forceVariant":0,"variants":{"bus_vid_price_labels_off":{"assigned":0,"id":"bus_vid_price_labels_off"},"bus_vid_price_labels_on":{"assigned":1,"id":"bus_vid_price_labels_on","versionedId":"bus_vid_price_labels_on_v02"}}},"cf_test_avia_main":{"id":"cf_test_avia_main","applied":0,"active":true,"forceVariant":0,"variants":{"CF-2358-avia_main_a":{"assigned":1,"id":"CF-2358-avia_main_a","versionedId":"CF-2358-avia_main_a"},"CF-2358-avia_main_b":{"assigned":0,"id":"CF-2358-avia_main_b"}}},"checkout_avia_7_android":{"id":"checkout_avia_7_android","applied":0,"active":true,"forceVariant":0,"variants":{"checkout_avia_7_android_off":{"assigned":0,"id":"checkout_avia_7_android_off"},"checkout_avia_7_android_on":{"assigned":1,"id":"checkout_avia_7_android_on","versionedId":"checkout_avia_7_android_on_v02"}}},"checkout_avia_8_ios":{"id":"checkout_avia_8_ios","applied":0,"active":true,"forceVariant":0,"variants":{"checkout_avia_8_ios_off":{"assigned":0,"id":"checkout_avia_8_ios_off"},"checkout_avia_8_ios_on":{"assigned":1,"id":"checkout_avia_8_ios_on","versionedId":"checkout_avia_8_ios_on_v01"}}},"checkout_avia_9_ios":{"id":"checkout_avia_9_ios","applied":0,"active":true,"forceVariant":0,"variants":{"checkout_avia_9_ios_off":{"assigned":0,"id":"checkout_avia_9_ios_off"},"checkout_avia_9_ios_on":{"assigned":1,"id":"checkout_avia_9_ios_on","versionedId":"checkout_avia_9_ios_on_v01"}}},"checkout_bus_1_android":{"id":"checkout_bus_1_android","applied":0,"active":true,"forceVariant":0,"variants":{"checkout_bus_1_android_off":{"assigned":0,"id":"checkout_bus_1_android_off"},"checkout_bus_1_android_on":{"assigned":1,"id":"checkout_bus_1_android_on","versionedId":"checkout_bus_1_android_on_v02"}}},"checkout_bus_1_ios":{"id":"checkout_bus_1_ios","applied":0,"active":true,"forceVariant":0,"variants":{"checkout_bus_1_ios_off":{"assigned":0,"id":"checkout_bus_1_ios_off"},"checkout_bus_1_ios_on":{"assigned":1,"id":"checkout_bus_1_ios_on","versionedId":"checkout_bus_1_ios_on_v02"}}},"checkout_voyager_suggester_ios":{"id":"checkout_voyager_suggester_ios","applied":0,"active":true,"forceVariant":0,"variants":{"checkout_voyager_suggester_ios_off":{"assigned":0,"id":"checkout_voyager_suggester_ios_off"},"checkout_voyager_suggester_ios_on":{"assigned":1,"id":"checkout_voyager_suggester_ios_on","versionedId":"checkout_voyager_suggester_ios_on_v01"}}},"dt_acceptance_test_alfa":{"id":"dt_acceptance_test_alfa","applied":0,"active":true,"forceVariant":0,"variants":{"dt_acceptance_test_alfa_off":{"assigned":0,"id":"dt_acceptance_test_alfa_off"},"dt_acceptance_test_alfa_on":{"assigned":1,"id":"dt_acceptance_test_alfa_on","versionedId":"dt_acceptance_test_alfa_on"}}},"dt_test_variative_router":{"id":"dt_test_variative_router","applied":0,"active":true,"forceVariant":0,"variants":{"dt_test_variative_router_a":{"assigned":1,"id":"dt_test_variative_router_a","versionedId":"dt_test_variative_router_a_v02"},"dt_test_variative_router_b":{"assigned":0,"id":"dt_test_variative_router_b"}}},"eco_wallet_bus_android":{"id":"eco_wallet_bus_android","applied":0,"active":true,"forceVariant":0,"variants":{"eco_wallet_bus_android_off":{"assigned":1,"id":"eco_wallet_bus_android_off","versionedId":"eco_wallet_bus_android_off_v01"},"eco_wallet_bus_android_on":{"assigned":0,"id":"eco_wallet_bus_android_on"}}},"eco_wallet_bus_ios":{"id":"eco_wallet_bus_ios","applied":0,"active":true,"forceVariant":0,"variants":{"eco_wallet_bus_ios_off":{"assigned":1,"id":"eco_wallet_bus_ios_off","versionedId":"eco_wallet_bus_ios_off_v01"},"eco_wallet_bus_ios_on":{"assigned":0,"id":"eco_wallet_bus_ios_on"}}},"eco_wallet_bus_web":{"id":"eco_wallet_bus_web","applied":0,"active":true,"forceVariant":0,"variants":{"eco_wallet_bus_web_off":{"assigned":0,"id":"eco_wallet_bus_web_off"},"eco_wallet_bus_web_on":{"assigned":1,"id":"eco_wallet_bus_web_on","versionedId":"eco_wallet_bus_web_on_v01"}}},"eco_wallet_hotels_android":{"id":"eco_wallet_hotels_android","applied":0,"active":true,"forceVariant":0,"variants":{"eco_wallet_hotels_android_off":{"assigned":0,"id":"eco_wallet_hotels_android_off"},"eco_wallet_hotels_android_on":{"assigned":1,"id":"eco_wallet_hotels_android_on","versionedId":"eco_wallet_hotels_android_on"}}},"eco_wallet_hotels_ios":{"id":"eco_wallet_hotels_ios","applied":0,"active":true,"forceVariant":0,"variants":{"eco_wallet_hotels_ios_off":{"assigned":1,"id":"eco_wallet_hotels_ios_off","versionedId":"eco_wallet_hotels_ios_off"},"eco_wallet_hotels_ios_on":{"assigned":0,"id":"eco_wallet_hotels_ios_on"}}},"eco_wallet_hotels_web":{"id":"eco_wallet_hotels_web","applied":0,"active":true,"forceVariant":0,"variants":{"eco_wallet_hotels_web_off":{"assigned":0,"id":"eco_wallet_hotels_web_off"},"eco_wallet_hotels_web_on":{"assigned":1,"id":"eco_wallet_hotels_web_on","versionedId":"eco_wallet_hotels_web_on_v01"}}},"etrain-1689_mobile_filters":{"id":"etrain-1689_mobile_filters","applied":0,"active":true,"forceVariant":0,"variants":{"etrain-1689_mobile_filters_new":{"assigned":1,"id":"etrain-1689_mobile_filters_new","versionedId":"etrain-1689_mobile_filters_new_v02"},"etrain-1689_mobile_filters_old":{"assigned":0,"id":"etrain-1689_mobile_filters_old"}}},"etrain-1737_mrasp_empty_date":{"id":"etrain-1737_mrasp_empty_date","applied":0,"active":true,"forceVariant":0,"variants":{"etrain-1737_mrasp_empty_date_new":{"assigned":1,"id":"etrain-1737_mrasp_empty_date_new","versionedId":"etrain-1737_mrasp_empty_date_new_v03"},"etrain-1737_mrasp_empty_date_old":{"assigned":0,"id":"etrain-1737_mrasp_empty_date_old"}}},"etrain-1895_sidebar":{"id":"etrain-1895_sidebar","applied":0,"active":true,"forceVariant":0,"variants":{"etrain-1895_sidebar_new":{"assigned":1,"id":"etrain-1895_sidebar_new","versionedId":"etrain-1895_sidebar_new"},"etrain-1895_sidebar_old":{"assigned":0,"id":"etrain-1895_sidebar_old"}}},"etrain-1928_mroute":{"id":"etrain-1928_mroute","applied":0,"active":true,"forceVariant":0,"variants":{"etrain-1928_mroute_new":{"assigned":1,"id":"etrain-1928_mroute_new","versionedId":"etrain-1928_mroute_new_v04"},"etrain-1928_mroute_old":{"assigned":0,"id":"etrain-1928_mroute_old"}}},"etrain-2073-occup-abc":{"id":"etrain-2073-occup-abc","applied":0,"active":true,"forceVariant":0,"variants":{"etrain-2073-occup-abc_off":{"assigned":0,"id":"etrain-2073-occup-abc_off"},"etrain-2073-occup-abc_on_link":{"assigned":1,"id":"etrain-2073-occup-abc_on_link","versionedId":"etrain-2073-occup-abc_on_link_v02"},"etrain-2073-occup-abc_on_popup":{"assigned":0,"id":"etrain-2073-occup-abc_on_popup"}}},"etrain-2076-schedule-aa-test":{"id":"etrain-2076-schedule-aa-test","applied":0,"active":true,"forceVariant":0,"variants":{"etrain-2076-schedule-aa-test_a":{"assigned":1,"id":"etrain-2076-schedule-aa-test_a","versionedId":"etrain-2076-schedule-aa-test_a_v06"},"etrain-2076-schedule-aa-test_b":{"assigned":0,"id":"etrain-2076-schedule-aa-test_b"}}},"etrain-2118_mobile_color":{"id":"etrain-2118_mobile_color","applied":0,"active":true,"forceVariant":0,"variants":{"etrain-2118_mobile_color_new":{"assigned":1,"id":"etrain-2118_mobile_color_new","versionedId":"etrain-2118_mobile_color_new_v04"},"etrain-2118_mobile_color_old":{"assigned":0,"id":"etrain-2118_mobile_color_old"}}},"etrain-2118_rasp_color":{"id":"etrain-2118_rasp_color","applied":0,"active":true,"forceVariant":0,"variants":{"etrain-2118_rasp_color_new":{"assigned":1,"id":"etrain-2118_rasp_color_new","versionedId":"etrain-2118_rasp_color_new_v03"},"etrain-2118_rasp_color_old":{"assigned":0,"id":"etrain-2118_rasp_color_old"}}},"etrain-2420_show_adriver":{"id":"etrain-2420_show_adriver","applied":0,"active":true,"forceVariant":0,"variants":{"etrain-2420_show_adriver_off":{"assigned":0,"id":"etrain-2420_show_adriver_off"},"etrain-2420_show_adriver_on":{"assigned":1,"id":"etrain-2420_show_adriver_on","versionedId":"etrain-2420_show_adriver_on_v05"}}},"etrain-3639_adtech_desktop":{"id":"etrain-3639_adtech_desktop","applied":0,"active":true,"forceVariant":0,"variants":{"etrain-3639_adtech_desktop_off":{"assigned":0,"id":"etrain-3639_adtech_desktop_off"},"etrain-3639_adtech_desktop_on":{"assigned":1,"id":"etrain-3639_adtech_desktop_on","versionedId":"etrain-3639_adtech_desktop_on_v08"}}},"etrain-3639_adtech_mobile":{"id":"etrain-3639_adtech_mobile","applied":0,"active":true,"forceVariant":0,"variants":{"etrain-3639_adtech_mobile_off":{"assigned":0,"id":"etrain-3639_adtech_mobile_off"},"etrain-3639_adtech_mobile_on":{"assigned":1,"id":"etrain-3639_adtech_mobile_on","versionedId":"etrain-3639_adtech_mobile_on_v07"}}},"etrain_app_benefits_main":{"id":"etrain_app_benefits_main","applied":0,"active":true,"forceVariant":0,"variants":{"etrain_app_benefits_main_control":{"assigned":1,"id":"etrain_app_benefits_main_control","versionedId":"etrain_app_benefits_main_control"},"etrain_app_benefits_main_enabled":{"assigned":0,"id":"etrain_app_benefits_main_enabled"}}},"etrain_app_benefits_schedule":{"id":"etrain_app_benefits_schedule","applied":0,"active":true,"forceVariant":0,"variants":{"etrain_app_benefits_schedule_control":{"assigned":0,"id":"etrain_app_benefits_schedule_control"},"etrain_app_benefits_schedule_enabled":{"assigned":1,"id":"etrain_app_benefits_schedule_enabled","versionedId":"etrain_app_benefits_schedule_enabled_v02"}}},"etrain_mobile_app_banners":{"id":"etrain_mobile_app_banners","applied":0,"active":true,"forceVariant":0,"variants":{"etrain_mobile_app_banners_app_icon":{"assigned":1,"id":"etrain_mobile_app_banners_app_icon","versionedId":"etrain_mobile_app_banners_app_icon_v01"},"etrain_mobile_app_banners_lady":{"assigned":0,"id":"etrain_mobile_app_banners_lady"},"etrain_mobile_app_banners_train":{"assigned":0,"id":"etrain_mobile_app_banners_train"}}},"etrain_mobile_footer_ads":{"id":"etrain_mobile_footer_ads","applied":0,"active":true,"forceVariant":0,"variants":{"etrain_mobile_footer_ads_first":{"assigned":0,"id":"etrain_mobile_footer_ads_first"},"etrain_mobile_footer_ads_second":{"assigned":1,"id":"etrain_mobile_footer_ads_second","versionedId":"etrain_mobile_footer_ads_second_v01"}}},"feed_hotels_map_selector_andr":{"id":"feed_hotels_map_selector_andr","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1740_hotels_map_slctr_fab":{"assigned":0,"id":"VID-1740_hotels_map_slctr_fab"},"VID-1740_hotels_map_slctr_hor":{"assigned":1,"id":"VID-1740_hotels_map_slctr_hor","versionedId":"VID-1740_hotels_map_slctr_hor_v01"},"VID-1740_hotels_map_slctr_pic":{"assigned":0,"id":"VID-1740_hotels_map_slctr_pic"}}},"feed_labels_bus_ios":{"id":"feed_labels_bus_ios","applied":0,"active":true,"forceVariant":0,"variants":{"feed_labels_bus_ios_off":{"assigned":1,"id":"feed_labels_bus_ios_off","versionedId":"feed_labels_bus_ios_off_v01"},"feed_labels_bus_ios_on":{"assigned":0,"id":"feed_labels_bus_ios_on"}}},"gladkikh_test":{"id":"gladkikh_test","applied":0,"active":true,"forceVariant":0,"variants":{"off1":{"assigned":0,"id":"off1"},"on1":{"assigned":1,"id":"on1","versionedId":"on1"}}},"hotels-review-web":{"id":"hotels-review-web","applied":0,"active":true,"forceVariant":0,"variants":{"hotels-review-web-new":{"assigned":1,"id":"hotels-review-web-new","versionedId":"hotels-review-web-new_v01"},"hotels-review-web-old":{"assigned":0,"id":"hotels-review-web-old"}}},"hotels_aa_campaign":{"id":"hotels_aa_campaign","applied":0,"active":true,"forceVariant":0,"variants":{"hotels_aa_campaign_a":{"assigned":1,"id":"hotels_aa_campaign_a","versionedId":"hotels_aa_campaign_a"},"hotels_aa_campaign_b":{"assigned":0,"id":"hotels_aa_campaign_b"}}},"hotels_details_redesign":{"id":"hotels_details_redesign","applied":0,"active":true,"forceVariant":0,"variants":{"hotels_details_redesign_off":{"assigned":1,"id":"hotels_details_redesign_off","versionedId":"hotels_details_redesign_off"},"hotels_details_redesign_on":{"assigned":0,"id":"hotels_details_redesign_on"}}},"hotels_details_shortcuts":{"id":"hotels_details_shortcuts","applied":0,"active":true,"forceVariant":0,"variants":{"HOTELS-4145_shortcuts_off":{"assigned":0,"id":"HOTELS-4145_shortcuts_off"},"HOTELS-4145_shortcuts_on":{"assigned":1,"id":"HOTELS-4145_shortcuts_on","versionedId":"HOTELS-4145_shortcuts_on"}}},"hotels_edit_stories":{"id":"hotels_edit_stories","applied":0,"active":true,"forceVariant":0,"variants":{"hotels_edit_stories_off":{"assigned":0,"id":"hotels_edit_stories_off"},"hotels_edit_stories_on":{"assigned":1,"id":"hotels_edit_stories_on","versionedId":"hotels_edit_stories_on_v01"}}},"hotels_payment_on_the_spot":{"id":"hotels_payment_on_the_spot","applied":0,"active":true,"forceVariant":0,"variants":{"hotels_payment_on_the_spot_off":{"assigned":0,"id":"hotels_payment_on_the_spot_off"},"hotels_payment_on_the_spot_on":{"assigned":1,"id":"hotels_payment_on_the_spot_on","versionedId":"hotels_payment_on_the_spot_on_v01"}}},"hotels_pay_later_android":{"id":"hotels_pay_later_android","applied":0,"active":true,"forceVariant":0,"variants":{"hotels_pay_later_android_off":{"assigned":0,"id":"hotels_pay_later_android_off"},"hotels_pay_later_android_on":{"assigned":1,"id":"hotels_pay_later_android_on","versionedId":"hotels_pay_later_android_on_v01"}}},"hotels_pay_later_web":{"id":"hotels_pay_later_web","applied":0,"active":true,"forceVariant":0,"variants":{"hotels_pay_later_web_off":{"assigned":0,"id":"hotels_pay_later_web_off"},"hotels_pay_later_web_on":{"assigned":1,"id":"hotels_pay_later_web_on","versionedId":"hotels_pay_later_web_on_v07"}}},"hotels_pricing_discount":{"id":"hotels_pricing_discount","applied":0,"active":true,"forceVariant":0,"variants":{"HOTELS-3881_without_discount":{"assigned":0,"id":"HOTELS-3881_without_discount"},"HOTELS-3881_with_discount":{"assigned":1,"id":"HOTELS-3881_with_discount","versionedId":"HOTELS-3881_with_discount_v01"}}},"hotels_pricing_ladder":{"id":"hotels_pricing_ladder","applied":0,"active":true,"forceVariant":0,"variants":{"hotels_pricing_ladder_off":{"assigned":0,"id":"hotels_pricing_ladder_off"},"hotels_pricing_ladder_on":{"assigned":1,"id":"hotels_pricing_ladder_on","versionedId":"hotels_pricing_ladder_on_v01"}}},"hotels_promocode":{"id":"hotels_promocode","applied":0,"active":true,"forceVariant":0,"variants":{"hotels_promocode_off":{"assigned":0,"id":"hotels_promocode_off"},"hotels_promocode_on":{"assigned":1,"id":"hotels_promocode_on","versionedId":"hotels_promocode_on_v04"}}},"hotels_recommended_two_models":{"id":"hotels_recommended_two_models","applied":0,"active":true,"forceVariant":0,"variants":{"hotels_recommended_two_models_1":{"assigned":1,"id":"hotels_recommended_two_models_1","versionedId":"hotels_recommended_two_models_1_v01"},"hotels_recommended_two_models_2":{"assigned":0,"id":"hotels_recommended_two_models_2"}}},"hotels_redesign_map":{"id":"hotels_redesign_map","applied":0,"active":true,"forceVariant":0,"variants":{"hotels_redesign_map_off":{"assigned":0,"id":"hotels_redesign_map_off"},"hotels_redesign_map_on":{"assigned":1,"id":"hotels_redesign_map_on","versionedId":"hotels_redesign_map_on_v03"}}},"hotels_use_feauture_store_bookings":{"id":"hotels_use_feauture_store_bookings","applied":0,"active":true,"forceVariant":0,"variants":{"hotels_use_feauture_store_bookings_off":{"assigned":0,"id":"hotels_use_feauture_store_bookings_off"},"hotels_use_feauture_store_bookings_on":{"assigned":1,"id":"hotels_use_feauture_store_bookings_on","versionedId":"hotels_use_feauture_store_bookings_on_v03"}}},"logo_2023_web":{"id":"logo_2023_web","applied":0,"active":true,"forceVariant":0,"variants":{"logo_2023_web_new":{"assigned":1,"id":"logo_2023_web_new","versionedId":"logo_2023_web_new_v01"},"logo_2023_web_old":{"assigned":0,"id":"logo_2023_web_old"}}},"main_hope_button":{"id":"main_hope_button","applied":0,"active":true,"forceVariant":0,"variants":{"main_hope_button_hope":{"assigned":1,"id":"main_hope_button_hope","versionedId":"main_hope_button_hope_v01"},"main_hope_button_map":{"assigned":0,"id":"main_hope_button_map"},"main_hope_button_status":{"assigned":0,"id":"main_hope_button_status"}}},"main_page_ae_tab_desktop":{"id":"main_page_ae_tab_desktop","applied":0,"active":true,"forceVariant":0,"variants":{"main_page_ae_tab_desktop_off":{"assigned":0,"id":"main_page_ae_tab_desktop_off"},"main_page_ae_tab_desktop_on":{"assigned":1,"id":"main_page_ae_tab_desktop_on","versionedId":"main_page_ae_tab_desktop_on_v03"}}},"main_page_ae_tab_mobile":{"id":"main_page_ae_tab_mobile","applied":0,"active":true,"forceVariant":0,"variants":{"main_page_ae_tab_mobile_off":{"assigned":0,"id":"main_page_ae_tab_mobile_off"},"main_page_ae_tab_mobile_on":{"assigned":1,"id":"main_page_ae_tab_mobile_on","versionedId":"main_page_ae_tab_mobile_on_v03"}}},"main_page_big_icon":{"id":"main_page_big_icon","applied":0,"active":true,"forceVariant":0,"variants":{"CF-3786_main_page_big_icon_off":{"assigned":0,"id":"CF-3786_main_page_big_icon_off"},"CF-3786_main_page_big_icon_on":{"assigned":1,"id":"CF-3786_main_page_big_icon_on","versionedId":"CF-3786_main_page_big_icon_on_v01"}}},"main_page_corporate_tab":{"id":"main_page_corporate_tab","applied":0,"active":true,"forceVariant":0,"variants":{"main_page_corporate_tab_off":{"assigned":0,"id":"main_page_corporate_tab_off"},"main_page_corporate_tab_on":{"assigned":1,"id":"main_page_corporate_tab_on","versionedId":"main_page_corporate_tab_on_v01"}}},"main_page_mb_hat_auth_simple":{"id":"main_page_mb_hat_auth_simple","applied":0,"active":true,"forceVariant":0,"variants":{"main_page_mb_hat_auth_simple_off":{"assigned":0,"id":"main_page_mb_hat_auth_simple_off"},"main_page_mb_hat_auth_simple_on":{"assigned":1,"id":"main_page_mb_hat_auth_simple_on","versionedId":"main_page_mb_hat_auth_simple_on_v01"}}},"main_ptt_popup":{"id":"main_ptt_popup","applied":0,"active":true,"forceVariant":0,"variants":{"main_ptt_popup_off":{"assigned":0,"id":"main_ptt_popup_off"},"main_ptt_popup_on":{"assigned":1,"id":"main_ptt_popup_on","versionedId":"main_ptt_popup_on_v01"}}},"main_ptt_popup_test":{"id":"main_ptt_popup_test","applied":0,"active":true,"forceVariant":0,"variants":{"main_ptt_popup_test_off":{"assigned":0,"id":"main_ptt_popup_test_off"},"main_ptt_popup_test_on":{"assigned":1,"id":"main_ptt_popup_test_on","versionedId":"main_ptt_popup_test_on"}}},"MAPP-5290_recommendation_avia":{"id":"MAPP-5290_recommendation_avia","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-5290_rec_avia":{"assigned":0,"id":"MAPP-5290_rec_avia"},"MAPP-5290_rec_nopush_avia":{"assigned":0,"id":"MAPP-5290_rec_nopush_avia"},"MAPP-5290_rec_static_avia":{"assigned":1,"id":"MAPP-5290_rec_static_avia","versionedId":"MAPP-5290_rec_static_avia"}}},"MAPP-5290_recommendation_train":{"id":"MAPP-5290_recommendation_train","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-5290_rec_nopush_train":{"assigned":0,"id":"MAPP-5290_rec_nopush_train"},"MAPP-5290_rec_static_train":{"assigned":0,"id":"MAPP-5290_rec_static_train"},"MAPP-5290_rec_train":{"assigned":1,"id":"MAPP-5290_rec_train","versionedId":"MAPP-5290_rec_train"}}},"MAPP-5942_viewed_hotels":{"id":"MAPP-5942_viewed_hotels","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-5942_viewed_hotels":{"assigned":0,"id":"MAPP-5942_viewed_hotels"},"MAPP-5942_viewed_hotels_nopush":{"assigned":1,"id":"MAPP-5942_viewed_hotels_nopush","versionedId":"MAPP-5942_viewed_hotels_nopush"}}},"MAPP-7241_tariffs_on_details":{"id":"MAPP-7241_tariffs_on_details","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-7241_tariffs_olds":{"assigned":0,"id":"MAPP-7241_tariffs_olds"},"MAPP-7241_tariff_expandable_cards":{"assigned":0,"id":"MAPP-7241_tariff_expandable_cards"},"MAPP-7241_tariff_scrollable_cards":{"assigned":1,"id":"MAPP-7241_tariff_scrollable_cards","versionedId":"MAPP-7241_tariff_scrollable_cards_v01"}}},"MAPP-7378_ios_tariffs_on_details":{"id":"MAPP-7378_ios_tariffs_on_details","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-7378_ios_tariffs_expandable_cards":{"assigned":0,"id":"MAPP-7378_ios_tariffs_expandable_cards"},"MAPP-7378_ios_tariffs_old":{"assigned":0,"id":"MAPP-7378_ios_tariffs_old"},"MAPP-7378_ios_tariffs_scrollable_cards":{"assigned":1,"id":"MAPP-7378_ios_tariffs_scrollable_cards","versionedId":"MAPP-7378_ios_tariffs_scrollable_cards"}}},"MAPP-logo_2023_android":{"id":"MAPP-logo_2023_android","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-logo_2023_android_new":{"assigned":1,"id":"MAPP-logo_2023_android_new","versionedId":"MAPP-logo_2023_android_new_v01"},"MAPP-logo_2023_android_old":{"assigned":0,"id":"MAPP-logo_2023_android_old"}}},"MAPP-logo_2023_ios":{"id":"MAPP-logo_2023_ios","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-logo_2023_ios_new":{"assigned":1,"id":"MAPP-logo_2023_ios_new","versionedId":"MAPP-logo_2023_ios_new_v01"},"MAPP-logo_2023_ios_old":{"assigned":0,"id":"MAPP-logo_2023_ios_old"}}},"martech_mainpage_geo_block":{"id":"martech_mainpage_geo_block","applied":0,"active":true,"forceVariant":0,"variants":{"MARTECH-24_geo":{"assigned":1,"id":"MARTECH-24_geo","versionedId":"MARTECH-24_geo_v01"},"MARTECH-24_stories":{"assigned":0,"id":"MARTECH-24_stories"}}},"mono_avia_android_ptt_banner":{"id":"mono_avia_android_ptt_banner","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-8013-android-ptt-hide-banner":{"assigned":0,"id":"MAPP-8013-android-ptt-hide-banner"},"MAPP-8013-android-ptt-show-banner":{"assigned":1,"id":"MAPP-8013-android-ptt-show-banner","versionedId":"MAPP-8013-android-ptt-show-banner_v02"}}},"mono_avia_ios_ptt_banner":{"id":"mono_avia_ios_ptt_banner","applied":0,"active":true,"forceVariant":0,"variants":{"MAPP-7932-ios-ptt-hide-banner":{"assigned":0,"id":"MAPP-7932-ios-ptt-hide-banner"},"MAPP-7932-ios-ptt-show-banner":{"assigned":1,"id":"MAPP-7932-ios-ptt-show-banner","versionedId":"MAPP-7932-ios-ptt-show-banner_v02"}}},"ptt_android_feed_hotels_favourites":{"id":"ptt_android_feed_hotels_favourites","applied":0,"active":true,"forceVariant":0,"variants":{"ptt_android_feed_hotels_favourites_off":{"assigned":0,"id":"ptt_android_feed_hotels_favourites_off"},"ptt_android_feed_hotels_favourites_on":{"assigned":1,"id":"ptt_android_feed_hotels_favourites_on","versionedId":"ptt_android_feed_hotels_favourites_on_v01"}}},"ptt_android_feed_hotels_new_rooms":{"id":"ptt_android_feed_hotels_new_rooms","applied":0,"active":true,"forceVariant":0,"variants":{"ptt_android_feed_hotels_new_rooms_off":{"assigned":1,"id":"ptt_android_feed_hotels_new_rooms_off","versionedId":"ptt_android_feed_hotels_new_rooms_off"},"ptt_android_feed_hotels_new_rooms_on":{"assigned":0,"id":"ptt_android_feed_hotels_new_rooms_on"}}},"ptt_android_feed_hotels_offers":{"id":"ptt_android_feed_hotels_offers","applied":0,"active":true,"forceVariant":0,"variants":{"ptt_android_feed_hotels_offers_off":{"assigned":0,"id":"ptt_android_feed_hotels_offers_off"},"ptt_android_feed_hotels_offers_on":{"assigned":1,"id":"ptt_android_feed_hotels_offers_on","versionedId":"ptt_android_feed_hotels_offers_on_v01"}}},"ptt_android_feed_mtp":{"id":"ptt_android_feed_mtp","applied":0,"active":true,"forceVariant":0,"variants":{"ptt_android_feed_mtp_off":{"assigned":0,"id":"ptt_android_feed_mtp_off"},"ptt_android_feed_mtp_on":{"assigned":1,"id":"ptt_android_feed_mtp_on","versionedId":"ptt_android_feed_mtp_on_v02"}}},"ptt_android_feed_train_price_calculation_for_child":{"id":"ptt_android_feed_train_price_calculation_for_child","applied":0,"active":true,"forceVariant":0,"variants":{"VID-3165_disable":{"assigned":0,"id":"VID-3165_disable"},"VID-3165_enable":{"assigned":1,"id":"VID-3165_enable","versionedId":"VID-3165_enable_v02"}}},"ptt_android_new_search_form_v3":{"id":"ptt_android_new_search_form_v3","applied":0,"active":true,"forceVariant":0,"variants":{"VID-3636_off":{"assigned":0,"id":"VID-3636_off"},"VID-3636_on":{"assigned":1,"id":"VID-3636_on","versionedId":"VID-3636_on_v01"}}},"ptt_android_search_tours":{"id":"ptt_android_search_tours","applied":0,"active":true,"forceVariant":0,"variants":{"VID-3505_off":{"assigned":0,"id":"VID-3505_off"},"VID-3505_on":{"assigned":1,"id":"VID-3505_on","versionedId":"VID-3505_on_v01"}}},"ptt_android_search_with_return":{"id":"ptt_android_search_with_return","applied":0,"active":true,"forceVariant":0,"variants":{"VID-3951_off":{"assigned":0,"id":"VID-3951_off"},"VID-3951_on":{"assigned":1,"id":"VID-3951_on","versionedId":"VID-3951_on"}}},"ptt_feed_cards_spacing_an2":{"id":"ptt_feed_cards_spacing_an2","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1764_cards_spacing_ab2_off":{"assigned":0,"id":"VID-1764_cards_spacing_ab2_off"},"VID-1764_cards_spacing_ab2_on":{"assigned":1,"id":"VID-1764_cards_spacing_ab2_on","versionedId":"VID-1764_cards_spacing_ab2_on_v01"}}},"ptt_feed_htl_fltrs_design_andr":{"id":"ptt_feed_htl_fltrs_design_andr","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1991_off":{"assigned":0,"id":"VID-1991_off"},"VID-1991_on":{"assigned":1,"id":"VID-1991_on","versionedId":"VID-1991_on_v01"}}},"ptt_feed_lazy_hotels_andr2":{"id":"ptt_feed_lazy_hotels_andr2","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1973_off":{"assigned":0,"id":"VID-1973_off"},"VID-1973_on":{"assigned":1,"id":"VID-1973_on","versionedId":"VID-1973_on_v01"}}},"ptt_feed_nearby_dates_andr3":{"id":"ptt_feed_nearby_dates_andr3","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1970_off":{"assigned":0,"id":"VID-1970_off"},"VID-1970_on":{"assigned":1,"id":"VID-1970_on","versionedId":"VID-1970_on_v01"}}},"ptt_feed_nearest_dates_ios_v2":{"id":"ptt_feed_nearest_dates_ios_v2","applied":0,"active":true,"forceVariant":0,"variants":{"VID-2063_dates_off":{"assigned":0,"id":"VID-2063_dates_off"},"VID-2063_dates_on":{"assigned":1,"id":"VID-2063_dates_on","versionedId":"VID-2063_dates_on_v02"}}},"ptt_hotels_checkout_skip_cart_an":{"id":"ptt_hotels_checkout_skip_cart_an","applied":0,"active":true,"forceVariant":0,"variants":{"HOTELS-3912_keep_cart":{"assigned":0,"id":"HOTELS-3912_keep_cart"},"HOTELS-3912_skip_cart":{"assigned":1,"id":"HOTELS-3912_skip_cart","versionedId":"HOTELS-3912_skip_cart"}}},"ptt_hotels_choose_rooms_an":{"id":"ptt_hotels_choose_rooms_an","applied":0,"active":true,"forceVariant":0,"variants":{"HOTELS-3218_new_choose_rooms":{"assigned":1,"id":"HOTELS-3218_new_choose_rooms","versionedId":"HOTELS-3218_new_choose_rooms"},"HOTELS-3218_old_choose_rooms":{"assigned":0,"id":"HOTELS-3218_old_choose_rooms"}}},"ptt_hotels_choose_rooms_ios":{"id":"ptt_hotels_choose_rooms_ios","applied":0,"active":true,"forceVariant":0,"variants":{"HOTELS-3132_new_choose_rooms":{"assigned":1,"id":"HOTELS-3132_new_choose_rooms","versionedId":"HOTELS-3132_new_choose_rooms"},"HOTELS-3132_old_choose_rooms":{"assigned":0,"id":"HOTELS-3132_old_choose_rooms"}}},"ptt_hotel_details_redesign":{"id":"ptt_hotel_details_redesign","applied":0,"active":true,"forceVariant":0,"variants":{"HOTELS-2815_redesign_off":{"assigned":0,"id":"HOTELS-2815_redesign_off"},"HOTELS-2815_redesign_on":{"assigned":1,"id":"HOTELS-2815_redesign_on","versionedId":"HOTELS-2815_redesign_on_v01"}}},"ptt_hotel_details_search_form_v2":{"id":"ptt_hotel_details_search_form_v2","applied":0,"active":true,"forceVariant":0,"variants":{"HOTELS-3154_search_form_off":{"assigned":0,"id":"HOTELS-3154_search_form_off"},"HOTELS-3154_search_form_on":{"assigned":1,"id":"HOTELS-3154_search_form_on","versionedId":"HOTELS-3154_search_form_on_v01"}}},"ptt_hotel_filters_design_ios":{"id":"ptt_hotel_filters_design_ios","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1993_new_design":{"assigned":1,"id":"VID-1993_new_design","versionedId":"VID-1993_new_design_v01"},"VID-1993_old_design":{"assigned":0,"id":"VID-1993_old_design"}}},"ptt_ios_feed_hotels_favourites":{"id":"ptt_ios_feed_hotels_favourites","applied":0,"active":true,"forceVariant":0,"variants":{"ptt_ios_feed_hotels_favourites_off":{"assigned":0,"id":"ptt_ios_feed_hotels_favourites_off"},"ptt_ios_feed_hotels_favourites_on":{"assigned":1,"id":"ptt_ios_feed_hotels_favourites_on","versionedId":"ptt_ios_feed_hotels_favourites_on_v01"}}},"ptt_ios_feed_hotels_new_rooms":{"id":"ptt_ios_feed_hotels_new_rooms","applied":0,"active":true,"forceVariant":0,"variants":{"ptt_ios_feed_hotels_new_rooms_off":{"assigned":0,"id":"ptt_ios_feed_hotels_new_rooms_off"},"ptt_ios_feed_hotels_new_rooms_on":{"assigned":1,"id":"ptt_ios_feed_hotels_new_rooms_on","versionedId":"ptt_ios_feed_hotels_new_rooms_on"}}},"ptt_ios_feed_hotels_offers":{"id":"ptt_ios_feed_hotels_offers","applied":0,"active":true,"forceVariant":0,"variants":{"ptt_ios_feed_hotels_offers_off":{"assigned":0,"id":"ptt_ios_feed_hotels_offers_off"},"ptt_ios_feed_hotels_offers_on":{"assigned":1,"id":"ptt_ios_feed_hotels_offers_on","versionedId":"ptt_ios_feed_hotels_offers_on_v01"}}},"ptt_ios_mtp_feed":{"id":"ptt_ios_mtp_feed","applied":0,"active":true,"forceVariant":0,"variants":{"ptt_ios_mtp_feed_off":{"assigned":0,"id":"ptt_ios_mtp_feed_off"},"ptt_ios_mtp_feed_on":{"assigned":1,"id":"ptt_ios_mtp_feed_on","versionedId":"ptt_ios_mtp_feed_on_v03"}}},"ptt_ios_not_selling_offers_in_filter":{"id":"ptt_ios_not_selling_offers_in_filter","applied":0,"active":true,"forceVariant":0,"variants":{"VID-3414_not_selling_in_filters":{"assigned":1,"id":"VID-3414_not_selling_in_filters","versionedId":"VID-3414_not_selling_in_filters_v01"},"VID-3414_only_selling_in_filters":{"assigned":0,"id":"VID-3414_only_selling_in_filters"}}},"ptt_ios_train_new_prices_for_kids":{"id":"ptt_ios_train_new_prices_for_kids","applied":0,"active":true,"forceVariant":0,"variants":{"VID-3146_prices_new":{"assigned":1,"id":"VID-3146_prices_new","versionedId":"VID-3146_prices_new_v02"},"VID-3146_prices_old":{"assigned":0,"id":"VID-3146_prices_old"}}},"ptt_map_selector_in_header_an":{"id":"ptt_map_selector_in_header_an","applied":0,"active":true,"forceVariant":0,"variants":{"VID-2255_default":{"assigned":0,"id":"VID-2255_default"},"VID-2255_in_header":{"assigned":1,"id":"VID-2255_in_header","versionedId":"VID-2255_in_header_v01"}}},"ptt_new_avia_offer_item_an":{"id":"ptt_new_avia_offer_item_an","applied":0,"active":true,"forceVariant":0,"variants":{"VID-2717_off":{"assigned":0,"id":"VID-2717_off"},"VID-2717_on":{"assigned":1,"id":"VID-2717_on","versionedId":"VID-2717_on_v01"}}},"ptt_new_bus_offer_item_an":{"id":"ptt_new_bus_offer_item_an","applied":0,"active":true,"forceVariant":0,"variants":{"VID-2591_off":{"assigned":0,"id":"VID-2591_off"},"VID-2591_on":{"assigned":1,"id":"VID-2591_on","versionedId":"VID-2591_on_v01"}}},"ptt_new_hotel_offer_item_an":{"id":"ptt_new_hotel_offer_item_an","applied":0,"active":true,"forceVariant":0,"variants":{"VID-2382_off":{"assigned":0,"id":"VID-2382_off"},"VID-2382_on":{"assigned":1,"id":"VID-2382_on","versionedId":"VID-2382_on_v01"}}},"ptt_new_train_offer_item_android2":{"id":"ptt_new_train_offer_item_android2","applied":0,"active":true,"forceVariant":0,"variants":{"VID-2870_new_horizontal2":{"assigned":1,"id":"VID-2870_new_horizontal2","versionedId":"VID-2870_new_horizontal2_v01"},"VID-2870_new_vertical2":{"assigned":0,"id":"VID-2870_new_vertical2"},"VID-2870_old2":{"assigned":0,"id":"VID-2870_old2"}}},"ptt_recomm_avia_offers_andr2":{"id":"ptt_recomm_avia_offers_andr2","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1889_2_off":{"assigned":0,"id":"VID-1889_2_off"},"VID-1889_2_on":{"assigned":1,"id":"VID-1889_2_on","versionedId":"VID-1889_2_on_v01"}}},"SEOTOOLS-309_geocontent_ptt_bann":{"id":"SEOTOOLS-309_geocontent_ptt_bann","applied":0,"active":true,"forceVariant":0,"variants":{"SEOTOOLS-309_without_banner":{"assigned":0,"id":"SEOTOOLS-309_without_banner"},"SEOTOOLS-309_with_banner":{"assigned":1,"id":"SEOTOOLS-309_with_banner","versionedId":"SEOTOOLS-309_with_banner"}}},"SF-545-recommendation-labels":{"id":"SF-545-recommendation-labels","applied":0,"active":true,"forceVariant":0,"variants":{"SF-545-recommendation-labels-off":{"assigned":0,"id":"SF-545-recommendation-labels-off"},"SF-545-recommendation-labels-on":{"assigned":1,"id":"SF-545-recommendation-labels-on","versionedId":"SF-545-recommendation-labels-on_v01"}}},"SF-615-details-price-diff":{"id":"SF-615-details-price-diff","applied":0,"active":true,"forceVariant":0,"variants":{"SF-615-details-price-diff-off":{"assigned":0,"id":"SF-615-details-price-diff-off"},"SF-615-details-price-diff-on":{"assigned":1,"id":"SF-615-details-price-diff-on","versionedId":"SF-615-details-price-diff-on_v01"}}},"sf_show_tariff_cabbin_luggage_info":{"id":"sf_show_tariff_cabbin_luggage_info","applied":0,"active":true,"forceVariant":0,"variants":{"sf_show_tariff_cabbin_luggage_info_hide":{"assigned":0,"id":"sf_show_tariff_cabbin_luggage_info_hide"},"sf_show_tariff_cabbin_luggage_info_show":{"assigned":1,"id":"sf_show_tariff_cabbin_luggage_info_show","versionedId":"sf_show_tariff_cabbin_luggage_info_show_v01"}}},"skip_details_bus_ios":{"id":"skip_details_bus_ios","applied":0,"active":true,"forceVariant":0,"variants":{"skip_details_bus_ios_off":{"assigned":0,"id":"skip_details_bus_ios_off"},"skip_details_bus_ios_on":{"assigned":1,"id":"skip_details_bus_ios_on","versionedId":"skip_details_bus_ios_on_v01"}}},"SPL-243-seats-s7-ios":{"id":"SPL-243-seats-s7-ios","applied":0,"active":true,"forceVariant":0,"variants":{"SPL-243-seats-s7-ios-off":{"assigned":0,"id":"SPL-243-seats-s7-ios-off"},"SPL-243-seats-s7-ios-on":{"assigned":1,"id":"SPL-243-seats-s7-ios-on","versionedId":"SPL-243-seats-s7-ios-on_v05"}}},"SPL-243-seats-s7-web":{"id":"SPL-243-seats-s7-web","applied":0,"active":true,"forceVariant":0,"variants":{"SPL-243-seats-s7-web-off":{"assigned":0,"id":"SPL-243-seats-s7-web-off"},"SPL-243-seats-s7-web-on":{"assigned":1,"id":"SPL-243-seats-s7-web-on","versionedId":"SPL-243-seats-s7-web-on_v04"}}},"SPL-428-s7_seats_prices":{"id":"SPL-428-s7_seats_prices","applied":0,"active":true,"forceVariant":0,"variants":{"SPL-428-s7_seats_prices-50":{"assigned":1,"id":"SPL-428-s7_seats_prices-50","versionedId":"SPL-428-s7_seats_prices-50_v01"},"SPL-428-s7_seats_prices-70":{"assigned":0,"id":"SPL-428-s7_seats_prices-70"},"SPL-428-s7_seats_prices-old":{"assigned":0,"id":"SPL-428-s7_seats_prices-old"}}},"SPL-445-upsale_texts_android":{"id":"SPL-445-upsale_texts_android","applied":0,"active":true,"forceVariant":0,"variants":{"SPL-445-upsale_texts_android_new":{"assigned":1,"id":"SPL-445-upsale_texts_android_new","versionedId":"SPL-445-upsale_texts_android_new_v01"},"SPL-445-upsale_texts_android_old":{"assigned":0,"id":"SPL-445-upsale_texts_android_old"}}},"SPL-445-upsale_texts_ios":{"id":"SPL-445-upsale_texts_ios","applied":0,"active":true,"forceVariant":0,"variants":{"SPL-445-upsale_texts_ios_new":{"assigned":1,"id":"SPL-445-upsale_texts_ios_new","versionedId":"SPL-445-upsale_texts_ios_new_v01"},"SPL-445-upsale_texts_ios_old":{"assigned":0,"id":"SPL-445-upsale_texts_ios_old"}}},"SPL-445-upsale_texts_web":{"id":"SPL-445-upsale_texts_web","applied":0,"active":true,"forceVariant":0,"variants":{"SPL-445-upsale_texts_web_new":{"assigned":1,"id":"SPL-445-upsale_texts_web_new","versionedId":"SPL-445-upsale_texts_web_new_v05"},"SPL-445-upsale_texts_web_old":{"assigned":0,"id":"SPL-445-upsale_texts_web_old"}}},"test_local_net_filter":{"id":"test_local_net_filter","applied":0,"active":true,"forceVariant":0,"variants":{"test_local_net_filter_off_a":{"assigned":1,"id":"test_local_net_filter_off_a","versionedId":"test_local_net_filter_off_a"},"test_local_net_filter_off_b":{"assigned":0,"id":"test_local_net_filter_off_b"}}},"tours_progressbar_buying":{"id":"tours_progressbar_buying","applied":0,"active":true,"forceVariant":0,"variants":{"tours_progressbar_buying_off":{"assigned":0,"id":"tours_progressbar_buying_off"},"tours_progressbar_buying_on":{"assigned":1,"id":"tours_progressbar_buying_on","versionedId":"tours_progressbar_buying_on_v03"}}},"tours_scenario_recommendation":{"id":"tours_scenario_recommendation","applied":0,"active":true,"forceVariant":0,"variants":{"tours_scenario_recommend_card":{"assigned":0,"id":"tours_scenario_recommend_card"},"tours_scenario_recommend_off":{"assigned":0,"id":"tours_scenario_recommend_off"},"tours_scenario_recommend_stamp":{"assigned":1,"id":"tours_scenario_recommend_stamp","versionedId":"tours_scenario_recommend_stamp_v04"},"tours_scenario_recommend_stat":{"assigned":0,"id":"tours_scenario_recommend_stat"}}},"tours_transfer_icon":{"id":"tours_transfer_icon","applied":0,"active":true,"forceVariant":0,"variants":{"tours_transfer_icon_hide":{"assigned":1,"id":"tours_transfer_icon_hide","versionedId":"tours_transfer_icon_hide_v02"},"tours_transfer_icon_new":{"assigned":0,"id":"tours_transfer_icon_new"},"tours_transfer_icon_old":{"assigned":0,"id":"tours_transfer_icon_old"}}},"tour_search_filter_question":{"id":"tour_search_filter_question","applied":0,"active":true,"forceVariant":0,"variants":{"tour_search_filter_question_off":{"assigned":0,"id":"tour_search_filter_question_off"},"tour_search_filter_question_on":{"assigned":1,"id":"tour_search_filter_question_on","versionedId":"tour_search_filter_question_on_v02"}}},"train_adaptive_main_zd":{"id":"train_adaptive_main_zd","applied":0,"active":true,"forceVariant":0,"variants":{"train_adaptive_main_zd_off":{"assigned":0,"id":"train_adaptive_main_zd_off"},"train_adaptive_main_zd_on":{"assigned":1,"id":"train_adaptive_main_zd_on","versionedId":"train_adaptive_main_zd_on_v05"}}},"train_android_scheme_v3":{"id":"train_android_scheme_v3","applied":0,"active":true,"forceVariant":0,"variants":{"train_android_scheme_v3_off":{"assigned":0,"id":"train_android_scheme_v3_off"},"train_android_scheme_v3_on":{"assigned":1,"id":"train_android_scheme_v3_on","versionedId":"train_android_scheme_v3_on_v02"}}},"train_autochoice4":{"id":"train_autochoice4","applied":0,"active":true,"forceVariant":0,"variants":{"train_autochoice4_filter":{"assigned":0,"id":"train_autochoice4_filter"},"train_autochoice4_off":{"assigned":0,"id":"train_autochoice4_off"},"train_autochoice4_old":{"assigned":0,"id":"train_autochoice4_old"},"train_autochoice4_rm_button":{"assigned":1,"id":"train_autochoice4_rm_button","versionedId":"train_autochoice4_rm_button_v01"},"train_autochoice4_single_button":{"assigned":0,"id":"train_autochoice4_single_button"}}},"train_autoticketing_new_wizard":{"id":"train_autoticketing_new_wizard","applied":0,"active":true,"forceVariant":0,"variants":{"train_autoticketing_new_wizard_off":{"assigned":0,"id":"train_autoticketing_new_wizard_off"},"train_autoticketing_new_wizard_on":{"assigned":1,"id":"train_autoticketing_new_wizard_on","versionedId":"train_autoticketing_new_wizard_on_v03"}}},"train_bu_pricing_adr":{"id":"train_bu_pricing_adr","applied":0,"active":true,"forceVariant":0,"variants":{"train_bu_pricing_adr_20220324":{"assigned":1,"id":"train_bu_pricing_adr_20220324","versionedId":"train_bu_pricing_adr_20220324_v02"},"train_bu_pricing_adr_20220607_dn":{"assigned":0,"id":"train_bu_pricing_adr_20220607_dn"},"train_bu_pricing_adr_20220607_up":{"assigned":0,"id":"train_bu_pricing_adr_20220607_up"},"train_bu_pricing_adr_off":{"assigned":0,"id":"train_bu_pricing_adr_off"}}},"train_bu_pricing_ios":{"id":"train_bu_pricing_ios","applied":0,"active":true,"forceVariant":0,"variants":{"train_bu_pricing_ios_20220324":{"assigned":1,"id":"train_bu_pricing_ios_20220324","versionedId":"train_bu_pricing_ios_20220324_v02"},"train_bu_pricing_ios_20220607_dn":{"assigned":0,"id":"train_bu_pricing_ios_20220607_dn"},"train_bu_pricing_ios_20220607_up":{"assigned":0,"id":"train_bu_pricing_ios_20220607_up"},"train_bu_pricing_ios_off":{"assigned":0,"id":"train_bu_pricing_ios_off"}}},"train_bu_pricing_web":{"id":"train_bu_pricing_web","applied":0,"active":true,"forceVariant":0,"variants":{"train_bu_pricing_web_20220324":{"assigned":1,"id":"train_bu_pricing_web_20220324","versionedId":"train_bu_pricing_web_20220324_v02"},"train_bu_pricing_web_20220607_dn":{"assigned":0,"id":"train_bu_pricing_web_20220607_dn"},"train_bu_pricing_web_20220607_up":{"assigned":0,"id":"train_bu_pricing_web_20220607_up"},"train_bu_pricing_web_anl_9819":{"assigned":0,"id":"train_bu_pricing_web_anl_9819"},"train_bu_pricing_web_off":{"assigned":0,"id":"train_bu_pricing_web_off"}}},"train_checkout_seats":{"id":"train_checkout_seats","applied":0,"active":true,"forceVariant":0,"variants":{"train_checkout_seats_off":{"assigned":0,"id":"train_checkout_seats_off"},"train_checkout_seats_on":{"assigned":1,"id":"train_checkout_seats_on","versionedId":"train_checkout_seats_on_v01"}}},"train_form_suggest_history":{"id":"train_form_suggest_history","applied":0,"active":true,"forceVariant":0,"variants":{"train_form_suggest_history_off":{"assigned":0,"id":"train_form_suggest_history_off"},"train_form_suggest_history_on":{"assigned":1,"id":"train_form_suggest_history_on","versionedId":"train_form_suggest_history_on_v01"}}},"train_insurance_description":{"id":"train_insurance_description","applied":0,"active":true,"forceVariant":0,"variants":{"train_insurance_desc_all":{"assigned":0,"id":"train_insurance_desc_all"},"train_insurance_desc_off":{"assigned":0,"id":"train_insurance_desc_off"},"train_insurance_desc_soft":{"assigned":1,"id":"train_insurance_desc_soft","versionedId":"train_insurance_desc_soft_v02"}}},"train_ios_scheme_v3":{"id":"train_ios_scheme_v3","applied":0,"active":true,"forceVariant":0,"variants":{"train_ios_scheme_v3_off":{"assigned":0,"id":"train_ios_scheme_v3_off"},"train_ios_scheme_v3_on":{"assigned":1,"id":"train_ios_scheme_v3_on","versionedId":"train_ios_scheme_v3_on_v01"}}},"train_main_ptt_banner":{"id":"train_main_ptt_banner","applied":0,"active":true,"forceVariant":0,"variants":{"train_main_ptt_banner_autochoose":{"assigned":0,"id":"train_main_ptt_banner_autochoose"},"train_main_ptt_banner_base":{"assigned":1,"id":"train_main_ptt_banner_base","versionedId":"train_main_ptt_banner_base_v01"},"train_main_ptt_banner_calendar":{"assigned":0,"id":"train_main_ptt_banner_calendar"},"train_main_ptt_banner_disabled":{"assigned":0,"id":"train_main_ptt_banner_disabled"},"train_main_ptt_banner_info_service":{"assigned":0,"id":"train_main_ptt_banner_info_service"},"train_main_ptt_banner_offline":{"assigned":0,"id":"train_main_ptt_banner_offline"},"train_main_ptt_banner_refund":{"assigned":0,"id":"train_main_ptt_banner_refund"}}},"train_mini_form_scroll":{"id":"train_mini_form_scroll","applied":0,"active":true,"forceVariant":0,"variants":{"train_mini_form_scroll_off":{"assigned":0,"id":"train_mini_form_scroll_off"},"train_mini_form_scroll_on":{"assigned":1,"id":"train_mini_form_scroll_on","versionedId":"train_mini_form_scroll_on_v01"}}},"train_mono_android_sales_closed_description":{"id":"train_mono_android_sales_closed_description","applied":0,"active":true,"forceVariant":0,"variants":{"train_mono_android_sales_closed_description_off":{"assigned":0,"id":"train_mono_android_sales_closed_description_off"},"train_mono_android_sales_closed_description_on":{"assigned":1,"id":"train_mono_android_sales_closed_description_on","versionedId":"train_mono_android_sales_closed_description_on_v01"}}},"train_mono_checkout_nevsky_android":{"id":"train_mono_checkout_nevsky_android","applied":0,"active":true,"forceVariant":0,"variants":{"train_mono_checkout_nevsky_android_off":{"assigned":0,"id":"train_mono_checkout_nevsky_android_off"},"train_mono_checkout_nevsky_android_on":{"assigned":1,"id":"train_mono_checkout_nevsky_android_on","versionedId":"train_mono_checkout_nevsky_android_on_v01"}}},"train_mono_ios_sales_closed_description":{"id":"train_mono_ios_sales_closed_description","applied":0,"active":true,"forceVariant":0,"variants":{"train_mono_ios_sales_closed_description_off":{"assigned":0,"id":"train_mono_ios_sales_closed_description_off"},"train_mono_ios_sales_closed_description_on":{"assigned":1,"id":"train_mono_ios_sales_closed_description_on","versionedId":"train_mono_ios_sales_closed_description_on_v02"}}},"train_mono_new_schedule_android":{"id":"train_mono_new_schedule_android","applied":0,"active":true,"forceVariant":0,"variants":{"train_mono_new_schedule_android_off":{"assigned":0,"id":"train_mono_new_schedule_android_off"},"train_mono_new_schedule_android_on":{"assigned":1,"id":"train_mono_new_schedule_android_on","versionedId":"train_mono_new_schedule_android_on_v05"}}},"train_mono_new_schedule_ios":{"id":"train_mono_new_schedule_ios","applied":0,"active":true,"forceVariant":0,"variants":{"train_mono_new_schedule_ios_off":{"assigned":0,"id":"train_mono_new_schedule_ios_off"},"train_mono_new_schedule_ios_on":{"assigned":1,"id":"train_mono_new_schedule_ios_on","versionedId":"train_mono_new_schedule_ios_on_v06"}}},"train_new_alfa_insurance_api":{"id":"train_new_alfa_insurance_api","applied":0,"active":true,"forceVariant":0,"variants":{"train_new_alfa_insurance_api_off":{"assigned":0,"id":"train_new_alfa_insurance_api_off"},"train_new_alfa_insurance_api_on":{"assigned":1,"id":"train_new_alfa_insurance_api_on","versionedId":"train_new_alfa_insurance_api_on_v02"}}},"train_passengers_rzd_bonus":{"id":"train_passengers_rzd_bonus","applied":0,"active":true,"forceVariant":0,"variants":{"train_passengers_rzd_bonus_off":{"assigned":0,"id":"train_passengers_rzd_bonus_off"},"train_passengers_rzd_bonus_on":{"assigned":1,"id":"train_passengers_rzd_bonus_on","versionedId":"train_passengers_rzd_bonus_on_v01"}}},"train_pricing_strategy":{"id":"train_pricing_strategy","applied":0,"active":true,"forceVariant":0,"variants":{"train_pricing_strategy_4438aid5":{"assigned":0,"id":"train_pricing_strategy_4438aid5"},"train_pricing_strategy_4438aii10":{"assigned":0,"id":"train_pricing_strategy_4438aii10"},"train_pricing_strategy_4438aii5":{"assigned":0,"id":"train_pricing_strategy_4438aii5"},"train_pricing_strategy_4438dc20":{"assigned":0,"id":"train_pricing_strategy_4438dc20"},"train_pricing_strategy_4438dc23":{"assigned":0,"id":"train_pricing_strategy_4438dc23"},"train_pricing_strategy_4438dd5":{"assigned":0,"id":"train_pricing_strategy_4438dd5"},"train_pricing_strategy_4438depth":{"assigned":0,"id":"train_pricing_strategy_4438depth"},"train_pricing_strategy_4438di10":{"assigned":0,"id":"train_pricing_strategy_4438di10"},"train_pricing_strategy_4438di5":{"assigned":0,"id":"train_pricing_strategy_4438di5"},"train_pricing_strategy_4438dwn10":{"assigned":0,"id":"train_pricing_strategy_4438dwn10"},"train_pricing_strategy_4438dwn4":{"assigned":0,"id":"train_pricing_strategy_4438dwn4"},"train_pricing_strategy_4438dwn5":{"assigned":0,"id":"train_pricing_strategy_4438dwn5"},"train_pricing_strategy_4438dwn8":{"assigned":0,"id":"train_pricing_strategy_4438dwn8"},"train_pricing_strategy_4438up10":{"assigned":1,"id":"train_pricing_strategy_4438up10","versionedId":"train_pricing_strategy_4438up10_v47"},"train_pricing_strategy_4438up4":{"assigned":0,"id":"train_pricing_strategy_4438up4"},"train_pricing_strategy_4438up5":{"assigned":0,"id":"train_pricing_strategy_4438up5"},"train_pricing_strategy_4438up8":{"assigned":0,"id":"train_pricing_strategy_4438up8"},"train_pricing_strategy_dc010":{"assigned":0,"id":"train_pricing_strategy_dc010"},"train_pricing_strategy_dc020":{"assigned":0,"id":"train_pricing_strategy_dc020"},"train_pricing_strategy_depth99":{"assigned":0,"id":"train_pricing_strategy_depth99"},"train_pricing_strategy_dep_1":{"assigned":0,"id":"train_pricing_strategy_dep_1"},"train_pricing_strategy_dep_2":{"assigned":0,"id":"train_pricing_strategy_dep_2"},"train_pricing_strategy_dm1000":{"assigned":0,"id":"train_pricing_strategy_dm1000"},"train_pricing_strategy_dm1433":{"assigned":0,"id":"train_pricing_strategy_dm1433"},"train_pricing_strategy_dm2421":{"assigned":0,"id":"train_pricing_strategy_dm2421"},"train_pricing_strategy_dm2701":{"assigned":0,"id":"train_pricing_strategy_dm2701"},"train_pricing_strategy_dm2805":{"assigned":0,"id":"train_pricing_strategy_dm2805"},"train_pricing_strategy_dm4014":{"assigned":0,"id":"train_pricing_strategy_dm4014"},"train_pricing_strategy_dm4304":{"assigned":0,"id":"train_pricing_strategy_dm4304"},"train_pricing_strategy_dm4438":{"assigned":0,"id":"train_pricing_strategy_dm4438"},"train_pricing_strategy_dm4438a":{"assigned":0,"id":"train_pricing_strategy_dm4438a"},"train_pricing_strategy_dm4438ai":{"assigned":0,"id":"train_pricing_strategy_dm4438ai"},"train_pricing_strategy_dm4804":{"assigned":0,"id":"train_pricing_strategy_dm4804"},"train_pricing_strategy_dm5129":{"assigned":0,"id":"train_pricing_strategy_dm5129"},"train_pricing_strategy_dm5399":{"assigned":0,"id":"train_pricing_strategy_dm5399"},"train_pricing_strategy_dm5643":{"assigned":0,"id":"train_pricing_strategy_dm5643"},"train_pricing_strategy_dm5761":{"assigned":0,"id":"train_pricing_strategy_dm5761"},"train_pricing_strategy_dm836":{"assigned":0,"id":"train_pricing_strategy_dm836"},"train_pricing_strategy_dm914":{"assigned":0,"id":"train_pricing_strategy_dm914"},"train_pricing_strategy_dmai02":{"assigned":0,"id":"train_pricing_strategy_dmai02"},"train_pricing_strategy_dmai04":{"assigned":0,"id":"train_pricing_strategy_dmai04"},"train_pricing_strategy_dp_min10":{"assigned":0,"id":"train_pricing_strategy_dp_min10"},"train_pricing_strategy_ic010":{"assigned":0,"id":"train_pricing_strategy_ic010"},"train_pricing_strategy_ic020":{"assigned":0,"id":"train_pricing_strategy_ic020"},"train_pricing_strategy_ic035":{"assigned":0,"id":"train_pricing_strategy_ic035"},"train_pricing_strategy_mnl99":{"assigned":0,"id":"train_pricing_strategy_mnl99"},"train_pricing_strategy_pelican":{"assigned":0,"id":"train_pricing_strategy_pelican"},"train_pricing_strategy_wide99":{"assigned":0,"id":"train_pricing_strategy_wide99"},"train_pricing_strategy_yaml":{"assigned":0,"id":"train_pricing_strategy_yaml"}}},"train_ptt_android_sales_closed_description":{"id":"train_ptt_android_sales_closed_description","applied":0,"active":true,"forceVariant":0,"variants":{"train_ptt_android_sales_closed_description_off":{"assigned":0,"id":"train_ptt_android_sales_closed_description_off"},"train_ptt_android_sales_closed_description_on":{"assigned":1,"id":"train_ptt_android_sales_closed_description_on","versionedId":"train_ptt_android_sales_closed_description_on_v03"}}},"train_ptt_autoticketing_android_v3":{"id":"train_ptt_autoticketing_android_v3","applied":0,"active":true,"forceVariant":0,"variants":{"train_ptt_autoticketing_android_v3_off":{"assigned":0,"id":"train_ptt_autoticketing_android_v3_off"},"train_ptt_autoticketing_android_v3_on":{"assigned":1,"id":"train_ptt_autoticketing_android_v3_on","versionedId":"train_ptt_autoticketing_android_v3_on_v02"}}},"train_ptt_autoticketing_ios_v3":{"id":"train_ptt_autoticketing_ios_v3","applied":0,"active":true,"forceVariant":0,"variants":{"train_ptt_autoticketing_ios_v3_off":{"assigned":0,"id":"train_ptt_autoticketing_ios_v3_off"},"train_ptt_autoticketing_ios_v3_on":{"assigned":1,"id":"train_ptt_autoticketing_ios_v3_on","versionedId":"train_ptt_autoticketing_ios_v3_on_v02"}}},"train_ptt_checkout_nevsky_android":{"id":"train_ptt_checkout_nevsky_android","applied":0,"active":true,"forceVariant":0,"variants":{"train_ptt_checkout_nevsky_android_off":{"assigned":0,"id":"train_ptt_checkout_nevsky_android_off"},"train_ptt_checkout_nevsky_android_on":{"assigned":1,"id":"train_ptt_checkout_nevsky_android_on","versionedId":"train_ptt_checkout_nevsky_android_on_v01"}}},"train_ptt_ios_sales_closed_description":{"id":"train_ptt_ios_sales_closed_description","applied":0,"active":true,"forceVariant":0,"variants":{"train_ptt_ios_sales_closed_description_off":{"assigned":0,"id":"train_ptt_ios_sales_closed_description_off"},"train_ptt_ios_sales_closed_description_on":{"assigned":1,"id":"train_ptt_ios_sales_closed_description_on","versionedId":"train_ptt_ios_sales_closed_description_on_v02"}}},"train_schedule_without_date_ptt_banner":{"id":"train_schedule_without_date_ptt_banner","applied":0,"active":true,"forceVariant":0,"variants":{"train_schedule_without_date_ptt_banner_autochoose":{"assigned":0,"id":"train_schedule_without_date_ptt_banner_autochoose"},"train_schedule_without_date_ptt_banner_booking_upsale":{"assigned":0,"id":"train_schedule_without_date_ptt_banner_booking_upsale"},"train_schedule_without_date_ptt_banner_calendar":{"assigned":1,"id":"train_schedule_without_date_ptt_banner_calendar","versionedId":"train_schedule_without_date_ptt_banner_calendar_v04"},"train_schedule_without_date_ptt_banner_disabled":{"assigned":0,"id":"train_schedule_without_date_ptt_banner_disabled"},"train_schedule_without_date_ptt_banner_info_service":{"assigned":0,"id":"train_schedule_without_date_ptt_banner_info_service"},"train_schedule_without_date_ptt_banner_offline":{"assigned":0,"id":"train_schedule_without_date_ptt_banner_offline"},"train_schedule_without_date_ptt_banner_promocode":{"assigned":0,"id":"train_schedule_without_date_ptt_banner_promocode"},"train_schedule_without_date_ptt_banner_refund":{"assigned":0,"id":"train_schedule_without_date_ptt_banner_refund"}}},"train_seo_pages_ptt_banner":{"id":"train_seo_pages_ptt_banner","applied":0,"active":true,"forceVariant":0,"variants":{"train_seo_pages_ptt_banner_off":{"assigned":0,"id":"train_seo_pages_ptt_banner_off"},"train_seo_pages_ptt_banner_on":{"assigned":1,"id":"train_seo_pages_ptt_banner_on","versionedId":"train_seo_pages_ptt_banner_on_v02"}}},"train_success_ptt_banner":{"id":"train_success_ptt_banner","applied":0,"active":true,"forceVariant":0,"variants":{"train_success_ptt_banner_calendar":{"assigned":0,"id":"train_success_ptt_banner_calendar"},"train_success_ptt_banner_disabled":{"assigned":0,"id":"train_success_ptt_banner_disabled"},"train_success_ptt_banner_info_service":{"assigned":0,"id":"train_success_ptt_banner_info_service"},"train_success_ptt_banner_offline":{"assigned":1,"id":"train_success_ptt_banner_offline","versionedId":"train_success_ptt_banner_offline_v02"},"train_success_ptt_banner_refund":{"assigned":0,"id":"train_success_ptt_banner_refund"}}},"train_swod_tag_desc":{"id":"train_swod_tag_desc","applied":0,"active":true,"forceVariant":0,"variants":{"train_swod_tag_desc_off":{"assigned":0,"id":"train_swod_tag_desc_off"},"train_swod_tag_desc_on":{"assigned":1,"id":"train_swod_tag_desc_on","versionedId":"train_swod_tag_desc_on_v01"}}},"train_vid_sales_closed_description":{"id":"train_vid_sales_closed_description","applied":0,"active":true,"forceVariant":0,"variants":{"train_vid_sales_closed_description_off":{"assigned":0,"id":"train_vid_sales_closed_description_off"},"train_vid_sales_closed_description_on":{"assigned":1,"id":"train_vid_sales_closed_description_on","versionedId":"train_vid_sales_closed_description_on_v01"}}},"train_wizard_b2b":{"id":"train_wizard_b2b","applied":0,"active":true,"forceVariant":0,"variants":{"train_wizard_b2b_hide":{"assigned":0,"id":"train_wizard_b2b_hide"},"train_wizard_b2b_show":{"assigned":1,"id":"train_wizard_b2b_show","versionedId":"train_wizard_b2b_show"}}},"train_wizard_company_payment":{"id":"train_wizard_company_payment","applied":0,"active":true,"forceVariant":0,"variants":{"train_wizard_company_payment_off":{"assigned":0,"id":"train_wizard_company_payment_off"},"train_wizard_company_payment_on":{"assigned":1,"id":"train_wizard_company_payment_on","versionedId":"train_wizard_company_payment_on_v01"}}},"train_wizard_google_pay":{"id":"train_wizard_google_pay","applied":0,"active":true,"forceVariant":0,"variants":{"train_wizard_google_pay_off":{"assigned":0,"id":"train_wizard_google_pay_off"},"train_wizard_google_pay_on":{"assigned":1,"id":"train_wizard_google_pay_on","versionedId":"train_wizard_google_pay_on_v01"}}},"train_wizard_redesign2":{"id":"train_wizard_redesign2","applied":0,"active":true,"forceVariant":0,"variants":{"train_wizard_redesign2_hide_sf":{"assigned":0,"id":"train_wizard_redesign2_hide_sf"},"train_wizard_redesign2_nocb":{"assigned":1,"id":"train_wizard_redesign2_nocb","versionedId":"train_wizard_redesign2_nocb_v02"},"train_wizard_redesign2_off":{"assigned":0,"id":"train_wizard_redesign2_off"},"train_wizard_redesign2_on":{"assigned":0,"id":"train_wizard_redesign2_on"}}},"USA-3847-checkout":{"id":"USA-3847-checkout","applied":0,"active":true,"forceVariant":0,"variants":{"USA-3847-new-checkout":{"assigned":1,"id":"USA-3847-new-checkout","versionedId":"USA-3847-new-checkout_v07"},"USA-3847-old-wizard":{"assigned":0,"id":"USA-3847-old-wizard"}}},"USA-4245-booking-upsales":{"id":"USA-4245-booking-upsales","applied":0,"active":true,"forceVariant":0,"variants":{"USA-4245-booking-upsale":{"assigned":0,"id":"USA-4245-booking-upsale"},"USA-4245-paylater":{"assigned":1,"id":"USA-4245-paylater","versionedId":"USA-4245-paylater_v03"}}},"VID-1807_remove_hotel_loading":{"id":"VID-1807_remove_hotel_loading","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1807_hotels_unload_off":{"assigned":0,"id":"VID-1807_hotels_unload_off"},"VID-1807_hotels_unload_on":{"assigned":1,"id":"VID-1807_hotels_unload_on","versionedId":"VID-1807_hotels_unload_on_v01"}}},"VID-1945_bronevik":{"id":"VID-1945_bronevik","applied":0,"active":true,"forceVariant":0,"variants":{"VID-1945_bronevik_off":{"assigned":0,"id":"VID-1945_bronevik_off"},"VID-1945_bronevik_on":{"assigned":1,"id":"VID-1945_bronevik_on","versionedId":"VID-1945_bronevik_on_v03"}}},"vid_avia_booking_results":{"id":"vid_avia_booking_results","applied":0,"active":true,"forceVariant":0,"variants":{"vid_avia_booking_results_off":{"assigned":0,"id":"vid_avia_booking_results_off"},"vid_avia_booking_results_on":{"assigned":1,"id":"vid_avia_booking_results_on","versionedId":"vid_avia_booking_results_on_v01"}}},"vid_avia_card_v2":{"id":"vid_avia_card_v2","applied":0,"active":true,"forceVariant":0,"variants":{"vid_avia_card_v2_off":{"assigned":0,"id":"vid_avia_card_v2_off"},"vid_avia_card_v2_on":{"assigned":1,"id":"vid_avia_card_v2_on","versionedId":"vid_avia_card_v2_on_v01"}}},"vid_avia_form_separate_date":{"id":"vid_avia_form_separate_date","applied":0,"active":true,"forceVariant":0,"variants":{"vid_avia_form_separate_date_off":{"assigned":0,"id":"vid_avia_form_separate_date_off"},"vid_avia_form_separate_date_on":{"assigned":1,"id":"vid_avia_form_separate_date_on","versionedId":"vid_avia_form_separate_date_on_v01"}}},"vid_avia_modal_bfr_wizard":{"id":"vid_avia_modal_bfr_wizard","applied":0,"active":true,"forceVariant":0,"variants":{"vid_avia_modal_bfr_wizard_off":{"assigned":0,"id":"vid_avia_modal_bfr_wizard_off"},"vid_avia_modal_bfr_wizard_on":{"assigned":1,"id":"vid_avia_modal_bfr_wizard_on","versionedId":"vid_avia_modal_bfr_wizard_on_v02"}}},"vid_bus_with_improves":{"id":"vid_bus_with_improves","applied":0,"active":true,"forceVariant":0,"variants":{"vid_bus_with_improves_off":{"assigned":0,"id":"vid_bus_with_improves_off"},"vid_bus_with_improves_on":{"assigned":1,"id":"vid_bus_with_improves_on","versionedId":"vid_bus_with_improves_on_v06"},"vid_bus_with_improves_withfeatur":{"assigned":0,"id":"vid_bus_with_improves_withfeatur"}}},"vid_hide_departed_trains":{"id":"vid_hide_departed_trains","applied":0,"active":true,"forceVariant":0,"variants":{"vid_hide_departed_trains_off":{"assigned":0,"id":"vid_hide_departed_trains_off"},"vid_hide_departed_trains_on":{"assigned":1,"id":"vid_hide_departed_trains_on","versionedId":"vid_hide_departed_trains_on_v01"}}},"vid_hotels_bronevik_offers":{"id":"vid_hotels_bronevik_offers","applied":0,"active":true,"forceVariant":0,"variants":{"vid_hotels_bronevik_offers_off":{"assigned":0,"id":"vid_hotels_bronevik_offers_off"},"vid_hotels_bronevik_offers_on":{"assigned":1,"id":"vid_hotels_bronevik_offers_on","versionedId":"vid_hotels_bronevik_offers_on_v06"}}},"vid_hotels_card_v2":{"id":"vid_hotels_card_v2","applied":0,"active":true,"forceVariant":0,"variants":{"vid_hotels_card_v2_off":{"assigned":0,"id":"vid_hotels_card_v2_off"},"vid_hotels_card_v2_on":{"assigned":1,"id":"vid_hotels_card_v2_on","versionedId":"vid_hotels_card_v2_on_v01"}}},"vid_hotels_sutochno":{"id":"vid_hotels_sutochno","applied":0,"active":true,"forceVariant":0,"variants":{"vid_hotels_sutochno_off":{"assigned":0,"id":"vid_hotels_sutochno_off"},"vid_hotels_sutochno_on":{"assigned":1,"id":"vid_hotels_sutochno_on","versionedId":"vid_hotels_sutochno_on_v03"}}},"vid_hotel_map_switch_visible":{"id":"vid_hotel_map_switch_visible","applied":0,"active":true,"forceVariant":0,"variants":{"vid_hotel_map_switch_visible_off":{"assigned":0,"id":"vid_hotel_map_switch_visible_off"},"vid_hotel_map_switch_visible_on":{"assigned":1,"id":"vid_hotel_map_switch_visible_on","versionedId":"vid_hotel_map_switch_visible_on_v01"}}},"vid_impr_unified_search":{"id":"vid_impr_unified_search","applied":0,"active":true,"forceVariant":0,"variants":{"vid_impr_unified_search_check":{"assigned":1,"id":"vid_impr_unified_search_check","versionedId":"vid_impr_unified_search_check_v03"},"vid_impr_unified_search_off":{"assigned":0,"id":"vid_impr_unified_search_off"},"vid_impr_unified_search_on":{"assigned":0,"id":"vid_impr_unified_search_on"}}},"vid_informers":{"id":"vid_informers","applied":0,"active":true,"forceVariant":0,"variants":{"vid_informers_off":{"assigned":0,"id":"vid_informers_off"},"vid_informers_on":{"assigned":1,"id":"vid_informers_on","versionedId":"vid_informers_on"}}},"vid_ptt_ad_train":{"id":"vid_ptt_ad_train","applied":0,"active":true,"forceVariant":0,"variants":{"vid_ptt_ad_train_off":{"assigned":0,"id":"vid_ptt_ad_train_off"},"vid_ptt_ad_train_on":{"assigned":1,"id":"vid_ptt_ad_train_on","versionedId":"vid_ptt_ad_train_on_v02"}}},"vid_simple_unified_search":{"id":"vid_simple_unified_search","applied":0,"active":true,"forceVariant":0,"variants":{"vid_simple_unified_search_off":{"assigned":0,"id":"vid_simple_unified_search_off"},"vid_simple_unified_search_on":{"assigned":1,"id":"vid_simple_unified_search_on","versionedId":"vid_simple_unified_search_on_v02"}}},"vid_sutochno_android":{"id":"vid_sutochno_android","applied":0,"active":true,"forceVariant":0,"variants":{"vid_sutochno_android_off":{"assigned":1,"id":"vid_sutochno_android_off","versionedId":"vid_sutochno_android_off"},"vid_sutochno_android_on":{"assigned":0,"id":"vid_sutochno_android_on"}}},"vid_sutochno_ios":{"id":"vid_sutochno_ios","applied":0,"active":true,"forceVariant":0,"variants":{"vid_sutochno_ios_off":{"assigned":1,"id":"vid_sutochno_ios_off","versionedId":"vid_sutochno_ios_off"},"vid_sutochno_ios_on":{"assigned":0,"id":"vid_sutochno_ios_on"}}},"vid_tours_promotion":{"id":"vid_tours_promotion","applied":0,"active":true,"forceVariant":0,"variants":{"vid_tours_promotion_off":{"assigned":0,"id":"vid_tours_promotion_off"},"vid_tours_promotion_on":{"assigned":1,"id":"vid_tours_promotion_on","versionedId":"vid_tours_promotion_on_v01"}}},"vid_train_card_v2":{"id":"vid_train_card_v2","applied":0,"active":true,"forceVariant":0,"variants":{"vid_train_card_v2_buttons":{"assigned":1,"id":"vid_train_card_v2_buttons","versionedId":"vid_train_card_v2_buttons_v01"},"vid_train_card_v2_off":{"assigned":0,"id":"vid_train_card_v2_off"},"vid_train_card_v2_table":{"assigned":0,"id":"vid_train_card_v2_table"}}},"vid_train_offers":{"id":"vid_train_offers","applied":0,"active":true,"forceVariant":0,"variants":{"vid_train_offers_new_feature":{"assigned":1,"id":"vid_train_offers_new_feature","versionedId":"vid_train_offers_new_feature_v07"},"vid_train_offers_off":{"assigned":0,"id":"vid_train_offers_off"},"vid_train_offers_on":{"assigned":0,"id":"vid_train_offers_on"}}},"vid_train_offers_sorting":{"id":"vid_train_offers_sorting","applied":0,"active":true,"forceVariant":0,"variants":{"vid_train_offers_sorting_off":{"assigned":0,"id":"vid_train_offers_sorting_off"},"vid_train_offers_sorting_on":{"assigned":1,"id":"vid_train_offers_sorting_on","versionedId":"vid_train_offers_sorting_on_v01"}}},"vid_train_othertransport":{"id":"vid_train_othertransport","applied":0,"active":true,"forceVariant":0,"variants":{"vid_train_othertransport_off":{"assigned":0,"id":"vid_train_othertransport_off"},"vid_train_othertransport_on":{"assigned":1,"id":"vid_train_othertransport_on","versionedId":"vid_train_othertransport_on_v03"},"vid_train_othertransport_without":{"assigned":0,"id":"vid_train_othertransport_without"}}},"vid_unified_search_form_tab_hotel":{"id":"vid_unified_search_form_tab_hotel","applied":0,"active":true,"forceVariant":0,"variants":{"vid_unified_search_form_tab_hotel_off":{"assigned":0,"id":"vid_unified_search_form_tab_hotel_off"},"vid_unified_search_form_tab_hotel_on":{"assigned":1,"id":"vid_unified_search_form_tab_hotel_on","versionedId":"vid_unified_search_form_tab_hotel_on_v02"}}},"web_main_middle_bdui_banner":{"id":"web_main_middle_bdui_banner","applied":0,"active":true,"forceVariant":0,"variants":{"web_main_middle_bdui_banner_off":{"assigned":0,"id":"web_main_middle_bdui_banner_off"},"web_main_middle_bdui_banner_on":{"assigned":1,"id":"web_main_middle_bdui_banner_on","versionedId":"web_main_middle_bdui_banner_on_v01"}}},"web_main_top_bdui_banner":{"id":"web_main_top_bdui_banner","applied":0,"active":true,"forceVariant":0,"variants":{"web_main_top_bdui_banner_off":{"assigned":0,"id":"web_main_top_bdui_banner_off"},"web_main_top_bdui_banner_on":{"assigned":1,"id":"web_main_top_bdui_banner_on","versionedId":"web_main_top_bdui_banner_on_v01"}}}},"sessionId":"7b230125-e5ca-4280-b49d-2f328a11d9ae"};var RM = RM || {}; RM.StaticData = RM.StaticData || {}; RM.StaticData["urlConfig"] = {"config":"config\/url.php","default-zone":"main","mobile_supported":"1","zone":{"main":{"common-domain":"tutu.ru","static-domain":"static.tu-tu.ru","default-subdomain":"www"},"ukraine":{"top-level-domain":"tutu.travel","common-domain":"ua.tutu.travel","static-domain":"static.tu-tu.ru","is-forbidden-subdomain":"1"},"belarus":{"top-level-domain":"tutu.travel","common-domain":"by.tutu.travel","static-domain":"static.tu-tu.ru","is-forbidden-subdomain":"1"},"english":{"common-domain":"tutu.travel","static-domain":"static.tu-tu.ru","default-subdomain":"www"}},"cache-enable":"1","host":"www.tutu.ru","https":1,"https_only":0};</script>
# <script src="https://cdn1.tu-tu.ru/scripts/build/url.js.983c40d97c7564bfe5c9ee77b3721ace11.js" charset="UTF-8"></script>

# <script src="https://cdn1.tu-tu.ru/js4/bld/lib/global.js.743fe0596402d430caa0d84732982c201.js" charset="UTF-8"></script>

# 	<script src="https://cdn1.tu-tu.ru/js4/vendors/rjs/require.js?v=2.1.15"></script>
# <script>require.config({baseUrl:"/js4/src",appDir:"",waitSeconds:30,paths:{widgets:"widgets",lib:"lib",trait:"trait",module:"module",template:"template",constant:"constant",legacy:"../legacy",trainStaticData:"app/train/data",vendors:"../vendors",Bloodhound:"../vendors/suggest/bloodhound.min",jquery:"../vendors/jq/1.10.2.min",lodash:"../vendors/lodash/3.9.3.min","lodash.assign":"../../../node_modules/lodash.assign/index","lodash.clone":"../../../node_modules/lodash.clone/index","lodash.isempty":"../../../node_modules/lodash.isempty/index",jqueryui:"../vendors/jq/ui.1.10.3.min",moment:"../vendors/jq/plugin/moment/min","moment-range":"../vendors/jq/plugin/moment/moment-range.min",momentRu:"../vendors/jq/plugin/moment/ru",text:"../vendors/rjs/plugin/text",twig:"../vendors/rjs/plugin/twig.min",twigjs:"../vendors/rjs/plugin/twigjs",json:"../vendors/rjs/plugin/json",backbone:"../vendors/backbone/backbone",react:"../vendors/react/14.8/react-with-addons.min","react-dom":"../vendors/react/14.8/react-dom.min","react-dom-server":"../vendors/react/14.8/react-dom-server.min",params:"empty:",logdata:"empty:",calendarParams:"empty:",php:"empty:",langLabels:"empty:",bemp:"reactjs/bemp",templates:"../../templates/twig","@tutu":"../../../node_modules/@tutu",qs:"../../../node_modules/qs/dist/qs",inputmask:"../../../node_modules/inputmask/dist/min/jquery.inputmask.bundle.min",superagent:"../../../node_modules/superagent/superagent",promise:"../../../node_modules/es6-promise/dist/es6-promise.min"},map:{"*":{underscore:"lodash","react/addons":"react"}},shim:{jqueryui:{exports:"$.ui"},typeahead:["jquery"]},config:{twigjs:{autoescape:!1}}});</script>


# <script>
# 	window.langLabels = {"bemp.blocks.train.form.main.error_blank_station":"Пожалуйста, укажите название станции","bemp.blocks.train.form.main.alertNoDepartureDate":"Пожалуйста, укажите дату поездки","bemp.blocks.train.form.calendar.today":"сегодня","bemp.blocks.train.form.calendar.title":"Календарь","train.interval.save":"Сохранить","bemp.blocks.train.form.main.back":"Обратно","common.default_popup_text_wrong":"Поле заполнено некорректно","datepicker.close":"Закрыть","datepicker.prev":"&#x3c;Пред","datepicker.next":"След&#x3e;","datepicker.current":"Сегодня","datepicker.today":"Сегодня","datepicker.tomorrow":"Завтра","datepicker.afterTomorrow":"Послезавтра","list.month.1":"Январь","list.month.10":"Октябрь","list.month.11":"Ноябрь","list.month.12":"Декабрь","list.month.2":"Февраль","list.month.3":"Март","list.month.4":"Апрель","list.month.5":"Май","list.month.6":"Июнь","list.month.7":"Июль","list.month.8":"Август","list.month.9":"Сентябрь","list.month_s.1":"Янв","list.month_s.10":"Окт","list.month_s.11":"Нояб","list.month_s.12":"Дек","list.month_s.2":"Фев","list.month_s.3":"Мар","list.month_s.4":"Апр","list.month_s.5":"Май","list.month_s.6":"Июнь","list.month_s.7":"Июль","list.month_s.8":"Авг","list.month_s.9":"Сен","list.weekdays.0":"воскресенье","list.weekdays.1":"понедельник","list.weekdays.2":"вторник","list.weekdays.3":"среда","list.weekdays.4":"четверг","list.weekdays.5":"пятница","list.weekdays.6":"суббота","list.weekdays_mid.0":"вск","list.weekdays_mid.1":"пнд","list.weekdays_mid.2":"втр","list.weekdays_mid.3":"срд","list.weekdays_mid.4":"чтв","list.weekdays_mid.5":"птн","list.weekdays_mid.6":"сбт","list.week_days.0":"Вс","list.week_days.1":"Пн","list.week_days.2":"Вт","list.week_days.3":"Ср","list.week_days.4":"Чт","list.week_days.5":"Пт","list.week_days.6":"Сб"};
# 	window.LOCALE = "rus";
# 	window.NLOCALE = "ru";
# 	window.phpCrossDomainParams = { 'origin': '', 'path': '' };
# </script>

# <script src="https://cdn1.tu-tu.ru/static/train/js/commons.dll.js.9d39deb3b03461d2fb37d968e6632e651.js" charset="UTF-8"></script>
# <script src="https://cdn1.tu-tu.ru/static/train/js/desktop/vokzalList.rus.bundle.js.53eba74dd79807362fb56a56129549811.js" charset="UTF-8"></script>
# <script>
# 	(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["desktop/vokzalList.eng"],{}]);
# </script>
# <script src="https://cdn1.tu-tu.ru/static/train/js/desktop/vokzalList.bundle.js.952057ee11557afb6087b1e6a5fe05b41.js" charset="UTF-8"></script>
	
# </body>
# </html>

# '''
# #print(html)

# soup = BeautifulSoup(html, "lxml")
# #print(soup)
# ar = soup.find_all('a', {"class": "b-train--vokzal_list--links__link"})
# for el in ar:
#     print(el.text)

import json

data = {}
with open('data.json', 'r', encoding='utf8') as file:
    data = json.load(file)
station_names = ['Абакан',
'Абдулино',
'Агрыз',
'Адлер',
'Аксаково',
'Алейская',
'Анапа',
'Ангарск',
'Анжерская',
'Арзамас-1',
'Арзамас-2',
'Армавир-1',
'Армавир-2',
'Арсеньев',
'Архангельск',
'Архара',
'Астрахань',
'Аткарск',
'Ачинск',
'Аша',
'Аэровокзальный Комплекс Адлер',
'Балаково',
'Балашов',
'Балтийский Вокзал',
'Барабинск',
'Барнаул',
'Бахчисарай',
'Белая Калитва',
'Белгород',
'Белово',
'Белогорск',
'Белорецк',
'Белореченская',
'Белорусский Вокзал',
'Бердяуш',
'Березники',
'Бийск',
'Бикин',
'Бира',
'Биробиджан',
'Благовещенск',
'Боготол',
'Богоявленск',
'Болотное',
'Борзя',
'Борисоглебск',
'Брянск - Орловский',
'Бугульма',
'Бузулук',
'Буй',
'Бурея',
'Валуйки',
'Ванино',
'Великие Луки',
'Великий Устюг',
'Вельск',
'Верхний Баскунчак',
'Верхний Уфалей',
'Веселое',
'Витебский Вокзал',
'Вихоревка',
'Владивосток',
'Владикавказ',
'Владимир',
'Волгоград',
'Волгодонская',
'Волжский',
'Вологда',
'Волховстрой-1',
'Воркута',
'Воронеж I',
'Восточный',
'Выборг',
'Вяземский',
'Вязовая',
'Галич',
'Георгиевск',
'Глазов',
'Горячий Ключ',
'Гродеково',
'Грозный',
'Грязи-Воронежские',
'Гудермес',
'Дальнереченск',
'Данилов',
'Дербент',
'Джанкой',
'Дзержинск',
'Димитровград',
'Ейск',
'Екатеринбург',
'Елец',
'Ершов',
'Ессентуки',
'Жигулевское Море',
'Забайкальск',
'Завитая',
'Залари',
'Заозерная',
'Заринская',
'Зверево',
'Зеленый Дол',
'Зима',
'Златоуст',
'Зубова Поляна',
'Иваново',
'Ижевск',
'Инза',
'Инская',
'Инта',
'Иркутск-Пассажирский',
'Иркутск-Сортировочный',
'Исакогорка',
'Исилькуль',
'Искитим',
'Йошкар-Ола',
'Кавказская',
'Казанский Вокзал',
'Казань',
'Калачинская',
'Калининград-Южный',
'Калуга-1',
'Каменск-Уральский',
'Каменская',
'Камень-На-Оби',
'Камышлов',
'Канаш',
'Канск-Енисейский',
'Карасук-1',
'Каргат',
'Карталы',
'Карымская',
'Кемерово',
'Керчь (Основной)',
'Керчь-Южная',
'Киевский Вокзал',
'Кизляр',
'Кинель',
'Кинешма',
'Киров',
'Кирсанов',
'Киселевск',
'Кисловодск',
'Княжпогост',
'Ковров',
'Когалым',
'Комсомольск-На-Амуре',
'Коноша',
'Коршуниха',
'Кострома',
'Котельниково',
'Котельнич',
'Котлас-Южный',
'Краснодар-1',
'Красноуфимск',
'Красноярск',
'Кропачево',
'Крымская',
'Кузнецк',
'Кулунда',
'Купино',
'Курган',
'Курганная',
'Курск',
'Курский Вокзал',
'Ладожский Вокзал',
'Лазаревская',
'Лев Толстой',
'Лена',
'Ленинградский Вокзал',
'Ленинск-Кузнецкий',
'Липецк',
'Лиски',
'Лихая',
'Лоо',
'Магдагачи',
'Магнитогорск',
'Майкоп',
'Мамоново',
'Мантурово',
'Мариинск',
'Махачкала',
'Междуреченск',
'Миасс',
'Микунь',
'Миллерово',
'Минеральные Воды',
'Мичуринск-Уральский',
'Могоча',
'Московский Вокзал',
'Мошково',
'Мурманск',
'Муром',
'Набережные Челны',
'Навашино',
'Называевская',
'Нальчик',
'Наушки',
'Невинномысск',
'Нерюнгри',
'Нестеров',
'Нижнекамск',
'Нижнеудинск',
'Нижний Новгород',
'Нижний Тагил',
'Никель',
'Новая Чара',
'Новгород',
'Новокузнецк',
'Новокуйбышевская',
'Новороссийск',
'Новосибирск-Восточный',
'Новосибирск-Главный',
'Новосибирск-Западный',
'Новосибирск-Южный',
'Новотроицк',
'Новочеркасск',
'Новый Ургал',
'Ноябрьск-1',
'Ноябрьск-2',
'Нурлат',
'Няндома',
'Облучье',
'Озинки',
'Олимпийский Парк',
'Омск',
'Орел',
'Оренбург',
'Орск',
'Павелецкий Вокзал',
'Падунские Пороги',
'Пенза-1',
'Первоуральск',
'Пермь-2',
'Петров Вал',
'Петровский Завод',
'Петрозаводск',
'Печора',
'Плесецкая',
'Поворино',
'Потьма',
'Прокопьевск',
'Прохладная',
'Псков',
'Пыть-Ях',
'Пятигорск',
'Раненбург',
'Ревда',
'Рижский Вокзал',
'Роза Хутор',
'Россошь',
'Ростов-Главный',
'Ростов-Ярославский',
'Ртищево',
'Рубцовск',
'Ружино',
'Рузаевка',
'Рыбинск',
'Рязань-1',
'Рязань-2',
'Савеловский Вокзал',
'Саки',
'Салават',
'Сальск',
'Самара',
'Саранск',
'Сарапул',
'Саратов-1',
'Свободный',
'Севастополь',
'Северобайкальск',
'Северодвинск',
'Сергач',
'Сердобск',
'Серов',
'Сибай',
'Сибирцево',
'Симферополь',
'Сковородино',
'Славгород',
'Слюдянка',
'Смоленск',
'Сосногорск',
'Сочи',
'Спасск-Дальний',
'Ставрополь',
'Станция Айвазовская',
'Станция Владиславовка',
'Станция Евпатория-Курорт',
'Станция Инкерман-1',
'Станция Красноперекопск',
'Станция Семь Колодезей',
'Станция Чистополье',
'Староминская',
'Старый Оскол',
'Стерлитамак',
'Сургут',
'Сызрань-1',
'Сызрань-Город',
'Сыктывкар',
'Таганрог',
'Тайга',
'Тайшет',
'Таксимо',
'Таловая',
'Тамбов',
'Татарская',
'Тверь',
'Тимашевская',
'Тихоокеанская',
'Тихорецкая',
'Тобольск',
'Тогучин',
'Тольятти',
'Томск',
'Тоннельная',
'Топки',
'Троицк',
'Туапсе',
'Туймазы',
'Тула',
'Тулун',
'Тында',
'Тюмень',
'Улан-Удэ',
'Ульяновск-Центральный',
'Урбах',
'Урюпинск',
'Усинск',
'Усолье-Сибирское',
'Уссурийск',
'Усть-Илимск',
'Усть-Катав',
'Уфа',
'Ухта',
'Феодосия',
'Финляндский Вокзал',
'Фролово',
'Хабаровск-1',
'Хасан',
'Хоста',
'Чаны',
'Чапаевск',
'Чебоксары',
'Челябинск',
'Черемхово',
'Черепаново',
'Череповец',
'Черкесск',
'Чертково',
'Чита-2',
'Чулымская',
'Шадринск',
'Шарья',
'Шахтная',
'Шахунья',
'Шепси',
'Шилка',
'Шимановская',
'Шумерля',
'Шумиха',
'Эсто-Садок',
'Юрга-1',
'Янаул',
'Ярославль-Главный',
'Ярославль-Московский',
'Ярославский Вокзал',]

station_set = set(station_names)

print(len(station_names))
print(len(station_set))
#res = {}
query = "INSERT INTO stations (code, name, region, settlement, transport_type, priority) VALUES "
countries = data.get('countries')
for country in countries:
    
    regions = country.get('regions')
    if country.get('title') == 'Россия':
        for region in regions:
            
            region_title = region.get('title')
            region_title.replace(',', '')
            #res[region_title] = {}
            settlements = region.get('settlements')
            for settlement in settlements:
                settlement_title = settlement.get('title')
                settlement_title.replace(',', '')
                #res[region_title][settlement_title] = {}
                stations = settlement.get('stations')
                for station in stations:
                    t = station.get('transport_type')
                    
                    if t == 'train' or t == 'suburban':
                        title = station.get('title')
                        title.replace(',', '')
                        #if title in station_set:
                        query += f"('{station.get('codes').get('yandex_code')}', '{title}', '{region_title}', '{settlement_title}', '{t}', 1),"
                        #print(f"{title} {t} {station.get('station_type')}")
                        # elif t=='suburban':
                        #     print(title)

#print(query)
with open("res.txt", "w", encoding="utf8") as file:
    file.write(query)
