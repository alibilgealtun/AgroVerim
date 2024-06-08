document.getElementById('cityForm').addEventListener('submit', function(event) {
    event.preventDefault();
    let city = document.getElementById('city').value;
    fetch('/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `city=${encodeURIComponent(city)}`
    })
    .then(response => response.json())
    .then(data => {
        let recommendationsDiv = document.getElementById('recommendations');
        recommendationsDiv.innerHTML = '';
        
        // Display recommendations
        let recommendationsText = data.recommendations.join(', '); // Join recommendations with comma
        let recommendationsElement = document.createElement('p');
        recommendationsElement.textContent = recommendationsText;
        recommendationsDiv.appendChild(recommendationsElement);

        // Display air quality
        let airQualityDiv = document.createElement('div');
        airQualityDiv.textContent = `Hava Değerleri: PM2.5 - ${data.air_quality.pm2_5}, PM10 - ${data.air_quality.pm10}, O3 - ${data.air_quality.o3}, NO2 - ${data.air_quality.no2}`;
        recommendationsDiv.appendChild(airQualityDiv);
        
        // Display temperature
        let temperatureDiv = document.createElement('div');
        temperatureDiv.textContent = `Yıllık Sıcaklık Ortalaması: ${data.temperature}°C`;
        recommendationsDiv.appendChild(temperatureDiv);
    })
    .catch(error => console.error('Error:', error));
});
