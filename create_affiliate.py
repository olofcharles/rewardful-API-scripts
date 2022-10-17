#!/usr/bin/env python
import requests
from requests.structures import CaseInsensitiveDict
import json
import time
import csv

# Open CSV file, indicate the file name as the first argument of the open function
with open('CSV-filename.csv', mode="r", encoding="utf-8-sig") as affiliate_data:
    affiliate = csv.reader(affiliate_data)
    list_affiliate = list(affiliate)

# Enter the API secret key of the company
api_secret = input("Enter API secret: ")
api_key = (api_secret, "")

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

affiliates_created = 0

for affiliate in list_affiliate:
    url = "https://api.getrewardful.com/v1/affiliates/"
    data = {
        "email": affiliate[0],
        "first_name": affiliate[1],
        "last_name": affiliate[2],
        "paypal_email": affiliate[3]
    }

    # Make the Create Affiliate API endpoint call
    resp = requests.post(url, headers=headers, data=data, auth=api_key)
    affiliates_created += 1
    print("Affiliate created: " + affiliate[0])
    time.sleep(5)

print("There were " + str(affiliates_created) + " affiliate accounts created.")

affiliate_data.close()


