def evaluar(peso, estatura, edad):
    imc = peso / (estatura ** 2)
    
    if edad < 45:
        if imc < 22:
            return "Riesgo bajo"
        else:
            return "Riesgo medio"
    else:
        if imc < 22:
            return "Riesgo medio"
        else:
            return "Riesgo alto"

if __name__ == '__main__':
    peso = int(input("Peso (kg): "))
    estatura = float(input("Estatura (m): "))
    edad = int(input("Edad: "))
    
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
