#!/usr/bin/env python3
from hermes_python.hermes import Hermes
import hermes_python 
import requests
from urls_ayto import nombre_item, url_item
from xml.etree import ElementTree as ET
# from datetime import datetime, date, time, timedelta
# import calendar

MQTT_IP_ADDR = "localhost" 
MQTT_PORT = 1883 
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT)) 

# a = datetime.now()
# f = a.date()
# defaultfecha = str(f)


def select_url(current_item):
    for x in nombre_item:
        if x == current_item:
            break
    idxm = nombre_item.index(x)
    urlm = url_item[idxm]
    return urlm






item = "Telefono"

        
url = select_url(item)
response = requests.get(url)
xml = response.text
root = ET.fromstring(xml)

telephone = root.find('Teléfono')
        
sentence = 'El número de teléfono del ayuntamiento es el ' + telephone

print(response)
