######
# To run in Python3:
# python3 -m pip install pytz
# python3 -m pip install requests
# Should also run in Default Python 2.7!
######
import requests
import datetime
import time
import pytz

while True:

   r = requests.get('https://cloud.iexapis.com/stable/stock/pd/quote/latestPrice?token=XXXXXXXXXXXXXXXXXXX)
   sharePrice = float(r.content)

   now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)

   headers = {'Content-Type': 'application/json', 'Authorization': "Token token=YOUTTOKEN"}
   payload = {'observation': {'value': None, 'observed_at': None}}

   url = "https://api.pagerduty.com/business_impact_metrics/PU9EIJS/observations"

   payload['observation']['value'] = sharePrice
   payload['observation']['observed_at'] = now.isoformat()

   print(payload)
              
   r = requests.post(url, json=payload, headers=headers)
   r.raise_for_status()
   print("  Sent observation: " + str(r.json()['observation']['observed_at']) + " Value: " +  str(r.json()['observation']['value']))
   time.sleep(50)
