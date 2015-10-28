#!/usr/bin/env python
# diaryRecorder with GUI by Lu, Oct 26 2015
# -*- coding: utf-8 -*-

from os.path import exists
from datetime import datetime
from Tkinter import *
import ttk

diary_existence = exists("myDiary.txt")
current_date_time = str(datetime.now())

#construct the main window
root = Tk()
#the text widget where existing diaries are shown
T = Text(root)
#text above the entry space
label = ttk.Label(root, text = "\nEnter your one line diary below:")
#place for user to enter new diary
entry = ttk.Entry(root, width = 30)
#in clicking this button the content in entry will be saved
buttonSubmit = ttk.Button(root, text = "sumbit")
#the button that closes the window and quit the process
buttonLeave = ttk.Button(root, text = "leave", command = root.destroy)
#text that shows after the user clicked the submit button, asking if the user wants to repeat
label2 = ttk.Label(root, text="")
buttonContinue = ttk.Button(root, text = "Yes")
buttonDiscontinue = ttk.Button(root, text = "No", command = root.destroy)

## define a function that reads the content of existing diary and saves it in the returned value
def readDiary():
    if diary_existence:
        txt = open("myDiary.txt")
        existingDiaries = txt.read()
        txt.close()
        printOut = '''Hi there, here's your current diary collection:\n\n%s''' % existingDiaries
    else:
        existingDiaries = ""
        printOut= '''I cannot find your diary book.\nNo worries tough, I'll create one called 'myDiary.txt' for you.'''
    return printOut
   
# this function read the content in the entry space, write it on widget T,
# and save it to myDiary.txt. It also reveals label2, buttonContinue and buttonDiscontinue 
def getNewDiary():
    diaryNew = current_date_time + "\n" + entry.get() +"\n\n"
    txt2 = open("myDiary.txt", 'a')
    txt2.write(diaryNew)
    txt2.close()
    print diaryNew
    label2.config(text="Your new diary has been saved.\nDo you want to write some more?")
    T.insert(END, diaryNew)
    buttonContinue.grid(row=6, column=0)
    buttonDiscontinue.grid(row=6, column=1)
    buttonSubmit.state(['disabled'])
    buttonContinue.state(['!disabled'])
    buttonDiscontinue.state(['!disabled'])

# defining things that happen after buttonContinue is clicked
def reEnter():
    entry.delete(0, END)
    buttonSubmit.state(['!disabled'])
    buttonContinue.state(['disabled'])
    buttonDiscontinue.state(['disabled'])
    label2.config(text="")
    

def foo():
    root.title("The Diary")
    T.grid(row=0, column=0, columnspan=2)
    T.insert(END, readDiary())
    label.grid(row=1, column=0, columnspan=2)
    entry.grid(row=2, column=0, columnspan=2)
    buttonSubmit.grid(row=4, column=0)
    buttonLeave.grid(row=4, column=1)
    label2.grid(row=5,column=0, columnspan=2)
    buttonSubmit.config(command = getNewDiary)
    buttonContinue.config(command = reEnter)
    root.mainloop()

if __name__ == '__main__':
    foo()
