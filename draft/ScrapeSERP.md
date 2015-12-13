# Notes on Scraping SERP
SERP is the abbreviation for 'search engine result page'.
  
## Background
In our project, our ultimate goal is: given a recommender's name, we want to find all books
on Amazon for which the recommender's name appears in the 'Editorial Review' section.

We discomposed the project into several steps, the first one is: given a recommender's name, 
to acquire a list of amazon urls which point to books that are possible to have the recommender
as an Editorial Reviewer.

The way to achieve this sub-goal is through scraping SERP

## Scraping SERP is different from scraping static webpages
### 1. Headers are essential
### 2. Knowledge of Proxies are required
Almost all search engines restrict the number of page downloads from each user, AOL is no
exception. 
Proxies can be necessary when web scraping because some websites restrict the number of page downloads from each user. With proxies it looks like your requests come from multiple users so the chance of being blocked is reduced.

Most people seem to first try collecting their proxies from the various free lists such as this one and then get frustrated because the proxies stop working. If this is more than a hobby then it would be a better use of your time to rent your proxies from a provider like packetflip, USA proxies, or proxybonanza. These free lists are not reliable because so many people use them.

Each proxy will have the format login:password@IP:port
The login details and port are optional. Here are some examples:

bob:eakej34@66.12.121.140:8000
219.66.12.12
219.66.12.14:8080

https://webscraping.com/blog/How-to-use-proxies/
   
