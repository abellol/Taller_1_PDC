letra : str
letra = str(input("Por favor ingrese una letra para ser evaluada"))
if len(letra) ==1:
    if ord(letra) >= 65 and ord(letra) <= 90:
        if ord(letra) == 65 or ord(letra) == 69 or ord(letra) == 73 or ord(letra) == 79 or ord(letra) == 85:
            print("La letra ingresada corresponde a una vocal mayuscula")
        else:
            print("La letra ingresada corresponde a una consonante mayuscula")
    elif ord(letra) >= 97 and ord(letra) <= 122: 
        if ord(letra) == 97 or ord(letra) == 101 or ord(letra) == 105 or ord(letra) == 111 or ord(letra) == 117:
            print("La letra ingresada corresponde a una vocal minuscula")
        else:
            print("La letra ingresada corresponde a una consonante minuscula")
else:
    print("La cadena ingresada no es una letra, o es mas de una")