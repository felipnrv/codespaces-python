import random

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

types.insert(0,'a')
print(types)

"""append(): Añade un ítem al final de la lista.
clear(): Vacía todos los ítems de una lista.
extend(): Une una lista a otra.
count(): Cuenta el número de veces que aparece un ítem.
index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
insert(): Agrega un ítem a la lista en un índice específico.
pop(): Extrae un ítem de la lista y lo borra.
remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
reverse(): Le da la vuelta a la lista actual.
sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor."""

#Tuplas son similares a las listas pero no se pueden modificar
tupla=(1,2,3,4,5,6,7,8,9,10)
rand=random.choice(tupla)
print(rand)

my_dict = {
    'avion': 'objeto volador',
    'name': 'Javier',
    'last_name': 'Sepulveda',
    'age': 109
}

print(my_dict)

#el tamanio del diccionario
print(len(my_dict))
#imprimiendo una llave 
print(my_dict['age'])
#La funcion get, si no existe el valor sale un mensaje none(Maneja el error)
# Se cambian los corchetes por parentesis(), ya que get es una funcion de python
print(my_dict.get('test'))
print('name' in my_dict)
print('other' in my_dict)

list=('1','3','5','7','9')
for element in list:
    print(element)

list1={'Uno':1,
       'Tres':3,
       'Cinco':5,
       'Siete':7,
       'Nueve':231
       }

for element in list1:
    print(list1[element]) #Si se pone solo el element imprime las llaves

for key,value in list1.items():
    print(key,value)



