def run():
    numero = int(input('Introduce un numero positivo: '))
    for i in range(numero,-1,-1):#el ultimo -1 señala cuanto se le resta al rango
        print(i,end = ',')


if __name__=='__main__':
    run()