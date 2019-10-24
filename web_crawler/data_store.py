from collections import defaultdict
import json

class DataStore:
   def __init__(self):
      self.documents = []
      self.tf = []
      self.idf = dict()
      self.count = 1


   def store_idf(self):
      'Store the idf table to hard drive'
      
      # Store idf
      with open(f'data/idf.json', 'w') as f:
         f.write(json.dumps(self.idf))

   def add_document(self, document, html, url):
      '''
      Add a document for storage.
      The document is a list of tokens.
      Simultaneously compute documents's tf-idf table.
      '''

      tf = defaultdict(int)
      checked = defaultdict(bool)
      most_frequent = ""

      # Compute term frequency (tf) table of the document and update global inverse term frequency table (idf)
      for term in document:
         if not checked[term]:
            self.idf[term] += 1
            checked[term] = True
         tf[term] += 1
         if tf[term] > tf[most_frequent]:
            most_frequent = term

      # Use raw frequency divided by the raw frequency of the most occurring term in the document to prevent a bias towards longer documents
      for k in tf.keys():
         tf[k] /= tf[most_frequent]    #TODO: check if this is the correct tf-idf formula

      # Add the new document with its url, html content and tf table
      new_doc = {
         'url': url,
         'html': html,
         'tf': tf
      }
      self.documents.append(new_doc)   # THIS MIGHT CAUSE MEMORY ERRORS AND MIGHT NEED TO BE COMMENTED 
      
      # Store document
      with open(f'webs/{self.count}.json', 'w') as f:
         f.write(json.dumps(new_doc))
      self.count += 1