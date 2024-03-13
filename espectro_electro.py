def espectro(frecuencia: float):
  if frecuencia < 3:
    return "Ondas de radio"
  elif frecuencia < 300e9:
    return "Microondas"
  elif frecuencia < 400e12:
    return "Infrarrojo"
  elif frecuencia < 750e12:
    return "Luz visible"
  elif frecuencia < 30e15:
    return "Ultravioleta"
  elif frecuencia < 30e18:
    return "Rayos X"
  else:
    return "Rayos gamma"

frecuencia = float(input("Ingrese la frecuencia (Hz) de la onda que desea consultar:  ")) 

f_onda = espectro(frecuencia)
print("la frecuencia", frecuencia, "pertence al espectro electromagnetico de:", f_onda)
