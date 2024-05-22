go = True
while(go):
    try:
        a = int(input("Ingrese un número: "))
        b = int(input("Ingrese otro número: "))
    except ValueError:
        print("Debe ingresar un numero.")
        a = int(input("Ingrese un número: "))
        b = int(input("Ingrese otro número: "))
    try:
        op = int(input("Escoga la operacion que desea realizar:\n1)Suma\n2)Resta\n3)Multiplicacion\n4)Division\n5)Resto:\n"))
        while op < 0 or op > 5:
            op = int(input("Opcion invalida. Escoga la operacion que desea realizar:\n1)Suma\n2)Resta\n3)Multiplicacion\n4)Division\n5)Resto:\n"))            
        if op == 1:
            print("Resultado: ",a+b)
        elif op == 2:
            print("Resultado: ",a-b)
        elif op == 3:
            print("Resultado: ",a*b)
        elif op == 4:
            print("Resultado: ",a/b)
        elif op == 5:
            print("Resultado: ",a%b)
    except ValueError:
        print("Favor ingresar una de las opciones indicadas.")
        op = int(input("Escoga la operacion que desea realizar:\n1)Suma\n2)Resta\n3)Multiplicacion\n4)Division\n5)Resto:\n"))       
    cont = input("Desea realizar otra operacion:\nY)Si\nN)No\n")   
    while cont.upper().strip() != "Y" and cont.upper().strip() != "N":
        print("Opcion invalida. Escoja una de las opciones validas.")
        cont = input("Desea realizar otra operacion:\nY)Si\nN)No\n")       
    if cont.upper().strip() == "N":
        print("Fin. Gracias por usar nuestra calculadora.")
        go = False


        """
while op == ValueError:
        op = int(input("Escoga la operacion que desea realizar:\n1)Suma\n2)Resta\n3)Multiplicacion\n4)Division\n5)Resto:\n"))
while not (1 or 2 or 3 or 4 or 5):
            print("Favor ingresar una de las opciones indicadas.")
            op = int(input("Escoga la operacion que desea realizar:\n1)Suma\n2)Resta\n3)Multiplicacion\n4)Division\n5)Resto:\n"))

"""
