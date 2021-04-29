"""
Defensive programming
Las excepciones se manajean con los keywords:
* try
* except
* finally
- Se pueden utilizar también para ramificar los programas
- No deben manejarse de manera silenciosa
- Aventar propia excepción utilizar *raise*
"""

def divide_elementos_de_lista(lista, divisor):
    try: #Keyword asegurarte que no tengas errores en tu código
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista
lista = list(range(10))
divisor = 0

print(divide_elementos_de_lista(lista, divisor))