#!/usr/bin/env python
import requests
from requests.structures import CaseInsensitiveDict
import json
import time

# List the commission IDs
commission_list = []

# Ask for the API secret
api_secret = input("Enter API secret: ")

# Input the date the commission was paid
date = ""
api_key = (api_secret, "")

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = {
    "paid_at": date
}

counter = 0

for commission in commission_list:
    url = "https://api.getrewardful.com/v1/commissions/" + commission
    resp = requests.put(url, headers=headers, data=data, auth=api_key)
    counter += 1
    print(str(counter) + ". Commission ID: " + commission + " Response: " + str(resp.status_code))
    time.sleep(5)

print("There were " + str(counter) + " commissions whose paid dates where changed to " + str(date))