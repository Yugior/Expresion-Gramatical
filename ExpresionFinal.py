# Horacio Villela Hernandez A01712206 28/04/2025   
# Actualizacion 21/05/2025
# Actualizacion 05/06/2025
# Nota: En caso de agregar palabras del diccionario al vocabulario, agrégalas en el apartado correspondiente o ocasionará ambigüedad al estar en dos estados en lugar de uno.

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

Det -> 'vana' | 'jug' | 'vaim' |'ane' 
N ->    'voe'|'vermi'|'vai' | 'vaba' | 'vehvi' | 'vadu' | 'geruda' | 'devado' | 'sotvad' | 'relva' | 'juv' | 'julo' | 'viri' | 'geruta'
Pron -> 'ani' | 'eso' | 'yaafu' | 'yaavaa' | 'esoen'
PossN -> 'vabani' | 'juso' | 'vadufu'
V -> 'sareqso' | 'sosorq' | 'vurqso' | 'daraqso' | 'katvso' | 'sotreqso' | 'lumaqso' | 'ramaqso' 
P -> 'ager' | 'no' | 'vaq' | 'sha' | 'mahno' | 'solno' | 'mahn' 

""")
# Create a parser with the defined grammar
parser = nltk.ChartParser(grammar)

# Input sentence to be parsed
sentence = "ane vai lumaqso mahno geruta"
# Tokenize the sentence
tokens = sentence.split()


# Parse the sentence
for tree in parser.parse(tokens):
    tree.pretty_print()
