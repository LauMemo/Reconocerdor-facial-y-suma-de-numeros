import Registrador as tk
import Rcara as rf
import contador as nts
R = 0
C = 0
r = 0

def reconocer():
    
    opciones = (input("Para comenzar con la ejecución del programa debe indicar una de las siguientes opciones: \n Presione R para registrar su rostro en el sistema. \n Presione C si ya esta registrado y continuar con el programa. \n --> "))

    if opciones == R or opciones == r:
        tk.create_Registro()
        rf.rum()
    else:
        suma = str(sum())
        sum_array = list (suma)

        image_recorgnized = tk.recorgnized()
        if image_recorgnized:
            print(f'El resultado es {suma}')
            nts.speech_number(sum_array)
def sum():
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))

    return num1 + num2
    if __name__ == '__inicio__':
        inicio()