ymaps.ready(init);

function init() {
    const infodiv = document.getElementById('infodiv')

    // Создаем выпадающую панель с поисковыми подсказками и прикрепляем ее к HTML-элементу по его id.
    var suggestViewOfLocation = new ymaps.SuggestView('suggest', {results: 4, boundedBy: [[55, 36], [56, 38]]});

    var suggestViewOfUndergorundStation = new ymaps.SuggestView('underground_station', {provider: provider, results: 4});

    function create_h2(text){
        const element = document.createElement("h2");
        element.innerText = text;
        element.style.textAlign = "right";
        element.style.fontFamily = "monospace";
        element.style.fontSize = "1em";
        element.style.color = "#ffffff";

        return element;
    }

    function create_p(text){
        const element = document.createElement("p");
        element.innerText = text;
        element.style.textAlign = "right";
        element.style.fontFamily = "monospace";
        element.style.fontSize = "0.6em";
        element.style.color = "#ffffff";
    }

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
            
            const location = create_p(district);

            infodiv.appendChild(location);

        });
    });




}
