# -*- coding: utf-8 -*-
import sae
import urlparse
import xml.etree.ElementTree as ET

import sae.const
import MySQLdb
import tpl

import time

# create row in table 'menu0' for a new subscriber
def new_subscriber(UserID):
    conn= MySQLdb.connect(host=sae.const.MYSQL_HOST,user=sae.const.MYSQL_USER,
                          passwd=sae.const.MYSQL_PASS,db=sae.const.MYSQL_DB,
                          port=int(sae.const.MYSQL_PORT),charset='utf8')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO menu0 (`id`, `openid`, `menu`) VALUES (NULL, '" + UserID + "', 'rea')")
    conn.close()
    
# delete row in table 'menu0' for a new unsubscriber
def new_unsubscriber(UserID):
    conn= MySQLdb.connect(host=sae.const.MYSQL_HOST,user=sae.const.MYSQL_USER,
                          passwd=sae.const.MYSQL_PASS,db=sae.const.MYSQL_DB,
                          port=int(sae.const.MYSQL_PORT),charset='utf8')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM menu0 WHERE `openid` = '" + UserID + "'")
    conn.close()
    
# turn on write mode for a certain user
def mode_switch(UserID):
    conn= MySQLdb.connect(host=sae.const.MYSQL_HOST,user=sae.const.MYSQL_USER,
                          passwd=sae.const.MYSQL_PASS,db=sae.const.MYSQL_DB,
                          port=int(sae.const.MYSQL_PORT),charset='utf8')
    cursor = conn.cursor()
    cursor.execute("UPDATE menu0 SET `menu`='wri' WHERE `openid` = '" + UserID + "'")
    conn.close()

def mode_switch_off(UserID):
    conn= MySQLdb.connect(host=sae.const.MYSQL_HOST,user=sae.const.MYSQL_USER,
                          passwd=sae.const.MYSQL_PASS,db=sae.const.MYSQL_DB,
                          port=int(sae.const.MYSQL_PORT),charset='utf8')
    cursor = conn.cursor()
    cursor.execute("UPDATE menu0 SET `menu`='rea' WHERE `openid` = '" + UserID + "'")
    conn.close()
    
    
# get mode for a certain user
def get_mode(UserID):
    conn= MySQLdb.connect(host=sae.const.MYSQL_HOST,user=sae.const.MYSQL_USER,
                          passwd=sae.const.MYSQL_PASS,db=sae.const.MYSQL_DB,
                          port=int(sae.const.MYSQL_PORT),charset='utf8')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menu0 WHERE `openid` = '" + UserID + "'")
    mode = cursor.fetchone()[2]
    conn.close()
    return mode
    
#get raw records from mysql db
def get_conn():
    # 'charaset' should be set to the encoding of the corresponding database  
    conn= MySQLdb.connect(host=sae.const.MYSQL_HOST,user=sae.const.MYSQL_USER,
                          passwd=sae.const.MYSQL_PASS,db=sae.const.MYSQL_DB,
                          port=int(sae.const.MYSQL_PORT),charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from diary0 ORDER BY ts DESC")
    data = cursor.fetchall()
    conn.close()
    return data
    

def writeDiary(receivedDiary): 
    conn = MySQLdb.connect(host=sae.const.MYSQL_HOST,user=sae.const.MYSQL_USER,
                          passwd=sae.const.MYSQL_PASS,db=sae.const.MYSQL_DB,
                          port=int(sae.const.MYSQL_PORT),charset='utf8')
    cursor = conn.cursor()
    cursor.execute("insert into diary0 (ts, diary) values (%s, %s)",
                   (time.strftime('%Y-%m-%d %H:%M:%S'), receivedDiary))
    conn.commit()
    conn.close()
    

#format raw db records
# transfer unicode into string
#should be able to handel long lines
def format_diary(raw):
    message = "Hi there, here's your current diary collection:\n\n"
    for line in raw:
        if len(line[1])>=50:
            line1=line[1][:50]+"......"
        else:
            line1=line[1]
        line1 = str(line1.encode('UTF-8'))
        message = message + str(line[0]) + "\n" + line1 + "\n\n"
        
    if len(message) >= 600:
        message = message[:600]+"\n"+"......"
    message = message + "\nFor complete record, please visit 3.agathehello.sinaapp.com"
    return message

