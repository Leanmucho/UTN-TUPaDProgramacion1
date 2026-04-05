# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# • Niño/a: menor de 12 años.
# • Adolescente: mayor o igual que 12 años y menor que 18 años.
# • Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# • Adulto/a: mayor o igual que 30 años.
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos
# que tiene un iterable tal como una lista o un string.
contrasena = input("Ingrese una contraseña: ")
if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) Escribir un programa que solicite al usuario el consumo mensual de energía eléctrica en
# kilovatios (kWh) e indique la categoría del consumo según el siguiente criterio:
# • Menor que 150 kWh: “Consumo bajo”.
# • Entre 150 y 300 kWh (inclusive): “Consumo medio”.
# • Mayor que 300 kWh: “Consumo alto”.
# Además, si el consumo supera los 500 kWh, mostrar un mensaje adicional que diga:
# “Considere medidas de ahorro energético”.
# El programa debe imprimir por pantalla la categoría correspondiente.
consumo = float(input("Ingrese el consumo mensual en kWh: "))
if consumo < 150:
    print("Consumo bajo")
elif consumo <= 300:
    print("Consumo medio")
else:
    print("Consumo alto")
if consumo > 500:
    print("Considere medidas de ahorro energético")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.
frase = input("Ingrese una frase o palabra: ")
vocales = "aeiouAEIOU"
if frase[-1] in vocales:
    print(frase + "!")
else:
    print(frase)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo con la opción seleccionada por
# el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.
nombre = input("Ingrese su nombre: ")
opcion = int(input("Elija una opción (1: MAYÚSCULAS, 2: minúsculas, 3: Primera letra mayúscula): "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción no válida")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# • Menor que 3: "Muy leve" (imperceptible).
# • Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# • Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# • Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# • Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# • Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año :
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()
mes = int(input("¿Qué mes del año es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

# Determinamos la estación según hemisferio norte
if (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia < 21):
    estacion_norte = "Primavera"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia < 23):
    estacion_norte = "Verano"
elif (mes == 9 and dia >= 23) or (mes in [10, 11]) or (mes == 12 and dia < 21):
    estacion_norte = "Otoño"
else:
    estacion_norte = "Invierno"

# En el hemisferio sur las estaciones son opuestas
opuestas = {"Primavera": "Otoño", "Verano": "Invierno", "Otoño": "Primavera", "Invierno": "Verano"}

if hemisferio == "N":
    print(f"Estás en: {estacion_norte}")
elif hemisferio == "S":
    print(f"Estás en: {opuestas[estacion_norte]}")
else:
    print("Hemisferio no válido. Ingrese N o S.")
