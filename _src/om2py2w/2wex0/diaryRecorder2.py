# diaryRecorder with GUI by Lu, Oct 26 2015
# -*- coding: utf-8 -*-

from os.path import exists
from datetime import datetime
from Tkinter import *
import ttk

root = Tk()
diary_existence = exists("myDiary.txt")
current_date_time = str(datetime.now())

if diary_existence:
    txt = open("myDiary.txt")
    existingDiaries = txt.read()
    txt.close()
    printOut = "Hi there, here's your current diary collection:\n\n%s" % existingDiaries
else:
    existingDiaries = ""
    printOut= '''I cannot find your diary book. 
    No worries tough, I'll create one called 'myDiary.txt' for you.'''

ttk.Label(root, text = printOut, wraplength = 300, background = 'white').grid(row=0, column=0)

button = ttk.Button(root, text = "Click me to write new diary")
button.grid(row=1, column=0)

def writeDiary(): 
    print "Please key in your one line diary for today."
    diary = current_date_time + "\n" + raw_input('>') +"\n\n"
    txt2 = open("myDiary.txt", 'a')
    txt2.write(diary)
    txt2.close()
    print "Your new diary has been saved.\nDo you want to write some more?"
    print "Enter 'y' to record a new line, any other letter to quit."
    return raw_input('>')
    
#button.config(command = writeDiary)
    
write_again = writeDiary()

while write_again == 'y':
    write_again = writeDiary()
    
print "Bye!"