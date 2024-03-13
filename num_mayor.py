num1 : float
num2 : float
num3 : float
num1 = float(input("Por favor ingrese el primer numero: "))
num2 = float(input("Por favor ingrese el segundo numero: "))
num3 = float(input("Por favor ingrese el tercer numero: "))
if num1 > num2 and num1 > num3:
    print(num1, ", siendo el primer numero ingresado, es el mayor entre los demas")
elif num2 > num1 and num2 > num3:
    print(num2, ", siendo el segundo numero ingresado, es el mayor entre los demas")
elif num3 > num1 and num3 > num2:
    print(num3, ", siendo el tercer numero ingresado, es el mayor entre los demas")
else:
    print("Hay 2 o mas numeros mayores o iguales que el resto")