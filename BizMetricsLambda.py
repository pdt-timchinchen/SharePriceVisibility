import json
from botocore.vendored import requests
import datetime
import time
import dateutil.tz

def lambda_handler(event, context):

   r = requests.get('https://cloud.iexapis.com/stable/stock/pd/quote/latestPrice?token=XXXXXXXXXXXXXXXXXXXX')
   sharePrice = float(r.content)

   utc = dateutil.tz.gettz('UTC')
   now = datetime.datetime.now(tz=utc)
  
   headers = {'Content-Type': 'application/json', 'Authorization': "Token token=YOURTOKEN"}
   payload = {'observation': {'value': None, 'observed_at': None}}
  
   url = "https://api.pagerduty.com/business_impact_metrics/PU9EIJS/observations"
  
   payload['observation']['value'] = sharePrice
   payload['observation']['observed_at'] = now.isoformat()
  
   print(payload)
            
   r = requests.post(url, json=payload, headers=headers)
   r.raise_for_status()
   print("  Sent observation: " + str(r.json()['observation']['observed_at']) + " Value: " +  str(r.json()['observation']['value']))
  
   return {
       'statusCode': 200,
       'body': json.dumps('Share Price updated:' + str(sharePrice) + ' at ' + now.isoformat())
