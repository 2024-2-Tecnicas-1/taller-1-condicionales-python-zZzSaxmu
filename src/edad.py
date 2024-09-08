from datetime import datetime
def evaluar(dia, mes, anno):
    # TODO: Coloca aquí el código del ejercicio 6: Edad
    from datetime import datetime

def calcular_edad(dia, mes, año):
    fecha_actual = datetime.now()
    edad = fecha_actual.year - año
    if (fecha_actual.month, fecha_actual.day) < (mes, dia):
        edad -= 1
    return edad

if __name__ == '__main__':
    dia = int(input("Día de nacimiento: "))
    mes = int(input("Mes de nacimiento: "))
    año = int(input("Año de nacimiento: "))
    
    edad = calcular_edad(dia, mes, año)
    print(f"Usted tiene {edad} años")


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
