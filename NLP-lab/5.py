import nltk
from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["playing", "played", "plays", "studies",
         "studying", "running", "happiness", "connected"]

print("Original Word\tStemmed Word")

for word in words:
    print(word, "\t\t", ps.stem(word))
