import requests
import json

limit = 500
days = 365

url = f'https://eonet.gsfc.nasa.gov/api/v2.1/events?limit={limit}&days={days}'
events_data = requests.get(url).json()
event_list = events_data['events']
 
with open('events.json', 'w') as f:
    f.write(json.dumps(events_data, indent=4))

for event in event_list:
    if 'fire' in str(event['categories']):
        print(event['title'])
