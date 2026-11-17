
import nltk
from nltk import CFG

grammar = CFG.fromstring("""
S -> NP_SG VP_SG | NP_PL VP_PL
NP_SG -> 'he' | 'she' | 'the boy'
NP_PL -> 'they' | 'we' | 'the boys'
VP_SG -> 'runs' | 'plays'
VP_PL -> 'run' | 'play'
""")

parser = nltk.ChartParser(grammar)

sentences = [
    "he runs",
    "they run",
    "she plays",
    "the boys play",
    "he run"
]

for sentence in sentences:
    words = sentence.split()
    trees = list(parser.parse(words))

    if trees:
        print(sentence, "-> Correct Agreement")
    else:
        print(sentence, "-> Incorrect Agreement")
