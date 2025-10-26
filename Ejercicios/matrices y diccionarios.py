# MATRIZ MÁGICA
def matriz_magica():
    print("Verificador de Matriz Mágica")
    n = int(input("Ingrese el tamaño de la matriz (n x n): "))

    # Crear la matriz con valores ingresados por el usuario
    matriz = []
    for i in range(n):
        fila = list(map(int, input(f"Ingrese los {n} valores de la fila {i+1}, separados por espacio: ").split()))
        matriz.append(fila)

    # Mostrar la matriz
    print("\nMatriz ingresada:")
    for fila in matriz:
        print(fila)

    # Verificar si la matriz es mágica
    def es_matriz_magica(matriz):
        n = len(matriz)
        for fila in matriz:
            if len(fila) != n:
                return False

        suma_objetivo = sum(matriz[0])

        # Comprobar filas
        for fila in matriz:
            if sum(fila) != suma_objetivo:
                return False

        # Comprobar columnas
        for j in range(n):
            if sum(matriz[i][j] for i in range(n)) != suma_objetivo:
                return False

        # Diagonales
        diag1 = sum(matriz[i][i] for i in range(n))
        diag2 = sum(matriz[i][n - 1 - i] for i in range(n))

        if diag1 != suma_objetivo or diag2 != suma_objetivo:
            return False

        return True

    if es_matriz_magica(matriz):
        print("\n✅ La matriz es mágica")
    else:
        print("\n❌ La matriz NO es mágica")

# IMPRIMIR VALORES ASCENDENTES DE UN DICCIONARIO

def imprimir_valores_asc():
    print(" Ejercicio 2: Imprimir valores ascendentemente")
    dic = {"a": 3, "b": 1, "c": 2}
    print("Diccionario original:", dic)
    valores = list(dic.values())
    valores.sort()
    print("Valores en orden ascendente:", valores)

# VERIFICAR SI UN DICCIONARIO ESTÁ CONTENIDO EN OTRO

def verificar_diccionarios():
    print("Ejercicio 3: Verificar diccionarios")
    dic1 = {"a": 1, "b": 2}
    dic2 = {"a": 1, "b": 2, "c": 3}
    print("Diccionario 1:", dic1)
    print("Diccionario 2:", dic2)

    def contenido(dic1, dic2):
        for clave, valor in dic1.items():
            if clave not in dic2 or dic2[clave] != valor:
                return False
        return True

    if contenido(dic1, dic2):
        print("Todos los elementos de dic1 están en dic2")
    else:
        print("No todos los elementos de dic1 están en dic2")

# MEZCLAR DOS DICCIONARIOS

def mezclar_diccionarios():
    print("Ejercicio 4: Mezclar diccionarios")
    dic1 = {"a": 10, "b": 20}
    dic2 = {"b": 5, "c": 15}
    print("Diccionario 1:", dic1)
    print("Diccionario 2:", dic2)

    nuevo = dic2.copy()
    nuevo.update(dic1)
    print("Diccionario mezclado:", nuevo)


#  PERSONAS EN UN RANGO DE EDAD

def personas_en_rango():
    print("Ejercicio 5: Personas dentro de un rango de edad ===")
    personas = [
        {"nombres": "Pedro Julio", "apellidos": "Tristán Merchán", "edad": 101},
        {"nombres": "Ana María", "apellidos": "Pérez Gómez", "edad": 25},
        {"nombres": "Luis Fernando", "apellidos": "Torres Rojas", "edad": 42},
        {"nombres": "Camila", "apellidos": "Jiménez López", "edad": 18}
    ]

    edad_min = int(input("Ingrese edad mínima: "))
    edad_max = int(input("Ingrese edad máxima: "))

    print(f"Personas entre {edad_min} y {edad_max} años:")
    for p in personas:
        if edad_min <= p["edad"] <= edad_max:
            print(f"- {p['nombres']} {p['apellidos']}")

# Ejecucion del programa

if __name__ == "__main__":
    matriz_magica()
    imprimir_valores_asc()
    verificar_diccionarios()
    mezclar_diccionarios()
    personas_en_rango()
