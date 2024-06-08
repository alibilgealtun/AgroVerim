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
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
