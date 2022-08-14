#!/user/bin/python
import requests
import json
from datetime import datetime
from dateutil import tz

# setup local timezone information, preset is "auto-detect"
from_zone = tz.tzutc()
to_zone = tz.tzlocal()

# uncomment to set manually timezones
# from_zone = tz.gettz('UTC')
# to_zone = tz.gettz('America/New_York')

current_hour = int(datetime.now().strftime("%H"))

# input lat/long info for api call
lat = "47.6062"
long = "-122.3321"
url = f"https://api.sunrise-sunset.org/json?lat={lat}&lng={long}&formatted=0"


def calculate_greeting(sunrise, sunset, current_time):
	if current_time >= sunset:
		return(" Evening")
	elif current_time >= sunrise and current_time < 12:
		return(" Morning")
	elif current_time >= 12:
		return(" Afternoon")
	else:
		return(" Evening")

def api_call():
	response = requests.get(url, verify=False).text
	response_json = json.loads(response)
	return(response_json)
	
	
def sunrise(results):
	sunrise = results['results']['sunrise']
	sunrise_parse = datetime.strptime(sunrise, "%Y-%m-%d" + "T" + "%H:%M:%S" + "+00:00")
	utc = sunrise_parse.replace(tzinfo=from_zone)
	adjusted_sunrise = utc.astimezone(to_zone)
	return(int(adjusted_sunrise.hour))


def sunset(results):
	sunset = results['results']['sunset']
	sunset_parse = datetime.strptime(sunset, "%Y-%m-%d" + "T" + "%H:%M:%S" + "+00:00")
	utc = sunset_parse.replace(tzinfo=from_zone)
	adjusted_sunset = utc.astimezone(to_zone)
	return(int(adjusted_sunset.hour))
	

def main():
	results = api_call()
	sunrise_time = sunrise(results)
	sunset_time	= sunset(results)
	print(calculate_greeting(sunrise_time, sunset_time, current_hour))



if __name__ == '__main__':
	main()


