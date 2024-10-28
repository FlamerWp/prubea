

print ("Calculadora ")
print ("1. Suma")
print ("2. Resta")
print ("3. Multiplicacion")
print ("4. Division")
opc = input("Ingrese la opcion de lo que quiere realizar: ")

match opc:
    case "1":
        print ("Suma")
    case "2":
        print ("Resta")
    case "3":
        print ("Multiplicacion")
    case "4":
        print ("Division")
    case _:
        print ("Opcion no valida")        
        
def suma(n1, n2):
    return n1 + n2

def resta(n1, n2):
    return n1 - n2

        