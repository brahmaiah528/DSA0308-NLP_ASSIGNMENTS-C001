
training_data = [
    [("The", "DET"), ("cat", "NOUN"), ("runs", "VERB")],
    [("A", "DET"), ("dog", "NOUN"), ("barks", "VERB")],
    [("The", "DET"), ("dog", "NOUN"), ("eats", "VERB"), ("food", "NOUN")],
    [("A", "DET"), ("cat", "NOUN"), ("eats", "VERB"), ("fish", "NOUN")]
]

word_tag_counts = {}
tag_counts = {}

for sentence in training_data:
    for word, tag in sentence:
        word = word.lower()
        word_tag_counts[(word, tag)] = word_tag_counts.get((word, tag), 0) + 1
        tag_counts[word] = tag_counts.get(word, 0) + 1

def pos_tag(sentence):
    words = sentence.split()
    tagged_words = []

    for word in words:
        word_lower = word.lower()
        best_tag = "NOUN"
        max_probability = 0

        for (w, tag), count in word_tag_counts.items():
            if w == word_lower:
                probability = count / tag_counts[word_lower]

                if probability > max_probability:
                    max_probability = probability
                    best_tag = tag

        tagged_words.append((word, best_tag))

    return tagged_words

sentence = "The cat eats fish"

print("Input Sentence:", sentence)
print("\nPOS Tagged Output:")

for word, tag in pos_tag(sentence):
    print(word, "->", tag)
