import os
import requests
from crewai import Agent
from dotenv import load_dotenv

load_dotenv()

class WeatherAgent:
    def __init__(self):
        self.agent = Agent(
            name="Weather Expert",
            role="Weather Analyst",
            goal="Provide accurate weather forecasts for any country.",
            backstory="A weather forecasting expert with years of experience."
        )
        self.weather_api_url = os.getenv("WEATHER_API_URL")
        self.geo_api_url = os.getenv("GEO_API_URL")

    def get_lat_lon(self, country):
        """Fetch latitude and longitude for a given country using geocoding API"""
        params = {"name": country, "count": 1, "language": "en", "format": "json"}
        response = requests.get(self.geo_api_url, params=params)

        if response.status_code == 200:
            data = response.json()
            if "results" in data and data["results"]:
                return data["results"][0]["latitude"], data["results"][0]["longitude"]
        return None, None  # Return None if no data found

    def get_weather(self, country):
        lat, lon = self.get_lat_lon(country)
        if lat is None or lon is None:
            return f"⚠️ Sorry, I couldn't find the weather for {country}. Try another country."

        params = {
            "latitude": lat,
            "longitude": lon,
            "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
            "timezone": "auto"
        }
        response = requests.get(self.weather_api_url, params=params)

        if response.status_code == 200 and response.text.strip():
            data = response.json()
            return (
                f"🌦️ **Weather in {country}**:\n"
                f"☀️ Max Temp: {data['daily']['temperature_2m_max'][0]}°C\n"
                f"❄️ Min Temp: {data['daily']['temperature_2m_min'][0]}°C\n"
                f"🌧️ Precipitation: {data['daily']['precipitation_sum'][0]}mm"
            )
        return "⚠️ Error: Weather API returned an empty response."

