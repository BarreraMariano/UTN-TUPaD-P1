# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")


# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.
nombre = input("ingrese su nombre: ")
print(f"Hola {nombre}!")


# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.
nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
edad = input("ingrese su edad: ")
lugarDeResidencia = input("ingrese su lugar de residencia: ")

print(f"Hola soy {nombre} {apellido}, tengo {edad} años y vivo en {lugarDeResidencia}")


# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.
radio = int(input("ingrese el radio de un circulo: "))
area = 3.1416 * (radio ** 2)
perimetro = 2 * 3.1416 * radio

print(f"el area de un circulo es {area} y el perímetro de un circulo es {perimetro}")


# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.
segundos = int(input("ingresar una cantidad de segundos"))
horas = segundos / 3600

print(f"{segundos} segundos equivale a {horas} horas")


# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.
numero = int(input("ingresar un numero"))
for i in range(1, 11): print(f"{numero} * {i} = {numero * i}")



# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numeroUno = int(input("ingresar el primer numero"))
numeroDos = int(input("ingresar el segundo numero"))

if numeroUno == 0 or numeroDos == 0:
        print("ingresar dos números enteros distintos del 0 ")  
else:
        print(f"{numeroUno} + {numeroDos} = ", numeroUno + numeroDos)
        print(f"{numeroUno} / {numeroDos} = ", numeroUno / numeroDos)
        print(f"{numeroUno} * {numeroDos} = ", numeroUno * numeroDos)
        print(f"{numeroUno} - {numeroDos} = ", numeroUno - numeroDos)


# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal.
altura = float(input("ingresar tu altura: "))
peso = float(input("ingresar tu peso :"))
imc = peso / altura ** 2

print(f"tu indice de masa corporal es {imc}")


# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. 
celsius = float(input("ingresar una temperatura en grados celsius: "))
fahrenheit = 9/5 * celsius + 32

print(f"la temperatura de {celsius} celsius es equivalente a {fahrenheit} fahrenheit")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.
numeroUno = float(input("ingresar el primer numero: "))
numeroDos = float(input("ingresar el segundo numero: "))
numeroTres = float(input("ingresar el tercer numero: "))
promedio = numeroUno + numeroDos + numeroTres / 3

print(f"el promedio de todos los numeros, {numeroUno}, {numeroDos} y {numeroTres} es {promedio}")