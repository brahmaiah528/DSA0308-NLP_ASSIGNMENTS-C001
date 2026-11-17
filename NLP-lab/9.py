
import re

def pos_tag(sentence):
    words = re.findall(r'\b\w+\b', sentence)
    tagged_words = []

    for word in words:
        if re.match(r'^(a|an|the)$', word, re.I):
            tag = "DET"
        elif re.match(r'.*ing$', word, re.I):
            tag = "VERB"
        elif re.match(r'.*ly$', word, re.I):
            tag = "ADV"
        elif re.match(r'.*ous$|.*ful$|.*able$', word, re.I):
            tag = "ADJ"
        elif re.match(r'.*ed$', word, re.I):
            tag = "VERB"
        else:
            tag = "NOUN"

        tagged_words.append((word, tag))

    return tagged_words

sentence = "The beautiful girl is playing happily"

print("Input Sentence:", sentence)
print("\nPOS Tagged Output:")

for word, tag in pos_tag(sentence):
    print(word, "->", tag)
