def evaluar(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Triángulo equilátero"
        elif a == b or a == c or b == c:
            return "Triángulo isósceles"
        else:
            return "Triángulo escaleno"
    else:
        return "Triángulo inválido"

if __name__ == '__main__':
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    
    respuesta = evaluar(a, b, c)
    print(respuesta)
