# Web crawler
This program consists of 2 sub-programs:
- One is a basic web crawler implemented using Python 3 and the Scrapy library (**web_crawler/**).
- The other program is a Python script that can be used to make queries on the scraped websites; Given an URL fetch the corresponding webpage, rank the scraped websites according to their similarity to the query and return the top M (**query.py**).

## Features
- Compliance with Politeness policies *(Scrapy's feature)*
- Depth First Order URL Frontier  *(can be tweaked in web_crawler/web_crawler/settings.py)*
- Crawls up to a depth of 10 levels  *(can be tweaked in web_crawler/web_crawler/settings.py)*
- Uses Spacy models to calculate document similarity

## Requirements
- NLTK stopwords (execute with python **nltk.download('stopwords')**)
- NLTK WordNet (execute with python **nltk.download('wordnet')**)
- Scrapy (install with **pip install scrapy**) 
- NLTK (install with **pip install nltk**) 
- Spacy (install with **pip install spacy**)
- Spacy's spanish model (install with **python -m spacy download es_core_news_sm**) 


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