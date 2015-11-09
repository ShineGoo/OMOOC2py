#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests #import the Requests module

diaryAddr = 'http://localhost:8080/diary'

#parse the html text so that it can be printed nicely
def printD(sourceResponse):
    x = sourceResponse.text
    y = x.split('<ul>')[1].split('\n<br>\n')
    for w in y:
        print w
        
def writeDiary(): 
    print "Please key in your one line diary for today. Press ctrl+C to quit."
    diary = raw_input('>')
    if diary:
        #make a HTTP POST request
        requests.post(diaryAddr, data = {'newdiary':diary})
    
def writeAnother():
    print "Your new diary has been saved."
    print "Do you want to write some more?\nEnter 'y' to record a new line, any other letter to quit."
    return raw_input('>')

def main():
    #print old diaries
    r = requests.get('http://localhost:8080/diary') #r is a Response object
    print "Yo, here's your current collection of diary!\n"
    printD(r) 
    writeDiary()
    writeAgain = writeAnother()
    while writeAgain == 'y':
        writeDiary()
        writeAgain = writeAnother()
    print "bye!"


if __name__ == "__main__":
    main()

    