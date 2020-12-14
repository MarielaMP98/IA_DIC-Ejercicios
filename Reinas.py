# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 19:07:59 2020
@author: marie
"""
Mat =[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
posicion=[]
valor = 0
posiciones = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def inicio(reinas, Mat, valor,posiciones):
    contened = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    cont = 0
    print("Reinas " + str(reinas))
 
    if reinas == 1:
        return res(Mat)
    else: 
        for i in range(len(Mat)):
            for r in range(len(Mat[i])):
                if cont == 0:
                    if posiciones[i][r] != 3:
                        if(Mat[i][r] == 0):
                            if reinas == 4:
                                posiciones[i][r] = 3
                            Mat[i][r] = 1
                            cont = cont + 1
                            posicion.append([i,r])

        Mat = iterar(Mat,posicion)

        posicion.pop(0)
        for i in Mat:
            if 0 in i:
                valor = 0
            else:
                valor = 1
        if valor == 1:
            print(valor)
            for i in contened:
                print(i)
            reinas=4
            valor=0
            return inicio(reinas,contened,valor,posiciones)
        if valor == 0:
            print(valor)
            reinas=num_reinas-1
            return inicio(reinas,Mat,valor,posiciones)

def iterar(Mat,posicion):
    a = posicion[0][0]
    b = posicion[0][1]
    r = range(len(Mat))
    b2 = b
    b1 = a
    print(posicion)
    
    for i in range(len(Mat)):
        for r in range(len(Mat[i])):
            Mat[a][r] = 2
            Mat[i][b] = 2
    imp(Mat)
    for i in range(len(Mat)):
        b2 = b2-1
        b1 = b1 -1
        if (b2 >= 0)and(b1 >=0):
            print("- -")
            Mat[b1][b2] = 2
    b2 = b
    b1 = a
    imp(Mat)
    for i in range(len(Mat)):
        b1 = b1 +1
        b2 = b2 +1
        if (b1 <= r)and(b2 <= r):
            print("+ +")
            Mat[b1][b2] = 2

    b2 = b
    b1 = a
    imp(Mat)
    for i in range(len(Mat)):
        b2 = b2+1
        b1 = b1 -1
        if (b2 < r)and(b1 >=0):
            print("+ -")
            Mat[b1][b2] = 2
    b2 = b
    b1 = a
    imp(Mat)
    for i in range(len(Mat)):
        b2 = b2-1
        b1 = b1 + 1
        if (b2 >= 0)and(b1 <r):
            print("- +")
            Mat[b1][b2] = 2
    Mat[a][b]=1
    imp(Mat)
    return Mat
    

def res(Mat):
    for i in range(len(Mat)):
        for r in range(len(Mat[i])):
            if (Mat[i][r]) == 0:
                 Mat[i][r] = 1
    print()
    for i in Mat:
        print(i)

def imp(Mat):
    for i in Mat:
        print(i)
inicio(4,Mat,0,posiciones)