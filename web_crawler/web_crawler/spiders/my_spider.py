import scrapy
from preprocessing import Preprocess
from data_store import DataStore

class WebSpider(scrapy.Spider):    
   name = "web"
   dstore = DataStore()   

   # Scrapy's method to start crawling
   def start_requests(self):
      # Seed URLs
      urls = [
         'http://quotes.toscrape.com/page/1/'
      ]

      # Start crawling process
      for u in urls:
         yield scrapy.Request(url=u, callback=self.parse)

      self.count = 0

   # Crawling Algorithm
   def parse(self, response):
      ''' This method is called repeatedly to process documents from the URL frontier.

      Scrapy handles compliance of Politeness policies    
      '''

      url = response.request.url

      # Remove html elements from the document
      raw_text =''.join(response.xpath("//body//text()").extract()).strip()

      # Preprocess the document's content
      tokens = Preprocess(raw_text)

      # Compute document's informations and store it in the local storage
      self.dstore.add_document(tokens, response.body, url)

      # Extract url references and add them to the url frontier
      for a in response.css('a'):
         yield response.follow(a, callback=self.parse)

      # WRITE LINKS TO FILE -- TEST
      filename = f'webs/links'
      with open(filename, 'w') as f:
         f.write(str(self.count) + " " + url)
         self.count += 1