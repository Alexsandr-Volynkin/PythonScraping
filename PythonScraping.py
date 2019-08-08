import os
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
import re

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

def main():
    lineUrl = input("Введите URL: ")
    title = getUrl(str(lineUrl))
    if title == None:
        print("URL not found") 

    direct = os.path.abspath(os.curdir)#current path

    html = requests.get(lineUrl)
    soup = BeautifulSoup(html.text, 'lxml')

    text = soup.find_all('h1')
    text += soup.find_all("p")
    text += soup.find_all("h2")
    textFound = re.sub(r'\<[^>]*\>', "", str(text))

    #print(textFound)
    fileName = lineUrl.split("://")
    file = str(fileName[1]).replace("/", "_")
    newfile = file.replace('?', "_")
    with open(str(direct) + "/%s.txt" % newfile, "w") as f:
            f.write(textFound)
    input("Done")

if __name__ == '__main__':
    main()


