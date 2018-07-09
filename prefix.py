#!/usr/bin/env python

import requests
import json
import time

url= 'http://<IP HERE>:8000/api/ipam/prefixes/'

counter=0
offset=50
while True:
    url_string = ''
    if counter == 0:
        url_string = url
        counter += 1 
    else:
        url_string = url + '?limit=50&offset=' + str(offset)

    response = requests.get(url_string)
    prefixes = json.loads(response.text)
    
    for i in prefixes['results']:
        print(i['prefix'])
    
    offset += 50
    if len(prefixes['results']) == 0:
        break 
