
import nltk
import spacy

nltk.download('punkt')

nlp = spacy.load("en_core_web_sm")

sentence = input("Enter a sentence: ")
doc = nlp(sentence)

print("Noun Phrases and Meanings:")

for chunk in doc.noun_chunks:
    print("Noun Phrase:", chunk.text)
    print("Root Word:", chunk.root.text)
    print("Meaning:", chunk.root.lemma_)
