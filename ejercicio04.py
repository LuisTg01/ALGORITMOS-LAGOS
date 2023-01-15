def run():
    cantidad_invertir =  float(input('Cantidad a invertir: '))
    interes_anual     =  float(input('Interes anual en %: '))
    años              =  int(input('Tiempo en años: '))
    
    for x in range (0,años):
        cantidad_invertir *= 1 + interes_anual/100  #se suma +1 al resulado de (interes_anual/100).
        cantidad_invertir = round(cantidad_invertir,2)      
        print('El capital obtenido en', (x+1), 'año es: s/. ' ,cantidad_invertir)

if __name__=='__main__':
    run()