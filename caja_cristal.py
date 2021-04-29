"""
Pruebas de caja de cristal
Se basan en el flujo del programa
Prueba todos los caminos posibles de una función.
    Ramificaciones, bubles for y while, recursión.
Regression testing o mocks.
Se considera que ya hay código escrito.
"""

import unittest

def mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False
    
class CajaDeCristalTest(unittest.TestCase):
    
    def test_si_mayor(self): 
        # Preparación
        edad = 20
        # Prueba
        resultado = mayor_de_edad(edad)
        # Verificación
        self.assertEqual(resultado, True)
    
    def test_no_mayor(self):
        edad = 16
        resultado = mayor_de_edad(edad)
        self.assertEqual(resultado, False)

if __name__ == '__main__':
    unittest.main()