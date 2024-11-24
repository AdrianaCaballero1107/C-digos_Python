# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:04:38 2024

@author: Adriana
"""
import random
import time
def Insertion_Sort(arr):
    n = len(arr)
    for i in range(1, n):
        aux = arr[i]
        j = i -1
        while j>=0 and aux < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = aux
    return None
        
#ejemplo de uso
#arr = [8,4,3,7,6]
arr = [random.randint(1,500) for i in range(1000)]
#medir el tiempo de ejecucion
star_time = time.time()
print(Insertion_Sort(arr))
#termine de ordenar el arreglo
end_time = time.time()
#mostrar el tiempo de ejecucion
print(f"Ordenar {len(arr)} numeros lleva: ")
print("Tiempo de ejecucion: {:.6f} segundos ".format(end_time - star_time))