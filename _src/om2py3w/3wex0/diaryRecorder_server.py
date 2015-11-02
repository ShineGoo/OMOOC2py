# -*- coding: utf-8 -*-

from os.path import exists
from datetime import datetime
import socket
from thread import *

diary_existence = exists("myDiary.txt")
current_date_time = str(datetime.now())
HOST = 'localhost'
PORT = 50007

def readDiary():
    if diary_existence:
        txt = open("myDiary.txt")
        existingDiaries = txt.read()
        txt.close()
        d = "Hi there, here's your current diary collection:\n\n%s" % existingDiaries
    else:
        existingDiaries = ""
        d = '''I cannot find your diary book. 
        No worries tough, I'll create one called 'myDiary.txt' for you.'''
    return d
    
def writeDiary(receivedDiary): 
    diary = current_date_time + "\n" + receivedDiary +"\n\n"
    txt2 = open("myDiary.txt", 'a')
    txt2.write(diary)
    txt2.close()
    #return raw_input('>')

# Function for handling connections. This will be used to create threads
def clientthread(conn, addr):
    conn.sendall(readDiary()) #send existing diaries to client
    newDiary = conn.recv(1024) #receive newly written diary from the client
    print "%r\n%r just wrote:\n %s" %(current_date_time, addr, newDiary)
    writeDiary(newDiary) #write it to myDiary.txt
    write_again = conn.recv(1024) #receive the 'write_again' decision from the client

    #print write_again
    while write_again == 'y':
        print "%s %s decides to write a new line." % (addr[0], addr[1])
        newD = conn.recv(1024)
        print "%r\n%s %s just wrote:\n %s" %(current_date_time, addr[0], addr[1], newD)
        write_again = conn.recv(1024)
        #print write_again
    print "%s %s quits" %(addr[0], addr[1])
    conn.close()

# the main function:
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print 'Socket created'

    s.bind((HOST, PORT))
    print 'Socket bind complete. Host: %s, Port: %s' %(HOST, PORT)

    s.listen(5)
    print 'Socket now listening'  

    while 1:
        conn, addr = s.accept()
        start_new_thread(clientthread, (conn, addr))
           
    s.close()
    
if __name__ == "__main__":
    main()
