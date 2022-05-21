"""
Programar una calculadora, la cual pida por consola las operaciones a realizar
además, consultar al usuario, si desea continuar o si no. 
La calculadora solo puede realizar una operación con 2 variables.
"""

#Ejemplo 1 (if, else y while)
print("Bienvenido 👋 a la calculadora 📝 en Python 🐍")
while True:
    #Mostramos las posibles operaciones
    print("Estas operaciones usted podrá realizar")
    print("Suma : + ")
    print("Resta : - ")
    print("Dividir : / ")
    print("Multiplicación : * ")
    print("Escriba el símbolo de la operación 👇🏻 ")
    #Pedimos la operación
    operacion = input("Ingrese la operación a realizar => ")
    #Llamaremos a los numeros "numero_A" y "numero_B"
    numero_A = int(input("Ingrese el primer numero => "))
    numero_B = int(input("Ingrese el segundo numero => "))
    #Inicializamos la variable "total" en cero
    #"Total" almacenará el valor de la operación
    total = 0
    if operacion == "+":
        #Operación Suma
        total = numero_A + numero_B
        print(f"El resultado de la suma es => {total}")
    elif operacion == "-":
        #Operación Resta
        total = numero_A - numero_B
        print(f"El resultado de la resta es => {total}")
    elif operacion == "/":
        #Operación División
        #OJO 👀, En matemáticas al igual que en Python, no se puede dividir entre 0
        #Por ello pondremos un condicional para validar el segundo numero
        if numero_B != 0:
            total = numero_A / numero_B
            print(f"El resultado de la división es {total}")
            continue
        #continue es una palabra reservada de Python, la cual, permite saltar la operación que sigue.
        print("No se puede dividir entre 0 😢")
    elif operacion == "*":
        total = numero_A * numero_B
        print(f"El resultado de la multiplicación es {total}")
    else:
        #Validamos si coloca un símbolo invalido o una operación que no podemos realizar
        print("No podemos realizar esa operación 😢 ")
    #Preguntamos al usuario si desea continuar
    condicion = input("¿ Desea continuar con otra operación 🤓 ? (S para continuar) ")
    if condicion != "S":
        break

#Ejemplo 2 (diccionarios):

#En este caso es una forma más reducida de realizar la calculadora.
#Es un poco más complicado, pero nada que no se pueda entender.
#A diferencia del anterior, declararemos una variable, la cual definira si el usuario continua con otra operación o no
continua = True
while continua:
    #Primero, al igual que el anterior pedimos la operación.
    operacion = input("Ingrese la operación a realizar => ")
    #Pedimos los números
    numero_A = int(input("Ingrese el primer numero => "))
    numero_B = int(input("Ingrese el segundo numero => "))

    #Declaramos un diccionario
    #Un diccionario se caracteriza porque contiene un:
    # Key : Valor
    operaciones = {
        "+":numero_A+numero_B,
        "-":numero_A-numero_B,
        "*":numero_A*numero_B,
        "/":numero_A/numero_B
    }
    #Primero validamos si la operación ingresada está las "Keys"
    #El método operaciones.keys() devuelve una lista
    if operacion not in operaciones.keys():
        print("No podemos realizar esa operación 😥 ")
    elif operacion == "/" and numero_B == 0:
        #Validamos si el segundo numero es igual 0
        #Pues como sabemos no se puede dividir entre 0
        print("No se puede dividir entre 0 😥")
    else: 
        #El método operaciones.get() devuelve el valor de la lista con la "Key" indicada
        total = operaciones.get(operacion)
        print(f"El resultado de la operación es => {total} ")
    
    condicion = input("¿ Desea continuar con otra operación 🤓 ? (S para continuar) ")
    if condicion != "S":
        continua = False
