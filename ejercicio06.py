def run():
    n = int(input('Numero: '))
    for i in range(0,11):
        multi = n
        multiplicacion = n*i
        print('-la multiplicación de',multi,'por',i,'es',multiplicacion)


if __name__ =='__main__':
    run()