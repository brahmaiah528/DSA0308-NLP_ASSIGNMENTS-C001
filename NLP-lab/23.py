
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = input("Enter a paragraph: ")

sentences = [s.strip() for s in text.split('.') if s.strip()]

if len(sentences) < 2:
    print("Enter at least two sentences")
else:
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(sentences)

    similarity = cosine_similarity(matrix)

    score = sum(
        similarity[i][i + 1]
        for i in range(len(sentences) - 1)
    ) / (len(sentences) - 1)

    print("Coherence Score:", round(score, 3))

    if score > 0.3:
        print("Text is coherent")
    else:
        print("Text has low coherence")
