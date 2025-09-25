#Encuesta sobre ideas de proyectos
print("Hola, a continuacion se realizara una breve encuesta para conocer su idea de proyecto para el curso de programacion de computadores")
while True:
    nombre = input("Ingresa tu nombre: ")
    idea = input("Ingrese la idea o ideas que tiene para realizar el proyecto del curso: ")
    print(f"Nombre: {nombre}")
    print(f"Idea de Proyecto: {idea}")
    continuar = input("Quiere ingresar otra respuesta? responda con un (si o no): ").lower()
    if continuar != "si":
        print("Gracias por responder la encuesta")
        break