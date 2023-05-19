#!/usr/bin/env python
import requests
from requests.structures import CaseInsensitiveDict
import json
import time
import csv

# Open CSV file, indicate the file name as the first argument of the open function
with open('filename.csv', mode="r", encoding="utf-8-sig") as affiliate_data:
    affiliates = csv.reader(affiliate_data)
    list_affiliate = list(affiliates)

# Ask user for the affiliate ID and the API key of the company asking for commission deletion
api_secret = input("Enter API secret: ")
api_key = (api_secret, "")

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

affiliates_created = 0

for affiliate in list_affiliate:
    url = "https://api.getrewardful.com/v1/affiliates/"
    data = {
        "email": affiliate[0].lower().strip(),
        "first_name": (affiliate[1].lower().strip()).title(),
        "last_name": (affiliate[2].lower().strip()).title(),
        "campaign_id": affiliate[3],
        "stripe_customer_id": affiliate[4],
    }

    resp = requests.post(url, headers=headers, data=data, auth=api_key)
    status = resp.status_code
    if status == 200:
        print("Response: " + str(status))
        affiliates_created += 1
        print("Affiliate created: " + affiliate[0])
    else:
        print(status)
        print("Affiliate NOT created: " + affiliate[0])
    print("Pausing for 2 seconds")
    time.sleep(2)

print("There were " + str(affiliates_created) + " affiliate accounts created.")

affiliate_data.close()
