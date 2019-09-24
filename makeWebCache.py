#!/usr/bin/env python3
# coding=utf-8

import requests
from bs4 import BeautifulSoup #pip3 install beautifulsoup4
from urls_ayto import urls_dict
import json
from datetime import datetime

cache_file = "cache.json"   # sets the name of the cache file

### obtain the html content

item = "contacto"           # indicate the item to retrieve from the web page 
url = urls_dict[item]       # search the url from the dict
response = requests.get(url)    # make a get http request    
# print(">>>> ",response.status_code)       # the status can be handled, in case of error
text_response = response.text   # obtaint the html response 
soup = BeautifulSoup(text_response, 'html.parser')      # parse the response as HTML code
# print(soup.prettify()) 

### extract the data from the web page and store it in the cache struct
cache = {}  #initialize the cache struct as a dictionary
cache["cache_datetime"] = str(datetime.now())   # set the date of the cache data
cache["address"]= soup.find("div", "address").text.strip()  # no whitespaces 
the_telephone_number= soup.find("div", "phone local").text[5:]   # without " +34 "
cache["telephone"] = the_telephone_number.replace(" ",", ",2) # prepare to better speech 
the_fax_number = soup.find("div", "phone fax").text[5:]   # without " +34 "
cache["fax"] = the_fax_number.replace(" ",", ",2)
cache["email"] = soup.find("div", "email").text.strip()
cache["URL"] = soup.find("div", "urlExterna").text.strip()

# print("CACHE dict >>>", cache)

### save the cache dict on file as a json
with open (cache_file, "w") as write_file:
    json.dump(cache, write_file)


# print("grabado json en file")

# with open ("cache.json", "r") as read_file:
#     data = json.load(read_file)

# print(type(data))
# print(">>>", data)
# print("telefono: ", data["telephone"])