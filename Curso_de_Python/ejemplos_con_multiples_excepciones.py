def dividir():
    while True:
        try:
            num1 = float(input("Digite un numero: "))
            num2 = float(input("Digite un numero: "))
            resultado = num1/num2
            print(f"El resultado de la division es: {resultado:.2f}")
        
        except ValueError: #Poniendo el tipo de excepcion, la haces especifica.
            print("Error -> Digite correctamente los valores numericos")

        except ZeroDivisionError: #Se pueden poner varias excepciones especificas, pero no repetir.
            print("Error -> No se puede dividir entre 0")

        else:
            break

dividir()