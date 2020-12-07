# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 11:20:56 2020
@author: marie
"""

import json
Grafo = False

with open ("Arbol.json","r") as read_file:
    data = json.load(read_file)
    Grafo = data['Arbol']

recorrido =[]
 
def buscar(i, num):
    recorrido.append(i)
    if i==num:
        return num
    for a,b in Grafo.items():
        if b==i:
            res =buscar(a,num)
            if res:
                return res
    recorrido.pop()
res = buscar("15","30")

if res:
    print("Numero encontrado")
else:
    print("Numero no encontrado")
print(recorrido)