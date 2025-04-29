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
        "espanol": "Yo voy",
        "gerudo": "ani sareqso",
        "analisis": "Pronombre + Verbo"
    },
   
    {
        "espanol": "La niña tiene una espada",
        "gerudo": "ju voe vurqso vaba vai",
        "analisis": "Determinante + Nombre + Verbo + Determinante + Nombre"
    },
    {
        "espanol": "El guerrero protege su tribu",
        "gerudo": "voe vadu daraqso vabani",
        "analisis": "Determinante + Nombre + Verbo + Posesivo + Nombre"
    },
    {
        "espanol": "Nosotros hablamos con respeto",
        "gerudo": "yaava katvso mahno geruta",
        "analisis": "Pronombre + Verbo + Preposición + Nombre"
    },
    {
        "espanol": "Ellos miran a la luna",
        "gerudo": "eso sareqso ager devado",
        "analisis": "Pronombre + Verbo + Preposición + Nombre"
    },
    {
        "espanol": "La reina canta en la torre",
        "gerudo": "voe relva lumaqso mahn juv",
        "analisis": "Determinante + Nombre + Verbo + Preposición + Nombre"
    },
    {
        "espanol": "Los niños juegan con fuego",
        "gerudo": "voe julo ramaqso mahno viri",
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
