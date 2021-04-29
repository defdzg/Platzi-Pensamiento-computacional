"""
Pruebas de caja negra
Se basan en la especificación de la función o el programa
Prueba inputs y valida outputs
Unit testing: probar función por función cada módulo (componente) del código.
Integration testing: probar que todos los módulos funcionan entre si.
"""

# Caja negra
# Suite test
# Test driven development
import unittest
from unittest import result # Módulo de Python que permite generar pruebas

def suma(num_1, num_2):
    return num_1 +  num_2

def resta(num_1, num_2):
    return num_1 -  num_2

class CajaNegraText(unittest.TestCase):
    
    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5
        
        resultado = suma(num_1,num_2)
        
        self.assertEqual(resultado, 15)
        
    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7
        
        resultado = resta(num_1, num_2)
        
        self.assertEqual(resultado, -3)
        
if __name__ == '__main__':
    unittest.main()