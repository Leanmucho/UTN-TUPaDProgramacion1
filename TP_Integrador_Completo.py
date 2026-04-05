# ============================================================================
# TRABAJO PRÁCTICO INTEGRADOR
# Estructuras Repetitivas, Condicionales y Secuenciales
# ============================================================================

# ============================================================================
# EJERCICIO 1 - "CAJA DEL KIOSCO"
# ============================================================================

def ejercicio_1():
    print("\n" + "="*60)
    print("EJERCICIO 1 - CAJA DEL KIOSCO")
    print("="*60)

    # Validar nombre del cliente
    while True:
        nombre = input("Cliente: ")
        if nombre.isalpha() and len(nombre) > 0:
            break
        print("Error: El nombre debe contener solo letras")

    # Validar cantidad de productos
    while True:
        cantidad_str = input("Cantidad de productos: ")
        if cantidad_str.isdigit() and int(cantidad_str) > 0:
            cantidad = int(cantidad_str)
            break
        print("Error: Ingrese un número mayor a 0")

    total_sin_descuento = 0
    total_con_descuento = 0

    # Por cada producto
    for i in range(1, cantidad + 1):
        # Validar precio
        while True:
            precio_str = input(f"Producto {i} - Precio: ")
            if precio_str.isdigit() and int(precio_str) > 0:
                precio = int(precio_str)
                break
            print("Error: Ingrese un número válido")

        # Validar descuento
        while True:
            descuento = input(f"Descuento (S/N): ").lower()
            if descuento in ['s', 'n']:
                break
            print("Error: Ingrese S o N")

        total_sin_descuento += precio

        if descuento == 's':
            precio_con_descuento = precio * 0.9
            total_con_descuento += precio_con_descuento
        else:
            total_con_descuento += precio

    ahorro = total_sin_descuento - total_con_descuento
    promedio = total_con_descuento / cantidad

    print(f"\nTotal sin descuentos: ${total_sin_descuento}")
    print(f"Total con descuentos: ${total_con_descuento:.2f}")
    print(f"Ahorro: ${ahorro:.2f}")
    print(f"Promedio por producto: ${promedio:.2f}")


# ============================================================================
# EJERCICIO 2 - "ACCESO AL CAMPUS Y MENÚ SEGURO"
# ============================================================================

def ejercicio_2():
    print("\n" + "="*60)
    print("EJERCICIO 2 - ACCESO AL CAMPUS Y MENÚ SEGURO")
    print("="*60)

    usuario_correcto = "alumno"
    clave_correcta = "python123"
    intentos = 0
    acceso_concedido = False

    # Proceso de login
    while intentos < 3 and not acceso_concedido:
        intentos += 1
        usuario = input(f"Intento {intentos}/3 - Usuario: ")
        clave = input("Clave: ")

        if usuario == usuario_correcto and clave == clave_correcta:
            print("Acceso concedido.")
            acceso_concedido = True
        else:
            print("Error: credenciales inválidas.\n")

    if not acceso_concedido:
        print("Cuenta bloqueada")
        return

    # Menú después del acceso
    clave_actual = clave_correcta

    while True:
        print("\n1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")

        while True:
            opcion = input("Opción: ")
            if opcion.isdigit() and opcion in ['1', '2', '3', '4']:
                break
            if not opcion.isdigit():
                print("Error: ingrese un número válido.")
            else:
                print("Error: opción fuera de rango.")

        if opcion == '1':
            print("Inscripto")
        elif opcion == '2':
            while True:
                nueva_clave = input("Nueva clave: ")
                if len(nueva_clave) >= 6:
                    confirmacion = input("Confirmación: ")
                    if nueva_clave == confirmacion:
                        clave_actual = nueva_clave
                        print("Clave cambiada exitosamente.")
                        break
                    else:
                        print("Error: las claves no coinciden.")
                else:
                    print("Error: mínimo 6 caracteres.")
        elif opcion == '3':
            print("¡Sigue adelante, estás en el camino correcto!")
        elif opcion == '4':
            print("Sesión cerrada.")
            break


# ============================================================================
# EJERCICIO 3 - "AGENDA DE TURNOS CON NOMBRES (sin listas)"
# ============================================================================

def ejercicio_3():
    print("\n" + "="*60)
    print("EJERCICIO 3 - AGENDA DE TURNOS CON NOMBRES")
    print("="*60)

    # Validar nombre del operador
    while True:
        operador = input("Nombre del operador: ")
        if operador.isalpha() and len(operador) > 0:
            break
        print("Error: El nombre debe contener solo letras")

    # Variables para los turnos (sin listas)
    lunes1, lunes2, lunes3, lunes4 = "", "", "", ""
    martes1, martes2, martes3 = "", "", ""

    while True:
        print("\n1) Reservar turno")
        print("2) Cancelar turno")
        print("3) Ver agenda del día")
        print("4) Ver resumen general")
        print("5) Cerrar sistema")

        while True:
            opcion = input("Opción: ")
            if opcion.isdigit() and opcion in ['1', '2', '3', '4', '5']:
                break
            print("Error: Ingrese una opción válida")

        if opcion == '1':  # Reservar turno
            while True:
                dia = input("Día (1=Lunes, 2=Martes): ")
                if dia.isdigit() and dia in ['1', '2']:
                    dia = int(dia)
                    break
                print("Error: Ingrese 1 o 2")

            while True:
                paciente = input("Nombre del paciente: ")
                if paciente.isalpha() and len(paciente) > 0:
                    break
                print("Error: El nombre debe contener solo letras")

            if dia == 1:
                # Verificar si no está repetido
                if paciente not in [lunes1, lunes2, lunes3, lunes4]:
                    if lunes1 == "":
                        lunes1 = paciente
                        print(f"Turno reservado para {paciente} el Lunes")
                    elif lunes2 == "":
                        lunes2 = paciente
                        print(f"Turno reservado para {paciente} el Lunes")
                    elif lunes3 == "":
                        lunes3 = paciente
                        print(f"Turno reservado para {paciente} el Lunes")
                    elif lunes4 == "":
                        lunes4 = paciente
                        print(f"Turno reservado para {paciente} el Lunes")
                    else:
                        print("No hay turnos disponibles para Lunes")
                else:
                    print("Error: El paciente ya tiene turno ese día")
            else:
                # Verificar si no está repetido
                if paciente not in [martes1, martes2, martes3]:
                    if martes1 == "":
                        martes1 = paciente
                        print(f"Turno reservado para {paciente} el Martes")
                    elif martes2 == "":
                        martes2 = paciente
                        print(f"Turno reservado para {paciente} el Martes")
                    elif martes3 == "":
                        martes3 = paciente
                        print(f"Turno reservado para {paciente} el Martes")
                    else:
                        print("No hay turnos disponibles para Martes")
                else:
                    print("Error: El paciente ya tiene turno ese día")

        elif opcion == '2':  # Cancelar turno
            while True:
                dia = input("Día (1=Lunes, 2=Martes): ")
                if dia.isdigit() and dia in ['1', '2']:
                    dia = int(dia)
                    break
                print("Error: Ingrese 1 o 2")

            while True:
                paciente = input("Nombre del paciente: ")
                if paciente.isalpha() and len(paciente) > 0:
                    break
                print("Error: El nombre debe contener solo letras")

            if dia == 1:
                if lunes1 == paciente:
                    lunes1 = ""
                    print(f"Turno de {paciente} cancelado")
                elif lunes2 == paciente:
                    lunes2 = ""
                    print(f"Turno de {paciente} cancelado")
                elif lunes3 == paciente:
                    lunes3 = ""
                    print(f"Turno de {paciente} cancelado")
                elif lunes4 == paciente:
                    lunes4 = ""
                    print(f"Turno de {paciente} cancelado")
                else:
                    print("El paciente no tiene turno ese día")
            else:
                if martes1 == paciente:
                    martes1 = ""
                    print(f"Turno de {paciente} cancelado")
                elif martes2 == paciente:
                    martes2 = ""
                    print(f"Turno de {paciente} cancelado")
                elif martes3 == paciente:
                    martes3 = ""
                    print(f"Turno de {paciente} cancelado")
                else:
                    print("El paciente no tiene turno ese día")

        elif opcion == '3':  # Ver agenda del día
            while True:
                dia = input("Día (1=Lunes, 2=Martes): ")
                if dia.isdigit() and dia in ['1', '2']:
                    dia = int(dia)
                    break
                print("Error: Ingrese 1 o 2")

            if dia == 1:
                print("\n--- AGENDA LUNES ---")
                print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
                print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
                print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
                print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
            else:
                print("\n--- AGENDA MARTES ---")
                print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
                print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
                print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

        elif opcion == '4':  # Ver resumen general
            ocupados_lunes = sum([1 for t in [lunes1, lunes2, lunes3, lunes4] if t != ""])
            disponibles_lunes = 4 - ocupados_lunes
            ocupados_martes = sum([1 for t in [martes1, martes2, martes3] if t != ""])
            disponibles_martes = 3 - ocupados_martes

            print("\n--- RESUMEN GENERAL ---")
            print(f"Lunes: {ocupados_lunes} ocupados, {disponibles_lunes} disponibles")
            print(f"Martes: {ocupados_martes} ocupados, {disponibles_martes} disponibles")

            if ocupados_lunes > ocupados_martes:
                print("Día con más turnos: Lunes")
            elif ocupados_martes > ocupados_lunes:
                print("Día con más turnos: Martes")
            else:
                print("Días empatados")

        elif opcion == '5':
            print("Sistema cerrado.")
            break


# ============================================================================
# EJERCICIO 4 - "ESCAPE ROOM: LA BÓVEDA"
# ============================================================================

def ejercicio_4():
    print("\n" + "="*60)
    print("EJERCICIO 4 - ESCAPE ROOM: LA BÓVEDA")
    print("="*60)

    # Validar nombre del agente
    while True:
        agente = input("Nombre del agente: ")
        if agente.isalpha() and len(agente) > 0:
            break
        print("Error: El nombre debe contener solo letras")

    # Variables iniciales
    energia = 100
    tiempo = 12
    cerraduras_abiertas = 0
    alarma = False
    codigo_parcial = ""
    racha_forzar = 0

    print(f"\n¡Bienvenido {agente}! Debes abrir 3 cerraduras antes de quedarte sin energía o tiempo.")

    while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):
        print(f"\n--- ESTADO ---")
        print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras abiertas: {cerraduras_abiertas}")
        if alarma:
            print("⚠️ ¡ALARMA ACTIVADA!")

        print("\n1) Forzar cerradura (-20 energía, -2 tiempo)")
        print("2) Hackear panel (-10 energía, -3 tiempo)")
        print("3) Descansar (+15 energía, -1 tiempo)")

        while True:
            opcion = input("Opción: ")
            if opcion.isdigit() and opcion in ['1', '2', '3']:
                break
            print("Error: Ingrese una opción válida")

        if opcion == '1':  # Forzar cerradura
            if energia >= 20 and tiempo >= 2:
                energia -= 20
                tiempo -= 2
                racha_forzar += 1

                if energia < 40:
                    print("⚠️ ¡RIESGO DE ALARMA! Ingrese un número 1-3:")
                    while True:
                        num = input("Número: ")
                        if num.isdigit() and num in ['1', '2', '3']:
                            if num == '3':
                                alarma = True
                            break
                        print("Error: Ingrese 1, 2 o 3")

                if racha_forzar == 3:
                    alarma = True
                    print("❌ ¡La cerradura se trabó! ALARMA ACTIVADA")
                    racha_forzar = 0
                elif not alarma:
                    cerraduras_abiertas += 1
                    print(f"✓ Cerradura abierta ({cerraduras_abiertas}/3)")
                    racha_forzar = 0
            else:
                print("No hay suficiente energía o tiempo")

        elif opcion == '2':  # Hackear panel
            if energia >= 10 and tiempo >= 3:
                energia -= 10
                tiempo -= 3
                racha_forzar = 0
                print("🔐 Hackeando panel...")
                for i in range(4):
                    codigo_parcial += "A"
                    print(f"  Paso {i+1}: {codigo_parcial}")

                if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                    cerraduras_abiertas += 1
                    print(f"✓ Cerradura abierta ({cerraduras_abiertas}/3)")
            else:
                print("No hay suficiente energía o tiempo")

        elif opcion == '3':  # Descansar
            if tiempo >= 1:
                tiempo -= 1
                racha_forzar = 0
                energia = min(energia + 15, 100)
                if alarma:
                    energia -= 10
                    print("Descansaste pero la alarma te consume energía extra")
                else:
                    print("Descansaste y recuperaste energía")
            else:
                print("No hay tiempo para descansar")

    print(f"\n{'='*60}")
    if cerraduras_abiertas == 3:
        print(f"🎉 ¡VICTORIA! {agente} ha abierto la bóveda")
    elif energia <= 0 or tiempo <= 0:
        print("💀 DERROTA - Sin energía o sin tiempo")
    elif alarma and tiempo <= 3:
        print("💀 DERROTA - Sistema bloqueado por alarma")
    print(f"{'='*60}")


# ============================================================================
# EJERCICIO 5 - "ESCAPE ROOM: LA ARENA DEL GLADIADOR"
# ============================================================================

def ejercicio_5():
    print("\n" + "="*60)
    print("EJERCICIO 5 - ESCAPE ROOM: LA ARENA DEL GLADIADOR")
    print("="*60)
    print("\n--- BIENVENIDO A LA ARENA ---")

    # Validar nombre del gladiador
    while True:
        nombre = input("Nombre del Gladiador: ")
        if nombre.isalpha() and len(nombre) > 0:
            break
        print("Error: Solo se permiten letras.")

    # Estadísticas iniciales
    vida_jugador = 100
    vida_enemigo = 100
    pociones = 3
    daño_base = 15
    daño_enemigo = 12

    print(f"\n=== INICIO DEL COMBATE ===")

    while vida_jugador > 0 and vida_enemigo > 0:
        print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
        print("\nElige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        # Validar opción
        while True:
            opcion = input("Opción: ")
            if opcion.isdigit() and opcion in ['1', '2', '3']:
                break
            print("Error: Ingrese un número válido.")

        if opcion == '1':  # Ataque Pesado
            daño = daño_base
            if vida_enemigo < 20:
                daño = daño_base * 1.5
                print(f"⚡ ¡GOLPE CRÍTICO!")
            vida_enemigo -= daño
            print(f"¡Atacaste al enemigo por {daño} puntos de daño!")

        elif opcion == '2':  # Ráfaga Veloz
            print(">> ¡Inicias una ráfaga de golpes!")
            for i in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")

        elif opcion == '3':  # Curar
            if pociones > 0:
                vida_jugador = min(vida_jugador + 30, 100)
                pociones -= 1
                print(f"Usaste una poción. Vida: {vida_jugador} | Pociones restantes: {pociones}")
            else:
                print("¡No quedan pociones!")

        # Ataque del enemigo
        if vida_enemigo > 0:
            vida_jugador -= daño_enemigo
            print(f">> ¡El enemigo contraataca por {daño_enemigo} puntos!")

        if vida_jugador > 0 and vida_enemigo > 0:
            print(f"\n=== NUEVO TURNO ===")

    print(f"\n{'='*60}")
    if vida_jugador > 0:
        print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
    else:
        print("DERROTA. Has caído en combate.")
    print(f"{'='*60}")


# ============================================================================
# MENÚ PRINCIPAL
# ============================================================================

def menu_principal():
    while True:
        print("\n" + "="*60)
        print("TRABAJO PRÁCTICO INTEGRADOR")
        print("="*60)
        print("1) Ejercicio 1 - Caja del Kiosco")
        print("2) Ejercicio 2 - Acceso al Campus")
        print("3) Ejercicio 3 - Agenda de Turnos")
        print("4) Ejercicio 4 - Escape Room: La Bóveda")
        print("5) Ejercicio 5 - Arena del Gladiador")
        print("6) Salir")

        opcion = input("\nSeleccione un ejercicio: ")

        if opcion == '1':
            ejercicio_1()
        elif opcion == '2':
            ejercicio_2()
        elif opcion == '3':
            ejercicio_3()
        elif opcion == '4':
            ejercicio_4()
        elif opcion == '5':
            ejercicio_5()
        elif opcion == '6':
            print("\n¡Hasta luego!")
            break
        else:
            print("Error: Opción no válida")


# ============================================================================
# EJECUTAR PROGRAMA
# ============================================================================

if __name__ == "__main__":
    menu_principal()