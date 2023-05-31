#!/usr/bin/env python

import requests
import requests
from requests.structures import CaseInsensitiveDict
import json
import time
import csv

# Ask user for the API secret of the company asking for affiliate updating
api_secret = str(input("Enter API secret: "))
pause = int(input("How many seconds to pause? "))

# Initialize URL request variables
api_key = (api_secret,"")

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

# Open CSV file, indicate the file name as the first argument of the open function
with open('filename.csv', mode="r", encoding="utf-8-sig") as affiliate_id:
    affiliates = csv.reader(affiliate_id)
    list_affiliate = list(affiliates)

affiliate_count = 0

# Iterate through the list of affiliate IDs.
for affiliate in list_affiliate:
    url = "https://api.getrewardful.com/v1/affiliates/" + affiliate[0]
    # Add the API endpoint parameters
    data = {
       "campaign_id": ""
    }

    resp = requests.put(url, headers=headers, data=data, auth=api_key)
    status = resp.status_code
    
    # Print server response of each request
    if status == 200:
        print("Affiliate transferred to new campaign: " + affiliate[0])
        affiliate_count += 1

    else:
        print("Affiliate not transferred to new campaign: " + affiliate[0])

    time.sleep(pause)

print("Total affiliates moved to new campaign: "+ str(affiliate_count))
