from models.modulos import *
try:
    print ("Sisteama Calculadora ")
    print ("1. Suma")
    print ("2. Resta")
    print ("3. Multiplicacion")
    print ("4. Division")
    opc = input("Ingrese la opcion de lo que quiere realizar: ")

    n1 = int(input ("Ingrese el primer valor para la operacion: "))
    n2 = int(input ("Ingrese el segundo valor para la operacion: "))
    match opc:
        case "1":
            suma (n1,n2)
        case "2":
            resta (n1,n2)
        case "3":
            multiplicacion (n1,n2)
        case "4":
            division (n1,n2)
        case _:
            print ("Opcion no valida")        
except TypeError: 
    print ("No es valida la opcion")
        
