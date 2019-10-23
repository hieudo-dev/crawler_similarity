import scrapy
from frontier import FIFOFrontier
from indexer import InvertedIndex


class WebSpider(scrapy.Spider):    
   name = "web"
   indexer = InvertedIndex()
   

   # Scrapy's method to start crawling
   def start_requests(self):
      # Seed URL; This will also be used to compute similarity rankings
      urls = [
         'http://quotes.toscrape.com/page/1/'
      ]

      # Start crawling process
      for u in urls:
         yield scrapy.Request(url=u, callback=self.parse)


   # Crawling Algorithm
   def parse(self, response):
      ''' This method is called repeatedly to process documents from the URL frontier.

      Scrapy handles compliance of Politeness policies    
      '''
      
      # Preprocess the url's html and keep raw text only 
      # TODO:lemmatization, stemming
      raw_text =''.join(response.xpath("//body//text()").extract()).strip()

      # Index the current document
      self.indexer.index((raw_text, response.request.url))
      
      # Extract url references and add them to the frontier
      for a in response.css('a'):
         yield response.follow(a, callback=self.parse)

      # WRITE TO FILE TESTS
      t = response.request.url
      filename = f'data/links'
      with open(filename, 'w') as f:
         f.write(t)