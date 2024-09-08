def evaluar(anno):
    if anno < 1582:
        if anno % 4 == 0:
            return f"{anno} es bisiesto"
        else:
            return f"{anno} no es bisiesto"
    else:
        if (anno % 400 == 0) or (anno % 4 == 0 and anno % 100 != 0):
            return f"{anno} es bisiesto"
        else:
            return f"{anno} no es bisiesto"

if __name__ == '__main__':
    anno = int(input("Año: "))
    respuesta = evaluar(anno)
    print(respuesta)
