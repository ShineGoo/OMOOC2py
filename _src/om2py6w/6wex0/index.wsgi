# -*- coding: utf-8 -*-
import sae
import urlparse
import xml.etree.ElementTree as ET

import sae.const
import MySQLdb
import tpl

import time

# dbManipulation.py is created by me and contains functions for db manipulation and text
# formattin
from dbManipulation import *
    
def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, response_headers)
    method = environ['REQUEST_METHOD']
    if method == "GET":
        query = environ['QUERY_STRING']
        echostr = urlparse.parse_qs(query)['echostr']
        return echostr
    
    elif method == "POST":
        post = environ['wsgi.input']
        root = ET.parse(post)
        fromUser = root.findtext(".//FromUserName")
        toUser = root.findtext(".//ToUserName")
        CreateTime = root.findtext(".//CreateTime")
        MsgType = root.findtext(".//MsgType")
        
        if MsgType == 'event':
            Event = root.findtext(".//Event")
            if Event == 'subscribe':
                reply = "Welcome! Enter 'read' to read diary, 'write' to write."
                new_subscriber(fromUser)
            elif Event == 'unsubscribe':
                reply = 'Sorry to see you go.'
                new_unsubscriber(fromUser)
            
        elif MsgType == 'text':
            Content = root.findtext(".//Content")
            Content = Content.encode('UTF-8')
        
            if Content == 'read':
                rows = get_conn()
                reply = format_diary(rows)
            
            elif Content == 'write':
                reply = "Send me your new line of dairy"
                mode_switch(fromUser) 
            
            elif get_mode(fromUser) == 'wri':
                writeDiary(Content)
                reply = 'Your new diary has benn saved.'
                mode_switch_off(fromUser)
           
            else:
                reply = "enter 'read' to read diary, 'write' to write."
                
        else:
            reply = "enter 'read' to read diary, 'write' to write."
            
        
        mtpl = tpl.texttpl(fromUser, toUser, CreateTime, reply)
        return mtpl

application = sae.create_wsgi_app(app)