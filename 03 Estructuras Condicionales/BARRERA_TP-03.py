#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edadUsuario = int(input("ingresar su edad: "))

if edadUsuario >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")   


#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.
notaUsuario = int(input("ingresar su nota: "))

if notaUsuario >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.
numeroUsuario = int(input("ingresar un numero: "))

if numeroUsuario % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")   


# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.
edadUsuario = int(input("ingresar su edad: "))

if edadUsuario < 12: 
    print("Niño/a")
elif(edadUsuario >= 12 and edadUsuario < 18):
    print("Adolescente")
elif(edadUsuario >= 18 and edadUsuario < 30):
    print("Adulto/a joven")
else:
    print("Adulto/a") 


# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.
contraseñaUsuario = input("ingresar su contraseña: ")
longitudDeContraseña = len(contraseñaUsuario)

if longitudDeContraseña >= 8 and longitudDeContraseña <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")   


# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números.
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
from statistics import mode, median, mean
import random

numerosAleatorios = [random.randint(1,100) for i in range(50)]
media = mean(numerosAleatorios)
moda = mode(numerosAleatorios)
mediana = median(numerosAleatorios)  

if(media > mediana and mediana > moda):
    print("Sesgo positivo o a la derecha")
elif(media < mediana and mediana < moda):
    print("Sesgo negativo o a la izquierda") 
else:
    print("Sin sesgo") 


# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.
fraseUsuario = input("ingresar una frase o palabra: ")
ultimaLetraDeFrase = fraseUsuario[len(fraseUsuario) - 1]

if(ultimaLetraDeFrase == "a" or ultimaLetraDeFrase == "e" or ultimaLetraDeFrase == "i" or ultimaLetraDeFrase == "o" or ultimaLetraDeFrase == "u"):
    print(fraseUsuario + "!")
else:
    print(fraseUsuario)        


# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas
nombreUsuario = input("ingresar su nombre: ")
numero = int(input("ingresar el número 1, 2 o 3: "))

if numero == 1:
    print(nombreUsuario.upper())
elif numero == 2:
    print(nombreUsuario.lower())
elif numero == 3:
    print(nombreUsuario.title())    


# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
magnitudDeTerremoto = int(input(" la magnitud de un terremoto"))

if(magnitudDeTerremoto < 3):
    print("Muy leve (imperceptible)")
elif(magnitudDeTerremoto >= 3 and magnitudDeTerremoto < 4):
    print("Leve (ligeramente perceptible)")
elif(magnitudDeTerremoto >= 4 and magnitudDeTerremoto < 5):
    print("Moderado (sentido por personas, pero generalmente no causa daños)")    
elif(magnitudDeTerremoto >=5 and magnitudDeTerremoto < 6):
    print("Fuerte (puede causar daños en estructuras débiles)")
elif(magnitudDeTerremoto >= 6 and magnitudDeTerremoto < 7):
    print("Muy Fuerte (puede causar daños significativos)")
elif(magnitudDeTerremoto >= 7):
    print("Extremo (puede causar graves daños a gran escala)")            


# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
#             Periodo del año                                                      Estación en el hemisferio norte                   Estación en el hemisferio sur
# Desde el 21 de diciembre hasta el 20 de  marzo (incluidos)                                Invierno                                             Verano
# Desde el 21 de marzo hasta el 20 de junio (incluidos)                                     Primavera                                            Otoño
# Desde el 21 de junio hasta el 20 de septiembre (incluidos)                                Verano                                               Invierno
# Desde el 21 de septiembre hasta el 20 de diciembre (incluidos)                            Otoño                                                Primavera

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa 
# información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisferio = input("ingresar si se encuentra en hemisferio norte o sur")
mes = input("ingresar el mes")
dia = int(input("ingresar el dia"))

if((mes.lower() == "diciembre" and dia >= 21 and dia <= 31) or (mes.lower() == "enero" and dia >= 1 and dia <= 31) or (mes.lower() == "febrero" and dia >= 1 
    and  dia <= 28) or (mes.lower() == "marzo" and dia >= 1 and dia <= 20)):
    if(hemisferio.lower() == "norte"):
        print("INVIERNO")
    elif(hemisferio.lower() == "sur"):
        print("VERANO")

elif((mes.lower() == "marzo" and dia >= 21 and dia <= 31) or (mes.lower() == "abril" and dia >= 1 and dia <= 30) or (mes.lower() == "mayo" and dia >= 1 and  dia <= 31) 
     or (mes.lower() == "junio" and dia >= 1 and dia <= 20)):  
   if(hemisferio.lower() == "norte"):
        print("PRIMAVERA")
   elif(hemisferio.lower() == "sur"):
        print("OTOÑO")

elif((mes.lower() == "junio" and dia >= 21 and dia <= 30) or (mes.lower() == "julio" and dia >= 1 and dia <= 31) or (mes.lower() == "agosto" and dia >= 1 and  dia <= 31) 
     or (mes.lower() == "septiembre" and dia >= 1 and dia <= 20)):
     if(hemisferio.lower() == "norte"):
        print("VERANO")
     elif(hemisferio.lower() == "sur"):
        print("INVIERNO")

elif((mes.lower() == "septiembre" and dia >= 21 and dia <= 30) or (mes.lower() == "octubre" and dia >= 1 and dia <= 31) or (mes.lower() == "noviembre" and dia >= 1 and  
    dia <= 30) or (mes.lower() == "diciembre" and dia >= 1 and dia <= 20)):
     if(hemisferio.lower() == "norte"):
        print("OTOÑO")
     elif(hemisferio.lower() == "sur"):
        print("PRIMAVERA")          