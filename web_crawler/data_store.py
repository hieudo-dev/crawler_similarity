from collections import defaultdict
import json

class DataStore:
   def __init__(self):
      self.documents = []

   def store_data(self):
      'Store the documents to hard drive'
      
      # IF THERE ARE RAM ISSUES SAVE DOCUMENTS TO SEPARATE JSON FILES 
      with open(f'data/docs.json', 'w') as f:
         f.write(json.dumps(self.documents))

   def add_document(self, document, html, url):
      '''
      Add a document for storage.
      The document is a list of tokens.
      '''

      # Add the new document with its url and terms content
      new_doc = {
         'url': url,
         'content': ' '.join(document)
      }
      self.documents.append(new_doc)