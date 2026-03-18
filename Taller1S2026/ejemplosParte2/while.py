# Ejemplo de bucle while con un contador

contador = 0          # Inicializa contador en 0

# Mientras contador sea menor que 5, se ejecuta el bloque
while contador < 5:
    print('Contador:', contador)   # Muestra el valor actual
    contador += 1                   # Incrementa contador en 1 (contador = contador + 1)

# Resumen:
# while repite un bloque mientras una condición sea verdadera.
# Es importante modificar la variable dentro del bucle para que la condición
# llegue a ser falsa en algún momento y no se repita infinitamente.


'''
# Ejemplo: pedir un número positivo hasta que el usuario ingrese uno

numero = -1          # Inicializamos con un valor que no cumple la condición

# Mientras numero sea menor que 0, seguimos pidiendo
while numero < 0:
    numero = int(input('Ingresa un número positivo: '))

print('Gracias! El número es:', numero)

# Resumen:
# Este while se usa para validar que el usuario ingrese un dato correcto.
# Se repite hasta que la condición (numero < 0) sea falsa.

'''