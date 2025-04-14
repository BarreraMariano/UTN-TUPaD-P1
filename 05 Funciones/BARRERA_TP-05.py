# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()    


# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.
def saludar_usuario(nombre):
    print(f"Hola {nombre}")

saludar_usuario(input("ingresar su nombre"))    


# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
def informacion_personal(nombre, apellido,edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("ingresar su nombre")
apellido = input("ingresar su apellido")
edad = int(input("ingresar su edad"))
residencia = input("ingresar su residencia")
informacion_personal(nombre, apellido, edad, residencia)


# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el 
# radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
import math 

def calcular_area_circulo(radio):
    return math.pi * (radio **2)

def calcular_perimetro_circulo(radio):  
    return 2 * math.pi * radio

radio = float(input("ingresar el radio del circulo"))
print(f"el area de un circulo es {calcular_area_circulo(radio)} y el perimetro de un circulo es {calcular_perimetro_circulo(radio)}")


# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = float(input("ingresar los segundo"))
print(f"la cantidad de hora que tiene {segundos} segundos es de {segundos_a_horas(segundos)} horas")


# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
        
tabla_multiplicar(int(input("ingresar un numero")))    


# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
def operaciones_basicas(a, b):
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")
    
numeroUno = int(input("ingresar el primer numero"))
numeroDos = int(input("ingresar el segundo numero"))
operaciones_basicas(numeroUno, numeroDos)


# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
     return peso / altura ** 2

peso = float(input("ingresar su peso"))                  
altura = float(input("ingresar su altura"))
print(f"su IMC es de {calcular_imc(peso, altura)}")  



# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.
def celsius_a_fahrenheit(celsius):
      return (celsius * 9/5) + 32

celsius = float(input("ingresar una temperatura en grados celsius"))
print(f"el equivalente de {celsius}°C a Fahrenheit es de {celsius_a_fahrenheit(celsius)}°F")   


# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

numeroUno = int(input("ingresar el primer numero"))            
numeroDos = int(input("ingresar el segundo numero"))            
numeroTres = int(input("ingresar el tercer numero"))
print(f"el promedio de los numeros {numeroUno}, {numeroDos}, {numeroTres} es de {calcular_promedio(numeroUno, numeroDos, numeroTres)}") 