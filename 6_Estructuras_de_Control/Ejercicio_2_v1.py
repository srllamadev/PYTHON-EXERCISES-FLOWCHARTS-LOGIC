def cajero_automatico():
    saldo = 10000
    limite_diario = 5000
    retirado_hoy = 0
    
    print("\nCajero: Saldo inicial = $10,000 | Límite diario = $5,000")
    while retirado_hoy < limite_diario:
        monto = int(input("\nMonto a retirar: $"))
        # Validar monto
        if monto <= 0:
            print("Monto inválido.")
        elif monto > saldo:
            print("Fondos insuficientes.")
        elif retirado_hoy + monto > limite_diario:
            print(f"Excede límite diario. Puede retirar hasta ${limite_diario - retirado_hoy}")
        else:
            saldo -= monto
            retirado_hoy += monto
            print(f"Retirado: ${monto} | Saldo restante: ${saldo} | Retirado hoy: ${retirado_hoy}")
        
        # Preguntar si desea continuar
        if retirado_hoy < limite_diario and input("¿Continuar? (s/n): ").lower() != 's':
            break

cajero_automatico()  # Ejecutar simulación