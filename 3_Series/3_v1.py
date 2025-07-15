#el codigo trata de reemplazar las decenas de un numero por la decena del siguiente numero en la lista
#si el siguiente numero no tiene decenas, se deja el numero sin cambios
#la salida es una lista de numeros con las decenas reemplazadas
#el primer numero de la lista se mueve al final de la lista
#el resultado es una lista de numeros con las decenas reemplazadas y el primer numero
def reemplazar_decenas(numeros):
   
    resultado = numeros[:]  

    def reemplaza_decena(num, nueva_decena):

        parte_superior = num // 100
        unidad = num % 10
        
        return parte_superior * 100 + nueva_decena * 10 + unidad

    N = len(numeros)
    for i in range(N):
        if numeros[i] >= 10:
            decena = (numeros[i] // 10) % 10
            siguiente = (i + 1) % N
            if resultado[siguiente] >= 10:
                resultado[siguiente] = reemplaza_decena(resultado[siguiente], decena)
    
    return resultado

if __name__ == "__main__":
    numeros = [4568, 746, 35, 5, 6575, 345, 657, 57]
    
    print("Entrada:")
    print(" ".join(map(str, numeros)))
    
    resultado = reemplazar_decenas(numeros)
    
    print("\nResultado:")
    orden_transformacion = resultado[1:] + resultado[:1]
    print(" ".join(map(str, orden_transformacion)))
