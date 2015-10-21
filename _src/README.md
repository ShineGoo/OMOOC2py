# OMOOC.py 实践代码目录
~ 收集每周任务代码

## 0wex1 

###source code 
script name: diaryRecorder.py
```
# -*- coding: utf-8 -*-

from os.path import exists
from datetime import datetime

diary_existence = exists("myDiary.txt")

if diary_existence:
    txt = open("myDiary.txt")
    existingDiaries = txt.read()
    txt.close()
    print "Hi there, here's your current diary collection:\n\n%s" % existingDiaries
else:
    existingDiaries = ""
    print "I cannot find your diary book. No worries tough, ",
    "I'll create one called 'myDiary.txt' for you."
    
current_date_time = str(datetime.now())

def writeDiary(): 
    print "Please key in your one line diary for today."
    diary = current_date_time + "\n" + raw_input('>') +"\n\n"
    txt2 = open("myDiary.txt", 'a')
    txt2.write(diary)
    txt2.close()
    print "Your new diary has been saved.\nDo you want to write some more?"
    print "Enter 'y' to record a new line, any other letter to quit."
    return raw_input('>')

write_again = writeDiary()

while write_again == 'y':
    write_again = writeDiary()
    
print "Bye!"
```

###diaryRecorder使用手册

- 将脚本文件diaryRecorder.py与保存有过往日记的文本文件myDiary.txt保存于同一文件夹中，如无过往日记，第
一次运行脚本时myDiary.txt将被新建。

- 在terminal中进入diaryRecorder.py所在的文件夹，在terminal中输入```$ python diaryRecorder.py```

- 过往日记内容将被打印在屏幕上。

- 按提示输入新日记内容，这些内容将被写入myDiary.txt中。

- 新内容被存储后按提示输入“y“则可再次写入新的日记，输入任何其他字母将退出程序。
