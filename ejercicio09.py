def run():

    frase = input("Ingrese una frase:\n ").lower()
    letra = input("Que letra desea buscar:\n ").lower()

    contador = 0

    for i in frase:
        if i == letra:
            contador = contador+1

    print("La letra",letra.upper(),"aparece",contador,"veces en la frase: ",frase)


if __name__ =='__main__':
    run()