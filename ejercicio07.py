def run():
    nombre = input('Ingrese palabra: ')
   
    for nombre in (nombre[::-1]):
        print(nombre, end=' ')



if __name__=='__main__':
    run()