from textwrap import dedent

valor3 = 0
r = 0


while valor3 != 4: 
    valor1 = int(input("Ingrese primer numero: "))
    valor2 = int(input("Ingrese segundo numero: "))
    print(dedent("""
      *Ingrese 1 si desea sumar los dos valores.
      *Ingrese 2 si desea restar al 1er valor el 2do numero.
      *Ingrese 3 si desea multiplicar el 1er valor por 2do numero.
      *Ingrese 4 si desea interrumpir este programa.
      """))
    valor3 = int(input("Ingrese respuesta: "))
    
    if valor3 == 1:
        r = valor1 + valor2
        print("Se eligió la opción ", valor3, " y el resultado es: ", r)
        
    elif valor3 == 2:
        r = valor1 - valor2
        print("Se eligió la opción ", valor3, " y el resultado es: ", r)
        
    elif valor3 == 3:
        r = valor1 * valor2
        print("Se eligió la opción ", valor3, " y el resultado es: ", r)
        
    elif valor3 == 4:
        print("Se finaliza el programa.")

    else:
        print("Valor incorrecto.")        
        
 
