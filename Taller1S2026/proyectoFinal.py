# Proyecto final: Calculadora con menú y funciones para cada operación

# Función para sumar
def sumar(a, b):
    return a + b

# Función para restar
def restar(a, b):
    return a - b

# Función para multiplicar
def multiplicar(a, b):
    return a * b

# Función para dividir (con control de división entre cero)
def dividir(a, b):
    if b == 0:
        return 'Error: No se puede dividir entre cero'
    return a / b

# Programa principal
print('============================')
print('   CALCULADORA EN PYTHON')
print('============================')

# Bucle infinito (while True) para repetir hasta que el usuario salga
while True:
    print()
    print('Operaciones disponibles:')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicación')
    print('4. División')
    print('5. Salir')

    # Pedimos la opción al usuario
    opcion = input('Elige una opción (1-5): ')

    # Si elige salir
    if opcion == '5':
        print('¡Hasta luego!')
        break          # Sale del bucle while y termina el programa

    # Verificar si la opción es válida (1,2,3 o 4)
    if opcion not in ['1', '2', '3', '4']:
        print('Opción no válida')
        continue       # Vuelve al inicio del bucle (pide otra opción)

    # Si llegamos aquí, la opción es válida, pedimos los números
    a = float(input('Primer número: '))    # Convertimos a float para permitir decimales
    b = float(input('Segundo número: '))

    # Según la opción, llamamos a la función correspondiente
    if opcion == '1':
        print('Resultado:', sumar(a, b))
    elif opcion == '2':
        print('Resultado:', restar(a, b))
    elif opcion == '3':
        print('Resultado:', multiplicar(a, b))
    elif opcion == '4':
        print('Resultado:', dividir(a, b))

# Resumen:
# Esta calculadora muestra un menú y permite al usuario elegir una operación.
# Cada operación está implementada en una función separada. Usa un bucle while
# para seguir mostrando el menú hasta que el usuario elija salir (opción 5).
# Incluye validación de opción y manejo de división entre cero.