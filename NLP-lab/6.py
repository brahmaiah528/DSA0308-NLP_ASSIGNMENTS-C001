import random

text = "I love machine learning. I love python programming. Machine learning is interesting."

words = text.lower().replace(".", "").split()

bigrams = {}

for i in range(len(words) - 1):
    first = words[i]
    second = words[i + 1]

    if first not in bigrams:
        bigrams[first] = []

    bigrams[first].append(second)

word = "i"
result = [word]

for i in range(10):
    if word not in bigrams:
        break

    word = random.choice(bigrams[word])
    result.append(word)

print("Generated Text:")
print(" ".join(result))
