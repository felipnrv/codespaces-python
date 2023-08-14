'''
#Clase
class Celular:
#Un objeto tiene 2 cosas propiedas y puede hacer acciones
    def __init__(self,marca,modelo,camara) -> None:
        self.marca=marca
        self.modelo=modelo
        self.camara=camara

celu1=Celular("Samsumg","A35","40MP")
celu2=Celular("Apple","IPhone","82MP") 
#Atributos de instancia se lo pasamos cuando creamos el objeto 

#print(celu2.modelo)

#Metodo
#Es una funcion que esta dentro de una clase entonces es una funcion 

class PC:
    #En el metodo se tiene
    def __init__(self,marca,modelo,camara) -> None:
        self.marca=marca
        self.modelo=modelo
        self.camara=camara

    def llamar(self):
        print(f'La PC se daño: {self.modelo}')
    def cortar(self):
        print(f'La PC se daño: {self.marca}')

celu1=PC("Samsumg","A35","40MP")
celu2=PC("Apple","IPhone","82MP")

celu1.llamar()


class Estudiante():
    def __init__(self,nombre,edad,grado):
        self.nombre=nombre
        self.edad=edad
        self.grado=grado
    def estudiar(self):
        print("Estudiando.... ")

#pedro = Estudiante("Pedro","23","3")
#print(pedro.edad)
nombre=input("Dime tu nombre: ")
edad=input("Dime tu edad: ")
grado=input("Dime tu grado: ")

estudiante=Estudiante(nombre,edad,grado)

print(f"""
     ***DATOS DEL ESTUDIANTE***\n
        Nombre:{estudiante.nombre} \n
        Edad:{estudiante.edad} \n
        Grado:{estudiante.grado} \n 
    """)

while True:
    estudiar = input()
    if(estudiar.lower()=="estudiar"):
        estudiante.estudiar()
        break

#Herencia Simple
#La clase hijo accede a todos los metodos y propiedades de la clase padre

class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad

    def hablar(self):
        print("Hola, estoy hablando.... ")

class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
       super().__init__(nombre,edad,nacionalidad)
       self.trabajo=trabajo
       self.salario=salario
    #Reescribio el metodo hablar()
    def hablar(self):
        print("Chao, me fui... ")

roberto=Empleado("Roberto",43,"Argentino","Programador",1000)

roberto.hablar()


#Herencia jerarquica 
#Una clase es padre de muchas sub clases


class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad

    def hablar(self):
        print("Hola, estoy hablando.... ")

class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
       super().__init__(nombre,edad,nacionalidad)
       self.trabajo=trabajo
       self.salario=salario
    
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad,notas,universidad)
        super().__init__(nombre,edad,nacionalidad)
        self.notas=notas
        self.universidad=universidad
            
roberto=Empleado("Roberto",43,"Argentino","Programador",1000)

roberto.hablar()

#Herencia multiple

class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad

    def hablar(self):
        print("Hola, estoy hablando.... ")

class Artista:
    def __init__(self,habilidad):
        self.habilidad=habilidad

    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"
        #pass

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad,notas,universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas=notas
        self.universidad=universidad

class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad,salario,empresa,habilidad):
        Persona.__init__(self,nombre, edad, nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario=salario
        self.empresa=empresa

    def presentarse(self):
        print(f'Hola soy:{self.nombre}, Mi habilidad es {self.mostrar_habilidad()}, trabajo en la empresa {self.empresa}')

roberto=EmpleadoArtista("Roberto",21,"Peru",1000,"Google","Pintar")

#roberto es una instancia de empleadoartista y artista porque hereda de artista y personas
herencia=issubclass(EmpleadoArtista,Artista)
instacia =isinstance(roberto,Artista)

roberto.presentarse()
print(instacia)

#MRO (Method Resolution Order)

class A:
    def hablar(self):
        print("Hola desde A")
class B(A):
    def hablar(self):
        print("Hola desde B")
class C(A):
    def hablar(self):
        print("Hola desde C")
class D(B,C):
    def hablar(self):
        print("Hola desde D")


#Se crea un objeto        
d=D()
#1 se llama a D, luego a B y C, despues en A, es porque D hereda B y C de A, si no lo haria se saltaria al siguiente 
d.hablar()

#En este caso 1 va D, luego a B ,y A , como no hereda de A no va hacia C 
class A:
    def hablar(self):
        print("Hola desde A")
class F:
     def hablar(self):
          print("Hola desde F")
class B(A):
    def hablar(self):
        print("Hola desde B")
class C(F):
    def hablar(self):
        print("Hola desde C")
class D(B,C):
    def hablar(self):
        print("Hola desde D")
        
d=D()
#Se pone D porque es la clase que hereda todo 
#Se pasa F.hablar(d) se pasa d=self, se llama a cada clase
F.hablar(d)
#d.hablar()
#print(D.mro())

class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def mostrar_datos(self):
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad}')

class Estudiante(Persona):
    def __init__(self, nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado=grado

    def mostrar_datos(self):
        print(f"Grado: {self.grado}")

estudiante=Estudiante("Juan","24","10mo")
estudiante.mostrar_datos()

'''
class Animal:
    def comer(self):
        print("El animal esta comiendo")
class Ave(Animal):
    def volar(self):
        print("El animal esta volando")
class Mamifero(Animal):
    def amamantar(self):
        print("El animal esta comiendo") 

class Murcielago(Mamifero,Ave):
    pass

ave = Ave()
ave.comer()
ave.volar()

#murcielago=Murcielago()
#murcielago.comer()
#murcielago.amamantar()
#murcielago.volar()