#!/usr/bin/env python3
# coding=utf-8

# from hermes_python.hermes import Hermes
# import hermes_python 
import requests
from bs4 import BeautifulSoup #pip3 install beautifulsoup4

from urls_ayto import urls_dict
from xml.etree import ElementTree 
import json

from datetime import datetime, date, time, timedelta
# import calendar

# MQTT_IP_ADDR = "localhost" 
# MQTT_PORT = 1883 
# MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT)) 



def select_url(current_item):
    for x in nombre_item:
        if x == current_item:
            break
    idxm = nombre_item.index(x)
    urlm = url_item[idxm]
    print(">>>>", urlm)
    return urlm


item = "contacto"
        
#        url = lista_urls["contacto"]

url = urls_dict[item]
response = requests.get(url)
print(">>>> ",response.status_code)
text_response = response.text
soup = BeautifulSoup(text_response, 'html.parser')
print("==========================================================")
print(soup.prettify())
print("==========================================================")

# for tag in print(soup.find_all(re.compile("phones"))):
#     print(tag)

cache = {}
cache["cache_datetime"] = str(datetime.now())
cache["address"]= soup.find("div", "address").text
cache["telephone"] = soup.find("div", "phone local").text
cache["fax"] = soup.find("div", "phone fax").text
cache["email"] = soup.find("div", "email").text
cache["URL"] = soup.find("div", "urlExterna").text

print("CACHE dict >>>", cache)

json_cache = json.dumps(cache)
print("CACHE json >>>", json_cache)

with open ("cache.json", "w") as write_file:
    json.dump(json_cache, write_file)

print("grabado json en file")

with open ("cache.json", "r") as read_file:
    data = json.load(read_file)

print("leido json >>>", data)
