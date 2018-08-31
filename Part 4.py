__author__ = 'Dreyke Boone'

import json, requests, sys

if len(sys.argv) < 2:
    print('Usage: Your current location')
    sys.exit()
location = ' '.join(sys.argv[1:])

url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=97008bf3b4cfcef070a25f4a88118a68' % (location)
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)

w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])