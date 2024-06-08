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
    .then(recommendations => {
        let recommendationsDiv = document.getElementById('recommendations');
        recommendationsDiv.innerHTML = '';
        recommendations.forEach(crop => {
            let cropElement = document.createElement('p');
            cropElement.textContent = crop;
            recommendationsDiv.appendChild(cropElement);
        });
    })
    .catch(error => console.error('Error:', error));
});