lista = [1, 3, 6, 9]

while True:
    valor_1 = int(input("Ingrese un numero del 0 al 9: "))
    if 0 <= valor_1 < 10:
        for valor in lista: 
            if valor == valor_1:
                print(f"El valor {valor_1} esta en la lista.")
                break
            else:
                continue
                
    else:
        print("Valor incorrecto.")
        
        