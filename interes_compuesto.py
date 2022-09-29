# Ejercicio # 26: Leer un capital C y que averigue e imprima en cuantos meses se duplica si lo colocamos a un interés compuesto del 5% mensual.

print("-----------------------------------------------")
print("---------Interés Compuesto de Capital----------")
print("-----------------------------------------------")


# input

C = int(input("Digite el valor del capital que desea calcular: "))

K = 0

B = 2*C

# procesing



while C <= B:
    C = (C*0.05)+C
    K=K+1


print("El capital será duplicado en " + str(K) + " meses")