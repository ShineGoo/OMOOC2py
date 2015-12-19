#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# using Amazon API to retrieve book attributes, including author name

import json
import bottlenose
import xml.etree.ElementTree as ET
import requests

recommender = "Gary_Klein"

text=open('amazonAPIkeys.txt')
keys=text.read().split('\n')
text.close()

AWS_ACCESS_KEY_ID = keys[0] #my access key
AWS_SECRET_ACCESS_KEY = keys[1] #my secret access key 
AWS_ASSOCIATE_TAG = keys[2] #my associate tag

amazon = bottlenose.Amazon(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ASSOCIATE_TAG)

def getbookurl(inputRecommender):
    fileName = inputRecommender + ".json"
    json_data = open(fileName).read()
    datat = json.loads(json_data)
    bookurllist = datat['amazonUrls']
    bookurllist = list(set(bookurllist))
    return bookurllist

def getbookattributes(inputasin):
    tag0 = '{http://webservices.amazon.com/AWSECommerceService/2011-08-01}'
    responset = amazon.ItemLookup(ItemId = inputasin, ResponseGroup = 'ItemAttributes',
                                  searchIndex = 'Books', IdType = "ASIN")
    tree = ET.ElementTree(ET.fromstring(responset))
    root = tree.getroot()
    Item = root.find(tag0 + 'Items').find(tag0+'Item')
    ItemAttributes = Item.find(tag0+'ItemAttributes')
    attributesCollection = {}
    for iattribute in ItemAttributes:
        attributesCollection[iattribute.tag.split(tag0)[1]] = iattribute.text
    return attributesCollection

x = getbookurl(recommender)
asin = x[7].split('/')[-1] #4 7 :ebook   
bookinfo = getbookattributes(asin)
bookinfo['Author'] #'Frank Partnoy'