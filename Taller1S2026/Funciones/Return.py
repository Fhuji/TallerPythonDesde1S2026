
# Ejemplo de función que devuelve un valor con return

def calcular_area(base, altura):
    area = base * altura   # Calcula el área
    return area             # Devuelve el resultado

# Guardamos el valor devuelto en una variable
mi_area = calcular_area(5, 3)
print('El área es:', mi_area)

# También podemos usar directamente el valor devuelto
print('Área:', calcular_area(10, 2))

# Resumen:
# return permite que una función envíe un resultado de vuelta al lugar
# desde donde fue llamada. Ese resultado se puede guardar o usar directamente.