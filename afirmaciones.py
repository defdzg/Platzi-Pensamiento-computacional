"""
Afirmaciones
Programación defensida
Puede utilizarse para verificar qu elos tipos sean correctos en una función
También sirve para hacer debuging
"""

# assert <expersión booleana>, <mensaje de error>

def primera_letra(lista_de_palabras):
    primeras_letras = []
    
    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, 'No se permiten str vacios'
        
        primeras_letras.append(palabra[0])
        
    return primeras_letras
    