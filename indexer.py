
# Abstract definition for a document Indexer
class Indexer:
   def __init__(self, parameter_list):
      raise NotImplementedError

   def index(self, parameter_list):
      raise NotImplementedError