from flask import Flask, render_template, request, jsonify
from main import get_all_data, recommend_crops
from city import get_lat_lon
from crop_profile import crop_profiles as cp

app = Flask(__name__, '/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    city = request.form['city']
    lat, lon = get_lat_lon(city, None)
    all_data = get_all_data(lat, lon)
    recommendations = recommend_crops(all_data, cp)
                                      
    air_quality = all_data['air_quality']
    temperature = all_data['climate_data']['temperature']
    
    response = {
        'recommendations': recommendations,
        'air_quality': air_quality,
        'temperature': temperature
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
