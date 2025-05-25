# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
    
numero = int(input("ingrese un numero entero"))    
print(f"el resultado de factorial de {numero} es {factorial(numero)}")  

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.

def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

for i in range(int(input("ingresar la posicion deseada"))):
    print(fibonacci(i))


# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛
# 𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    
base = int(input("ingresar la base"))    
exponente = int(input("ingresar el exponente"))
print(f"la {base} elevada a {exponente} es {potencia(base, exponente)}")  

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.

def decimalBinario(numero):
    if numero == 0:
        return ""
    else:
        return decimalBinario(numero // 2) + str(numero % 2)

def transformaBinario(num):
    if num == 0:
        return "0"
    return decimalBinario(num)

numero = int(input("ingresar un numero entero"))
print(f"el numero binario de {numero} es {transformaBinario(numero)}")

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.
#  Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

def palindromo(palabra):
    if len(palabra) <= 1:
        return True
    
    if palabra[0] != palabra[-1]:
        return False
    
    return palindromo(palabra[1:-1])

print(palindromo(input("ingresar una palabra"))) 

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
#  Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

def sumaDigitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + sumaDigitos(n // 10)

print(sumaDigitos(1234))
print(sumaDigitos(9))
print(sumaDigitos(305)) 

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide

def contarBloques(n):
    if n == 1:
        return 1
    else:
        return n + contarBloques(n - 1)
       
print(contarBloques(1))
print(contarBloques(2))
print(contarBloques(4))

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.


def contarDigito(num, digito):
    if num == 0:
        return 0
    
    ultimoDigito = num % 10

    if ultimoDigito == digito:
        return 1 + contarDigito(num // 10, digito)
    else:
        return contarDigito(num // 10, digito)
    
print(contarDigito(12233421, 2))
print(contarDigito(5555, 5))
print(contarDigito(123456, 7))