
import re

def initial_tag(word):
    if re.match(r'^(a|an|the)$', word, re.I):
        return "DET"
    elif word.endswith("ing"):
        return "NOUN"
    else:
        return "NOUN"

def transform_tag(word, tag):
    if word.endswith("ing"):
        tag = "VERB"
    elif word.endswith("ly"):
        tag = "ADV"
    elif word.endswith("ed"):
        tag = "VERB"
    elif word.endswith(("ous", "ful", "able")):
        tag = "ADJ"

    return tag

def pos_tag(sentence):
    words = sentence.split()
    tagged_words = []

    for word in words:
        tag = initial_tag(word)
        tag = transform_tag(word, tag)
        tagged_words.append((word, tag))

    return tagged_words

sentence = "The boy is playing happily"

print("Input Sentence:", sentence)
print("\nPOS Tagged Output:")

for word, tag in pos_tag(sentence):
    print(word, "->", tag)
