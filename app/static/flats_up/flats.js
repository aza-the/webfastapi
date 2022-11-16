console.log("FLATS.JS started");

// function that scrolls to obj_scrollto smoothly
function scroll_to(obj_scrollto){
    obj_scrollto.scrollIntoView({behavior: "smooth", block: "center", inline: "nearest"});
}

let changed_obj;

// function that makes the font bigger and brighter
function hihglight_obj(obj){
    changed_obj.style.fontSize = "1.4em";  // should return to the original size of .sidenav a (styles.css file) font size
    changed_obj.style.color = "#cdcdcd";  // should return to the original color of .sidenav a (styles.css file) color
    obj.style.fontSize = "1.7em";
    obj.style.color = "#ffffff";
    changed_obj = obj;
}


const formelement_about = document.getElementById("formelement_about");
const about = document.getElementById("about");
about.style.fontSize = "1.7em";
about.style.color = "#ffffff";
changed_obj = about;
about.addEventListener("click", () => {
    scroll_to(formelement_about);
    hihglight_obj(about);
}); 


const formelement_place = document.getElementById("formelement_place");
const place = document.getElementById("place");
place.addEventListener("click", () => {
    scroll_to(formelement_place);
    hihglight_obj(place);
}); 

const formelement_underground = document.getElementById("formelement_underground");
const underground = document.getElementById("underground");
underground.addEventListener("click", () => {
    scroll_to(formelement_underground);
    hihglight_obj(underground);
}); 

const formelement_about_flat = document.getElementById("formelement_about_flat");
const about_flat = document.getElementById("about_flat");
about_flat.addEventListener("click", () => {
    scroll_to(formelement_about_flat);
    hihglight_obj(about_flat);
}); 

const formelement_about_building = document.getElementById("formelement_about_building");
const about_building = document.getElementById("about_building");
about_building.addEventListener("click", () => {
    scroll_to(formelement_about_building);
    hihglight_obj(about_building);
}); 

const formelement_walls = document.getElementById("formelement_walls");
const walls = document.getElementById("walls");
walls.addEventListener("click", () => {
    scroll_to(formelement_walls);
    hihglight_obj(walls);
}); 



// next buttons

const formelement_about_next = document.getElementById("formelement_about_next");
formelement_about_next.addEventListener("click", () => {
    scroll_to(formelement_place);
    hihglight_obj(place);
}); 

const formelement_place_next = document.getElementById("formelement_place_next");
formelement_place_next.addEventListener("click", () => {
    scroll_to(formelement_underground);
    hihglight_obj(underground);
}); 

const formelement_underground_next = document.getElementById("formelement_underground_next");
formelement_underground_next.addEventListener("click", () => {
    scroll_to(formelement_about_flat);
    hihglight_obj(about_flat);
}); 

const formelement_about_flat_next = document.getElementById("formelement_about_flat_next");
formelement_about_flat_next.addEventListener("click", () => {
    scroll_to(formelement_about_building);
    hihglight_obj(about_building);
}); 

const formelement_about_building_next = document.getElementById("formelement_about_building_next");
formelement_about_building_next.addEventListener("click", () => {
    scroll_to(formelement_walls);
    hihglight_obj(walls);
}); 





// IMG RADIO BUTTON 
let uncheck_undergorund;
function unhighlight_check_img(){
    if(uncheck_undergorund){
        uncheck_undergorund.style.height = "100px";
        uncheck_undergorund.style.width = "100px";
    }
}

function highlight_check_img(obj) {
    unhighlight_check_img()
    obj.style.height = "120px";
    obj.style.width = "120px";
    uncheck_undergorund = obj;
}

const by_foot_radio = document.getElementById("by_foot_radio");
const by_foot_img = document.getElementById("by_foot_img");
by_foot_img.addEventListener("click", () => { highlight_check_img(by_foot_img) });
by_foot_radio.addEventListener("click", () => { highlight_check_img(by_foot_img) });

const by_transport_radio = document.getElementById("by_transport_radio");
const by_transport_img = document.getElementById("by_transport_img");
by_transport_img.addEventListener("click", () => { highlight_check_img(by_transport_img) });
by_transport_radio.addEventListener("click", () => { highlight_check_img(by_transport_img) });
