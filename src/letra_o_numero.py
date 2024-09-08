def evaluar(caracter):
    # TODO: Coloca aquí el código del ejercicio 4: Letra o número
    if caracter.isdigit():
        return f"{caracter} es número"
    elif caracter.isalpha():
        if caracter.isupper():
            return f"{caracter} es letra mayúscula"
        else:
            return f"{caracter} es letra minúscula"
    else:
        return f"{caracter} no es letra ni número"
    return "";

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
