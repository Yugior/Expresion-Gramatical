#Horacio Villela Hernandez A01712206 28/04/2025



## Se debe tomar en consideracion que el script preente solo despliega las oraciones, su traduccion correspondiente y el tipo de palabra usada en la oracion. 
## En caso de requerir nuevas palabras para probar la expresion gramatical, deberan buscar las palabras desde el diccionario y agregarlas manualmente
"""
Este módulo contiene ejemplos de oraciones traducidas del español al gerudo,
una lengua ficticia basada en patrones definidos por el usuario.

Cada oración incluye:
- Texto en español
- Traducción en gerudo
- Análisis gramatical
"""

# Lista de oraciones con traducción y análisis
oraciones = [
    {
        "espanol": "Yo alabo",
        "gerudo": "ani sareqso", # Valido
        "analisis": "Pronombre + Verbo"
    },

      {
        "espanol": "Yo alabo",     
         "gerudo": "sareqso ani", # Rechazado: comienza con verbo, no hay NP antes de VP
        "analisis": "Pronombre + Verbo"
    },
   
    {
        "espanol": "Esa niña tiene una espada",
        "gerudo": "jug vehvi vurqso vaim vermi", # Valido
        "analisis": "Determinante + Nombre + Verbo + Determinante + Nombre"
    },

     {
        "espanol": "Esa niña tiene una espada",
        "gerudo": "jug vurqso vaim vermi",  # Rechazado: "jug" sin nombre asociado
        "analisis": "Determinante + Nombre + Verbo + Determinante + Nombre"
    },

    {
        "espanol": "El guardia  comercia con su abuela",
        "gerudo": "ane geruda sotreqso ager vabani", # Valido
        "analisis": "Determinante + Nombre + Verbo + Posesivo + Nombre"
    },

    {
        "espanol": "El guardia protege con su abuela",
        "gerudo": "ane vadu daraqso ager",  # Rechazado: "ager" sin objeto de la preposición
        "analisis": "Determinante + Nombre + Verbo + Preposision + Posesivo + Nombre"
    },


    {
        "espanol": "Ellos alaban la luna",
        "gerudo": "yaavaa sareqso ane devado", # Valido
        "analisis": "Pronombre + Verbo + Determinante + Nombre"
    },

    {
        "espanol": "Ellos alaban la luna",
        "gerudo": "yaavaa sareqso aska devado",  # Rechazado: Palabra "aska" inexistente
        "analisis": "Pronombre + Verbo + Determinante + Nombre"
    },

    {
        "espanol": "La mujer canta debajo de la aldea",
        "gerudo": "ane vai lumaqso mahno geruta", # Valido
        "analisis": "Determinante + Nombre + Verbo + Preposición + Nombre"
    },

    {
        "espanol": "La mujer canta debajo de la aldea ",
        "gerudo": "vai vai lumaqso mahno geruta",  # Rechazado: "vai vai" es ambiguo, doble nombre
        "analisis": "Determinante + Nombre + Verbo + Preposición + Nombre"
    },

    {
        "espanol": "Ese niño juegan con fuego",
        "gerudo": "jug vehvi ramaqso mahno viri", # Valido
        "analisis": "Determinante + Nombre + Verbo + Preposición + Nombre"
    },

    {
        "espanol": "Ese niño juegan con fuego",
        "gerudo": "jug vehvi ramaqso vaba viri",  #Rechazado: "vaba" es un nombre y no una Preposición
        "analisis": "Determinante + Nombre + Verbo + Preposición + Nombre"
    }
]

def mostrar_oraciones():
    """
    Muestra todas las oraciones con su traducción y análisis.
    """
    for i, oracion in enumerate(oraciones, start=1):
        print(f"{i}. Español: {oracion['espanol']}")
        print(f"   Gerudo: {oracion['gerudo']}")
        print(f"   Análisis: {oracion['analisis']}\n")

if __name__ == "__main__":
    mostrar_oraciones()
