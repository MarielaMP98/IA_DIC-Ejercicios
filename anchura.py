# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 01:19:11 2020
@author: marie
"""

import json
Grafo = False

with open ("arbol.json","r") as read_file:
    data = json.load(read_file)
    Arbol = data['Arbol']

recorrido =[]
fin =[]
 
def buscar(i, num, c):
    recorrido.append(i)
    if i==num:
        return (True,c)
    agregar(i)
    if len(fin)==0:
        return (False,c)
    return buscar(fin.pop(0),num,c+1)

def agregar(i):
    for a,b in Arbol.items():
        if b==i:
            fin.append(a)
 
res,c=buscar("15","15",1)

if res:
    print("Número encontrado")
else:
    print("Número no encontrado")
    
print(recorrido)
