import scrapy
from scrapy import signals
from scrapy.exceptions import CloseSpider
from scrapy.xlib.pydispatch import dispatcher
from preprocessing import Preprocess
from data_store import DataStore
   
   
LIMIT = 1000

class WebSpider(scrapy.Spider):    
   name = "web"

   def __init__(self):
      dispatcher.connect(self.spider_closed, signals.spider_closed)
      self.dstore = DataStore()   

   # Scrapy's method to start crawling
   def start_requests(self):
      # Seed URLs
      urls = [
         'https://es.wikipedia.org/wiki/Procesamiento_de_lenguajes_naturales',
         'https://es.wikipedia.org/wiki/Aprendizaje_autom%C3%A1tico',
         'https://es.wikipedia.org/wiki/B%C3%BAsqueda_y_recuperaci%C3%B3n_de_informaci%C3%B3n',
         'https://es.wikipedia.org/wiki/Modelo_de_espacio_vectorial'
      ]

      # Start crawling process
      for u in urls:
         yield scrapy.Request(url=u, callback=self.parse)

      # Set scraped count to 0
      self.count = 0

   # Crawling Algorithm
   def parse(self, response):
      ''' This method is called repeatedly to process documents from the URL frontier.

      Scrapy handles compliance of Politeness policies    
      '''

      url = response.request.url

      # Remove html tags from the document
      raw_text =''.join(response.xpath("//body//text()").extract()).strip()

      # Preprocess the document's content
      tokens = Preprocess(raw_text)

      # Add document to be stored in local storage
      if self.count < LIMIT:
         self.dstore.add_document(tokens, response.body, url)

      # Extract url references and add them to the url frontier
      for a in response.css('a'):
         if 'href' in a.attrib:
            yield response.follow(a, callback=self.parse)

      # Limit of pages to crawl
      if self.count > LIMIT:
         raise CloseSpider(reason='reached_limit')    # Force spider to close

      print(str(self.count) + '\n\n')     # IGNORE/COMMENT THIS
      
      self.count += 1
      

   def spider_closed(self, spider):
      # Store scraped documents when spider finishes crawling
      self.dstore.store_data()