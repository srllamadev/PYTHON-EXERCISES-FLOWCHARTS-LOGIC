# Guía Completa de Python - Desde Cero

## 📋 Índice
1. [Instalación](#instalación)
2. [Fundamentos](#fundamentos)
3. [Estructuras de Control](#estructuras-de-control)
4. [Estructuras de Datos](#estructuras-de-datos)
5. [Funciones](#funciones)
6. [Programación Orientada a Objetos](#programación-orientada-a-objetos)
7. [Módulos y Paquetes](#módulos-y-paquetes)
8. [Manejo de Archivos](#manejo-de-archivos)
9. [Manejo de Errores](#manejo-de-errores)
10. [Librerías Esenciales](#librerías-esenciales)
11. [Proyectos Prácticos](#proyectos-prácticos)

---

## 🚀 Instalación

### 1. **Windows**
```bash
# 1. Descargar instalador desde python.org
# 2. Marcar "Add Python to PATH" durante instalación
# 3. Verificar instalación:
python --version
```

### 2. **macOS**
```bash
# Opción 1: Instalador oficial
# Descargar desde python.org

# Opción 2: Homebrew
brew install python3

# Verificar instalación
python3 --version
```

### 3. **Linux (Ubuntu/Debian)**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Verificar instalación
python3 --version
pip3 --version
```

### 4. **Verificar Instalación**
```python
# Abrir terminal/consola y ejecutar:
python --version  # o python3 --version

# También puedes ejecutar el intérprete interactivo:
python  # luego escribir print("¡Hola Mundo!")
```

---

## 📚 Fundamentos

### **Primeros Pasos**
```python
# Comentarios de una línea
'''
Comentarios
multi-línea
'''

# Salida por consola
print("¡Hola, Mundo!")

# Entrada de usuario
nombre = input("¿Cuál es tu nombre? ")
print(f"Hola, {nombre}")
```

### **Variables y Tipos de Datos**
```python
# Variables básicas
entero = 10
flotante = 3.14
cadena = "Python"
booleano = True
nulo = None

# Tipado dinámico
variable = 42      # Ahora es entero
variable = "texto" # Ahora es string

# Conversión de tipos
str(123)     # "123"
int("456")   # 456
float("3.14") # 3.14
```

### **Operadores**
```python
# Aritméticos
suma = 5 + 3       # 8
resta = 10 - 4     # 6
multi = 3 * 2      # 6
div = 10 / 3       # 3.333...
div_ent = 10 // 3  # 3
mod = 10 % 3       # 1
potencia = 2 ** 3  # 8

# Comparación
5 > 3    # True
5 == 5   # True
5 != 3   # True
5 >= 5   # True

# Lógicos
True and False  # False
True or False   # True
not True        # False

# Asignación
x = 5
x += 3      # x = 8
x -= 2      # x = 6
```

---

## 🔄 Estructuras de Control

### **Condicionales**
```python
# if-elif-else
edad = 18

if edad < 13:
    print("Niño")
elif edad < 18:
    print("Adolescente")
elif edad < 65:
    print("Adulto")
else:
    print("Adulto mayor")

# Operador ternario
estado = "Mayor" if edad >= 18 else "Menor"
```

### **Bucles**
```python
# For loop
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8):       # 2, 3, 4, 5, 6, 7
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8
    print(i)

# While loop
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Control de bucles
for i in range(10):
    if i == 3:
        continue    # Salta esta iteración
    if i == 7:
        break       # Termina el bucle
    print(i)
```

---

## 🗂️ Estructuras de Datos

### **Listas**
```python
# Creación
mi_lista = [1, 2, 3, 4, 5]
frutas = ["manzana", "banana", "cereza"]

# Operaciones
frutas.append("naranja")        # Añadir al final
frutas.insert(1, "uva")         # Insertar en posición
frutas.remove("banana")         # Remover elemento
ultimo = frutas.pop()           # Remover y devolver último
frutas.sort()                   # Ordenar
frutas.reverse()                # Invertir orden

# Slicing
numeros = [0, 1, 2, 3, 4, 5]
numeros[2:5]      # [2, 3, 4]
numeros[:3]       # [0, 1, 2]
numeros[3:]       # [3, 4, 5]
numeros[::2]      # [0, 2, 4] (cada 2 elementos)
numeros[::-1]     # [5, 4, 3, 2, 1, 0] (invertir)

# Comprensión de listas
cuadrados = [x**2 for x in range(10)]
pares = [x for x in range(20) if x % 2 == 0]
```

### **Tuplas**
```python
# Inmutables
mi_tupla = (1, 2, 3)
coordenadas = (10.5, 20.3)

# Desempaquetado
x, y = coordenadas
a, b, c = mi_tupla

# Uso común para retorno múltiple
def obtener_coordenadas():
    return 10, 20

x, y = obtener_coordenadas()
```

### **Diccionarios**
```python
# Creación
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceso
nombre = persona["nombre"]           # Juan
edad = persona.get("edad")           # 30
pais = persona.get("pais", "España") # Valor por defecto

# Modificación
persona["edad"] = 31                 # Actualizar
persona["profesion"] = "Ingeniero"   # Agregar
persona.update({"edad": 32, "hobby": "fútbol"})

# Métodos
claves = persona.keys()              # dict_keys(['nombre', 'edad', ...])
valores = persona.values()
pares = persona.items()

# Comprensión de diccionarios
cuadrados = {x: x**2 for x in range(5)}
```

### **Sets**
```python
# Colección no ordenada, sin duplicados
mi_set = {1, 2, 3, 3, 4}  # {1, 2, 3, 4}

# Operaciones
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

union = A | B            # {1, 2, 3, 4, 5, 6}
interseccion = A & B     # {3, 4}
diferencia = A - B       # {1, 2}
diferencia_sim = A ^ B   # {1, 2, 5, 6}
```

---

## 📞 Funciones

### **Funciones Básicas**
```python
def saludar(nombre="Mundo"):
    """Función que saluda a una persona"""
    return f"Hola, {nombre}!"

# Llamada
mensaje = saludar("Ana")
mensaje2 = saludar()  # Usa valor por defecto

# Argumentos posicionales y nombrados
def describir_persona(nombre, edad, ciudad):
    print(f"{nombre}, {edad} años, de {ciudad}")

describir_persona("Carlos", 25, "Barcelona")
describir_persona(ciudad="Madrid", nombre="Laura", edad=30)

# Argumentos arbitrarios
def suma(*args):
    return sum(args)

resultado = suma(1, 2, 3, 4, 5)  # 15

# Argumentos con palabras clave arbitrarias
def crear_perfil(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

crear_perfil(nombre="Pedro", edad=25, ciudad="Sevilla")
```

### **Funciones Lambda**
```python
# Funciones anónimas
cuadrado = lambda x: x**2
cuadrado(5)  # 25

# Uso común con map, filter, sorted
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))  # [1, 4, 9, 16, 25]
pares = list(filter(lambda x: x % 2 == 0, numeros))  # [2, 4]
```

### **Ámbito de Variables**
```python
# Variable global
contador = 0

def incrementar():
    global contador
    contador += 1
    return contador

# Variables no locales (closures)
def contador_fabrica():
    cuenta = 0
    
    def incrementar():
        nonlocal cuenta
        cuenta += 1
        return cuenta
    
    return incrementar

mi_contador = contador_fabrica()
print(mi_contador())  # 1
print(mi_contador())  # 2
```

---

## 🏗️ Programación Orientada a Objetos

### **Clases y Objetos**
```python
class Persona:
    # Atributo de clase
    especie = "Humano"
    
    # Constructor
    def __init__(self, nombre, edad):
        # Atributos de instancia
        self.nombre = nombre
        self.edad = edad
    
    # Método de instancia
    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"
    
    # Método de clase
    @classmethod
    def desde_nacimiento(cls, nombre, año_nacimiento):
        from datetime import datetime
        edad = datetime.now().year - año_nacimiento
        return cls(nombre, edad)
    
    # Método estático
    @staticmethod
    def es_mayor_de_edad(edad):
        return edad >= 18

# Uso
persona1 = Persona("Ana", 25)
print(persona1.presentarse())
print(Persona.es_mayor_de_edad(20))

# Crear con método de clase
persona2 = Persona.desde_nacimiento("Carlos", 1995)
```

### **Herencia**
```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        raise NotImplementedError("Subclase debe implementar este método")

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)  # Llamar al constructor del padre
        self.raza = raza
    
    def hablar(self):
        return "¡Guau!"
    
    def descripcion(self):
        return f"{self.nombre} es un {self.raza}"

# Polimorfismo
animales = [Perro("Rex", "Pastor Alemán"), Animal("Genérico")]
for animal in animales:
    try:
        print(animal.hablar())
    except NotImplementedError:
        print("Este animal no sabe hablar")
```

### **Propiedades y Encapsulamiento**
```python
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular  # Atributo "protegido"
        self.__saldo = saldo_inicial  # Atributo "privado"
    
    # Getter y setter con propiedades
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def titular(self, nuevo_titular):
        if len(nuevo_titular) > 0:
            self._titular = nuevo_titular
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
    
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return cantidad
        return 0

# Uso
cuenta = CuentaBancaria("Juan", 1000)
cuenta.depositar(500)
print(cuenta.saldo)  # 1500
cuenta.titular = "Juan Pérez"
```

---

## 📦 Módulos y Paquetes

### **Crear y Usar Módulos**
```python
# mi_modulo.py
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

PI = 3.14159

# main.py (en el mismo directorio)
import mi_modulo

print(mi_modulo.suma(5, 3))
print(mi_modulo.PI)

# Importar específicamente
from mi_modulo import resta
print(resta(10, 4))

# Alias
import mi_modulo as mm
from mi_modulo import suma as s
```

### **Paquetes**
```
mi_paquete/
├── __init__.py
├── modulo1.py
├── modulo2.py
└── subpaquete/
    ├── __init__.py
    └── modulo3.py
```

```python
# Uso del paquete
import mi_paquete.modulo1
from mi_paquete import modulo2
from mi_paquete.subpaquete.modulo3 import funcion
```

### **Módulos Estándar**
```python
import math
import random
import datetime
import os
import sys

# Ejemplos
print(math.sqrt(16))  # 4.0
print(random.randint(1, 10))
print(datetime.datetime.now())

# Path actual
print(os.getcwd())

# Argumentos de línea de comandos
print(sys.argv)
```

---

## 📁 Manejo de Archivos

### **Archivos de Texto**
```python
# Escribir archivo
with open("archivo.txt", "w", encoding="utf-8") as f:
    f.write("Línea 1\n")
    f.write("Línea 2\n")
    f.writelines(["Línea 3\n", "Línea 4\n"])

# Leer archivo completo
with open("archivo.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
    print(contenido)

# Leer línea por línea
with open("archivo.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(linea.strip())  # strip() quita \n

# Leer todas las líneas en lista
with open("archivo.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()

# Modos: r (lectura), w (escritura), a (añadir), r+ (lectura/escritura)
```

### **Archivos JSON**
```python
import json

# Datos
datos = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Madrid",
    "hobbies": ["leer", "correr", "viajar"]
}

# Escribir JSON
with open("datos.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=2, ensure_ascii=False)

# Leer JSON
with open("datos.json", "r", encoding="utf-8") as f:
    datos_cargados = json.load(f)

# Convertir entre string y objeto
json_str = json.dumps(datos)
objeto = json.loads(json_str)
```

---

## 🛡️ Manejo de Errores

### **Try-Except**
```python
# Manejo básico
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Error: Debes ingresar un número válido")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
except Exception as e:
    print(f"Error inesperado: {e}")
else:
    print("Operación completada exitosamente")
finally:
    print("Este bloque siempre se ejecuta")
```

### **Excepciones Personalizadas**
```python
class SaldoInsuficienteError(Exception):
    """Excepción para saldo insuficiente"""
    def __init__(self, saldo, cantidad):
        self.saldo = saldo
        self.cantidad = cantidad
        self.mensaje = f"Saldo insuficiente: {saldo} < {cantidad}"
        super().__init__(self.mensaje)

class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
    
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise SaldoInsuficienteError(self.saldo, cantidad)
        self.saldo -= cantidad
        return cantidad

# Uso
try:
    cuenta = CuentaBancaria(100)
    cuenta.retirar(150)
except SaldoInsuficienteError as e:
    print(f"Error: {e}")
```

---

## 📚 Librerías Esenciales

### **Data Science & Análisis**
```python
# pip install numpy pandas matplotlib scikit-learn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# NumPy - Arrays y matemáticas
arr = np.array([1, 2, 3, 4, 5])
matriz = np.random.rand(3, 3)

# Pandas - Análisis de datos
df = pd.DataFrame({
    'Nombre': ['Ana', 'Juan', 'María'],
    'Edad': [25, 30, 28],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
})

# Matplotlib - Gráficos
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico simple')
plt.show()
```

### **Desarrollo Web**
```python
# pip install flask django requests beautifulsoup4

# Flask - Framework web ligero
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '¡Hola, Mundo!'

# Requests - Peticiones HTTP
import requests
respuesta = requests.get('https://api.example.com/data')
datos = respuesta.json()

# BeautifulSoup - Web scraping
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
```

### **Automatización y Scripting**
```python
import os
import sys
import subprocess
import shutil
import pathlib
import argparse

# Ejecutar comandos del sistema
resultado = subprocess.run(['ls', '-la'], capture_output=True, text=True)

# Manejo de rutas moderno
ruta = pathlib.Path('mi_archivo.txt')
print(ruta.absolute())
print(ruta.parent)

# Argumentos de línea de comandos
parser = argparse.ArgumentParser(description='Mi script')
parser.add_argument('--nombre', help='Tu nombre')
args = parser.parse_args()
```

---

## 🎯 Proyectos Prácticos

### **1. Calculadora**
```python
def calculadora():
    while True:
        print("\n--- Calculadora ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == '5':
            print("¡Hasta luego!")
            break
        
        try:
            num1 = float(input("Primer número: "))
            num2 = float(input("Segundo número: "))
            
            if opcion == '1':
                print(f"Resultado: {num1 + num2}")
            elif opcion == '2':
                print(f"Resultado: {num1 - num2}")
            elif opcion == '3':
                print(f"Resultado: {num1 * num2}")
            elif opcion == '4':
                if num2 != 0:
                    print(f"Resultado: {num1 / num2}")
                else:
                    print("Error: No se puede dividir por cero")
            else:
                print("Opción no válida")
        except ValueError:
            print("Error: Ingresa números válidos")
```

### **2. Gestor de Tareas (To-Do)**
```python
import json
import os

class GestorTareas:
    def __init__(self, archivo="tareas.json"):
        self.archivo = archivo
        self.tareas = self.cargar_tareas()
    
    def cargar_tareas(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, 'r') as f:
                return json.load(f)
        return []
    
    def guardar_tareas(self):
        with open(self.archivo, 'w') as f:
            json.dump(self.tareas, f, indent=2)
    
    def agregar_tarea(self, descripcion):
        tarea = {
            "id": len(self.tareas) + 1,
            "descripcion": descripcion,
            "completada": False
        }
        self.tareas.append(tarea)
        self.guardar_tareas()
        print(f"Tarea '{descripcion}' agregada")
    
    def listar_tareas(self):
        if not self.tareas:
            print("No hay tareas")
            return
        
        for tarea in self.tareas:
            estado = "✓" if tarea["completada"] else "✗"
            print(f"{tarea['id']}. [{estado}] {tarea['descripcion']}")
    
    def marcar_completada(self, id_tarea):
        for tarea in self.tareas:
            if tarea["id"] == id_tarea:
                tarea["completada"] = True
                self.guardar_tareas()
                print(f"Tarea {id_tarea} marcada como completada")
                return
        print(f"No se encontró tarea con ID {id_tarea}")
    
    def eliminar_tarea(self, id_tarea):
        self.tareas = [t for t in self.tareas if t["id"] != id_tarea]
        self.guardar_tareas()
        print(f"Tarea {id_tarea} eliminada")

# Menú principal
def main():
    gestor = GestorTareas()
    
    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == '1':
            desc = input("Descripción de la tarea: ")
            gestor.agregar_tarea(desc)
        elif opcion == '2':
            gestor.listar_tareas()
        elif opcion == '3':
            try:
                id_tarea = int(input("ID de la tarea: "))
                gestor.marcar_completada(id_tarea)
            except ValueError:
                print("ID debe ser un número")
        elif opcion == '4':
            try:
                id_tarea = int(input("ID de la tarea: "))
                gestor.eliminar_tarea(id_tarea)
            except ValueError:
                print("ID debe ser un número")
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
```

---

## 🎓 Recursos de Aprendizaje

### **Documentación Oficial**
- [Python.org](https://www.python.org/)
- [Documentación oficial](https://docs.python.org/3/)
- [Tutorial oficial](https://docs.python.org/3/tutorial/)

### **Cursos y Tutoriales**
- [Real Python](https://realpython.com/)
- [Python para todos](https://www.pythonparatodos.es/)
- [W3Schools Python](https://www.w3schools.com/python/)

### **Práctica**
- [Codewars](https://www.codewars.com/)
- [LeetCode](https://leetcode.com/)
- [HackerRank](https://www.hackerrank.com/domains/tutorials/10-days-of-python)

### **Comunidad**
- [Stack Overflow](https://stackoverflow.com/questions/tagged/python)
- [Reddit - r/learnpython](https://www.reddit.com/r/learnpython/)
- [Discord Python España](https://discord.gg/python-es)

---

## ✅ Buenas Prácticas

### **PEP 8 - Guía de Estilo**
```python
# Variables y funciones en snake_case
mi_variable = 10
def mi_funcion():
    pass

# Clases en CamelCase
class MiClase:
    pass

# Constantes en MAYÚSCULAS
PI = 3.14159
MAX_USUARIOS = 100

# Espaciado
x = 1
y = 2
resultado = x + y  # Espacio alrededor de operadores

# Límite de línea: 79 caracteres
linea_larga = ("Esta es una línea muy larga que debe ser "
               "dividida para cumplir con PEP 8")
```

### **Consejos Importantes**
1. **Escribe código legible** - El código se escribe una vez pero se lee muchas veces
2. **Usa nombres descriptivos** - `total_ventas` es mejor que `tv`
3. **Mantén funciones pequeñas** - Una función, una responsabilidad
4. **Documenta tu código** - Docstrings y comentarios útiles
5. **Escribe pruebas** - Asegura que tu código funciona correctamente
6. **Usa control de versiones** - Git es esencial
7. **Virtual environments** - Aísla dependencias de cada proyecto

---

## 🚀 Siguientes Pasos

### **Áreas de Especialización**
1. **Ciencia de Datos**: Pandas, NumPy, Scikit-learn, TensorFlow
2. **Desarrollo Web**: Django, Flask, FastAPI
3. **Automatización**: Scripts, scraping, bots
4. **Machine Learning**: Scikit-learn, PyTorch, Keras
5. **DevOps**: Automatización, AWS, Docker
6. **Desarrollo de Juegos**: PyGame

### **Proyectos para Practicar**
1. **Web scraper** - Extraer datos de sitios web
2. **API REST** - Crear un servicio web
3. **Bot de Telegram/Discord** - Automatización
4. **Análisis de datos** - Visualización con gráficos
5. **Juego simple** - Adivinanzas, ahorcado
6. **Automatización de tareas** - Organizar archivos, enviar emails

---
