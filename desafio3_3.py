suma = 0
print("Numeros impares: ")

for numero  in range(1,101,2):
    print(numero, end=" ")
    suma += numero
else:
    print("\nLa sumatoria de numeros impares entre 1 y 100 es: ", suma)