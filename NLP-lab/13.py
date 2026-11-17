
import nltk
from nltk import CFG
from nltk.tree import Tree

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'cat' | 'dog'
V -> 'chased' | 'saw'
""")

sentence = "the cat chased a dog".split()

parser = nltk.ChartParser(grammar)

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
