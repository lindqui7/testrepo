# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 13:53:09 2023

@author: lindq
"""
import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
parms = dict()
parms['address'] = address
print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())

info = json.loads(data)
print(info)
sum_count = 0
counter = 0
for comment in info["comments"]:
    sum_count += int(comment["count"])
    counter += 1

print('Count:', counter)
print('Sum:', sum_count)
