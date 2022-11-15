ymaps.ready(init);

function init() {
    // Создаем выпадающую панель с поисковыми подсказками и прикрепляем ее к HTML-элементу по его id.
    var suggestViewOfLocation = new ymaps.SuggestView('suggest', {results: 4, boundedBy: [[55, 36], [56, 38]]});

    var suggestViewOfUndergorundStation = new ymaps.SuggestView('underground_station', {provider: provider, results: 4});

    const find = document.getElementById('formelement_place_next');
    find.addEventListener( "click", () => {
        const suggest = document.getElementById('suggest');

        ymaps.geocode(suggest.value, { results : 1 }).then(function (res) {

            return ymaps.geocode(res.geoObjects.get(0).geometry.getCoordinates(), { kind: 'district', results: 1 });
    
        }).then(function (res) {
    
            const result = res.geoObjects.get(0).properties.getAll();
            const district = result.text;
            const place_to_save = document.getElementById("suggest");
            place_to_save.value = district;
            console.log(district);
    
        });
    });




}
