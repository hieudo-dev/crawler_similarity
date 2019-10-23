
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

   # Returns whether the Frontier is empty
   def isEmpty(self, parameter_list):
      raise NotImplementedError