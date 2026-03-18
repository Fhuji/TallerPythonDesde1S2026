
#  Guía de Componentes de Python

Referencia rápida de palabras clave, operadores, funciones y símbolos usados en Python Básico.

---

##  Variables y Tipos de Datos

| Componente | ¿Qué es? | ¿Para qué se usa? | Ejemplo |
|---|---|---|---|
| `=` | Operador de asignación | Guarda un valor dentro de una variable | `edad = 25` |
| `int` | Tipo de dato — número entero | Guardar números sin decimales: edades, puntajes, contadores | `vidas = 3` |
| `float` | Tipo de dato — número decimal | Guardar números con decimales: precios, temperaturas | `precio = 9.99` |
| `str` | Tipo de dato — texto (string) | Guardar cualquier texto entre comillas | `nombre = 'Ana'` |
| `bool` | Tipo de dato — booleano | Guardar solo dos valores posibles: `True` o `False` | `vivo = True` |
| `' '` | Comillas simples | Delimitan un texto (string) | `'Hola mundo'` |
| `" "` | Comillas dobles | Delimitan un texto igual que las simples | `"Hola mundo"` |

---

##  Operadores Aritméticos

| Operador | Nombre | ¿Para qué se usa? | Ejemplo | Resultado |
|---|---|---|---|---|
| `+` | Suma | Sumar dos números. También une (concatena) textos | `10 + 3` | `13` |
| `-` | Resta | Restar dos números | `10 - 3` | `7` |
| `*` | Multiplicación | Multiplicar dos números. También repite textos | `10 * 3` | `30` |
| `/` | División | Dividir dos números. Siempre devuelve decimal | `10 / 3` | `3.333...` |
| `//` | División entera | Divide y descarta los decimales, solo da el entero | `10 // 3` | `3` |
| `%` | Módulo / Residuo | Da el sobrante de una división. Útil para saber si es par o impar | `10 % 3` | `1` |
| `**` | Potencia | Eleva un número a una potencia | `2 ** 8` | `256` |

### Operadores de Asignación Compuesta

| Operador | ¿Qué hace? | Equivale a | Ejemplo |
|---|---|---|---|
| `+=` | Suma y guarda | `x = x + 1` | `x += 1` |
| `-=` | Resta y guarda | `x = x - 1` | `x -= 1` |
| `*=` | Multiplica y guarda | `x = x * 2` | `x *= 2` |
| `/=` | Divide y guarda | `x = x / 2` | `x /= 2` |

---

##  Operadores de Comparación

Siempre devuelven `True` o `False`.

| Operador | Nombre | ¿Para qué se usa? | Ejemplo | Resultado |
|---|---|---|---|---|
| `==` | Igual a | Compara si dos valores son iguales | `5 == 5` | `True` |
| `!=` | Diferente de | Compara si dos valores son distintos | `5 != 3` | `True` |
| `>` | Mayor que | Verifica si el izquierdo es mayor | `7 > 3` | `True` |
| `<` | Menor que | Verifica si el izquierdo es menor | `2 < 9` | `True` |
| `>=` | Mayor o igual que | Verifica si es mayor o exactamente igual | `5 >= 5` | `True` |
| `<=` | Menor o igual que | Verifica si es menor o exactamente igual | `3 <= 7` | `True` |

>  **No confundir:** `=` asigna un valor. `==` compara dos valores.

---

##  Operadores Lógicos

| Operador | En español | ¿Para qué se usa? | Ejemplo | Resultado |
|---|---|---|---|---|
| `and` | Y | Verdadero solo si **ambas** condiciones son verdaderas | `5 > 3 and 2 < 9` | `True` |
| `or` | O | Verdadero si **al menos una** condición es verdadera | `5 > 3 or 2 > 9` | `True` |
| `not` | No | Invierte el resultado de una condición | `not True` | `False` |

### Operadores de Pertenencia e Identidad

| Operador | En español | ¿Para qué se usa? | Ejemplo | Resultado |
|---|---|---|---|---|
| `in` | Contiene | Verifica si un elemento está dentro de algo | `'a' in 'Ana'` | `True` |
| `not in` | No contiene | Verifica si un elemento **no** está dentro de algo | `'z' not in 'Ana'` | `True` |
| `is` | Es el mismo objeto | Compara identidad de objeto, principalmente con `None` | `x is None` | `True` / `False` |

---

##  Palabras Clave de Control de Flujo

### Condicionales

| Palabra clave | En español | ¿Para qué se usa? | Ejemplo |
|---|---|---|---|
| `if` | Si | Ejecuta un bloque **si** la condición es verdadera | `if edad >= 18:` |
| `elif` | Si no, si | Segunda condición a evaluar si el `if` fue falso | `elif edad >= 13:` |
| `else` | Si no | Bloque que se ejecuta si ninguna condición anterior fue verdadera | `else:` |

```python
edad = 20

if edad >= 18:
    print('Mayor de edad')
elif edad >= 13:
    print('Adolescente')
else:
    print('Menor de edad')
```

### Bucles

| Palabra clave | En español | ¿Para qué se usa? | Ejemplo |
|---|---|---|---|
| `for` | Para | Repite un bloque un número **conocido** de veces o por cada elemento de una colección | `for i in range(5):` |
| `while` | Mientras | Repite un bloque **mientras** una condición sea verdadera | `while contador < 5:` |
| `break` | Romper | Sale del bucle **inmediatamente**, sin terminar las demás vueltas | `break` |
| `continue` | Continuar | Salta al inicio de la **siguiente vuelta** del bucle, omitiendo el resto | `continue` |

```python
# Ejemplo for
for i in range(1, 6):
    print('Número:', i)

# Ejemplo while
contador = 0
while contador < 5:
    print('Turno:', contador)
    contador += 1
```

---

##  Funciones

| Palabra clave | En español | ¿Para qué se usa? | Ejemplo |
|---|---|---|---|
| `def` | Definir | Define (crea) una función con nombre propio | `def saludar():` |
| `return` | Retornar / Devolver | Devuelve un valor desde la función al lugar donde fue llamada | `return a + b` |

```python
def sumar(a, b):
    return a + b

resultado = sumar(10, 5)
print(resultado)  # 15
```

---

##  Funciones Integradas de Python

Estas funciones ya vienen incluidas en Python, no hay que instalar nada.

| Función | ¿Qué hace? | ¿Para qué se usa? | Ejemplo |
|---|---|---|---|
| `print()` | Imprime en pantalla | Mostrar texto, números o variables al usuario | `print('Hola')` |
| `input()` | Lee lo que escribe el usuario | Recibir datos del usuario por teclado. **Siempre devuelve texto (str)** | `input('Tu nombre: ')` |
| `int()` | Convierte a entero | Convertir texto o decimal a número entero | `int('25')` → `25` |
| `float()` | Convierte a decimal | Convertir texto o entero a número decimal | `float('3.14')` → `3.14` |
| `str()` | Convierte a texto | Convertir un número u otro tipo a texto | `str(42)` → `'42'` |
| `type()` | Devuelve el tipo | Saber qué tipo de dato tiene una variable | `type(3.14)` → `<class 'float'>` |
| `range()` | Genera una secuencia | Crear una secuencia de números para usar en un `for` | `range(1, 6)` → `1,2,3,4,5` |
| `max()` | Devuelve el mayor | Encontrar el valor más grande entre dos o más valores | `max(3, 7)` → `7` |
| `min()` | Devuelve el menor | Encontrar el valor más pequeño entre dos o más valores | `min(3, 7)` → `3` |
| `len()` | Devuelve la longitud | Contar cuántos elementos tiene una cadena o lista | `len('Ana')` → `3` |
| `abs()` | Valor absoluto | Devuelve el valor positivo de un número | `abs(-5)` → `5` |

### Uso de `range()`

| Forma | Genera | Explicación |
|---|---|---|
| `range(5)` | `0, 1, 2, 3, 4` | Del 0 al 4 (5 números) |
| `range(1, 6)` | `1, 2, 3, 4, 5` | Del 1 al 5 |
| `range(0, 10, 2)` | `0, 2, 4, 6, 8` | Del 0 al 8 saltando de 2 en 2 |

---

## 🔣 Símbolos de Estructura

| Símbolo | Nombre | ¿Para qué se usa? | Ejemplo |
|---|---|---|---|
| `:` | Dos puntos | Obligatorio al final de `if`, `elif`, `else`, `for`, `while`, `def` | `if x > 0:` |
| `#` | Comentario | Todo lo que va después es ignorado por Python. Son notas para humanos | `# esto es una nota` |
| `( )` | Paréntesis | Llamar funciones y agrupar expresiones | `print('hola')` |
| `[ ]` | Corchetes | Definir listas y acceder a elementos por posición | `lista[0]` |
| `{ }` | Llaves | Definir diccionarios (pares clave-valor) | `{'nombre': 'Ana'}` |
| `\n` | Salto de línea | Dentro de un texto, genera un salto de línea al imprimir | `print('a\nb')` |
| `_` | Guión bajo | Separar palabras en nombres de variables. También variable desechable | `nombre_completo` |

---

## Colecciones

### Lista (`list`)

Una colección **ordenada** de elementos. Se escribe entre corchetes `[ ]`. Puede contener cualquier tipo de dato y se puede modificar.

```python
frutas = ['manzana', 'pera', 'uva']
numeros = [1, 2, 3, 4, 5]
mixta = ['Ana', 25, True, 9.99]

# Acceder a un elemento por su posición (empieza en 0)
print(frutas[0])   # manzana
print(frutas[1])   # pera

# Agregar un elemento
frutas.append('naranja')

# Longitud de la lista
print(len(frutas))  # 4
```

> La posición de los elementos empieza en **0**, no en 1. Al primer elemento le corresponde el índice 0, al segundo el índice 1, y así sucesivamente.

### Diccionario (`dict`)

Una colección de pares **clave-valor**. Se escribe entre llaves `{ }`. Cada elemento tiene un nombre (clave) y un dato (valor).

```python
persona = {
    'nombre': 'Ana',
    'edad': 22,
    'ciudad': 'Guatemala'
}

# Acceder por clave
print(persona['nombre'])  # Ana
print(persona['edad'])    # 22
```

---

##  Variables de Control Comunes

| Variable | ¿Para qué se usa típicamente? | Ejemplo |
|---|---|---|
| `i` | Contador en bucles `for`. Viene de *index* (índice) | `for i in range(10):` |
| `a`, `b` | Parámetros genéricos en funciones matemáticas | `def sumar(a, b): return a + b` |
| `n` | Variable numérica genérica | `def es_par(n): return n % 2 == 0` |
| `x` | Variable genérica en matemáticas y pruebas | `x = int(input('Número: '))` |

> Estos son solo nombres de convención. Puedes usar cualquier nombre válido. Lo importante es que sea descriptivo del dato que guarda.

---

##  Tabla de Verdad — Operadores Lógicos

| `a` | `b` | `a and b` | `a or b` | `not a` |
|---|---|---|---|---|
| `True` | `True` | `True` | `True` | `False` |
| `True` | `False` | `False` | `True` | `False` |
| `False` | `True` | `False` | `True` | `True` |
| `False` | `False` | `False` | `False` | `True` |

---

##  Errores Comunes

| Error | Causa | Solución |
|---|---|---|
| `= ` en lugar de `==` | Usar asignación donde se quería comparar | Usar `==` para comparar |
| Olvidar `:` | Falta los dos puntos al final del `if`, `for`, `def`, etc. | Agregar `:` al final |
| Falta de indentación | El bloque no tiene 4 espacios de sangría | Indentar con 4 espacios |
| Sumar `str` con `int` | `input()` devuelve texto, no número | Convertir con `int()` o `float()` |
| `True` / `False` en minúscula | Python no reconoce `true` ni `false` | Escribir con mayúscula inicial |
| Decimal con coma | Python usa punto para decimales, no coma | Usar `.` en vez de `,` |

---

*Documentación oficial en español: [docs.python.org/es](https://docs.python.org/es)*