
import spacy

nlp = spacy.load("en_core_web_sm")

text = "Sundar Pichai is the CEO of Google. He was born in India."

doc = nlp(text)

print("Input Text:", text)
print("\nNamed Entities:")

for ent in doc.ents:
    print(ent.text, "->", ent.label_)
