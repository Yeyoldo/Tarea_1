from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import choice
import time
import random
import msvcrt


def crearcuenta(): 
    #Creacion de correo de forma random y la contraseña 
    valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Ynombre = ""
    Ynombre = Ynombre.join([choice(valores) for i in range(12)])
    dominio = "@yopmail.com"
    correo = Ynombre + dominio

    #Creacion de cuenta en la pagina tomando los valores y llenando estos en la misma
    browser = webdriver.Chrome()
    browser.get("https://mariakawaii.cl/mi-cuenta/")
    time.sleep(5)
    username = browser.find_element_by_id("reg_username")
    email = browser.find_element_by_id("reg_email")
    password = browser.find_element_by_id("reg_password")

    username.clear()
    email.clear()
    password.clear()

    username.send_keys(Ynombre)
    email.send_keys(correo)
    password.send_keys(Ynombre)

    login_attempt = browser.find_element_by_xpath("//*[@name='register']").click()


    #Guardamos en txt el usuario creado
    guardar = correo + " " + Ynombre
    f = open ("usuarios.txt", "a")
    f.write(guardar + '\n')
    f.close()

    

def iniciosesion(DECISION):
    #tomamos los usuarios creados en el archivo txt
    usuarios = open("usuarios.txt","r")
    contador = 0
    while(True):
        U = usuarios.readline()
        if not U:
            break
        print(str(contador) + '.- Credenciales:' + U)
        contador = contador + 1
    usuarios.close()

    #elegimos la credencial a utilizar y separamos para obtener el correo y contraseña por separado
    credencial = int(input("Ingrese un numero de credencial: "))

    usuarios = open("usuarios.txt","r")
    contador = 0
    S = ""
    C = ""

    flag = True
    while(flag):
        U = usuarios.readline()
        print(U)
        if credencial == contador:
            print("El usuario a utilizar es: " + U)
            separar = U.split()
            S = separar[0]
            C = separar[1]
            flag = False
        contador = contador + 1
        if not U:
            print("Numero no valido")
            break
    usuarios.close()


    #Iniciamos Sesion con los datos obtenidos ya separados
    browser = webdriver.Chrome()
    browser.get("https://mariakawaii.cl/mi-cuenta/")
    time.sleep(5)

    username = browser.find_element_by_id("username")
    password = browser.find_element_by_id("password")

    username.clear()
    password.clear()

    username.send_keys(S)
    password.send_keys(C)

    login_attempt = browser.find_element_by_xpath("//*[@name='login']").click()
    time.sleep(5)
    valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"    
    
    if(DECISION == 0):
        #hasta aqui es inicio de sesion
        return

    else:
        #en este punto se produce el cambio de contraseña ya teniendo la sesion iniciada
        browser.get("https://mariakawaii.cl/mi-cuenta/edit-account/")

        actual = C
        nueva = ""
        nueva = nueva.join([choice(valores) for i in range(12)])
        
        nombre =browser.find_element_by_id("account_first_name")
        apellido = browser.find_element_by_id("account_last_name")
        act = browser.find_element_by_id("password_current")
        new = browser.find_element_by_id("password_1")
        confirmar = browser.find_element_by_id("password_2")

        nombre.send_keys("Nombre")
        apellido.send_keys("Apellido")
        act.send_keys(C)
        new.send_keys(nueva)
        confirmar.send_keys(nueva)

        login_attempt = browser.find_element_by_xpath("//*[@name='save_account_details']").click()

        

        #Registramos nueva contrasenia
        usuarios = open("usuarios.txt","r")
        flag = True
        contador = 0
        while(flag):
            U = usuarios.readline()
            if credencial == contador:
                separar = U.split()
                S = separar[0]
                C = nueva
                newline = S + " " + C
                reemplazar_linea('usuarios.txt',credencial,newline)
                print('NUEVAS CREDENCIALES' + newline)
                flag = False
            contador = contador + 1
            if not U:
                print("Numero no valido")
                break
        usuarios.close()


        #Nos logueamos con las nuevas credenciales
        browser = webdriver.Chrome()
        browser.get("https://mariakawaii.cl/mi-cuenta/")
        time.sleep(5)

        username = browser.find_element_by_id("username")
        password = browser.find_element_by_id("password")

        username.clear()
        password.clear()

        username.send_keys(S)
        password.send_keys(C)

        login_attempt = browser.find_element_by_xpath("//*[@name='login']").click()
        time.sleep(5)

def reemplazar_linea(nombre_archivo, numero_linea, reemplazo):
    #permite reemplazar la linea por las credenciales nuevas
    linea = open(nombre_archivo, 'r').readlines()
    linea[numero_linea] = reemplazo + '\n'
    out = open(nombre_archivo, 'w')
    out.writelines(linea)
    out.close()


def reestablecer():
    #permite restablecer la contraseña por el link adjuntando el correo del usuario que se encuentra en el archivo txt
    usuarios = open("usuarios.txt","r")
    contador = 0
    S = ""
    while(True):
        U = usuarios.readline()
        if not U:
            break
        print(str(contador) + '.- Credenciales:' + U)
        contador = contador + 1
    usuarios.close()

    credencial = int(input("Ingrese un numero de credencial: "))
    
    flag = True
    us = open("usuarios.txt","r")
    contador = 0
    while(flag):
        Z = us.readline()

        if not Z:
            print("Numero no valido")
            break
        
        if credencial == contador:
            print("El usuario a utilizar es: " + Z)
            separar = Z.split()
            S = separar[0]
            flag = False
    
        contador = contador + 1
    us.close()

    browser = webdriver.Chrome()
    browser.get("https://mariakawaii.cl/mi-cuenta/lost-password/")
    na = browser.find_element_by_id("user_login")
    na.send_keys(S)
    login_attempt = browser.find_element_by_xpath("//*[@value='Restablecer contraseña']").click()


#MAIN O MENÚ 
print("1.- Crear cuenta")
print("2.- Inicio de sesion")
print("3.- Reestablecer contraseña")
print("4.- Modificar contraseña")
opcion = int(input("Ingrese una opción: "))    


if(opcion==1):
    crearcuenta()
    print("Presione una tecla para cerrar...")
    msvcrt.getch()

elif (opcion==2):
    iniciosesion(0)
    print("Presione una tecla para cerrar...")
    msvcrt.getch()

elif (opcion==3):
    reestablecer()
    print("Presione una tecla para cerrar...")
    msvcrt.getch()

elif (opcion==4):
    iniciosesion(1)
    print("Presione una tecla para cerrar...")
    msvcrt.getch()

else:
    print()



    
