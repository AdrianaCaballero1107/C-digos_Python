# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 17:43:34 2024

@author: Adriana
"""
import time
#fibonacci
def fibonacci_1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_1(n-1) + fibonacci_1(n-2)
        
numerito =30
inicio = time.time()
print(f"El factorial de {numerito} es {fibonacci_1(numerito)}")
fin = time.time()
print(f"El tiempo de ejecucion es: {fin - inicio} s")