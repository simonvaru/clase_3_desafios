list_1 = ["h", 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o']#longitud 10 elementos, lista a comparar
list_2 = ["h", 'o', 'l', 'a', ' ', 'l', 'u', 'n', 'a'] #longitud 9 elementos
list_3 = []#lista resultado
n_1 = 0#indice para list_1
n_3 = 0#indice para list_3

x = list_1[n_1]
n_2 = 0#indice para list_2
for n_1 in range(10):#bucle for para list_1
    x = list_1[n_1]
    n_2 = 0
    for n_2 in range(8):#bucle for para list_2
        y = list_2[n_2]
        if (x == y): #verifico 1er elemento de lista_1 en TODOS los elementos de lista_2
            list_3.append(x)
            n_3 += 1
            n_2 = 0
            n_1 += 1
            break
    
        else:
            n_2 += 1
            if n_2 == 8:
                n_2 = 0
                n_1 += 1   
        
            else:
                pass
else:
    print(f"Lista a comparar: {list_1}")#imprimo las 3 listas  
    print(f"Lista con valores tentativos: {list_2}") 
    print(f"Lista resultado: {list_3}")    
    
    
    

        
        
            