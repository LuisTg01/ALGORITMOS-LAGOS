def run():
    n = int(input("Ingrese un numero: "))
    for contador in range(0,n+1):

        for contador1 in range (contador, 0, -1):
            print('*',end =" ")
        print("")


if __name__=='__main__':
    run()