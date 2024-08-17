# Aquest programa implementa una calculadora bàsica
#
# Demana dos nombres per entrada estàndard i mostra el
# resultat de sumar-los, restar-li el segon al primer, multiplicar-los,
# dividir el primer entre el segon.
#
# El programa no controla valors no adequats d'entrada

primer_operand = int(input("Primer numero?\n"))
segon_operand = int(input("Segon operand?\n"))

suma = primer_operand + segon_operand
resta = primer_operand - segon_operand
multiplicacion = primer_operand * segon_operand
division = primer_operand / segon_operand

print(f"La suma de {primer_operand} + {segon_operand} es: {suma}")
print(f"La resta de {primer_operand} - {segon_operand} es: {resta}")
print(f"La multiplicacion de {primer_operand} * {segon_operand} es: {multiplicacion}")
print(f"La division de {primer_operand} / {segon_operand} es: {division}")