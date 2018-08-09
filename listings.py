# This script pulls JSON listing data from the Coin Market Cap Listing API and displays it in the console.
# Written by Pavon Dunbar using Python v3.7.0 on Aug 9, 2018.

import json
import requests

listing_url = 'https://api.coinmarketcap.com/v2/listings/'

request = requests.get(listing_url)
results = request.json()

# print(json.dumps(results, sort_keys=True, indent=4))

data = results['data']
for currency in data:
    rank = currency['id']
    name = currency['name']
    symbol = currency['symbol']
    print(str(rank) + ': ' + name + ' (' + symbol + ')')
