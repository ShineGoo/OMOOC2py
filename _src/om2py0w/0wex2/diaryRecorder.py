#this is an attempt to revise _src/om2py0w/0wex1/diaryRecorder.py
#the goal is to use class

# -*- coding: utf-8 -*-

from os.path import exists
from datetime import datetime

class diaryRecorder(object):

    def __init__(self):
        self.diary_existence = exists("myDiary.txt")
        self.current_date_time = str(datetime.now())
        
    def greeding(self):
        if self.diary_existence:
            txt = open("myDiary.txt")
            existingDiaries = txt.read()
            txt.close()
            print "Hi there, here's your current diary collection:\n\n%s" % existingDiaries
        else:
            existingDiaries = ""
            print "I cannot find your diary book. No worries tough, ",
            "I'll create one called 'myDiary.txt' for you."
        
    def writeDiary(self):
        print "Please key in your one line diary for today."
        diary = self.current_date_time + "\n" + raw_input('>') +"\n\n"
        txt2 = open("myDiary.txt", 'a')
        txt2.write(diary)
        txt2.close()
        print "Your new diary has been saved.\nDo you want to write some more?"
        print "Enter 'y' to record a new line, any other letter to quit."
        return raw_input('>')
        
#######################################################################################        
Myrecorder = diaryRecorder()
Myrecorder.greeding()
write_again = Myrecorder.writeDiary()
while write_again == 'y':
    write_again = writeDiary()
print "Bye!"