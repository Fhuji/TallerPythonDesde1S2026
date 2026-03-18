

# Ejemplo de operadores de comparación y lógicos


# ==  igual a 
# !=  diferente de 
# >   mayor que 
# <   menor que 
# >=  mayor o igual 
# <=  menor o igual 
  
# Operadores lógicos 
# and  (ambas condiciones verdaderas) 
# or   (al menos una verdadera) 
# not  (niega la condición) 



nota = 85          # Guarda la nota
asistencia = True  # Guarda si asistió (True = sí)

# and: ambas condiciones deben ser verdaderas
if nota >= 60 and asistencia:   # Si nota >= 60 Y asistencia es True
    print('Aprobado')
else:
    print('No aprobado')

# Resumen:
# Los operadores de comparación (>=, <=, ==, etc.) devuelven True o False.
# Los operadores lógicos (and, or, not) combinan condiciones.
# En este caso, se necesita cumplir ambas para aprobar.