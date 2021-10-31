const API_KEY = 'dd0e4a79194c92a2d50ebf990138ec69';

function onGeoOk(position){
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;
    const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`
    fetch(url).then(response => response.json()).then(data => {
        const weather = document.querySelector('.temp span');
        const city = document.querySelector('.city');
        city.innerText = data.name;
        weather.innerText = `${data.main.temp}º`
    });
}
function onGeoError(){
    alert("Can't find you. No weather for you.");
}

navigator.geolocation.getCurrentPosition(onGeoOk, onGeoError)



