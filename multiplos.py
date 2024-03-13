um1 : float
num2 : float
num1 = float(input("Por favor ingrese el primer numero: "))
num2 = float(input("Por favor ingrese el segundo numero: "))
multiplo : float
multiplo = num2%num1
if multiplo == 0:
    print("El primer numero ingresado " ,num1, " es multiplo del segundo numero ingresado " ,num2)
else:
    print("El primer numero ingresado " ,num1, " no es multiplo del segundo numero ingresado " ,num2)