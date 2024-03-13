# Declarar constantes
VEL_LUZ: float = 3e+8
VEL_SONIDO: float = 343
VEL_BOLT: float = 10.44
VEL_CHIRON: float = 147.5

if __name__ == "__main__":

    distancia= float(input("ingrese una distancia en metros:   "))  #Se inserta el valor de la distancia (en metros)

    # devuelve el tiempo que cada velocidad tardaría en recorrer esa distancia
    luz = print("a la luz le tomaría:", distancia/VEL_LUZ, "s")
    sonido =print("al sonido le tomaria:", distancia/VEL_SONIDO, "s")
    bolt= print("a Usain Bolt le tomaría:", distancia/VEL_BOLT, "s" )
    auto= print("al Koenigsegg Jesko Absolut le tomaría:", distancia/VEL_CHIRON, "s")

   





