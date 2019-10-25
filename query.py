from os import listdir
from os.path import isfile, join
from collections import defaultdict
from math import log
import heapq
import json
import requests
from web_crawler.preprocessing import Preprocess


# Length of documents collection
N = 11000

if __name__ == "__main__":
   # URL used to check for similarities
   url = 'https://es.wikipedia.org/wiki/Procesamiento_de_lenguajes_naturales'
   
   # Fetch html of the query url
   r = requests.get(url)
   query_raw_text = r.text

   # Preprocess query document
   query_document = Preprocess(query_raw_text)

   # Retrieve idf table
   idf = None
   with open('web_crawler/data/idf.json', 'r') as f:
      idf = json.loads(f.read())

   # Compute term frequency (tf) table of the given url and update global inverse term frequency table (idf)
   checked = defaultdict(bool)
   query_tf = defaultdict(int)
   most_frequent = ""
   for term in query_document:
      if not checked[term]:
         idf[term] += 1
         checked[term] = True
      query_tf[term] += 1
      if query_tf[term] > query_tf[most_frequent]:
         most_frequent = term

   # Use raw frequency divided by the raw frequency of the most occurring term in the document to prevent a bias towards longer documents
   for k in query_tf.keys():
      query_tf[k] /= query_tf[most_frequent]    #TODO: check if this is the correct tf-idf formula


   #-------------------------- DOCUMENTS RANKING ----------------------------------------------- 

   # Get a list of documents in local storage
   path = 'web_crawler/webs/'
   documents = [f for f in listdir(path) if isfile(join(path, f))]

   # Compute the tf-idf vector of the query document
   query_tf_idf = []
   for term, doc_freq in idf.keys():
      query_tf_idf.append(query_tf[term] * log(N / doc_freq))

   # Load each document in storage and compare with query document
   heap = []
   for path in documents:
      with open(doc, 'r') as f:
         doc = json.loads(f.read())
      
      # Compute the tf-idf vector of the current document
      cur_tf_idf = []
      for term, doc_freq in idf.keys():
         cur_tf_idf.append(doc['tf'][term] * log(N / doc_freq))

      # Compute cosine similarity
      similarity_coef = 0 #TODO:

      # Add to heap for sorting
      heapq.heappush(heap, (similarity_coef, doc['url'], doc['html']))

      # Keep top 1000 documents only
      if len(heap) > 1000:
         heapq.heappop(heap)
