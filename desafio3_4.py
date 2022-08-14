n = 0
valor_3 = 0
media = 0
print("¿Cuantos numeros desea introducir: ?", end=" ")
valor_1 = int(input())

while n != valor_1:
    n = n + 1
    valor_2 =int(input())
    valor_3 = valor_3 + valor_2
    
media = valor_3 / n
print(f"La media aritmerica es: {media}")
    