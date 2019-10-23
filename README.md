# Web crawler
This is a basic web crawler implemented using Python 3 and the Scrapy library.

## Features
- Compliance with Politeness policies *(Scrapy's features)*
- Depth First Order URL Frontier  *(web_crawler/web_crawler/settings.py)*
- Crawls up to a depth of 20 levels  *(web_crawler/web_crawler/settings.py)*
- Inverted Index Indexer

##     Crawling algorithm
Generic crawling algorithm followed by this program

```python
AddURL(URL_frontier, URL_seeds) 
while !empty URL_frontier
   url = Pop(URL_frontier) 
   page = Fetch(url) 
   Index(page)
   url_list = extract_urls(page)
   filtered_urls = Filter(url_list)
   for each url in filtered_urls
      AddURL(URL_frontier, url)
```

This algorithm is implemented in */web_crawler/spiders/my_spider.py*