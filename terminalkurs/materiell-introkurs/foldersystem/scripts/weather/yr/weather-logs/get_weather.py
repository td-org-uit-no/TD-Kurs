import json
from datetime import datetime
import urllib.request

def get_request(url: str,
                user_agent = "Mozilla/5.0 (platform; rv:gecko-version) Gecko/gecko-trail Firefox/firefox-version"):
    request = urllib.request.Request(url, headers={
                'User-Agent': user_agent
    })

    try:
        with urllib.request.urlopen(request) as response:
            data = response.read().decode("utf-8")  # Read and decode response
    except urllib.error.HTTPError as e:
        raise ConnectionError(f"HTTP Error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        raise ConnectionError(f"URL Error: {e.reason}")

    return data

def ExtractOutsideTemperature(url: str):
    try:
        response = get_request(url)
    except Exception as e:
        print(f'Failed to get weather data! {e}')
        return []
    
    data = json.loads(response)
    data = data['properties']['timeseries']

    currentHour = datetime.now().replace(minute=0, second=0, microsecond=0)

    temperatures = []
    for entry in data:
        # Parse the time string into a datetime object
        time = datetime.strptime(entry['time'], "%Y-%m-%dT%H:%M:%SZ")

        # Only add data from current time and forwards
        if time >= currentHour:
            temperatures.append(entry['data']['instant']['details']['air_temperature'])

    return temperatures

def print_temperatures(temperatures: list):
    for temp in temperatures:
        print(f"{temp} Celsius")

tempratures = ExtractOutsideTemperature("https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=59.93&lon=10.72&altitude=90")
print_temperatures(tempratures)
