#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Lu Zeng contact: janicezeng.12@foxmail.com

#for different recommender, edit line 14&15 accordingly

from urllib2 import urlopen, HTTPError
import urllib2
from bs4 import BeautifulSoup
import requests
import json

#query of interest (recommender specific)
#recommender = 'Gary_Klein'
recommender = 'Steven_Pinker'
q0 = '%22Editorial+Reviews%22+%22Steven+Pinker%22+%22Books%22+site%3Aamazon.com'
#q0 = '%22Editorial+Reviews%22+%22Gary+Klein%22+%22Books%22+site%3Aamazon.com'

#specify user_agent
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"
headers = {'User-Agent': user_agent}

#url related values
#base_url = 'http://search.aol.com/aol/search?s_chn=prt_main5&v_t=comsearch&page='
base_url = 'http://search.aol.com/aol/search?s_chn=prt_main5&v_t=comsearch'
#suffix = '&s_it=topsearchbox.search&oreq=915eda57a04c423ab462f6b0a41cbb94'

#construct url used for searching    
def formURL(inputpage, inputquery):
    urlt = base_url + '&q=' + inputquery + '&s_it=topsearchbox.search' + '&page=' + str(inputpage) 
    return urlt

#get serp content of page 1, and  get the result count
page = 1
url = formURL(page, q0)
response2 = requests.get(url, headers=headers)

#save page 1's content
pages = [page]
responses = [response2.content]

#get result count
if responses[0].find('Your search returned no results') > -1:
    print "Scraping page 1 failed, please check if the aol search url structure has changed"
else:
    x = BeautifulSoup(responses[0]).findAll(id="result-count")
    resultCount=int(x[0].get_text().split()[1])
    print resultCount

####################################
#get content of rest of the serp's
def getSerpContent(pageID):
    url = formURL(pageID, q0)
    responset = requests.get(url, headers=headers)
    return responset

for j in range(2, resultCount/10+2):
    responset = getSerpContent(j)
    if responset == 'Request denied: source address is sending an excessive volume of requests.':
        print(responset)
        break
    else:
        pages.append(j)
        responses.append(responset.content)
        print "page %r obtained" %(j)
            
# for Steven Pinker, all 98 pages are obtained
##################################
#parse page content and get amazon urls
def linkSelector(sourceurl):
    isTarget = True
    sull = sourceurl.lower()
    
    if sull.find('amazon') == -1:
        isTarget = False
    elif sull.find('aol.com') != -1:
        isTarget = False
    elif sull.find('tracking?s_ch') !=-1: #no need to escape metacharacter '?'
        isTarget = False
    elif sull.find('search?s_ch') !=-1: 
        isTarget = False
    elif sull.find('search?s_it') !=-1:    
        isTarget = False
    elif sull.find('search?q=') !=-1:     
        isTarget = False
    elif sull.find('search?query=') !=-1:     
        isTarget = False
    elif sull.find('topsearchbox') !=-1:     
        isTarget = False
    elif sull.startswith('http://www.google.com'):
        isTarget = False      
        
    return isTarget
    
def getAmazonUrl(pageID):
    x = BeautifulSoup(responses[pageID-1]).findAll('a', href=True)
    amazonUrlst = []
    for link in x:
        if linkSelector(link['href']):
            amazonUrlst.append(link['href'])
    return amazonUrlst

amazonUrls = []

for j in range(1, resultCount/10+2):
    amazonUrls.append(getAmazonUrl(j))

amazonUrlsGeneric = sum(amazonUrls, [])


#save final result:    
data = {'query': q0, 'pages': pages, 'responsesRaw':responses, 'amazonUrls': amazonUrls}
data2 = {'query': q0, 'amazonUrls': amazonUrlsGeneric}

localPath = '/Users/apple/Documents/gitHub/OMOOC2py/1sTry/amazon/'
fileName = localPath + recommender+'.json'
with open(fileName, 'w') as fp:
    json.dump(data2, fp)

#try reloading saved data
json_data = open(fileName).read()
datata = json.loads(json_data)
print(datata)
