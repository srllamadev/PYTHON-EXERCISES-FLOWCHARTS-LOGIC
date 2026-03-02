# 02 - Estructuras Condicionales

## Descripción General

Este módulo cubre las estructuras de control condicional en Python, que permiten que tu programa tome decisiones y ejecute diferentes bloques de código según las condiciones especificadas.

## Estructura del Módulo

### 📁 [01_If_Elif_Else](01_If_Elif_Else/)
Aprende a usar las sentencias condicionales básicas para tomar decisiones en tu código.

**Temas clave:**
- Sentencia if simple
- if-else para dos alternativas
- if-elif-else para múltiples condiciones
- Condicionales anidados
- Buenas prácticas

### 📁 [02_Operadores_Logicos](02_Operadores_Logicos/)
Domina los operadores lógicos para combinar múltiples condiciones.

**Temas clave:**
- Operador AND (y lógico)
- Operador OR (o lógico)
- Operador NOT (negación)
- Combinación de operadores
- Cortocircuito de evaluación

### 📁 [03_Expresiones_Booleanas](03_Expresiones_Booleanas/)
Entiende cómo trabajar con valores booleanos y expresiones lógicas complejas.

**Temas clave:**
- Valores de verdad (Truthy y Falsy)
- Comparaciones múltiples
- Expresiones booleanas complejas
- Simplificación de condiciones
- Leyes de De Morgan

### 📁 [04_Operador_Ternario](04_Operador_Ternario/)
Aprende a escribir condicionales de manera concisa usando el operador ternario.

**Temas clave:**
- Sintaxis del operador ternario
- Casos de uso apropiados
- Ternarios anidados
- Alternativas más legibles
- Cuándo usar y cuándo evitar

## Objetivos de Aprendizaje

Al completar este módulo, serás capaz de:

✅ Escribir condicionales simples y complejas  
✅ Combinar múltiples condiciones con operadores lógicos  
✅ Entender la evaluación de expresiones booleanas  
✅ Usar el operador ternario apropiadamente  
✅ Anidar condicionales cuando sea necesario  
✅ Escribir código condicional limpio y legible  
✅ Depurar problemas en lógica condicional  

## Requisitos Previos

- ✅ Módulo 01_Introduccion completado
- Variables y tipos de datos
- Operadores de comparación
- Conceptos básicos de input/output

## Tiempo Estimado

⏱️ **1-2 semanas** (2-3 horas diarias)

## Proyecto Integrador del Módulo

Al finalizar, completa el **Proyecto Final: Sistema de Calificaciones**

### Descripción
Crea un programa que:
1. Solicite las calificaciones de un estudiante (3-5 materias)
2. Calcule el promedio
3. Determine si aprobó o reprobó cada materia
4. Asigne una letra de calificación (A, B, C, D, F)
5. Determine si tiene mención honorífica
6. Muestre un reporte completo formateado
7. Incluya validaciones de entrada

### Criterios de Calificación
```
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59

Mención honorífica: Promedio >= 95
Aprobado: Todas las materias >= 60
```

### Ejemplo de Salida
```
========================================
    SISTEMA DE CALIFICACIONES
========================================

Ingresa las calificaciones (0-100):
Matemáticas: 95
Física: 88
Química: 92

========================================
         REPORTE ACADÉMICO
========================================
Materia          Calif.  Letra  Estado
----------------------------------------
Matemáticas        95      A    ✓ Aprobado
Física             88      B    ✓ Aprobado
Química            92      A    ✓ Aprobado
----------------------------------------
PROMEDIO:         91.67    A

Estado General: ✓ APROBADO
Mención Honorífica: No
========================================
```

## Recursos Complementarios

### Libros
- "Python Crash Course" (Capítulo 5) - Eric Matthes
- "Automate the Boring Stuff" (Capítulo 2) - Al Sweigart
- "Think Python" (Capítulo 5) - Allen Downey

### Documentación Oficial
- [Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Boolean Operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
- [Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)

### Videos Recomendados
- Python Conditionals and Booleans - Corey Schafer
- Python if statements - Programming with Mosh

### Práctica Online
- [Codecademy - Python Conditionals](https://www.codecademy.com/)
- [HackerRank - Python If-Else](https://www.hackerrank.com/)
- [LeetCode - Easy Conditionals](https://leetcode.com/)

## Evaluación

### Checklist de Competencias

Antes de avanzar al siguiente módulo, asegúrate de poder:

- [ ] Escribir sentencias if simples correctamente
- [ ] Usar if-elif-else para múltiples alternativas
- [ ] Combinar condiciones con AND, OR, NOT
- [ ] Entender la precedencia de operadores lógicos
- [ ] Identificar valores truthy y falsy
- [ ] Usar el operador ternario apropiadamente
- [ ] Evitar condicionales anidados excesivos
- [ ] Escribir condiciones legibles y mantenibles
- [ ] Depurar lógica condicional incorrecta
- [ ] Validar entrada de usuarios con condicionales

### Ejercicios de Autoevaluación

1. **If básico**: Verificador de edad para votar
2. **If-elif-else**: Calculadora de descuentos por categoría
3. **Operadores lógicos**: Sistema de acceso con múltiples validaciones
4. **Expresiones booleanas**: Validador de contraseñas seguras
5. **Operador ternario**: Formateador de mensajes condicionales
6. **Proyecto integrador**: Sistema de calificaciones completo

## Patrones Comunes

### 1. Validación de Entrada
```python
edad = int(input("Edad: "))
if edad < 0:
    print("Error: Edad inválida")
elif edad < 18:
    print("Menor de edad")
else:
    print("Mayor de edad")
```

### 2. Rangos de Valores
```python
if 0 <= temperatura < 10:
    print("Frío")
elif 10 <= temperatura < 25:
    print("Templado")
else:
    print("Calor")
```

### 3. Múltiples Validaciones
```python
if usuario and contraseña and len(contraseña) >= 8:
    print("Acceso concedido")
else:
    print("Credenciales inválidas")
```

### 4. Flags (Banderas)
```python
es_premium = True
descuento_activo = True

if es_premium and descuento_activo:
    precio_final = precio * 0.8
```

## Consejos de Estudio

💡 **Tips para Dominar Condicionales:**

1. **Dibuja diagramas de flujo** - Visualiza la lógica antes de codificar
2. **Prueba todos los caminos** - Asegúrate de probar cada rama
3. **Simplifica condiciones** - Usa variables descriptivas
4. **Evita redundancia** - No repitas condiciones innecesarias
5. **Usa indentación consistente** - Python la requiere
6. **Comenta lógica compleja** - Explica el "por qué"

⚠️ **Errores Comunes a Evitar:**

- Usar `=` en vez de `==` en comparaciones
- Olvidar los dos puntos `:` después de la condición
- Indentación incorrecta del bloque de código
- Condiciones redundantes o contradictorias
- No considerar todos los casos posibles
- Anidar demasiado (más de 3 niveles)
- No usar paréntesis para claridad en condiciones complejas

## Buenas Prácticas

### ✅ Código Limpio
```python
# BIEN: Descriptivo y claro
if edad >= 18 and tiene_licencia:
    print("Puede conducir")

# MAL: Poco claro
if x >= 18 and y:
    print("OK")
```

### ✅ Evitar Anidación Excesiva
```python
# BIEN: Guard clauses (retorno temprano)
if not usuario_valido:
    return "Error: Usuario inválido"
if not contraseña_valida:
    return "Error: Contraseña inválida"
return "Acceso concedido"

# MAL: Anidación profunda
if usuario_valido:
    if contraseña_valida:
        return "Acceso concedido"
    else:
        return "Error: Contraseña inválida"
else:
    return "Error: Usuario inválido"
```

### ✅ Usar Expresiones Booleanas Directamente
```python
# BIEN
es_adulto = edad >= 18

# MAL
if edad >= 18:
    es_adulto = True
else:
    es_adulto = False
```

## Depuración de Condicionales

### Técnicas Útiles:
1. **Print debugging** - Imprime valores antes de la condición
2. **Usar debugger** - Paso a paso con breakpoints
3. **Simplificar** - Divide condiciones complejas
4. **Tabla de verdad** - Para lógica booleana compleja

## Siguiente Módulo

Una vez domines las estructuras condicionales, estarás listo para:

➡️ **03_Estructuras_Repetitivas** - Bucles y iteración

---

**¡Éxito en tu aprendizaje!** 🚀🐍

**Recuerda:** Las decisiones son fundamentales en programación. Dominar condicionales es esencial para escribir programas útiles e inteligentes.
