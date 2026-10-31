import nltk
from nltk.stem import PorterStemmer

# Create Porter Stemmer object
ps = PorterStemmer()

# List of words
words = ["playing", "played", "plays", "studies",
         "studying", "running", "happiness", "connected"]

# Perform stemming
print("Original Word\tStemmed Word")

for word in words:
    print(word, "\t\t", ps.stem(word))
