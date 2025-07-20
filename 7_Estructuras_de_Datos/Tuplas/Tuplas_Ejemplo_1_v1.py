# 1. Crea una tupla con los siguientes colores: 'rojo', 'verde', 'azul'
colores = ('rojo', 'verde', 'azul')

# 2. Accede e imprime el segundo elemento de la tupla
print(colores[1])  # Debe mostrar: verde

# 3. Intenta modificar el primer elemento a 'amarillo' (comenta el error)
# colores[0] = 'amarillo'  # Descomentar para ver el error

# 4. Convierte la tupla en lista, añade 'amarillo' y convierte de vuelta a tupla
lista_colores = list(colores)
lista_colores.append('amarillo')
nueva_tupla = tuple(lista_colores)
print(nueva_tupla)  # Debe mostrar: ('rojo', 'verde', 'azul', 'amarillo')

# 5. Cuenta cuántas veces aparece 'azul' en la tupla original
print(colores.count('azul'))  # Debe mostrar: 1

# 6. Encuentra la posición de 'verde'
print(colores.index('verde'))  # Debe mostrar: 1