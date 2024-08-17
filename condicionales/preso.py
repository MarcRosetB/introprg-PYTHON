#Programa que recuerda a los mayores de edad que ya son responsables delante de la ley

nombre = input("Nombre? ")
edad = int(input("Edad? "))

if edad < 18:
    print(f"Aneu amb compte {nombre}")
else:
    print("Vos ja podeu anar a la presó!")
    print(f"Aneu amb compte {nombre}")
