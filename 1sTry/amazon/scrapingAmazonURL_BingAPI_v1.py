#!/usr/bin/env python
# -*- coding: utf-8 -*-
# to use: specify recommender name in line 13; specify the full path of the text file 
#         containing the Bing Search API Key in line 14; specify the path for your result 
#          json file in line 15.

import requests
from requests.auth import HTTPBasicAuth
import urllib2
import json

#input area #recommender = 'Steven Pinker' / 'Carol Dweck' / 'Gerd Gigerenzer' / 'James G March'
recommender = 'James G March'
API_KEY_path = '/Users/apple/Documents/PythonClass/amazonProj/BingSearchAPIkey.txt'
result_path = '/Users/apple/Documents/PythonClass/amazonProj/'

#search query
q0 = '"Editorial Reviews" "'+recommender+'" "Books" site:Amazon.com'

# create search url
service_root_uri = 'https://api.datamarket.azure.com/Bing/Search/' 
top = 50 #the number of results to return. The default is 50

def formURL(inputskip):
    base_url = service_root_uri + "Composite" + "?Sources=%27web%27"
    query = '%27' + urllib2.quote(q0) + '%27'
    urlt = base_url + '&Query=' + query + '&$top=' + str(top) + '&$skip=' + str(inputskip) + '&$format=' + 'json'
    return urlt

# get json output from a url
API_KEY = open(API_KEY_path).read()
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"

def getJson(inputurl):
    # create auth object
    auth = HTTPBasicAuth(API_KEY, API_KEY)
    headers = {'User-Agent': user_agent}
    # get response from search url
    try:
        response_data_t = requests.get(inputurl, headers=headers, auth = auth, verify=False, timeout=10)
        json_result_t = response_data_t.json()
    except requests.RequestException as e:
        json_result_t = None
        print "There is a connection error. Please check your Internet Connection and run this code later."
    return json_result_t
    
# get first 50 results and get result count
#the offset requested for the starting point of results . The default is zero.

skip = 0 
url = formURL(skip)
json_result_1 = getJson(url)
if json_result_1 is None:
    quit()

result_count_1 = int(json_result_1['d']['results'][0]['WebTotal'])
print 'The initial result count is %r' % (result_count_1) #6100

search_result_url_1 = []
for k in json_result_1['d']['results'][0]['Web']:
    search_result_url_1.append(k['Url'])

###############################
#Now I'm ready to scrape all result!
def getPage(page):
    skipp = 50*(page-1)
    url = formURL(skipp)
    json_result_p = getJson(url)
    if json_result_p is None:
        datap = None
    else:
        result_count_p = json_result_p['d']['results'][0]['WebTotal']
        search_result_url_p = []
        for k in json_result_p['d']['results'][0]['Web']:
            search_result_url_p.append(k['Url'])
        datap = {'result_count':result_count_p, 'search_result_url':search_result_url_p}
    return datap

search_result_url = [search_result_url_1]
result_count = [result_count_1]

for k in range(2, result_count_1/50+2):
    search_result_t = getPage(k)
    if search_result_t is None:
        print "There is a connection error. Please check your Internet Connection and run this code later."
        quit()
    else:
        search_count_t = search_result_t['result_count']
        search_result_url_t = search_result_t['search_result_url']
        if (search_count_t == '') and (len(search_result_url_t)==0):
            print "page %r is blank" % (k)
            break
        else:
            search_result_url.append(search_result_url_t)
            result_count.append(search_count_t)
            print "page %r obtained" % (k)

# for Steven Pinker, ... page 21 obtained, page 22 is blank, essentially only 1050 results, not 6100   
# to see this, print result_count, the 1st to the 20th element of result_count is 6100
# while the 21st element of result_count is 1000
# len(search_result_url[20]) #49 slightly smaller than 50

################################
##save result
amazonUrlsGeneric = sum(search_result_url, [])
#len(amazonUrlsGeneric) #1099
amazonUrlsGeneric = list(set(amazonUrlsGeneric))

data2 = {'query': q0, 'amazonUrls': amazonUrlsGeneric}

fileName = result_path + recommender.replace(' ', '_')+'_BING.json'

with open(fileName, 'w') as fp:
    json.dump(data2, fp)
    
#try reloading saved data and print to screen
json_data = open(fileName).read()
datata = json.loads(json_data)
for ele in datata['amazonUrls']:
    print ele

print "%r unique urls obtained for %r" %(len(datata['amazonUrls']), recommender) 
