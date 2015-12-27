#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# author: Lu Zeng
# to use: replace url0 in line #10 with traget url
# try to find the hierachical classification of a book, given the book's url
# example: http://www.amazon.com/Intrinsic-Motivation-Work-2nd-Edition/dp/1620642727
import requests
from bs4 import BeautifulSoup

def getPageContent(inputURL):
    url0 = inputURL
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"
    headers = {'User-Agent': user_agent}
    try:
        response_data_t = requests.get(url0, headers=headers, timeout=10)
        outputContent = response_data_t.content
        print "Page html obtained\n\n"
    except requests.RequestException as e:
        print "There is a connection error. Please check your Internet Connection and run this code later."
        outputContent = None
    return outputContent

def getNode(inputContent):
    nodeSet = []
    if inputContent is None:
        print "No page content is obtained due to connection error. Please try again."
    else:
        soup = BeautifulSoup(inputContent)
        foo = soup.findAll('div', attrs={'id':'wayfinding-breadcrumbs_container'})
        if foo is None or len(foo) != 1:
            print "check this url: %s" % (url0)
        else:
            kk = foo[0].text.split(u'\u203a')
            for kkk in kk:
                nodeSet.append(kkk.strip())
    return nodeSet

url0 = 'http://www.amazon.com/Intrinsic-Motivation-Work-2nd-Edition/dp/1620642727'
resultNodes = getNode(getPageContent(url0))

print url0, '\n'
for node in resultNodes:
    print node, '\n'

############################
##test on multiple books
#import json
#import time
#import random

#recommender = "Edward_Deci"
#resultPath = '/Users/apple/Documents/PythonClass/amazonProj/BINGresult/' 

#def getbookurl(inputRecommender):
#    fileName = resultPath + inputRecommender + "_BING.json"
#    json_data = open(fileName).read()
#    datat = json.loads(json_data)
#    bookurllist = datat['amazonUrls']
#    bookurllist = list(set(bookurllist))
#    return bookurllist

#x = getbookurl(recommender)

#for url in x:
#    resultNodes = getNode(getPageContent(url))
#    print url, '\n'
#    for node in resultNodes:
#        print node
#    print '\n\n'
#    time.sleep(3+random.random()*6)