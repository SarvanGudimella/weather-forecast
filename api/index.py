from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__, template_folder="../templates")

API_KEY = os.environ.get("d25d7f54b706acec2c89459c2a1508b3")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error_message = None

    if request.method == "POST":
        city = request.form.get("city")
        if not city:
            error_message = "Please enter a city name"
        else:
            params = {"q": city, "appid": API_KEY, "units": "metric"}
            response = requests.get(BASE_URL, params=params)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                error_message = f"City '{city}' not found or API error."

    return render_template("index.html", weather_data=weather_data, error=error_message)
