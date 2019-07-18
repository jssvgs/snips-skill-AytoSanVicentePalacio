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



def intent_received(hermes, intentMessage):

if intentMessage.intent.intent_name == 'jvegas:telefono':

        
        # item = "Telefono"

        
        # url = select_url(item)
        # response = requests.get(url)
        # xml = response.text
        # root = ET.fromstring(xml)

        # telephone = root.find('Teléfono')
        telephone = "983 825 006"
        
        sentence = 'El número de teléfono del ayuntamiento es el ' + telephone


    else:
        return
    
    hermes.publish_end_session(intentMessage.session_id, sentence)
    
    
with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
