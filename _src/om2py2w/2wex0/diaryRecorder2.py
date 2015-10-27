# diaryRecorder with GUI by Lu, Oct 26 2015
# -*- coding: utf-8 -*-

from os.path import exists
from datetime import datetime
from Tkinter import *
import ttk

root = Tk()
diary_existence = exists("myDiary.txt")
current_date_time = str(datetime.now())

def readDiary():
    if diary_existence:
        txt = open("myDiary.txt")
        existingDiaries = txt.read()
        txt.close()
        printOut = '''Hi there, here's your current diary collection:\n\n%s''' % existingDiaries
    else:
        existingDiaries = ""
        printOut= '''I cannot find your diary book. 
        No worries tough, I'll create one called 'myDiary.txt' for you.'''
    return printOut
    
printOut = readDiary()

label = ttk.Label(root, text = printOut + "\nEnter your one lien diary below:", wraplength = 300, background = 'white')
label.grid(row=0, column=0, columnspan=2)

entry = ttk.Entry(root, width = 30)
entry.grid(row=1, column=0, columnspan=2)

buttonSubmit = ttk.Button(root, text = "sumbit")
buttonSubmit.grid(row=3, column=0)

buttonLeave = ttk.Button(root, text = "leave", command = root.destroy)
buttonLeave.grid(row=3, column=1)

label2 = ttk.Label(root, text="")
label2.grid(row=4,column=0, columnspan=2)

buttonContinue = ttk.Button(root, text = "Yes")
buttonDiscontinue = ttk.Button(root, text = "No", command = root.destroy)


def getNewDiary():
    diaryNew = current_date_time + "\n" + entry.get() +"\n\n"
    txt2 = open("myDiary.txt", 'a')
    txt2.write(diaryNew)
    txt2.close()
    print diaryNew
    label2.config(text="Your new diary has been saved.\nDo you want to write some more?")
    label.config(text = printOut + "\n\n" + diaryNew +"\nEnter your one lien diary below:")
    buttonContinue.grid(row=5, column=0)
    buttonDiscontinue.grid(row=5, column=1)
    buttonSubmit.state(['disabled'])
    buttonContinue.state(['!disabled'])
    buttonDiscontinue.state(['!disabled'])

def reEnter():
    entry.delete(0, END)
    buttonSubmit.state(['!disabled'])
    buttonContinue.state(['disabled'])
    buttonDiscontinue.state(['disabled'])
    label2.config(text="")
    
buttonSubmit.config(command = getNewDiary)
buttonContinue.config(command = reEnter)

root.mainloop()