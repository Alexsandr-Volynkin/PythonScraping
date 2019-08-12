# -*- coding: utf-8 -*-

from .tools import getUrl, loadHTML, re_, writeToFile

def main():

    lineUrl = input("Введите URL: ")
    title = getUrl(str(lineUrl))
    if title == None:
        print("URL not found") 

    text = loadHTML(lineUrl)

    textFound = re_(text)

    writeToFile(textFound, lineUrl)

    input("Done")

if __name__ == '__main__':
    main()


