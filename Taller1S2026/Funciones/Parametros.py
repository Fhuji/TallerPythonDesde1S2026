# Ejemplo de función que recibe parámetros

# Función que saluda a una persona (recibe un nombre)
def saludar_persona(nombre):
    print('¡Hola,', nombre + '!')   # Usa el parámetro dentro

# Llamadas con diferentes argumentos
saludar_persona('Ana')   # nombre toma el valor 'Ana'
saludar_persona('Luis')  # nombre toma el valor 'Luis'

# Función con dos parámetros que muestra una suma
def sumar(a, b):
    resultado = a + b
    print(a, '+', b, '=', resultado)

# Llamada a sumar
sumar(5, 3)   # Muestra 5 + 3 = 8

# Resumen:
# Los parámetros son variables que reciben valores al llamar la función.
# Permiten que la función trabaje con diferentes datos cada vez.