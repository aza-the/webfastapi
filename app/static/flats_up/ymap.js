var myMap;

// Дождёмся загрузки API и готовности DOM.
ymaps.ready(init);

function init () {

    $('#formelement_about_building_find_out').bind({
        click: function () {
            myMap = new ymaps.Map('map', {
                center: [55.76, 37.64], // Новосибирск
                zoom: 10
            }, {
                searchControlProvider: 'yandex#search'
            });
        }
    });

}