'''
#Clase
class Celular:
#Un objeto tiene 2 cosas propiedas y puede hacer acciones
    def __init__(self,marca,modelo,camara) -> None:
        self.marca=marca
        self.modelo=modelo
        self.camara=camara

celu1=Celular("Samsumg","A35","40MP")
celu2=Celular("Apple","IPhone","82MP") #Atributos de instancia se lo pasamos cuando creamos el objeto 

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

'''

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
        print(f"Mi habilidad es: {self.habilidad}")

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
        print(f'{super().mostrar_habilidad()}')
