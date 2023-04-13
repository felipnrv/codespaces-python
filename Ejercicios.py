print("Hello world")
#Comentarios 
"""Comentarios
Test
"""
user="felipe"
#f sirve para dar formato y que se imprima la variable 
print(f'{user}')
#2 ejercicio 
nom="felipe"
apellido="garcia"
variable="Mi nombre es {} y mi apellido {}".format(nom,apellido)
print(variable)
# 3 ejercicio
lives=4
lives -=1
print(lives)
#(%) Modulo o Residuo
#(//) Division con valor entero
#(**) Exponenciación
y=4.161592653589793
x=2.001213456789
y_str=format(y,".2g")
print(y_str)

tolerancia=0.00001
print(abs(y-x)>tolerancia)

txt="Hola y chao"
print("Hola" in txt)

size=len('hello world    ')
print(size)

print(txt.swapcase())
print(txt.startswith('Ho'))
print(txt.endswith('ao'))
print(txt.replace('Hola','Adios'))
print(txt.capitalize())

text="Hola mundo"
print(text[0])
print(text[1])
print(text[1:5])
print(text[:10])
#Da saltos en el texto
print(text[1:5:2])

types=[1,2,3,4,5,'z',7,'y',9,'x']
print(types)
