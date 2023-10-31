import requests
import pandas as pd
import json

# Membaca file CSV
df = pd.read_csv('alamat_tps.csv') #file CSV berisi alamat dari setiap TPS 

# Membaca API key dari config.json
with open('config.json') as f:
    config = json.load(f)
api_key = config['api_key']

# Menggunakan geocoding API dari MapBox
base_url = 'https://api.mapbox.com/geocoding/v5/mapbox.places/'

queries = df.iloc[:, 1]
for query in queries:
    # Konstruksi API URL
    url = f'{base_url}{query}.json?access_token={api_key}'
    
    # Membuat API request
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        longitude, latitude = data['features'][0]['geometry']['coordinates']
        print(f'Query: {query}, Latitude: {latitude}, Longitude: {longitude}')
    else:
        print(f'Error for query "{query}": {response.status_code}')
