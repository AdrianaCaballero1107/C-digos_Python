# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:43:42 2024

@author: Adriana
"""
def Busqueda_Binaria(lista, elemento):
    #si la lista esta vacia, retomar -1
    if not lista:
        return -1
    #calcular el punto medio de la lista
    medio = len(lista)//2 #int(len(lista) / 2)
    
    #verificar si el elemneto esta en el medio
    if lista[medio] == elemento:
        return medio
    
    #si el elemento es mayor, buscar en la mitad derecha
    elif lista[medio] < elemento:
        lista_derecha = lista[medio + 1 :]
        #buscar el elemnto en la sublista derecha
        subresultado = Busqueda_Binaria(lista_derecha, elemento)
        
        #si el elemnto se encuentra en la sublista derecha
        #ajustar el indice
        if subresultado != -1:
            return medio + 1 + subresultado
        #ajustar indice con la posicion del subarreglo
        else:
            return -1
    #si el elemento es menor, buscar en la mitad izquierda
    else:
        return Busqueda_Binaria(lista[:medio], elemento)
    
    #ejemplo de uso, recordar que la lista debe estar ordenada
lista = [2,3,5,7,11,13,17,19,23,29,31]
elemento_a_buscar = 18
resultado = Busqueda_Binaria(lista, elemento_a_buscar)

#imprimir mensajes basados en el resultado de la busqueda
if resultado != -1:
    print (f"El elemento {elemento_a_buscar} esta en el indice: {resultado}")
else:
    print(f"El elemento {elemento_a_buscar} no esta en la lista")
    
    
    
    
    
    
    
