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
         'https://es.wikipedia.org/wiki/Procesamiento_de_lenguajes_naturales',
         'https://es.wikipedia.org/wiki/Aprendizaje_autom%C3%A1tico',
         'https://es.wikipedia.org/wiki/B%C3%BAsqueda_y_recuperaci%C3%B3n_de_informaci%C3%B3n',
         'https://es.wikipedia.org/wiki/Modelo_de_espacio_vectorial'
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

      # Limit of pages to crawl
      if self.count >= 10000:
         return

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

      # WRITE CURRENT LINK TO FILE -- TEST
      filename = f'current'
      with open(filename, 'w') as f:
         f.write(str(self.count) + " " + url)
         self.count += 1

      print('\n\n')