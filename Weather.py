import streamlit as st

st.title("Weather App")
st.write("Welcome to the weather app!")

import requests

# Replace with your actual API key
OPENWEATHER_API_KEY = '013958d1bff87faf90802a49ec85ff56'

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric'
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        weather_data = response.json()
        
        result = {
            'name': weather_data['name'],
            'temp': f"{weather_data['main']['temp']}°C",
            'weather': weather_data['weather'][0]['description'],
            'humidity': f"{weather_data['main']['humidity']}%",
            'wind_speed': f"{weather_data['wind']['speed']} m/s"
        }
    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': f"HTTP error occurred: {http_err}"}), 500
    except Exception as err:
        return jsonify({'error': f"Other error occurred: {err}"}), 500

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
