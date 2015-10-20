# -*- coding: utf-8 -*-

from os.path import exists
from datetime import datetime

diary_existence = exists("myDiary.txt")

if diary_existence:
    txt = open("myDiary.txt")
    existingDiaries = txt.read()
    txt.close()
    print "Hi there, here's your current diary collection:\n%s" % existingDiaries
else:
    existingDiaries = ""
    print "I cannot find your diary book. No worries tough, ",
    "I'll create one called 'myDiary.txt' for you."
    
current_date_time = str(datetime.now())

prompt = '>'
print "Please key in your one line diary for today."
diary = current_date_time + "\n" + raw_input(prompt) +"\n\n"

txt2 = open("myDiary.txt", 'a')
txt2.write(diary)

txt2.close()


