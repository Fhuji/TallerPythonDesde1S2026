# Variables y Tipos de Datos en Python
# Una variable es como una caja donde guardamos información. En Python no necesitamos 
# declarar el tipo de dato: Python lo detecta automáticamente. 




# Ejemplo de variables y tipos de datos en Python

# Las variables son como cajas donde guardamos información.
# En Python no se necesita declarar el tipo, se asigna directamente.

# --- Enteros (int) ---
edad = 25          # 'edad' guarda el número entero 25
año = 2024         # 'año' guarda el número entero 2024

# --- Decimales (float) ---
precio = 19.99     # 'precio' guarda el número decimal 19.99
pi = 3.14159       # 'pi' guarda el número decimal 3.14159

# --- Texto (str) ---
# Las comillas simples o dobles indican que es texto (cadena de caracteres)
nombre = 'Ana'             # 'nombre' guarda el texto "Ana"
ciudad = "Guatemala"       # 'ciudad' guarda el texto "Guatemala"

# --- Booleanos (bool) ---
# Solo pueden ser True (verdadero) o False (falso)
es_estudiante = True       # 'es_estudiante' guarda el valor verdadero
aprobado = False           # 'aprobado' guarda el valor falso

# --- Ver el tipo de una variable ---
# type() nos dice qué tipo de dato tiene la variable
print(type(edad))          # Muestra: <class 'int'> (es un entero)
print(type(nombre))        # Muestra: <class 'str'> (es texto)

# Resumen:
# Este código muestra cómo crear variables con diferentes tipos de datos
# (números enteros, decimales, texto y booleanos) y cómo verificar su tipo
# con type(). Las variables guardan información que podemos usar después.