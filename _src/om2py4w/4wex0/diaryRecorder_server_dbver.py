#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from os.path import exists
from datetime import datetime
from bottle import route, request, post, run, template, static_file
import sqlite3

book_name = "myDiary.db"
#diary_existence = exists(book_name)

def readDiary():
    conn = sqlite3.connect(book_name, \
           detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    cursor = conn.cursor()
    existingDiaries = cursor.execute("select * from diary").fetchall()
    x = []
    for row in existingDiaries:
        z = []
        ts = str(row[0])
        ts = ts[:len(ts)-7]
        z.append(ts)
        z.append(row[1])
        x.append(z)
    conn.close()
    return x

    
def writeDiary(receivedDiary): 
    conn = sqlite3.connect(book_name, \
           detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    cursor = conn.cursor()
    cursor.execute("insert into diary (ts, diary) values (?, ?)", \
                   (datetime.now(), receivedDiary))
    conn.commit()
    conn.close()

# template. will be moved to a separate file later
d_tpl = '''
           <html>
           <head>
           <style>
           body {
               background-image: url("/static/water_pattern.jpg");
               background-repeat: repeat;
               background-position: rigt top;
               margin-right: 200px;
           }
           </style>
           </head>
           <body text="white">
           Welcome!<br><br>
           <form action="/diary" method="post">
            Input your online diary here: <input name="newdiary" type="text" />
            <input value="Submit" name="do_submit" type="submit">
            </form>
            <p>Hi there, here's your current diary collection:</p>
            <p>
            % for line in d:
            {{line[0]}}<br>{{line[1]}}<br><br>
            % end
            </p>
            </body>
           </html>'''


@route('/static/<filename:path>')
def sever_static(filename):
    return static_file(filename, root = '')

@route('/diary')
def diary():
    data = readDiary()
    return template(d_tpl, d = data)
    
@route('/diary', method = 'POST')
def newDiary():
    #getValue = request.POST.decode('utf-8')
    nd = request.POST.get('newdiary')
    if nd:
        writeDiary(nd)
    return template(d_tpl, d = readDiary())


run(host = 'localhost', port = 8080, debug = True)
