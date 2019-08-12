# -*- coding: utf-8 -*-

import functools
import os
import requests
import re
import textwrap

from bs4 import BeautifulSoup
from urllib.request import urlopen
from .config import ALL_TAGS, MAX_LENGTH, DIRECT

def getUrl(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsoup = BeautifulSoup(html.read(), 'lxml')
        title = bsoup.body.h1
    except AttributeError as e:
        return None
    return title

def loadHTML(self):
    html = requests.get(self)
    soup = BeautifulSoup(html.text, 'lxml')
    i = 0
    text = ' '  
    while i < len(ALL_TAGS):
        text += str(soup.find_all(ALL_TAGS[i]))
        text += '\n\n'
        i += 1
    return text

def re_(self):
    text = re.sub(r'\<[^>]*\>', "", str(self))
    return text

def writeToFile(self, value):
    fileName = value.split("://")
    file = str(fileName[1]).replace("/", "_")
    pathFile = file.replace('?', "_")
    with open(str(DIRECT) + "/%s.txt" % pathFile, "w") as f:
        f.write(textwrap.fill(self, width=MAX_LENGTH))
        f.write('\n\n')
