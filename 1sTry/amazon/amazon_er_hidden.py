#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# find editorial review info within a page which is hidden inside a javascript 
# example: http://www.amazon.com/Theories-Team-Cognition-Cross-Disciplinary-Perspectives/dp/0415874130

import json
import bottlenose
import xml.etree.ElementTree as ET
import urllib2
from bs4 import BeautifulSoup
import requests
import re


recommender = "Gary_Klein"

text=open('amazonAPIkeys.txt')
keys=text.read().split('\n')
text.close()

def getbookurl(inputRecommender):
    fileName = inputRecommender + ".json"
    json_data = open(fileName).read()
    datat = json.loads(json_data)
    bookurllist = datat['amazonUrls']
    bookurllist = list(set(bookurllist))
    return bookurllist

x = getbookurl(recommender)
asin = x[17].split('/')[-1] #u'0415874130'

url0 = x[17]
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"
headers = {'User-Agent': user_agent}
response_data_t = requests.get(url0, headers=headers)
soup = BeautifulSoup(response_data_t.content)

#f = soup.findAll('div', attrs={'class':'productDescriptionWrapper'})
#f = soup.findAll('div', attrs={'id':'pdIframeContent'})
#f = soup.findAll('div', attrs = {'class' : 'a-container'})
#f2 = f[0].findAll('div', attrs = {'id' : 'iframe-wrapper'})

tpp = response_data_t.content.find('Editorial%20Reviews') #284851
response_data_t.content[tpp:tpp+700]
pattern2 = re.compile('var\s*iframeContent\s*=\s*".*"')
pattern2.match(response_data_t.content)
match = re.search(pattern2, response_data_t.content)
print(urllib2.unquote(match.group()))
soup2 = BeautifulSoup(urllib2.unquote(match.group()))
soup2.findAll('h2')
soup2.findAll('div', attrs={'class':'productDescriptionWrapper'})








#soup.text.find('Editorial%20Reviews') #160921
#soup.text[160921:162000]

#pattern = re.compile(r'Editorial%20Reviews')
#k = soup.find(text=pattern)
#type(k)

##obj.initialize = function (onloadCallback, needWidthAdjust) {\n    var iframeContent = 
#script = soup.find('script', text = lambda x: 'iframeContent' in x)
#pattern2 = re.compile('var\s*iframeContent\s*=\s*".*"')
#str(k)
#pattern2.match(str(k))
#print(pattern2.match(str(k)))

# To discuss automated access to Amazon data please contact api-services-support@amazon.com.









