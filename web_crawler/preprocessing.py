from nltk.stem import WordNetLemmatizer 
from nltk.tokenize import RegexpTokenizer
import nltk
from bs4 import BeautifulSoup


# This method defines how documents are preprocessed

# Create Lemmatizer
lemmatizer = WordNetLemmatizer() 

# Create tokenizer
tokenizer = RegexpTokenizer("\w+")

# Spanish stop words list
sw = nltk.corpus.stopwords.words('spanish')


def Preprocess(text):
   '''
   Returns documents token list 
   Tokens are lemmatized
   Stop words are removed
   '''
   
   # Tokenize document
   tokens = tokenizer.tokenize(text)

   # Loop through tokens and
   # - convert to lower case
   # - remove Stop Words
   # - lemmatize words
   words = []
   for word in tokens:
      w = word.lower()
      if w in sw:
         continue
      words.append(lemmatizer.lemmatize(w))

   return words


# Method to get text from html files
def GetText(html):
   soup = BeautifulSoup(html)

   # kill all script and style elements
   for script in soup(["script", "style"]):
      script.extract()    # rip it out

   # get text
   text = soup.get_text()

   # break into lines and remove leading and trailing space on each
   lines = (line.strip() for line in text.splitlines())
   # break multi-headlines into a line each
   chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
   # drop blank lines
   text = '\n'.join(chunk for chunk in chunks if chunk)

   return text