# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:36:46 2024

@author: Adriana
"""
#clase nodo que representa cada nodo del arbol binario
class Cristian:
    """
    Inicializar un nuevo nodo con un valor especifico
    Parametros:
        v: Cualquier valor a almacenar en el nodo
    """
    def __init__(self, v):
        self.homo = None #referencia al hijo izquierdo del nodo
        self.hetero = None #referencia al hijo derecho del nodo
        self.elemento = v #dato o valor almacenado en el nodo
    
def Inorder(taro):
        """
        Realiza el recorrido inorden del arbol binario
        Imprime los nodos en el orden: I-R-D

        Parametros:
            taro: nodo raiz del arbol o subarbol a recorrer
        """
        if taro: # si el nodo actual no es nulo
        #recorrer el subarbol izquierdo
              Inorder(taro.homo)
            
            #visitar el nodo raiz
              print(taro.elemento, end=" ")
             
             #recorrer el subarbol derecho
              Inorder(taro.hetero)
              
def Preorder(taro):
    """
    Realiza el recorrido inorden del arbol binario
    Imprime los nodos en el orden: R-I-D

    Parametros:
        taro: nodo raiz del arbol o subarbol a recorrer
    """
    if taro: # si el nodo actual no es nulo
        #visitar el nodo raiz
          print(taro.elemento, end=" ")
          #recorrer el subarbol izquierdo
          Preorder(taro.homo)
         #recorrer el subarbol derecho
          Preorder(taro.hetero)
          
def Postorder(taro):
    """
    Realiza el recorrido inorden del arbol binario
    Imprime los nodos en el orden: I-D-R

    Parametros:
        taro: nodo raiz del arbol o subarbol a recorrer
    """
    if taro: # si el nodo actual no es nulo
    #recorrer el subarbol izquierdo
          Postorder(taro.homo)
         #recorrer el subarbol derecho
          Postorder(taro.hetero)
         #visitar el nodo raiz
          print(taro.elemento, end=" ")
#funcion principal que se ejecuta al correr el scrip
if __name__== "__main__":
    #construccion manual del arbol binario
    #nodo raiz del arbol
    groot = Cristian(12) #nodo raiz del arbol
    
    #cronstructor del subarbol izquierdo
    groot.homo = Cristian(7) #nodo izquierdo de la raiz 12
    groot.homo.homo = Cristian(4) #nodo izquierdo de la raiz 7
    groot.homo.homo.homo = Cristian(2) #nodo izquierdo de la raiz 4
    groot.homo.hetero = Cristian(9) #nodo derecho de la raiz 7
    groot.homo.hetero.homo = Cristian(8) # nodo izquierdo de la raiz 9
    groot.homo.hetero.hetero = Cristian(11) #nodo derecho de la raiz 9
    
    #cronstruccion del subarbol derecho
    groot.hetero = Cristian(21) #nodo derecho de la raiz 12
    groot.hetero.homo = Cristian(16) #nodo izquierdo de la raiz 21
    groot.hetero.hetero = Cristian(25)# nodo derecho de la raiz 21
    groot.hetero.homo.hetero = Cristian(19) #nodo derecho de la raiz 16
    
    #llamada a las funciones de recorrido
    print("Recorrido en inorder: ", end=" ")
    Inorder(groot) #imprime recorrido inorder
    print("Recorrido en preorder: ",end=" ")
    Preorder(groot)#imprime recorrido preorder
    print("Recorrido en Postorder: ", end=" ")
    Postorder(groot) #imprime 