# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300
precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva':1450}
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)


# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melon"] = 2800

print(precios_frutas)


# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.
frutas = list(precios_frutas.keys())
print(frutas)


# 4) Crear una clase llamada Persona que contenga un método __init__ con los atributos
# nombre, pais y edad y el método saludar. El método saludar debe imprimir por pantalla un
# mensaje de salud que siga la estructura "¡Hola! Soy [nombre], vivo en [pais] y tengo [edad]
# años."
class Persona:
    def __init__(self,nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saluda(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

persona = Persona("Mariano", "Argentina", 24)
persona.saluda()  


# 5) Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y
# calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente.
import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        print(f"el area del circulo es {math.pi * self.radio ** 2}")

    def calcular_perimetro(self):
        print(f"el perimetro del circulo es {2 * math.pi * self.radio}") 

circulo = Circulo(float(input("ingresar el radio del circulo")))
circulo.calcular_area()
circulo.calcular_perimetro()


# 7) Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir:
# ● Agregar clientes (encolar).
# ● Atender clientes (desencolar).
# ● Mostrar el siguiente cliente en la fila.
from collections import deque

class Cola:
    def __init__(self):
        self.clientes = deque()

    def agregarClientes(self):
        self.clientes.append(input("agregar un cliente"))

    def colaVacia(self):
        return len(self.clientes) == 0    
    
    def atenderClientes(self):
        return self.clientes.popleft() if not self.colaVacia() else "La cola esta vacía"
    
    def siguienteCliente(self):
        return self.clientes[0] if not self.colaVacia() else "La cola esta vacía"
    
cola = Cola()  
cola.agregarClientes()
cola.agregarClientes()
cola.agregarClientes()
print(cola.atenderClientes())  
print(cola.siguienteCliente())


# 8) Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar
# los valores almacenados.
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.primer = None

    def agregar(self, valor):
        nuevoNodo = Nodo(valor)
        nuevoNodo.siguiente = self.primer
        self.primer = nuevoNodo

    def mostrar(self):
        actual = self.primer
        while actual:
            print(actual.valor, end="==>")
            actual = actual.siguiente
        print("None")
        
        
lista = ListaEnlazada()
lista.agregar(3)                    
lista.agregar(2)                    
lista.agregar(1)
lista.mostrar()
