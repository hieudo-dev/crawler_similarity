import heapq
import json
import requests
import spacy
from web_crawler.preprocessing import Preprocess


# Length of documents collection
N = 10000

# Query result size
M = 100

if __name__ == "__main__":
   # URL used to check for similarities
   url = 'https://es.wikipedia.org/wiki/Procesamiento_de_lenguajes_naturales'
   
   # Fetch html of the query url
   r = requests.get(url)
   query_raw_text = r.text

   # Preprocess query document
   query_document = Preprocess(query_raw_text)

   # Load documents list
   documents = []
   with open('web_crawler/data/docs.json', 'r') as f:
      documents = json.loads(f.read())

   #-------------------------- DOCUMENTS RANKING ----------------------------------------------- 

   # Load spacy spanish language model
   nlp = spacy.load('es_core_news_sm')

   # Process query document
   query_nlp = nlp(' '.join(query_document))

   # Load each document in local storage and compare with query document
   heap = []
   s = 0
   for doc in documents:
      # Print amount of processed documents
      print(s)
      s += 1

      # Process current document
      cur_nlp = nlp(doc['content'])

      # Compute cosine similarity
      similarity_val = query_nlp.similarity(cur_nlp)

      # Add to heap for sorting
      heapq.heappush(heap, (similarity_val, doc['url'], doc['content']))

      # Keep only top M documents
      if len(heap) > M:
         heapq.heappop(heap)

   # Store top M documents in results folder
   n = 1
   for sim_val, url, content in heap:
      with open(f'results/{n}.txt', 'w') as f:
         f.write(f'{str(sim_val)} {url} \n')
         f.write(content)
      n += 1