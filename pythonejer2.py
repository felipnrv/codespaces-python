# import this #Imprime el Zen de Python

import random


''' Tuplas son similares a las listas pero no se pueden modificar se usa parentesis() 
Las listas son mutables se usa corchetes[]
En los direccionarios se usa llaves{} y sirven para guardar datos de forma clave-valor 
Set es el unico que no se puede repetir los valores,no es ordenado y 
no se puede acceder a los valores por indice ,se usa llaves{}'''
'''
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

'''

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
'''
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

matriz=[[1,2,3],
        [4,5,6],
        [7,8,9]]

print(matriz[0][1])

for row in matriz:
    print(row) # Imprime 1,2,3
    for column in row:
        print(column) # Imprime 1/2/3 ,todo para abajo

print((8 / 2) + 4 * 8)

elemt=[1,2,3,4,5,6,7,8,9,10]
for elem in elemt:
        print(elem)


set_paises = {'España', 'Francia', 'Alemania', 'Italia',
              'Portugal', 'España', 1, 1, 2, 3, 4.2, False}
# Imprime el conjunto de paises sin repetir, se puede colocar cualquier tipo de dato
print(set_paises)

set_string = set('Hola')
print(set_string)  # No se repiten las letras
# Se puede utilizar con tuplas y listas

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers) # Convierte el conjunto en lista
'''
'''add(): Añade un elemento.
update(): Añade cualquier tipo de objeto iterable como: listas, tuplas.
discard(): Elimina un elemento y si ya existe no lanza ningún error.
remove(): Elimina un elemento y si este no existe lanza el error “keyError”.
pop(): Nos devuelve un elemento aleatorio y lo elimina y 
si el conjunto está vacío lanza el error “key error”.
clear(): Elimina todo el contenido del conjunto.'''

'''
# Ejemplo de todos
set_paises.add('Suiza')
print(set_paises)
set_paises.update(['Suiza', 'Holanda', 'Belgica'])
print(set_paises)
set_paises.discard('Holanda')
print(set_paises)
set_paises.remove('Belgica')
print(set_paises)
set_paises.pop()
print(set_paises)
set_paises.clear()
print(set_paises)

set_a = {'Colombia', 'Peru', 'Ecuador', 'Venezuela', 'Chile'}
set_b = {'Argentina', 'Brasil', 'Paraguay', 'Uruguay', 'Chile'}

set_union = set_a.union(set_b)
print(set_union)
print(set_a | set_b)  # Otra forma de hacer union

set_union = set_a.intersection(set_b)
print(set_union)
print(set_a & set_b)  # Otra forma de hacer interseccion

set_union = set_a.difference(set_b)
print(set_union)
print(set_a - set_b)  # Otra forma de hacer diferencia

set_union = set_a.symmetric_difference(set_b)
print(set_union)
print(set_a ^ set_b)  # Otra forma de hacer diferencia simetrica

numbers=[]
for element in range (1,11):
    numbers.append(element)

print(numbers)

numbers_v2=[element * 2 for element in range (1,11)]
print(numbers_v2)

dict = {}
for i in range (1,11):
    dict[i]=i*2

print(dict)

dict = {dict[i]:i*2 for i in range (1,5)}

print(dict)

dictv2={i: i*2 for i in range(1,5)}
print(dictv2)
# stash es para guardar cambios pero sin hacer commit

countries={'Ec','Pe','Co','Gr','Fr'}
population={}

for country in countries :
    population[country]=random.randint(1,1000)

print(population)

names=['nico','zule','santi']
ages=[20,30,40]

"""{
    'nico':20,
    'zule':30,
    'santi':40

}"""

#ZIP retorna una lista de tuplas (x,y) 
print(list(zip(names,ages)))

new_dict={name:ages for (name,ages) in zip(names,ages)}
print(new_dict)

## Otro ejercicio

populationv2={country: random.randint(1,100) for country in countries }
print(populationv2)

result={country:population for (country,population) in populationv2.items() if population > 20}
print(result)

names=['nico','zule','santi']
age=[21,34,47]

print(list(zip(names,age)))

new_dict={names:ages for (names,age)in zip(names,age)}
print(new_dict)

text='Hola soy Felipe'
unique={c: c.upper() for c in text if c in 'aeiou' }
print(unique)
'''

'''def myprint():
    print('Hola mundo')
    print('Hola con todos')

myprint()

def myprintx2(text):
    print(text * 2)
    
myprintx2('Hola ')

x=10
y=30

c=x+y

def myprintsuma3 (x , y):
    myprintx2 ( x + y )

myprintsuma3(10,30)
myprintsuma3(2,5)

def sum_with_range (min,max):
    sum=0
    for x in range(min,max):
        sum += x
    return sum

result=sum_with_range(1,10)
print (result)
result2=sum_with_range(result , result+10)
print(result2)

#Las variables locales no se pueden modificar desde fuera de la funcion
#Las variables globales si se pueden modificar desde dentro de la funcion

price=100

def increment():
    price=200
    result=price+50
    print(result)
    return result

print(price)
price2 = increment()
print(price2)

#lambda es una funcion anonima que sirve para hacer una funcion en una sola linea

incrementv2=lambda x: x+1
print(incrementv2(10))

full_name=lambda name,lastname: f'Full name es {name.title()}, {lastname.title()}'

text=full_name('felipe','garcia')
print(text)

def high_ord_func(x,func):
    return x + func(x)

high_ord_func= lambda x,func:x + func(x)

result=high_ord_func(2,incrementv2)
print(result)

result=high_ord_func(2,incrementv2)
print(result)
result=high_ord_func(2,lambda x:x+2 )
print(result)
result=high_ord_func(2,lambda x:x*3 )
print(result)

# map es una funcion que recibe una funcion y un iterable y retorna un iterable
# sirve para aplicar una funcion a cada elemento de un iterable

numbers=[1,2,3,4,5]
numbers_v2=[]
for i in numbers:
    numbers_v2.append(i*2)

numbers_v3=list(map(lambda i:i*2,numbers))

print(numbers)
print(numbers_v2)
print(numbers_v3)

numbers1=[1,2,3,4,5]
numbers2=[6,7,8,9,10]

result=list(map(lambda x,y:x+y,numbers1,numbers2))
print(result)

items=[{
    'name':'laptop',
    'price':1000
},
{
    'name':'mouse',
    'price':50  
},
{
    'name':'monitor',
    'price':500
}
    ]

prices=list(map(lambda item:item['price'],items))
print(prices)

def taxes(item):
    item['price'] = item['price'] * 1.9
    return item

new_items=list(map(taxes,items))
print(new_items)
'''

# lamba es una funcion anonima que sirve para hacer una funcion en una sola linea
# sirve para hacer funciones que no se van a volver a usar


#filter sirve para filtrar elementos de un iterable
'''
numbers = [1,2,3,4,5]
new_numbers = list(filter(lambda x: x %2 == 0, numbers))
print(new_numbers)

matches = [
    {
    'home_team':'Colombia',
    'away_team':'Peru',
    'home_score':1,
    'away_score':0,
    'home_team_result':'Win',

    },
    {'home_team':'Ecuador',
    'away_team':'Bolivia',
    'home_score':1,
    'away_score':0,
    'home_team_result':'Draw',},

    {'home_team':'Argentina',
     'away_team':'Chile',
     'home_score':1,
     'away_score':0,
     'home_team_result':'Lose',},
]
print(matches)
print(len(matches))

new_list=list(filter(lambda item: 
    item['home_team_result'] == 'Win',matches))
print(new_list)
print(len(new_list))


def filter_by_length(words):
   # Escribe tu solución 👇
   return list(filter(lambda palabras: len(palabras) >= 4,words))

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)
'''

#reduce sirve para reducir un iterable a un solo valor
#Se usa para sumar todos los elementos de una lista y 
# obtener un solo valor

import functools

numbers = [1,2,3,4]

def accum(counter,item):
    print("counter => ",counter)
    print("item => ",item)
    return counter + item 

result = functools.reduce(accum,numbers)

print(result)

