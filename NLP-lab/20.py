
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Python is a programming language",
    "Machine learning uses Python",
    "Natural language processing is useful"
]

query = input("Enter search query: ")

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(documents + [query])

scores = cosine_similarity(tfidf[-1], tfidf[:-1]).flatten()

for i in scores.argsort()[::-1]:
    print("Document:", documents[i])
    print("Score:", round(scores[i], 3))
