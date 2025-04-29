#Horacio Villela Hernandez A01712206 28/04/2025

import nltk
from nltk import CFG
nltk.download('punkt')

# Define a context-free grammar
grammar = CFG.fromstring("""


S -> NP VP

VP -> VSimple
VP -> VCompuesto
VP -> VConPP

VSimple -> V
VCompuesto -> V NP
VConPP -> V NP PP
VConPP -> V PP

NP -> Pron
NP -> N
NP -> Det N
NP -> Det N PP
NP -> P PossN

PP -> P NP



Det -> 'vaba' | 'ju' | 'vai' | 'voe' | 'vehvi' | 'vadu' | 'geruta' | 'devado' | 'sotvad' |

N -> 'vaba' | 'ju' | 'vai' | 'voe' | 'vehvi' | 'vadu' | 'geruta' | 'devado' | 'sotvad' | 'vabani' | 'relva' | 'juv'  | 'julo' | 'viri' 

Pron -> 'ani' | 'eso' | 'yaafu' | 'yaava'

PossN -> 'vabani' | 'juso' | 'vadufu'

V -> 'sareqso' | 'sosorq' | 'vurqso' | 'daraqso' | 'katvso' | 'sotreqso' | 'lumaqso' | 'ramaqso' 

P -> 'ager' | 'no' | 'vaq' | 'sha' | 'mahno' | 'solno' | 'mahn' 

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
