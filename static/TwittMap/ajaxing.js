var searchKeyword;
var locations;
var markers=[];

function initMap() {
        var uluru = {lat: 20, lng: -30};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 3,
          center: uluru
        });
        var marker = new google.maps.Marker({
          position: uluru,
          map: map
        });
        var selectedword=getElementById("KeyWords");
        searchKeyword=selectedword.options[selectedword.selectedIndex].value;
        console.log();
}