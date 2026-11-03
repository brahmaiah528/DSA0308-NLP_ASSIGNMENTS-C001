import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

text = "The student is learning Python programming."

words = nltk.word_tokenize(text)

pos_tags = nltk.pos_tag(words)

print("Words and POS Tags:")

for word, tag in pos_tags:
    print(word, "->", tag)
