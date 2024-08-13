#programa que me calcula el nombre con la edad mayor
#autor:juliana saavedra
#fecha: 07/05/2024
nombre= input("digite el nombre de la primera persona: ")
edad1= int(input("digite la edad: "))

# pedir nombre y edad de la segunda persona
nombre2= input("ingrese el nombre de la segunda persona: ")
edad2= int(input("ingrese la edad de la segunda persona: "))

# pedir nombre y edad de la tercera persona
nombre3= input("ingrese el nombre de la tercera persona: ")
edad3= int(input("ingrese la edad de la tercera persona: "))
while nombre!="FIN":
    if edad1 > edad2 and edad1 > edad3:
        print(f"{nombre} es la persona de mayor edad.")
    elif edad2 > edad1 and edad2 > edad3:
        print(f"{nombre2} es la persona de mayor edad.")
    else:
        print(f"{nombre3} es la persona de mayor edad.")
    nombre= input("digite el nombre de la primer persona: ")
    if nombre =="FIN":
        break
    edad1= int(input("digite la edad: "))

# pedir nombre y edad de la segunda persona
    nombre2= input("ingrese el nombre de la segunda persona: ")
    edad2= int(input("ingrese la edad de la segunda persona: "))

# pedir nombre y edad de la tercera persona
    nombre3= input("ingrese el nombre de la tercera persona: ")
    edad3= int(input("ingrese la edad de la tercera persona: "))
