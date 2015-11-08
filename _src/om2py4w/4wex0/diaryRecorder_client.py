# -*- coding: utf-8 -*-

import sys
import requests
from bs4 import BeautifulSoup


r = requests.get('http://localhost:8080/diary')
ddd = BeautifulSoup(r.text, 'html.parser')
requests.post('http://localhost:8080/diary', data = {'newdiary':"try"})


#def writeDiary(): 
#    print "Please key in your one line diary for today. Press ctrl+C to quit."
#    diary = raw_input('>')
#    return diary

#def writeAnother():
#    print "Your new diary has been saved."
#    print "Do you want to write some more?\nEnter 'y' to record a new line, any other letter to quit."
#    return raw_input('>')

#def main():
#    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
#    s.connect((HOST, PORT))
#    existingDiaries = s.recv(1024) #get existing diaries from the server
#    print existingDiaries #and print it on the client end
#    s.sendall(writeDiary()) #send the newly wrote line to server
#    ##what if the user use ctrl+C to quit?
#    writeAgain = writeAnother()
#    s.sendall(writeAgain)
#    while writeAgain == 'y':
#        newD = (writeDiary())
#        s.sendall(newD)
#        writeAgain = writeAnother()
#        s.sendall(writeAgain)
#    print "bye!"
#    s.close()
    
#if __name__ == "__main__":
#    main()