#Vamos a hacer un programa que pida un numero al usuario y lo duplica

import sys

if len(sys.argv) > 1:
    numero_introducido = int(sys.argv[1])
    numero_duplicado = numero_introducido * 2
    print(f"El doble de {numero_introducido} es {numero_duplicado}")
else:
    print("No se ha proporcionado ningún valor para duplicar.")