# Ejemplo de condicionales: decidir según la edad

# Pedimos la edad al usuario y la convertimos a entero
edad = int(input('¿Cuántos años tienes? '))

# Estructura if - elif - else
if edad >= 18:                     # Si edad es mayor o igual a 18
    print('Eres mayor de edad')
elif edad >= 13:                    # Si no se cumple el primero, pero edad >= 13
    print('Eres adolescente')
else:                               # Si ninguna condición anterior se cumple
    print('Eres menor de edad')

# Resumen:
# El condicional if permite ejecutar diferentes bloques de código según
# se cumplan o no condiciones. elif significa "si no, si" y else es "si no".

# if = si
# elif = si no, es....
# else = de lo contrario (si no se cumple nada anterior)

# otro ejemplo

'''

entero = 100
if entero == 99:                # Si entero es igual a 99 imprime 99
    print('Es 99')
elif entero == 100:             # Si entero es igual a 100 imprime 100
    print('Es 100')
else:                       
    print('No es ni 99 ni 100') # Si entero no es ni 99 ni 100 imprime esto

'''