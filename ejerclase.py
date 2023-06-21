
print("Formula de la recta")
print("1 opcion punto-punto\n2 opcion punto-pendiente\n3 opcion punto-b")
resp = input(" Ingrese la opcion que desee: ")
if resp=="1":
    print("Punto-Punto")
    x1=int(input("Ingrese el primer valor del punto x "))
    y1=int(input("Ingrese el primer valor del punto y "))
    x2=int(input("Ingrese el segundo valor del punto x "))
    y2=int(input("Ingrese el valor del segundo punto y "))
    respu=(y2-y1)/(x2-x1)
    print(respu)
elif resp=="2":
    print("Opcion-Punto")
    x1=int(input("Ingrese el valor de x"))
    y1=int(input("Ingrese el valor de y"))
    m=int(input("Ingrese el valor de la pendiente (m)"))
    resp2=(-x1*m)+y1
    resp3=m+"x"+resp2
    print(resp3)

elif resp=="3":
    print("Opcion punto-b")
        
else:
    print("Ingrese una opcion correcta")
