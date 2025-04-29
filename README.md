# Expresion-Gramatical

El lenguaje Gerudo es una lengua construida ficticia, inspirada en la cultura del pueblo Gerudo de la serie *The Legend of Zelda*. Esta implementación formaliza su gramática y vocabulario, permitiendo su análisis sintáctico mediante herramientas como NLTK.

## ✨ Características generales

### ✍️ Composición gramatical

El lenguaje Gerudo se estructura mediante una **gramática libre de contexto (CFG)**, compuesta por los siguientes elementos principales:

- **S (Sentence / Oración)**: Representa una oración completa, que se compone de un sintagma nominal (**NP**) seguido de un sintagma verbal (**VP**).
- **NP (Noun Phrase / Sintagma Nominal)**: Incluye sujetos, objetos o complementos nominales. Puede estar formado por:
  - Un pronombre (**Pron**)
  - Un sustantivo (**N**)
  - Un determinante seguido de un sustantivo (**Det N**)
  - Una combinación de determinante, sustantivo y complemento preposicional (**Det N PP**)
  - Un nombre posesivo (**PossN**)
- **VP (Verb Phrase / Sintagma Verbal)**: Expresa la acción. Puede ser:
  - Un verbo solo (**V**)
  - Un verbo con objeto directo (**V NP**)
  - Un verbo con preposición (**V PP**)
  - Un verbo con múltiples complementos preposicionales (**VP PP**)
- **PP (Prepositional Phrase / Sintagma Preposicional)**: Frase iniciada por una preposición (**P**) seguida de un sintagma nominal o posesivo (**NP | PossN**).
- **Det (Determinante)**: Palabras que introducen sustantivos y determinan su referencia.
- **N (Nombre o Sustantivo)**: Palabras que representan personas, objetos o conceptos.
- **Pron (Pronombre)**: Sustituyen a los nombres propios o comunes.
- **PossN (Nombre Posesivo)**: Indica pertenencia.
- **V (Verbo)**: Expresa acciones o estados.
- **P (Preposición)**: Palabras que relacionan un sustantivo con otra parte de la oración.

---

## 🎤 Fonética

El lenguaje Gerudo tiene una fonética suave, caracterizada por:
- Alta presencia de vocales suaves: **a, o, u**
- Consonantes predominantes: **v, s, d, g, j, k, q**
- Sílabas frecuentes: **va, so, ju, ve, da, no**

---

## 🧪 Construcción del léxico y gramática

Debido a la escasa información canónica disponible, se recurrió a la **improvisación controlada** para expandir el vocabulario. Este proceso incluyó:
1. Combinación morfológica de raíces conocidas (ej: *vaba + ani = vabani*, "mi cosa").
2. Asignación fonética coherente para mantener estética uniforme.
3. Creación desde cero de palabras basadas en sonidos frecuentes.

El resultado es un vocabulario funcional documentado en el archivo *"Diccionario Gerudo - Español"*.

---

## 🔹 Gramática Gerudo (resumen formal)
La gramática utilizada contiene recursividad a la izquierda y ambigüedad, lo que fue un reto para los analizadores sintácticos. Se muestra aquí antes del proceso de transformación:

### Versión inicial (con ambigüedad):
```bnf
S -> NP VP
NP -> Pron | N | Det N | Det N PP | PossN
PP -> P NP | P PossN
VP -> V | V NP | V PP | VP PP
Det -> 'vaba' | 'ju' | 'vai' | 'voe' | 'vehvi' | 'vadu' | 'geruta' | 'devado' | 'sotvad'
N -> 'vaba' | 'ju' | 'vai' | 'voe' | 'vehvi' | 'vadu' | 'geruta' | 'devado' | 'sotvad'
Pron -> 'ani' | 'eso' | 'yaafu' | 'yaava'
PossN -> 'vabani' | 'juso' | 'vadufu'
V -> 'sareqso' | 'sosorq' | 'vurqso' | 'daraqso' | 'katvso' | 'sotreqso'
P -> 'ager' | 'no' | 'vaq' | 'sha' | 'mahno' | 'solno'
```
### 🌪️ Árboles de análisis mostrando ambigüedad (antes de eliminar recursividad a la izquierda)
```bnf
            S
  __________|____
 |               VP
 |     __________|____
 NP   VP              PP       
 |    |           ____|____     
 N    V          P       PossN 
 |    |          |         |    
 ju sosorq     mahno     vabani

            S
  __________|____
 |               VP
 |     __________|____
 |    |               PP
 |    |           ____|____
 NP   VP         |         NP
 |    |          |         |
 N    V          P       PossN
 |    |          |         |
 ju sosorq     mahno     vabani

            S
  __________|____
 |               VP
 |     __________|____
 NP   |               PP
 |    |           ____|____
 N    V          P       PossN
 |    |          |         |
 ju sosorq     mahno     vabani

            S
  __________|____
 |               VP
 |     __________|____
 |    |               PP
 |    |           ____|____
 NP   |          |         NP
 |    |          |         |
 N    V          P       PossN
 |    |          |         |
 ju sosorq     mahno     vabani
```


