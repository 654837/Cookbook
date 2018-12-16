#!/usr/bin/env python3

import requests
import datetime

price_url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
data = requests.get(price_url).json()
price_in_usd = data['bpi']['USD']['rate']

time = datetime.datetime.now()
print("It is " + time.strftime("%X") + " and Bitcoin price is currently at $" + price_in_usd + " USD")
