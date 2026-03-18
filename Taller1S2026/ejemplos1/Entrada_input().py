# Ejemplo de cómo leer datos del usuario con input()

# input() muestra un mensaje y espera que el usuario escriba algo.
# Siempre devuelve un texto (string).
nombre = input('¿Cómo te llamas? ')   # Guarda lo que el usuario escriba
print('Hola, ' + nombre + '!')        # Saluda usando el nombre

# Para trabajar con números, debemos convertir el texto a número.
# int() convierte a entero, float() convierte a decimal.
edad_texto = input('¿Cuántos años tienes? ')   # Lee texto
edad = int(edad_texto)                          # Convierte a entero
print('En 10 años tendrás:', edad + 10)         # Calcula y muestra

# Resumen:
# input() permite que el usuario ingrese datos desde el teclado.
# Como siempre devuelve texto, si necesitamos números usamos int() o float()
# para convertirlos.