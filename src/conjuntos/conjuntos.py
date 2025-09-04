'''
#Elementos unicos

Elementos unicos o sets en conjuntos
En los conjuntos, los elementos son unicos, es decir, no pueden repetirse.

#Creacion de conjuntos

#Forma 1: usando llaves {}
colores = {"rojo", "verde", "azul", "rojo"}
print(colores)  # {'verde', 'azul', 'rojo'}

#Forma 2: usando la funcion set()
numeros = set([1, 2, 3, 2, 1])
print(numeros)  # {1, 2, 3}

#Caracterizticas de los elementos unicos
#1. No se permiten elementos duplicados: En los conjuntos los elementos duplicados se eliminan automaticamente.
usuarios = set(["ana", "carlos", "ana", "elena", "carlos"])
print(usuarios)  # {'ana', 'elena', 'carlos'}

#2. Verifican la pertenencia: Puedes verificar si un elemento pertenece a un conjunto usando el operador 'in'.
frutas = {"manzana", "naranja", "plátano"}
print("manzana" in frutas)  # True
print("uva" in frutas)      # False

#Inmutabilidad de los elementos: Los elementos de un conjunto deben ser inmutables, como tuplas, cadenas o numeros.
# Esto funciona (todos los elementos son inmutables)
conjunto_valido = {1, "hola", (1, 2)}

# Esto produce un error (las listas son mutables)
# conjunto_invalido = {1, [2, 3]}  # TypeError: unhashable type: 'list'

#Casos de usos practicos
#1. Eliminar duplicados de una lista
# Eliminar duplicados de una lista manteniendo el orden original
def eliminar_duplicados(secuencia):
    return list(dict.fromkeys(secuencia))

lista_con_duplicados = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(eliminar_duplicados(lista_con_duplicados))  # [3, 1, 4, 5, 9, 2, 6]

#2. Encontrar elementos unicos entre colecciones
grupo_a = {"Ana", "Carlos", "Elena", "David"}
grupo_b = {"Elena", "Fernando", "Gabriela", "Carlos"}

# Personas que están solo en el grupo A
solo_en_a = grupo_a - grupo_b
print(solo_en_a)  # {'Ana', 'David'}

#3. Verificar si todos los elementos son unicos
def todos_unicos(items):
    return len(items) == len(set(items))

print(todos_unicos([1, 2, 3, 4]))     # True
print(todos_unicos([1, 2, 3, 1, 4]))  # False

#Restricciones de los conjuntos
#1. No mantienen orden: Los conjuntos no mantienen el orden de los elementos.
numeros = {3, 1, 4, 1, 5, 9}
print(numeros)  # El orden puede variar: {1, 3, 4, 5, 9}

#2. No pwemirwn indexacion: No puedes acceder a los elementos de un conjunto mediante un indice.
colores = {"rojo", "verde", "azul"}
# Esto produce un error
# print(colores[0])  # TypeError: 'set' object is not subscriptable

#3. Solo elementos inmutables: Los elementos de un conjunto deben ser inmutables.

# Conjuntos vacíos
# Esto NO crea un conjunto vacío, sino un diccionario vacío
no_es_conjunto = {}
print(type(no_es_conjunto))  # <class 'dict'>

# Forma correcta de crear un conjunto vacío
conjunto_vacio = set()
print(type(conjunto_vacio))  # <class 'set'>

# Operaciones basicas con conjuntos
# Añadir elementos:
# Add() - Añade un solo elemento al conjunto.
tecnologias = {"Python", "JavaScript", "SQL"}
tecnologias.add("Java")
print(tecnologias)  # {'Python', 'JavaScript', 'SQL', 'Java'}

# Update() - Añade múltiples elementos al conjunto.
lenguajes = {"Python", "Java"}
nuevos_lenguajes = ["Go", "Rust", "TypeScript"]
lenguajes.update(nuevos_lenguajes)
print(lenguajes)  # {'Python', 'Java', 'Go', 'Rust', 'TypeScript'}

numeros = {1, 2, 3}
numeros.add(2)  # Intentamos añadir un elemento que ya existe
print(numeros)  # {1, 2, 3} - No hay cambios

# Eliminar elementos:
# Remove() - Elimina un elemento del conjunto. Lanza un error si el elemento no existe.
frutas = {"manzana", "naranja", "plátano"}
frutas.remove("naranja")
print(frutas)  # {'manzana', 'plátano'}

# Si intentamos eliminar un elemento que no existe:
# frutas.remove("uva")  # KeyError: 'uva'

# Discard() - Elimina un elemento del conjunto. No lanza error si el elemento no existe.
animales = {"perro", "gato", "conejo"}
animales.discard("pájaro")  # No existe, pero no genera error
print(animales)  # {'perro', 'gato', 'conejo'}

# Pop() - Elimina y devuelve un elemento aleatorio del conjunto.
colores = {"rojo", "verde", "azul"}
color_eliminado = colores.pop()
print(f"Se eliminó: {color_eliminado}")
print(f"Conjunto resultante: {colores}")

# Clear() - Elimina todos los elementos del conjunto.
numeros = {1, 2, 3, 4, 5}
numeros.clear()
print(numeros)  # set()

#Consultas basicas
len() - Devuelve el número de elementos en el conjunto.
planetas = {"Mercurio", "Venus", "Tierra", "Marte"}
print(len(planetas))  # 4

# in - Verifica si un elemento pertenece al conjunto.
dias = {"lunes", "martes", "miércoles", "jueves", "viernes"}
print("sábado" in dias)  # False
print("lunes" in dias)   # True

# copy() - Devuelve una copia superficial del conjunto.
original = {1, 2, 3}
copia = original.copy()
copia.add(4)
print(original)  # {1, 2, 3} - No se modifica
print(copia)     # {1, 2, 3, 4}

# Iteracion sobre conjuntos
# Puedes iterar sobre los elementos de un conjunto usando un bucle for.
ciudades = {"Madrid", "Barcelona", "Valencia", "Sevilla"}
for ciudad in ciudades:
    print(f"Visitando {ciudad}")

# Conversion entre tipos de datos
# Convertir una lista a un conjunto para eliminar duplicados
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5]
conjunto_sin_duplicados = set(lista_con_duplicados)
print(conjunto_sin_duplicados)  # {1, 2, 3, 4, 5}

# Convertir un conjunto a una lista
conjunto = {"a", "b", "c", "d"}
lista = list(conjunto)
print(lista)  # ['a', 'b', 'c', 'd'] (el orden puede variar)

# Comprobacion de subconjuntos y superconjuntos
# issubset() - Verifica si un conjunto es subconjunto de otro.
numeros_pares = {2, 4, 6, 8}
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros_pares.issubset(numeros))  # True

# issuperset() - Verifica si un conjunto es superconjunto de otro.
frutas = {"manzana", "naranja", "plátano", "fresa", "kiwi"}
frutas_tropicales = {"plátano", "kiwi"}
print(frutas.issuperset(frutas_tropicales))  # True

Ejemplo practico
# Registro inicial de asistentes
asistentes_dia1 = {"Ana", "Carlos", "Elena", "David", "Beatriz"}
asistentes_dia2 = {"Carlos", "Elena", "Fernando", "Gabriela"}

# Añadir nuevos asistentes al día 1
asistentes_dia1.add("Héctor")
print(f"Asistentes día 1: {asistentes_dia1}")

# Personas que asistieron ambos días
asistentes_ambos_dias = asistentes_dia1.intersection(asistentes_dia2)
print(f"Asistieron ambos días: {asistentes_ambos_dias}")

# Eliminar a alguien que canceló su asistencia
asistentes_dia1.discard("David")
print(f"Asistentes día 1 actualizado: {asistentes_dia1}")

# Comprobar si todos los del día 2 asistieron también el día 1
todos_repiten = asistentes_dia2.issubset(asistentes_dia1)
print(f"¿Todos los del día 2 asistieron el día 1?: {todos_repiten}")

# Total de asistentes únicos en ambos días
total_asistentes = len(asistentes_dia1.union(asistentes_dia2))
print(f"Total de asistentes únicos: {total_asistentes}")

# Metodos set
# Metodos para operaciones de conjuntos
# Intersection() - Devuelve un nuevo conjunto con los elementos comunes a ambos conjuntos.
grupo_a = {"Ana", "Carlos", "Elena", "David"}
grupo_b = {"Carlos", "Elena", "Fernando"}
comunes = grupo_a.intersection(grupo_b)
print(comunes)  # {'Carlos', 'Elena'}

# Union() - Devuelve un nuevo conjunto con todos los elementos de ambos conjuntos, sin duplicados.
equipo1 = {"Juan", "María", "Pedro"}
equipo2 = {"Ana", "Pedro", "Luis"}
todos = equipo1.union(equipo2)
print(todos)  # {'Juan', 'María', 'Pedro', 'Ana', 'Luis'}

# Difference() - Devuelve un nuevo conjunto con los elementos que están en el primer conjunto pero no en el segundo.
inventario = {"laptop", "teléfono", "tablet", "auriculares"}
vendidos = {"laptop", "auriculares"}
disponibles = inventario.difference(vendidos)
print(disponibles)  # {'teléfono', 'tablet'}

# Symmetric_difference() - Devuelve un nuevo conjunto con los elementos que están en uno u otro conjunto, pero no en ambos.
ciencias = {"física", "química", "biología", "matemáticas"}
artes = {"literatura", "música", "pintura", "matemáticas"}
exclusivos = ciencias.symmetric_difference(artes)
print(exclusivos)  # {'física', 'química', 'biología', 'literatura', 'música', 'pintura'}

# Metodos que modifican el conjunto original
# intersection_update() - Actualiza el conjunto original para que contenga solo los elementos comunes a ambos conjuntos.
usuarios_activos = {"user1", "user2", "user3", "user4"}
usuarios_premium = {"user2", "user4", "user5"}
# Actualiza usuarios_activos para contener solo usuarios activos que también son premium
usuarios_activos.intersection_update(usuarios_premium)
print(usuarios_activos)  # {'user2', 'user4'}

# update() - Actualiza el conjunto original añadiendo elementos de otro conjunto.
frutas_locales = {"manzana", "pera", "naranja"}
frutas_importadas = {"piña", "mango", "kiwi"}
# Añade todas las frutas importadas a las locales
frutas_locales.update(frutas_importadas)
print(frutas_locales)  # {'manzana', 'pera', 'naranja', 'piña', 'mango', 'kiwi'}


'''