#!/usr/bin/env python
# -*- coding: utf-8 -*-

#this version is based on ver0
#for different recommender, edit line 14&15 accordingly
####################
#try scraping aol search:
from urllib2 import urlopen, HTTPError
from bs4 import BeautifulSoup
import requests
impory json

#query of interest (recommender specific)
#recommender = 'Gary_Klein'
recommender = 'Steven_Pinker'
q0 = '%22Editorial+Reviews%22+%22Steven+Pinker%22+%22Books%22+site%3Aamazon.com'
#q0 = '%22Editorial+Reviews%22+%22Gary+Klein%22+%22Books%22+site%3Aamazon.com'

#specify user_agent
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"
headers = {'User-Agent': user_agent}

#get serp content of page 1, and  get the result count
#construct url used for searching    
page = 1
url = 'http://search.aol.com/aol/search?s_chn=prt_main5&v_t=comsearch&page='+str(page)+'&q='+q0+'&s_it=topsearchbox.search&oreq=915eda57a04c423ab462f6b0a41cbb94'
# get page 1
response2 = requests.get(url, headers=headers)

#save page 1's content
pages = []
pages.append(page)
responses = []
responses.append(response2.content)

#get result count
x = BeautifulSoup(response2.content).findAll(id="result-count")
resultCount=int(x[0].get_text().split()[1]) #resultCount=975

####################################
#get content of rest of the serp's
def getSerpContent(pageID):
    url = 'http://search.aol.com/aol/search?s_chn=prt_main5&v_t=comsearch&page='+str(pageID)+'&q='+q0+'&s_it=topsearchbox.search&oreq=915eda57a04c423ab462f6b0a41cbb94'
    responset = requests.get(url, headers=headers)
    return responset
    
for j in range(2, resultCount/10+2):
    responset = getSerpContent(j)
    pages.append(j)
    responses.append(responset.content)
    print "page %r obtained" %(j)
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

fileName = recommender+'.json'
with open(fileName, 'w') as fp:
    json.dump(data2, fp)

#try reloading saved data
json_data = open(fileName).read()
datata = json.loads(json_data)
print(datata)
