import requests
import json

limit = 500
days = 365

url = f'https://eonet.gsfc.nasa.gov/api/v3/events/geojson?limit={limit}&days={days}'
events_data = requests.get(url).json()

# event_list = events_data['events']  alte V2.1
event_list = events_data['features']  # neue V3.0
with open('eventsV3.json', 'w') as f:
    f.write(json.dumps(events_data, indent=4))

for event in event_list:
    if 'fire' in str(event['properties']): 
        print(event['properties']['title'] ,' Koordinaten: ', event['geometry']['coordinates'])
        