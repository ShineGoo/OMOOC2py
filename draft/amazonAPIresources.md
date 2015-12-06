# Amazon API Resources
  
## Introduction
此次要使用的Amazon API全名"Amazon Product Advertising API", 原名"Associates Web Service （AWS）",
现在很多相关的库及教程仍使用AWS的称呼。
   
## Python库
### 1. [官方资源](https://aws.amazon.com/python/)

### 2. [python-amazon-product-api](https://pypi.python.org/pypi/python-amazon-product-api/)
   经试用可以进行连接与基本查询（待补充代码）
   * [documentation](http://python-amazon-product-api.readthedocs.org/en/latest/index.html#)

### [Boto3](https://aws.amazon.com/sdk-for-python/)
   在aws.amazon.com上官方给出的AWS SDK(Software Development Kit)，但时还未尝试。
   
### [bootlenose](https://github.com/lionheart/bottlenose)
   试了一下，查询时会报错。还未再次尝试。

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
      AWS associate tage申请入口：http://docs.aws.amazon.com/AWSECommerceService/latest/DG/becomingAssociate.html

## 其他  
### Vim
   想要在terminal中编辑.amazonXXX，使用text editor ```vim```。关于vim的操作，参考了[这个资料]
   (http://stackoverflow.com/questions/5764071/how-to-use-vim-in-the-terminal)

   * You can pass a filename as an option and it will open that file, e.g. ```vim main.c.```
   * Press "a" to start INSERT mode (in append after cursor mode, which is what you are probably used to).
   * To leave INSERT mode, press “Esc”.
   * To save your file, use “:w.” To save and exit, use “:x”.
