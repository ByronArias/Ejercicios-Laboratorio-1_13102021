# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 19:24:32 2021

@author: Byron Arias
"""

print('Empezando a trabajar con Python')
print('Realizado por: Byron Arias')
print('\n')
print('\n')
print('Consultando los tipos de valores:')
print('\n')
print('El tipo de dato de 875 es:')
print(type(875)) #comando utilizado para evaluar 1er valor
print('\n')
print('El tipo de dato de 4.89 es:')
print(type(4.89)) #comando utilizado para evaluar 2do valor
print('\n')
print('El tipo de dato del texto Now is better than never. es:')
print(type('Now is better than never.')) #comando utilizado para evaluar 3er valor
print('\n')
print('El tipo de dato de 1.32 es:')
print(type(1.32)) #comando utilizado para evaluar 4to valor
print('\n')
print('El tipo de dato de 5+8i es:')
print(type(complex(5,8))) #comando utilizado para evaluar 4to valor
print('\n')
print('¿El valor 5+8i corresponde a un valor entero?')
print(isinstance(complex(5,8),int))#imprime la comparacion 
print('\n')
print('¿El valor 8.2 corresponde a un valor entero?')
print(isinstance(8.2,int))#imprime la comparacion
print('\n')
print('¡El texto: Readability count, corresponde a un string?')
print(isinstance('Readability counts',str))#imprime la comparacion
