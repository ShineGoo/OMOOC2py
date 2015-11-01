# -*- coding: utf-8 -*-

#from os.path import exists
#from datetime import datetime
import socket
import sys
    
HOST = 'localhost'
PORT = 50007 

def writeDiary(): 
    print "Please key in your one line diary for today."
    diary = raw_input('>')
    return diary

def writeAnother():
    print "Your new diary has been saved."
    print "Do you want to write some more?\nEnter 'y' to record a new line, any other letter to quit."
    return raw_input('>')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
s.connect((HOST, PORT))
existingDiaries = s.recv(1024)
print existingDiaries
s.sendall(writeDiary())
writeAgain = writeAnother()
s.sendall(writeAgain)
while writeAgain == 'y':
    newD = (writeDiary())
    s.sendall(newD)
    writeAgain = writeAnother()
    s.sendall(writeAgain)
print "bye!"

s.close()