def evaluar(dividendo, divisor):
    cociente = dividendo // divisor
    residuo = dividendo % divisor

    if residuo ==0:
     respuesta = "La división es exacta. \n" \
            "Cociente: " + str(cociente) + "\n" \
            "Residuo: " + str(residuo)
    else:
        respuesta = "La división no es exacta. \n" \
            "Cociente: " + str(cociente) + "\n" \
            "Residuo: " + str(residuo)
    return respuesta

if __name__ == '__main__':
    dividendo = int(input("Dividendo: "))
    divisor = int(input("Divisor: "))
    
    respuesta = evaluar(dividendo, divisor)
    print(respuesta)
