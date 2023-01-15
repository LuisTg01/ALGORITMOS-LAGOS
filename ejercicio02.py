def run():
    n = int(input('Ingrese un número:'))
    for i in range(0,n+1):
        if i % 2 == 1:
            print(i,end=',')
    print('Programa terminado...')
            

if __name__ == '__main__':
    run()