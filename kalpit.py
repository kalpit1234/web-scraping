import os
import serpapi
from dotenv import load_dotenv
import pandas as pd
mobile_number=[]
SERP_API_KEY='6aef7b9d52284b4636fb58dfa191ca28f2440e43ff33bd4e822f64e86304998a'
load_dotenv()
api_key=os.getenv('SERP_API_KEY')
client=serpapi.Client(api_key=api_key)
search_query = 'e-mitra Shajapur	'
location =    'Shajapur	,India'
result=client.search({
    'engine':'google_maps',
    'type':'search',
    'q':search_query,
    'location':location
    
})
print(result)
mobile_address = []

for place in result['local_results']:
    if 'phone' in place:
        mobile_address.append(place['phone'])
    if 'address' in place:
        mobile_number.append(place['address'])    
        

print(mobile_address)
print(mobile_number)

if mobile_address:
    df = pd.DataFrame({'address': mobile_number,"phone":mobile_address})
    df.to_csv('mapsscraper.csv', index=False)
    print("CSV file created successfully.")
else:
    print("No mobile numbers found.")
