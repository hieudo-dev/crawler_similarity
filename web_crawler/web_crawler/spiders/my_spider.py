import scrapy


class WebSpider(scrapy.Spider):    
   name = "web"
   

   # Scrapy's method to start crawling
   def start_requests(self):
      # Seed URLs
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
      
      # Extract url references and add them to the url frontier
      for a in response.css('a'):
         yield response.follow(a, callback=self.parse)

      # WRITE LINKS TO FILE -- TEST
      filename = f'data/links'
      with open(filename, 'w') as f:
         f.write(response.request.url)