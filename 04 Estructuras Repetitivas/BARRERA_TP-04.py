# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(0, 101):
    print(i)


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
numero = int(input("ingresar un numero entero"))
cont = 0

while numero > 0:
   numero //= 10
   cont += 1 

print(f"la cantidad de dígitos es {cont}")    


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
numeroUno = int(input("ingresar el primer numero"))
numeroDos = int(input("ingresar el segundo numero"))

if(numeroUno > numeroDos):
    for i in range(numeroDos + 1, numeroUno):
        print(i)
else:
    for i in range(numeroUno + 1, numeroDos):
        print(i)                


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
suma = 0
numero = 1

while numero > 0:
    numero = int(input(f"ingresar el numeros enteros si el numero ingresado es 0 corta el programa"))
    suma += numero

print(f"la suma de todos los numeros es de {suma}")


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random

numeroAdivinar = random.randrange(0, 9)
cont = 0

while True:
    numero = int(input("ingresar un numero del uno al nueve"))
    if numero == numeroAdivinar:
        break
    cont += 1

print(f"la cantidad de intentos fue de {cont}")    


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
for i in range(100, 0, -2):
    print(i)


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
numero = int(input("ingresar un numero"))
suma = 0

if(numero > 0):
    for i in range(0, numero + 1):
        suma += i 
else:
    print("ingresar un numero positivo")          

print(f"suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario es de {suma}")


# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
positivo= 0
negativo = 0
par = 0
impar = 0

for i in range(1, 101):
    numero = int(input(f"ingresar el numero{i}"))

    if numero > 0:
        positivo +=1
    else:
        negativo +=1

    if numero % 2 == 0:
        par += 1
    else:
        impar +=1

print(f"la cantidad de numeros pares es {par}")
print(f"la cantidad de numeros impares es {impar}")
print(f"la cantidad de numeros positivos es {positivo}")
print(f"la cantidad de numeros negativo es {negativo}")


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
suma = 0
for i in range(1, 101):
    numero = int(input(f"ingresar el numero {i}"))
    suma += numero

print(f"la suma de la media es {suma / 100}")


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numero = int(input("ingresar un numero entero"))
nuevoNumero = 0
while numero > 0:
   nuevoNumero = nuevoNumero * 10 + numero % 10
   numero //= 10
   
print(nuevoNumero) 