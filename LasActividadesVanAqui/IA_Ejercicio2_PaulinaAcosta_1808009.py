###################################
#  Ejercicio 2                    #
#  Introducción a Python          #
#                                 #
#  Elaborado por:                 #
#  Paulina Merari Acosta Sánchez  #
#                                 #
#  Fecha: 01/09/2021              #
###################################

# ENTRADA DE DATOS
num_E1 = int(input("Inserte su primer número entero: "))
num_E2 = int(input("Inserte su segundo número entero: "))
num_F1 = float(input("Inserte su primer número flotante: "))
num_F2 = float(input("Inserte su segundo número flotante: "))

# OPERACIONES ARITMETICAS
#  Números enteros
res_1 = num_E1 + num_E2
res_2 = num_E1 - num_E2
res_3 = num_E1 * num_E2
res_4 = num_E1 / num_E2
# Números flotantes
res_5 = num_F1 + num_F2
res_6 = num_F1 - num_F2
res_7 = num_F1 * num_F2
res_8 = num_F1 / num_F2

# SALIDA DEL PROGRAMA
print("\nOperaciones aritmeticas de los dos números enteros:")
print(f"{num_E1} + {num_E2} = {res_1}")
print(f"{num_E1} - {num_E2} = {res_2}")
print(f"{num_E1} * {num_E2} = {res_3}")
print(f"{num_E1} / {num_E2} = {res_4}")

print("\nOperaciones aritmeticas de los dos números flotantes:")
print(f"{num_F1} + {num_F2} = {res_5}")
print(f"{num_F1} - {num_F2} = {res_6}")
print(f"{num_F1} * {num_F2} = {res_7}")
print(f"{num_F1} / {num_F2} = {res_8}")