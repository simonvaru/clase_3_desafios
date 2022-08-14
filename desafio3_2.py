numero = int(input("Ingrese un numero impar por teclado: "))

while numero%2 == 0:
    print("Numero par. Vuelva a ingresar un numero por teclado")
    numero = int(input("Ingrese un numero impar por teclado: "))
    
print("Numero ingresado es impar. Se finalisa el programa..")