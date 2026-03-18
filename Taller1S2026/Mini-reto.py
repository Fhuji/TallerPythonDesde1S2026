
# Mini-reto: Adivinar un número secreto en 3 intentos

numero_secreto = 7   # Número fijo que hay que adivinar
intentos = 3         # Cantidad de intentos permitidos

print('Adivina el número del 1 al 10')
print('Tienes', intentos, 'intentos')

# Bucle for que se repite tantas veces como intentos (3)
for intento in range(intentos):
    numero = int(input('Tu intento: '))   # Lee el intento del usuario

    if numero == numero_secreto:          # Si acierta
        print('¡Correcto! Ganaste!')
        break                               # Sale del bucle for
    elif numero < numero_secreto:          # Si el número es menor
        print('El número es mayor')
    else:                                   # Si es mayor
        print('El número es menor')
else:
    # Este else se ejecuta si el bucle for termina sin haber hecho break
    print('Se acabaron los intentos. Era el', numero_secreto)

# Resumen:
# El programa tiene un número secreto y da 3 oportunidades para adivinarlo.
# En cada intento da una pista (mayor o menor). Si acierta, sale con break.
# Si no acierta en los 3 intentos, muestra cuál era el número.