def sumar(n):
    return n+n
def restar(n):
    return n-n
def multiplicar(n):
    return n*n
def dividir(n):
    return n/n
def modulo(n):
    return n%n

def operacion(f,nums):
    resultados = []
    for numero in nums:
        resultado = f(numero)
        resultados.append(resultado)
    print(resultados)
        
nums = [1,2,3,4,5]
operacion(sumar,nums)
