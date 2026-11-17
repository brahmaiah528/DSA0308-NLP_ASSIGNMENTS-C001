
import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')
nltk.download('omw-1.4')

word = input("Enter a word: ")

synsets = wordnet.synsets(word)

if synsets:
    print("\nSynsets of", word, ":")

    for syn in synsets:
        print("\nSynset:", syn.name())
        print("Meaning:", syn.definition())
        print("Examples:", syn.examples())
        print("Synonyms:", [lemma.name() for lemma in syn.lemmas()])
else:
    print("No synsets found for the given word.")
