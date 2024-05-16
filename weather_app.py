import requests
import json
import os
try:
    city = input("Enter the name of the city: ")

    url = f"http://api.weatherapi.com/v1/current.json?key=cbcb21eaf00f461baa980911241505&q={city}&aqi=no"

    r = requests.get(url)

    wdic = json.loads(r.text)

    c = (f"Current temperature in {wdic['location']['name']} is: {wdic['current']['temp_c']}°C\nFeels like {wdic['current']['feelslike_c']}°C")

    f = (f"Current temperature in {wdic['location']['name']} is: {wdic['current']['temp_f']}°F\nFeels like {wdic['current']['feelslike_f']}°F")

    print(f"Local date and time is: {wdic['location']['localtime']}")
    print(c)
    print(f)
except KeyError as e:
    print(e,"Enter a valid location name.")