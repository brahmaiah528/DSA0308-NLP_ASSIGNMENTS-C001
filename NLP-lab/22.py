
import spacy

nlp = spacy.load("en_core_web_sm")

text = input("Enter a text: ")
doc = nlp(text)

for token in doc:
    if token.pos_ == "PRON":
        print("Pronoun:", token.text)
        print("Possible Reference:", token.head.text)
