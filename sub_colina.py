# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 22:09:58 2020
@author: marie
"""
import json
import random

from operator import itemgetter

with open('Conocimiento_colina.json') as file:
	Conocimiento = json.load(file)

ruta=[]
camino=[]
sig = []

def sub_colina(i,v,ant):
	ruta.append(i)
	print("La ruta inicial es "+i)
	print("La ruta anterior es " + ant)
	if sig:
		del sig[:]
		del camino[:]
	if v == i:
		print("Valor encontrado")
		return i
	if ant == "":
		ant = i
	for valor in Conocimiento:
		if valor[0] == i:
			if ant != "":
				if valor[1] != ant:
					camino.append(valor)
	print(min(camino, key=itemgetter(2))[:])
	print (camino)
	Min = (min(camino, key=itemgetter(2))[2])
	
	for c in camino:
		if c[2] == Min:
			print("entra")
			sig.append(c)
	print("Valores")
	print(sig)
	cont = 0
	for n in sig:
		cont = cont +1
		if cont > 1:
			r = random.random()
			print("n")
			print(n)
			if r < 0.5:
				sig.pop()
			else: 
				sig.pop(0)
		else:
			print(sig)
	if sig:
		for n in sig:
			print("nodo")
			print(n[1])
			return sub_colina(n[1],v,i)


colina=sub_colina("A","H","")
if colina:
	print("nodo")
	print(colina)
	print("ruta")
	print(ruta)
