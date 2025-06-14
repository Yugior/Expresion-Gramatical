# Expresion-Gramatical
## Horacio Villela Hernández  
## A01712206  
## 29/04/2025  

El lenguaje Gerudo es una lengua construida ficticia, inspirada en la cultura del pueblo Gerudo de la serie *The Legend of Zelda*. Esta implementación formaliza su gramática y vocabulario, permitiendo su análisis sintáctico mediante herramientas como NLTK.

##  Características generales

###  Composición gramatical

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

##  Fonética

El lenguaje Gerudo tiene una fonética suave, caracterizada por:
- Alta presencia de vocales suaves: **a, o, u**
- Consonantes predominantes: **v, s, d, g, j, k, q**
- Sílabas frecuentes: **va, so, ju, ve, da, no**

---

##  Construcción del léxico y gramática

Debido a la escasa información canónica disponible, se recurrió a la **improvisación controlada** para expandir el vocabulario. Este proceso incluyó:
1. Combinación morfológica de raíces conocidas (ej: *vaba + ani = vabani*, "mi cosa").
2. Asignación fonética coherente para mantener estética uniforme.
3. Creación desde cero de palabras basadas en sonidos frecuentes.

El resultado es un vocabulario funcional documentado en el archivo *"Diccionario Gerudo - Español"*. De igual forma se exhibe a continuacion un fragmento de el documento.

##  Determinantes y Sustantivos

| Gerudo  | Tipo     | Significado      | Origen / Composición |
|---------|----------|------------------|----------------------|
| ane   | Det / N  | la / el          | -                    |
| jug      | Det / N  | ese / cosa       | -                    |
| vaim     | Det / N  | una / uno        | -                    |
| voe     | Det / N  | hombre           | -                    |
| vai   | Det / N  | mujer            | -                    |
| vehvi   | Det / N  | niño/niña    | -                    |
| vermi   | Det / N  | espada            | -                    |
| devado   | Det / N  | luna            | -                    |
| vadu    | Det / N  | casa             | -                    |
| geruda  | Det / N  | guardia          | -                    |
| geruta  | Det / N  | aldea            | -                    |
| devado  | Det / N  | templo            | -                    |
| sotvad  | Det / N  | mercado           | -                    |

##  Pronombres

| Gerudo  | Tipo     | Significado      |
|---------|----------|------------------|
| ani     | Pron     | yo               |
| eso     | Pron     | tú               |
| yaafu   | Pron     | él / ella        |
| yaava   | Pron     | nosotros         |

##  Posesivos

| Gerudo  | Tipo     | Significado      | Compuesto de      |
|---------|----------|------------------|-------------------|
| vabani  | PossN    | mi abuela          | vaba + ani        |
| jugso    | PossN    | tu cosa          | ju + eso          |
| vadufu  | PossN    | su abuela         | vadu + yaava      |

##  Verbos

| Gerudo   | Tipo     | Significado      |
|----------|----------|------------------|
| sareqso  | V        | alabar          |
| vurqso   | V        | tener            |
| daraqso  | V        | caminar          |  
| katvso   | V        | construir         |
| lumaqso   | V        | cantar       |
| sotreqso | V        | comerciar         |

##  Preposiciones

| Gerudo  | Tipo     | Significado      |
|---------|----------|------------------|
| ager    | P        | con               |
| no      | P        | en               |
| vaq     | P        | hacia             |
| sha     | P        | para            |
| mahno   | P        | debajo de         |
| solno   | P        | sobre            |

### Análisis de ambigüedad y clasificación en la jerarquía de Chomsky

La gramática Gerudo, al presentar múltiples formas válidas de parsear ciertas oraciones, exhibe ambigüedad. Además, el uso de producciones con recursividad a la izquierda (`VP → VP PP`) añade complejidad al análisis sintáctico.

Esto posiciona a la gramática dentro del conjunto de gramáticas libres de contexto (Context-free) en la Jerarquía Extendida de Chomsky, como se muestra en la siguiente imagen:

Este tipo de gramáticas son suficientes para expresar la mayoría de las estructuras del lenguaje natural, aunque su ambigüedad requiere parsers más robustos (por ejemplo, "Earley" o "GLR" en lugar de "LL(1)").

El objetivo de este proyecto fue buscar un lenguaje que pudiera adaptarse a un análisis sintáctico de tipo "LL(1)". Sin embargo, debido a la ambigüedad presente, la gramática inicial no es adecuada para este tipo de parser sin ser transformada. Es por ello que se exploraron múltiples formas de derivación y se consideraron estrategias para eliminar la ambigüedad.

---

##  Gramática Gerudo 
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
Como se observa, existen varias formas diferentes de asociar los complementos PP al VP, lo que genera múltiples árboles de derivación (es decir, ambigüedad estructural).

Posteriormente, se eliminó la recursividad a la izquierda siguiendo técnicas estándar de transformación de gramáticas, similares a las utilizadas para expresar la precedencia de operadores en gramáticas matemáticas.

Nueva versión sin ambigüedad en VP:
```bnf

S -> NP VP
NP -> Pron | N | Det N | Det N PP | PossN
PP -> P NP | P PossN
VP -> V VP'
VP' -> NP VP' | PP VP' | ε
Det -> 'vaba' | 'ju' | 'vai' | 'voe' | 'vehvi' | 'vadu' | 'geruta' | 'devado' | 'sotvad'
N -> 'vaba' | 'ju' | 'vai' | 'voe' | 'vehvi' | 'vadu' | 'geruta' | 'devado' | 'sotvad'
Pron -> 'ani' | 'eso' | 'yaafu' | 'yaava'
PossN -> 'vabani' | 'juso' | 'vadufu'
V -> 'sareqso' | 'sosorq' | 'vurqso' | 'daraqso' | 'katvso' | 'sotreqso'
P -> 'ager' | 'no' | 'vaq' | 'sha' | 'mahno' | 'solno'

```
### ¿Por qué se eliminó la ambigüedad?

La ambigüedad surgía originalmente de la producción recursiva VP -> VP PP, que permitía infinitas formas de asociar complementos preposicionales (PP) a distintos niveles del VP, haciendo incierta la estructura. Al reformular VP como V VP', donde VP' se encarga de manejar opcionalmente complementos (NP o PP) de manera estrictamente secuencial y sin recursividad izquierda, se fuerza a que cada verbo tome un conjunto de complementos de manera determinista. Así, cada oración tiene una única forma de derivación sintáctica, eliminando las múltiples interpretaciones posibles.

###  Árbol corregido (estructura sin ambigüedad):

```bnf
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

En este proceso se denota también otro proceso de ambiguedad. Con esta informacion se procedió a eliminar la fuente, esta vez derivada de la producción PP:

#### Versión previa con ambigüedad:
```bnf
NP -> Pron | N | Det N | Det N PP | P PossN
PP -> P NP | P PossN
```
Se eliminó la regla "PP -> P PossN" y se conservó únicamente "PP -> P NP". Esto obliga a que las construcciones posesivas aparezcan únicamente dentro de un NP bien definido, removiendo así la bifurcación de interpretación de "PP".

#### Nueva forma sin ambigüedad:

```bnf
S -> NP VP
NP -> Pron | N | Det N | Det N PP | P PossN
PP -> P NP
VP -> V | V NP | V PP

            S
  __________|____
 |               VP
 |     __________|____
 NP   |               NP       
 |    |           ____|____     
 N    V          P       PossN 
 |    |          |         |    
 ju sosorq     mahno     vabani
```
Al eliminar la doble opción de derivación para PP, se evita que el analizador sintáctico deba decidir entre dos formas de reducir la misma cadena, y por tanto se elimina la ambigüedad.

------

##  Cómo y por qué se eliminó la recursividad a la izquierda al eliminar la ambigüedad

Durante el proceso de eliminación de ambigüedad en la gramática del lenguaje Gerudo, fue necesario también eliminar la recursividad a la izquierda, ya que era una de las principales fuentes de ambigüedad estructural.

### ¿Dónde estaba la recursividad a la izquierda?

La recursividad a la izquierda aparecía principalmente en la regla de **VP**:

```bnf
VP -> V | V NP | V PP | VP PP
```

La producción `VP -> VP PP` es recursiva a la izquierda, porque el símbolo `VP` aparece de nuevo como primer elemento de su propia definición. Esto permitía expandir infinitamente la regla, generando múltiples árboles sintácticos diferentes para la misma cadena de entrada, provocando ambigüedad.

### ¿Cómo se elimina?

Suponniendo que esta regla no fuera modificada,Se aplicaria el proceso estándar para eliminar recursividad a la izquierda:

1. Se identifica que `VP -> VP PP` causaba la recursividad.
2. Se reorganiza la producción de `VP` para que empezara siempre por un verbo (`V`), seguido opcionalmente de complementos (`NP` o `PP`).
3. Se introduce un nuevo no terminal `VP'` (VP prima) que se encarga de manejar secuencias opcionales de complementos:

```bnf
VP -> V VP'
VP' -> NP VP' | PP VP' | ε
```
Esto garantiza que no haya más auto-llamadas inmediatas a `VP` desde su primera posición, eliminando así la recursividad a la izquierda.

### ¿Por qué fue necesario eliminarla?

- Porque la recursividad a la izquierda impide construir árboles sintácticos de forma determinista en analizadores descendentes como los LL(1).
- En este caso estaba directamente relacionada con la ambigüedad, ya que múltiples interpretaciones surgían dependiendo de cómo se aplicaba la expansión `VP -> VP PP`.
- Al forzar una estructura donde primero siempre hay un verbo seguido de complementos de manera secuencial, se garantiza que solo exista un árbol sintáctico posible para cada oración, eliminando así tanto la recursividad a la izquierda como la ambigüedad.

------


## Clasificación de oraciones simples y compuestas

Durante la evolución de la gramática, se decidió detallar las estructuras de los sintagmas verbales dividiendo el no terminal `VP` en componentes más específicos:

```bnf
S -> NP VP

VP -> VSimple
VP -> VCompuesto
VP -> VConPP

VSimple -> V
VCompuesto -> V NP
VConPP -> V NP PP
VConPP -> V PP

            S
  __________|______
 |                 VP
 |                 |
 |             VCompuesto
 |     ____________|_______
 NP   |                    NP
 |    |             _______|____
 N    V            P          PossN
 |    |            |            |
 ju sosorq       mahno        vabani
```


Esta división permite clasificar oraciones según su complejidad verbal:

- **Oración simple**: Solo contiene un verbo (`VSimple`).
- **Oración compuesta o extendida**: Contiene un verbo con uno o más complementos (`VCompuesto` o `VConPP`).

### ¿Por qué se hizo esta clasificación?

1. **Claridad estructural**: Ayuda a comprender mejor el tipo de acción expresada y su grado de complejidad.
2. **Facilitación del análisis sintáctico**: La distinción permite una identificación más precisa y rápida del tipo de oración.
3. **Evolución hacia análisis semántico**: Al identificar si una oración es simple o compuesta, se allana el camino para un análisis semántico más fino (como el número de participantes en la acción).

Esta decisión también permitió refinar el conjunto de árboles sintácticos aceptables y redujo aún más los casos de ambigüedad al especificar más claramente las construcciones posibles en cada tipo de oración.

##  Complejidad de Archivos 


### Archivos analizados:
- `ExpresionGramatical.py`
- `Sinambiguedad1.py`
- `Sinambiguedad2.py`
- `ExpresionFinal.py`
- `ExpF.py`

---

### Complejidad computacional y estructural

#### 1. **Uso de gramáticas libres de contexto (CFG)**
Todos los archivos definen una gramática libre de contexto (CFG) utilizando el módulo `nltk` de Python. Estas gramáticas son procesadas mediante el algoritmo `ChartParser`, que emplea técnicas de parseo eficientes como "Earley parser" o "bottom-up chart parsing".

- **Complejidad temporal promedio del parser**: \( O(n^3) \) en el peor de los casos para frases ambiguas, donde \( n \) es la longitud de la cadena de entrada (tokens).
- **Complejidad espacial**: \( O(n^2) \) a \( O(n^3) \), dado que se almacenan sub-análisis parciales en una tabla (chart).

#### 2. **Tamaño de la gramática**
- Archivos como `ExpresionFinal.py` y `ExpF.py` presentan una gramática más completa y refinada con varias reglas alternativas para `VP`, `NP` y `PP`, lo que incrementa el número potencial de derivaciones, especialmente si se producen ambigüedades sintácticas.
- Los archivos `Sinambiguedad1.py` y `Sinambiguedad2.py` muestran versiones simplificadas que reducen ambigüedad al eliminar producciones como `VP -> VP PP` o `PP -> P PossN`.

#### 3. **Control de ambigüedad**
- El archivo `ExpresionGramatical.py` tiene variantes como `VSimple`, `VCompuesto` y `VConPP`, lo que permite modular la complejidad del predicado verbal.
- Se hace un manejo manual para prevenir ambigüedades (comentarios en `ExpF.py`: "ocasionará ambigüedad al estar en dos estados"). Esto evita que una palabra pertenezca simultáneamente a dos categorías gramaticales.

#### 4. **Validación de oraciones** (`ExpF.py`)
- Se agrega una función `validar_oraciones` que analiza una lista de oraciones desde `EjemplosFuncionales.py`. Esto representa una complejidad adicional de tipo \( O(m \cdot n^3) \), donde \( m \) es el número de oraciones.
- Aunque el parseo sigue siendo pesado en casos ambiguos, la validación está bien estructurada y permite automatizar pruebas sintácticas de forma efectiva.

---

##  Licencia

Este proyecto es educativo y no oficial. Inspirado por la serie *The Legend of Zelda*. Toda la lógica gramatical y vocabulario fueron diseñados para fines académicos.

## Archivos

- "ExpresionGramatical.py" Muestra la expresion original antes de quitar ambiguedad
- "Sinambiguedad1.py" Muestra la expresion al quitar la ambiguedad generada por "VP"
- "Sinambiguedad2.py" Muestra la expresion al quitar la amiguedad generada por "PP" luego de haber quitado la anterior
- "ExpresionFinal.py" Muestra la ultima edicion, permitiendo el uso de oraciones mas complejas
- "ExpF.py" Muestra casos de prueba a partir de las oraciones posibles de "ExpresionFinal.py"
- "Ejemplosfuncionales.py" Casos de muestra de oraciones que se ejecutan en Español y el idioma correspondiente
## Uso adecuado del programa

- Si bien en el dicionario pararecen mas tipos de palabras, por temas de complejidad solo se permiten las mostradas en la documentacion

- Tener en cuenta donde agregar palabras, el uso de los ejemplos de prueba se añadieron las palabras correspondientes una por una, de requerir una palabra que no este en los scripts
  Se les pide estar atentos al momento de elegir y colocar la palabra dentro de este, de lo contrario la oracion no sera aceptada por el programa

- Para evitar problemas con el programa se quitaron las comillas de las palabras debido al malfuncionamiento y errores que causaban, en caso de agregar nuevas palabras recuerden quitar las comillas
  en caso de ser necesario

  ## Actualización
  - Se modifico el archivo "ExpresionFinal.py" para corregir los siguientes errores.
    - Se mejoraron y agregaron comentarios adicionales
    - Caso de error de ambiguedad, causado a partir de duplicidad de palabras en posisiones incorrectas dentro de la expresión regular y a partir de un simbolo "|" extra en las    reglas terminales Det y Poss
  - Se agrego una funcion para el caso de pruebas junto a un nuevo archivo llamado "ExpF.py" Se recomienda usar este para correr las pruebas, en lugar de "ExpresionFinal.py", debido a que en este ultimo solo se ejecutan las pruebas de uno en uno
  - Se modifoco el archivo "Ejemplosfuncionales.py" para corregir lo siguiente.
    - Se agregaron comentarios a las pruebas
    - Se agregaron pruebas de rechazo y validas para corroborar la Expresion gramatical.
  - Se modifico el diccionario debido a varios errores
    - Exisitian palabras iguales con diferente signiicado ej(vanabi/abuela,vanabi/niñ@)
    - Falta de congruencia entre oraciones
    - Se mejoro y actualizo las tablas del diccionario (Cabe aclarar que no estan todas las palabras en el "Readme" o en "Diccionario.pdf" debido a la complejidad de modificar diferentes archivos, en caso de bscar una palabra en especifico, favor de checar ambos.)
  - Se agrego la explicacion de la complejidad en los archivos
  
## Bibliografia

Abril, R. R. (2024). La Jerarquía de Chomsky. La Máquina Oráculo. https://lamaquinaoraculo.com/deep-learning/la-jerarquia-de-chomsky/

Seiboz. (n.d.). Intro to the Fan-Expanded Gerudo Language (OC) : r/Breath_of_the_Wild. https://www.reddit.com/r/Breath_of_the_Wild/comments/oqnxat/intro_to_the_fanexpanded_gerudo_language_oc/

Seiboz. (n.d.). Brainstorming: Gerudo Verb System (Gerudo Language Fan Expansion Pt 2) : r/Breath_of_the_Wild. https://www.reddit.com/r/Breath_of_the_Wild/comments/p7ail8/brainstorming_gerudo_verb_system_gerudo_language/?utm_medium=android_app&utm_source=share
