#!/usr/bin/env python
# -*- coding: utf-8 -*-
# combine two set of search results
# to use: 

#import requests
#from requests.auth import HTTPBasicAuth
#import urllib2
import json

#input area #recommender = 'Steven Pinker' / 'Carol Dweck' 'Carol S Dweck' / 'Gerd Gigerenzer' /
#                          'James G March' 'James March' / 'Gary Klein' 'Gary A Klein'/
#                          'Keith E Stanovich' 'Keith Stanovich' /'Daniel Kahneman'/
#                          'Martin E P Seligman' 'Martin Seligman'/
#                          'Clayton M Christensen' 'Clayton Christensen'/ 'Richard Dawkins'
#                          'Daniel C Dennett' 'Daniel Dennett' /'Edward L Deci' ''Edward Deci''

input_path = '/Users/apple/Documents/PythonClass/amazonProj/BINGresult/'
result_path = '/Users/apple/Documents/PythonClass/amazonProj/BINGresult/combined/'

withMiddleName = 'Edward L Deci'
noMiddleName = withMiddleName.split()[0]+" "+withMiddleName.split()[-1]

inputFileNameLong = input_path + withMiddleName.replace(' ', '_')+'_BING.json'
inputFileNameShort = input_path + noMiddleName.replace(' ', '_')+'_BING.json'

json_data_long = open(inputFileNameLong).read()
json_data_short = open(inputFileNameShort).read()

datata_long = json.loads(json_data_long)
datata_short = json.loads(json_data_short)

len(datata_long['amazonUrls']) #71
len(datata_short['amazonUrls']) #765

newList = datata_short['amazonUrls']
for ele in datata_long['amazonUrls']:
    newList.append(ele)

len(newList) #836
len(list(set(newList))) #808

newQuery = [datata_long['query'], datata_short['query']]

data2 = {'query': newQuery, 'amazonUrls': newList}

outFileName = result_path + withMiddleName.replace(' ', '_')+'_BING.json'

with open(outFileName, 'w') as fp:
    json.dump(data2, fp)

#######################
#try reloading saved data and print to screen
json_data = open(outFileName).read()
datata = json.loads(json_data)
for ele in datata['amazonUrls']:
    print ele

print "%r unique urls obtained for %r and %r" %(len(datata['amazonUrls']), withMiddleName, noMiddleName) 
