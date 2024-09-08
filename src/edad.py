from time import localtime
def evaluar(dia_nac, mes_nac, anno_nac):
    t = localtime()
    dia_actual = t.tm_mday
    mes_actual = t.tm_mon
    anno_actual = t.tm_year

    edad = anno_actual - anno_nac

    if (mes_nac > mes_actual) or (mes_nac == mes_actual and dia_nac > dia_actual):
        edad -= 1

    return f"Usted tiene {edad} años"


if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
