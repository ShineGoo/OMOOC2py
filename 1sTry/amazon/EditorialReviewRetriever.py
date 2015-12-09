######################################################
# use bootlenose
import bottlenose
from lxml import etree

text=open('amazonAPIkeys.txt')
x=text.read().split('\n')
text.close()

AWS_ACCESS_KEY_ID = x[0] #my access key
AWS_SECRET_ACCESS_KEY = x[1] #my secret access key 
AWS_ASSOCIATE_TAG = x[2] #my associate tag

amazon = bottlenose.Amazon(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ASSOCIATE_TAG)

def retrieveER(ISBN):
    response = amazon.ItemLookup(ItemId=ISBN, ResponseGroup="EditorialReview", 
                                 SearchIndex="Books", IdType="ISBN")
    return response
    
def parseER(raw):
    root = etree.fromstring(raw)   
    for item in root[1][1:]:
        print(etree.tostring(item[1]))
        print('\n')
    
    
parseER(retrieveER('0787996491'))
parseER(retrieveER('0230613519'))
# neither search generates desirable result
    
#########################################################
from bs4 import BeautifulSoup
import requests

def retrieveER_bs(ISBN):
    urlo = 'http://www.amazon.com/gp/product/'
    url = urlo + ISBN + '/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content)
    f = soup.findAll('div', attrs={'class':'productDescriptionWrapper'})
    for ele in f:
        print(ele.text)
        
retrieveER_bs('0787996491')
retrieveER_bs('0230613519')

#issue with beautifulsoup: sometimes not all editorial reviews are showen on the 
#product page, user has to click a "read all editorial reviews" and then be redirected
#to another page where the originally hidden editorial reviews are shown. This 'hidden'
#part appears to be unscrapable for me. See book 0787996491 for an example, and relevant
#webpage looks like:
#</div>
#<div class="seeAll">
#<a href="http://www.amazon.com/gp/product/product-description/0787996491">See all Editorial Reviews</a>
#</div> </div>
#see 0787996491 as an example


#need to refine the scrapper: identify the h3 with class "productDescriptionSource" immediately
#preceding the div with class "productDescriptionWrapper", in order to distinguish real 
#editorial reviews from product description and author info. See 0230613519 as an example

##############################################################
ISBNid = raw_input("input the ISBN, two examples are 0787996491 and 0230613519\n")
retrieveMethod = raw_input("input 'bot' for useing bottlenose, input 'bs' for using beautifulsoup\n")
if retrieveMethod == 'bot':
    parseER(retrieveER(ISBNid))
elif retrieveMethod == 'bs':
    retrieveER_bs(ISBNid)
else:
    print('Bye')