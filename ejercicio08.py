def run():
    password = input('Ingrese una contraseña:\n')

    copy_password= input('Repita la contraseña:\n')
        
    while copy_password == password:
        print('La contraseña fue creada...')
        break
    else:
        print('La contraseña no concuerda...')


if __name__=='__main__':
    run()