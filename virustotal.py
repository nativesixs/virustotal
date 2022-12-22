# -*- coding: utf-8 -*-
"""
Created on Fri Oct  12 03:18:00 2022

@author: zencamat
"""
import requests

key=input("Enter your VirusTotal API key:\n")
filehash=input("Enter file hash:\n")


url = 'https://www.virustotal.com/vtapi/v2/file/report'


params = {'apikey': key,
          'resource': filehash}

response = requests.get(url, params=params)

with open('output.json','wb') as f:
    f.write(response.content)

print(response.json())





