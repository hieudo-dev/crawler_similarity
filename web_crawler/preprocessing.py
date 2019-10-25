from nltk.stem import WordNetLemmatizer 
from nltk.tokenize import RegexpTokenizer
import nltk


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