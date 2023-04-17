# import this #Imprime el Zen de Python

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
