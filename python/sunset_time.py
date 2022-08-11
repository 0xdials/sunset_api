#!/user/bin/python
import requests
from datetime import datetime, tzinfo
import pytz

lat = "47.6062"
long = "-122.3321"

url = f"https://api.sunrise-sunset.org/json?lat={lat}&lng={long}&formatted=0"

def api_call():

	response = requests.get(url, verify=False)
	print(response.json('sunrise'))


api_call()