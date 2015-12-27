#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# author: Lu Zeng
# try to find whether the recommender's name is inside quotation marks
# example: http://www.amazon.com/Shakespeares-Double-Helix-Shakespeare-Now/dp/0826491200/

import urllib2
from bs4 import BeautifulSoup, Tag
import requests
import re

recommender = "Richard Dawkins"
url0 = 'http://www.amazon.com/Shakespeares-Double-Helix-Shakespeare-Now/dp/0826491200/'
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"
headers = {'User-Agent': user_agent}
try:
    response_data_t = requests.get(url0, headers=headers, timeout=10)
    #response_data_t.content
    print "Page html obtained\n\n"
except requests.RequestException as e:
    print "There is a connection error. Please check your Internet Connection and run this code later."
    quit()

pattern2 = re.compile('var\s*iframeContent\s*=\s*".*"')
match = re.search(pattern2, response_data_t.content)

if match is None:
    print "Cannot locate the 'Editorial Reviews' area. Please check the source html"
    quit()

#print(urllib2.unquote(match.group()))
soup2 = BeautifulSoup(urllib2.unquote(match.group()))
#soup2.findAll('h2')
#soup2.findAll('div', attrs={'class':'productDescriptionWrapper'})

#soup2.find('h2', {"text" : "Editorial%20Reviews"}).next_siblings

if soup2.find(text = 'Review') is None:
    print "Cannot locate the 'Review' section under the 'Editorial Reviews' area. Please check the source html"


rrr = []
for item in soup2.find(text = 'Review').parent.next_siblings:
    if isinstance(item, Tag):
        if 'class' in item.attrs and 'productDescriptionWrapper' in item.attrs['class']:
            rrr.append(item)
        if 'class' in item.attrs and 'productDescriptionSource' in item.attrs['class'] and 'About the Author' in item.text:
            break

paragraphs = []
for child in rrr[0].children:
    if str(child) != '<br/>':
        paragraphs.append(str(child).replace('<div>', '').replace('</div>', ''))

text = ''
for para in paragraphs:
  text = text+para+'\n'
  
text = re.sub(r"<div[^>]*?>", "", text)

if "Richard Dawkins" in text:
    print "%s is found in 'Editorial Reviews' for %s" % (recommender, url0), '\n\n'
else:
    print "%s is not found in 'Editorial Reviews' for %s" % (recommender, url0)
    quit()

quoted_strings=re.findall('"[^"]+?"',text)

if len(quoted_strings)>0:
    startIndex0 = text.find(quoted_strings[0])
    unquoted_strings=[text[:startIndex0]]
    if len(quoted_strings)>1:
        text_temp = text[(startIndex0+len(quoted_strings[0])):]
        for k in range(1, len(quoted_strings)):
#            print k
            startIndex = text_temp.find(quoted_strings[k])
            unquoted_strings.append(text_temp[:startIndex])
            text_temp = text_temp[(startIndex+len(quoted_strings[k])):]
        if len(text_temp)>0:
            unquoted_strings.append(text_temp)


for quo in quoted_strings:
    if "Richard Dawkins" in quo:
        print "%s is found in a quoted string" %(recommender), quo, '\n\n'
        break
        

for quo in unquoted_strings:
    if "Richard Dawkins" in quo:
        print "%s is found in an unquoted string" % (recommender), quo, '\n\n'
        break 