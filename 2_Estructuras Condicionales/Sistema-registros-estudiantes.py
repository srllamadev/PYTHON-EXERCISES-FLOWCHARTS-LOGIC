# Versión mínima: Python 3.10 para usar match-case como switch

def verificar_requisitos(edad, promedio, curso):
    """
    Evalúa si un estudiante cumple con los requisitos de inscripción según el curso elegido.
    """
    print(f"\nVerificando requisitos para el curso: {curso}")
    
    if curso == "Matemáticas Avanzadas":
        if edad >= 18 and promedio >= 80:
            return "Inscripción exitosa en Matemáticas Avanzadas."
        elif edad < 18:
            return "Debes ser mayor de edad para inscribirte en este curso."
        else:
            return "Tu promedio no cumple con el requisito mínimo de 80."
    
    elif curso == "Programación Básica":
        if promedio >= 60:
            return "Inscripción exitosa en Programación Básica."
        else:
            return "Necesitas al menos 60 de promedio para este curso."
    
    elif curso == "Historia Moderna":
        return "Inscripción exitosa en Historia Moderna. No hay requisitos previos."
    
    else:
        return "Curso no reconocido. Intente de nuevo."


def mostrar_menu():
    print("\n=== MENÚ DE CURSOS DISPONIBLES ===")
    print("1. Matemáticas Avanzadas")
    print("2. Programación Básica")
    print("3. Historia Moderna")
    print("4. Salir")


def seleccionar_curso(opcion):
    """
    Simulación de switch usando match-case (requiere Python 3.10+)
    """
    match opcion:
        case 1:
            return "Matemáticas Avanzadas"
        case 2:
            return "Programación Básica"
        case 3:
            return "Historia Moderna"
        case 4:
            return None
        case _:
            return "Opción inválida"


# Función principal
def main():
    print("=== Sistema de Inscripción de Cursos ===")
    nombre = input("Ingrese su nombre: ")
    
    try:
        edad = int(input("Ingrese su edad: "))
        promedio = float(input("Ingrese su promedio general (0-100): "))
    except ValueError:
        print("Error: Debes ingresar datos válidos para edad y promedio.")
        return

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción (1-4): "))
        except ValueError:
            print("Debe ingresar un número válido.")
            continue

        curso = seleccionar_curso(opcion)
        if curso is None:
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        elif curso == "Opción inválida":
            print("Esa opción no existe. Intente de nuevo.")
            continue

        resultado = verificar_requisitos(edad, promedio, curso)
        print(f"\n{nombre}, resultado: {resultado}")

# Ejecutamos la función principal
main()
