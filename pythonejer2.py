# import this #Imprime el Zen de Python

import random


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
print(unique_numbers)  # Convierte el conjunto en lista

'''add(): Añade un elemento.
update(): Añade cualquier tipo de objeto iterable como: listas, tuplas.
discard(): Elimina un elemento y si ya existe no lanza ningún error.
remove(): Elimina un elemento y si este no existe lanza el error “keyError”.
pop(): Nos devuelve un elemento aleatorio y lo elimina y 
si el conjunto está vacío lanza el error “key error”.
clear(): Elimina todo el contenido del conjunto.'''

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
ages=[21,34,47]

print(list(zip(names,ages)))

