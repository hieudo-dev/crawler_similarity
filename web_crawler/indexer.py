
# Abstract definition for a document Indexer
class Indexer:
   def __init__(self, parameter_list):
      raise NotImplementedError

   def index(self, parameter_list):
      raise NotImplementedError


#------------------- IMPLEMENTATIONS -------------------

# Invertex Index Indexer
class InvertedIndex:
   def __init__(self):
      pass

   def index(self, parameter_list):
      pass
   

# Other types of Indexers can be implemented and used interchangeably as long as they implement the methods defined by the class Indexer.