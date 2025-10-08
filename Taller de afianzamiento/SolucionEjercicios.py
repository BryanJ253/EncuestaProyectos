def cuadrado_numero():
    """Imprime el cuadrado de los números ingresados hasta que se ingrese un negativo."""
    print("Ejercicio 1: Cuadrado de números")
    while True:
        numero = float(input("Ingresa un número: "))
        if numero < 0:
            print("Programa finalizado.\n")
            break
        print(f"El cuadrado de {numero} es {numero ** 2}")
        print("Si desea salir del programa ingrese un numero negativo")


def secuencia_numero():
    """Aplica n/2 si es par o 3n + 1 si es impar hasta llegar a 1."""
    print("Ejercicio 2: ")
    n = int(input("Ingresa un número entero positivo: "))
    if n <= 0:
        print("El número debe ser positivo.\n")
        return
    
    print("Secuencia:", end=" ")
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n, end=" ")
    print("\n")


def crecimiento_poblacional():
    """Calcula el año en que la población del país B supera a la de A."""
    print("Problema 3: Crecimiento poblacional")
    poblacion_a = 25000000
    poblacion_b = 18900000
    tasa_a = 0.02
    tasa_b = 0.03
    anio = 2022
    print(f"A: {poblacion_a}  B: {poblacion_b}")
    while poblacion_b <= poblacion_a:
        poblacion_a *= (1 + tasa_a)
        poblacion_b *= (1 + tasa_b)
        anio += 1

    print(f"La población del país B superará a la de A en el año {anio}.\n")


def epsilon_maquina():
    """Calcula el epsilon de máquina: el número más pequeño que sumado a 1 produce un valor diferente de 1."""
    print("=== Problema 4: Cálculo del épsilon de máquina ===")
    epsilon = 1.0
    while 1.0 + epsilon != 1.0:
        epsilon /= 2
    epsilon *= 2  # se corrige al último valor que funcionó
    print(f"El épsilon de la máquina es aproximadamente: {epsilon}\n")



def listado_cuadrados():
    print("Problema 5: Cuadrados del 1 al 100 ")
    for i in range(1, 101):
        print(f"{i}^2 = {i**2}")
    print()


def impares_y_pares():
    print("Problema 6: Impares y Pares")
    print("Impares del 1 al 999:")
    for i in range(1, 1000, 2):
        print(i, end=" ")
    print("\n\nPares del 2 al 1000:")
    for i in range(2, 1001, 2):
        print(i, end=" ")
    print("\n")


def pares_descendentes():
    print("Problema 7: Pares descendentes hasta 2")
    n = int(input("Ingresa un número natural n ≥ 2: "))
    if n < 2:
        print("El número debe ser mayor o igual que 2.\n")
        return
    print("Pares descendentes:")
    for i in range(n if n % 2 == 0 else n - 1, 1, -2):
        print(i, end=" ")
    print("\n")


def factoriales_hasta_n():
      print("Problema 8: Factoriales de 1 hasta n")
      n = int(input("Ingresa un número natural: "))

      def factorial(k):
        resultado = 1
        for i in range(2, k + 1):
            resultado *= i
        return resultado

      for i in range(1, n + 1):
        print(f"{i}! = {factorial(i)}")
      print()

      

def potencia_de_dos():
    print("Problema 9: 2 elevado a la potencia n")
    n = int(input("Ingresa el valor de n: "))
    print(f"2^{n} = {2 ** n}\n")


def potencia_x_n():
    print("Problema 10: x elevado a la potencia n")
    n = int(input("Ingresa un número natural n: "))
    x = float(input("Ingresa un número real x: "))
    print(f"{x}^{n} = {x ** n}\n")


def tablas_multiplicar():
    print("Problema 11: Tablas de multiplicar del 1 al 9 ")
    for i in range(1, 10):
        print(f"\nTabla del {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
    print()


def exp_maclaurin():
    print("Problema 12: Aproximación de exp(x)")
    x = float(input("Ingresa el valor de x: "))
    n = int(input("Ingresa el número de términos n: "))

    # Función factorial
    def factorial(k):
        resultado = 1
        for i in range(2, k + 1):
            resultado *= i
        return resultado

    resultado = 0
    for i in range(n + 1):
        termino = (x ** i) / factorial(i)
        resultado += termino

    print(f"exp({x}) ≈ {resultado}\n")


def sin_maclaurin():
     print("Problema 13: Aproximación de sin(x)")
     x = float(input("Ingresa el valor de x (en radianes): "))
     n = int(input("Ingresa el número de términos n: "))

     def factorial(k):
        resultado = 1
        for i in range(2, k + 1):
            resultado *= i
        return resultado

     resultado = 0
     for i in range(n + 1):
        termino = ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
        resultado += termino

     print(f"sin({x}) ≈ {resultado}\n")
    
# Ejecución de los problemas
if __name__ == "__main__":
    cuadrado_numero()
    secuencia_numero()
    crecimiento_poblacional()
    epsilon_maquina()
    listado_cuadrados()
    impares_y_pares()
    pares_descendentes()
    factoriales_hasta_n()
    potencia_de_dos()
    potencia_x_n()
    tablas_multiplicar()
    exp_maclaurin()
    sin_maclaurin()
    
