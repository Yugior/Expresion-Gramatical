#Horacio Villela Hernandez A01712206 28/04/2025

import nltk
from nltk import CFG
nltk.download('punkt')

# Define a context-free grammar
# Se quito en VP -> VP PP Para la ambiguedad 
grammar = CFG.fromstring("""

S -> NP VP
NP -> Pron | N | Det N | Det N PP | PossN
PP -> P NP | P PossN
VP -> V | V NP | V PP
Det -> 'vaba' | 'ju' | 'vai' | 'voe' | 'vehvi' | 'vadu' | 'geruta' | 'devado' | 'sotvad'
N -> 'vaba' | 'ju' | 'vai' | 'voe' | 'vehvi' | 'vadu' | 'geruta' | 'devado' | 'sotvad'
Pron -> 'ani' | 'eso' | 'yaafu' | 'yaava'
PossN -> 'vabani' | 'juso' | 'vadufu'
V -> 'sareqso' | 'sosorq' | 'vurqso' | 'daraqso' | 'katvso' | 'sotreqso'
P -> 'ager' | 'no' | 'vaq' | 'sha' | 'mahno' | 'solno'


""")

# Create a parser with the defined grammar
parser = nltk.ChartParser(grammar)

# Input sentence to be parsed
sentence = "ju sosorq mahno vabani"

# Tokenize the sentence
tokens = sentence.split()


# Parse the sentence
for tree in parser.parse(tokens):
    tree.pretty_print()