#!/bin/python3
import requests

with open('file') as file:
    my_list = [line.strip() for line in file.readlines()]


for domain in my_list:
    try:
        r = requests.head(domain)
        print(r.status_code, domain)
    except requests.ConnectionError:
        print("failed to connect", domain)