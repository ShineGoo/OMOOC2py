# Amazon API Resources
  
## Introduction
此次要使用的Amazon API全名"Amazon Product Advertising API", 原名"Associates Web Service （AWS）",
现在很多相关的库及教程仍使用AWS的称呼。
   
## Python库
### 1. [官方资源](https://aws.amazon.com/python/)

### 2. [python-amazon-product-api](https://pypi.python.org/pypi/python-amazon-product-api/)
* 经试用可以进行连接与基本查询（待补充代码）
* [documentation](http://python-amazon-product-api.readthedocs.org/en/latest/index.html#)
* 试用时使用的code：
  * 安装：```$ sudo pip install python-amazon-product-api```
  * 创建amazon api credentials 文件： 
    ```localhost:~ apple$ touch .amazon-product-api
        localhost:~ apple$ vim .amazon-product-api
  在vim编辑器中编辑文件```.amazon-product-api```的内容，编辑好的内容如下：
     ```localhost:~ apple$ cat .amazon-product-api
        [Credentials]
        access_key = XXXX-XXXX-XXXX
        secret_key = XXXXXXXXXXXXXXXXXXX
        associate_tag = XXXXXXXXXXXXXX
  * 进入python，试用python-amazon-product-api
     
        >>> from amazonproduct import *
        >>> api = API(locale='us')
        >>> items = api.item_search('Books', Publisher="O'Reilly")
        >>> items
        >>> type(items)
   最后一条命令返回值为<class 'amazonproduct.processors._lxml.SearchPaginator'>
   

### 3. [Boto3](https://aws.amazon.com/sdk-for-python/)
在aws.amazon.com上官方给出的AWS SDK(Software Development Kit)，但时还未尝试。
   
### 4. [bootlenose](https://github.com/lionheart/bottlenose)
试用成功
    >>> import bottlenose
    >>> AWS_ACCESS_KEY_ID = 'XXXX-XXXX-XXXX' #my access key
    >>> AWS_SECRET_ACCESS_KEY = 'XXXXXXXXXXXXXXXXXXX' #my secret access key
    >>> AWS_ASSOCIATE_TAG = 'XXXXXXXXXXXXXX' #my associate tag
    >>> amazon = bottlenose.Amazon(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ASSOCIATE_TAG)
    >>> response = amazon.ItemLookup(ItemId="0596520999", ResponseGroup="Images",
    ... SearchIndex="Books", IdType="ISBN")
    >>> type(response)
最后一条命令返回值为 <type 'str'>


## 连接API所需的credentials
1. AWS Access Key ID
2. AWS Secret Key
   * [documentation](http://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html)
   * 在[这个网址]中使用我原有的amazon购物用的邮箱与秘密登陆，然后在section"Your Security Credentials"
     中找到 AWS Access Key ID
   * As described in a previous announcement, you cannot retrieve the existing secret 
     access keys for your AWS root account, though you can still create a new root 
     access key at any time. 创立新access key id的时候可以看见对应的secret key。
3. AWS associate tage
即亚马逊联盟的ID，需申请。申请时需先选择所在地区，先申请了中国区的，美国区需电话验证所以目前为申请。
AWS associate tage申请入口：
http://docs.aws.amazon.com/AWSECommerceService/latest/DG/becomingAssociate.html

## [the EditorialReview response group](http://docs.aws.amazon.com/AWSECommerceService/latest/DG/RG_EditorialReview.html)
* The EditorialReview response group returns Amazon's review of the item, which appears on 
  the Product Detail page for each item in the response.

* Note: Copyrighted editorial reviews are not returned. For this reason, the reviews 
  returned may be different than those returned by Amazon.com. This is a very point, see 
  the example below:
  Use the following code to retrieve Editorial Reviews for book with id 031606792X:
  ```resp2 = amazon.ItemLookup(ItemId='031606792X', ResponseGroup='EditorialReview')```
  Recall that resp2 is a string. looking for tag 'EditorialReviews' gives two editorial reviews:
  one is the production description itself, the other one is "Amazon.com Review".
  
  now visit page http://www.amazon.com/gp/product/031606792X?ie=UTF8&isInIframe=1&n=283155&redirect=true&ref_=dp_proddesc_0&s=books&showDetailProductDesc=1#iframe-wrapper,
  we can see that there are three editorial reviews. The first one it "Amazon.com Review",
  which is the same as the API returns. However the other two editorial reviews "Form 
  Publishers Weekly" and "From School Library Journal" can be seen on the webpage but is not
  returned by the API. The reason for this is that both editorial reviews end with "All 
  rights reserved." and thus are copyrighted.
  
  So we need to keep it in mind that copyrighted editorial reviews won't be return by the API.
  
* Big difference between EditorialReview and [Reviews](http://docs.aws.amazon.com/AWSECommerceService/latest/DG/RG_Reviews.html), as response groups. 
  For RG (abbreviation for Response Group) Reviews, the sole returned value is a URL to an 
  iframe that contains customer reviews. The only way (among all ways I can think of) to view
  the actual content of reviews is to embed the iframe on a web page by doing ```<iframe src="reviews_iframe_url" />```.

  With the iframe URL, I can view the content of reviews in the browser as an iframe, but
  how can I scrape the text content of the reviews with the iframe URL? I did a lot of web
  searching but find no result.
  
  Luckily, RG EditorialReviews returns readable texts other than iframe. 
  
  Still, I'd very much to learn if the reviews can be scrapped, with the iframe url in hand.  

## 其他  
### 1. Vim
想要在terminal中编辑.amazonXXX，使用text editor ```vim```。关于vim的操作，参考了[这个资料]
(http://stackoverflow.com/questions/5764071/how-to-use-vim-in-the-terminal)

* You can pass a filename as an option and it will open that file, e.g. ```vim main.c.```
* Press "a" to start INSERT mode (in append after cursor mode, which is what you are probably used to).
* To leave INSERT mode, press “Esc”.
* To save your file, use “:w.” To save and exit, use “:x”.
