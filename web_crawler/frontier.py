
# Abstract class definition for an URL Frontier
class URLFrontier:
   def __init__(self, parameter_list):
      raise NotImplementedError

   # Remove from frontier and return the next URL to be fetched
   def popURL(self, parameter_list):
      raise NotImplementedError

   # Add an URL to the frontier
   def addURL(self, parameter_list):
      raise NotImplementedError

   # Returns the size of the Frontier
   def size(self, parameter_list):
      raise NotImplementedError


#------------------- IMPLEMENTATIONS -------------------

# An URL frontier using first in first out policy
class FIFOFrontier:
   def __init__(self):
      self.q = []

   # Remove from frontier and return the next URL to be fetched
   def popURL(self):
      return self.q.pop(0)

   # Add an URL to the frontier
   def addURL(self, url):
      self.q.append(url)

   # Returns the size of the Frontier
   def size(self):
      return len(self.q)


# Other types of URL frontiers that sorts the documents using a priority function can be implemented and used interchangeably as long as they implement the 3 methods defined by the class URLFrontier.