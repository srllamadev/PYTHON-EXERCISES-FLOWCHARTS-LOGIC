def validar_password():
    password_correcta = "PyTh0nR0cks!"
    intentos = 3
    
    print("\nSistema de acceso (Password = 'PyTh0nR0cks!')")
    while intentos > 0:
        entrada = input(f"Contraseña ({intentos} intentos restantes): ")
        if entrada == password_correcta:
            print("¡Acceso concedido!")
            return
        else:
            print("Contraseña incorrecta.")
            intentos -= 1
    
    print("¡Cuenta bloqueada!")  # Si agota los intentos

validar_password()  # Ejecutar validación