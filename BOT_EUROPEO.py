from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from random import choice
import time
import random
import msvcrt
import pyperclip as clipboard
import keyboard




def crearcuenta(): 
    #Creacion de correo
    valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    phone = "0123456789"
    Ynombre = ""
    Ynumero = ""
    Ynombre = Ynombre.join([choice(valores) for i in range(4,15)])
    Ynumero = Ynumero.join([choice(phone) for i in range(8)])
    Ynumero = "9" + Ynumero
    dominio = "@yopmail.com"
    correo = Ynombre + dominio

    #Creacion de cuenta
    browser = webdriver.Chrome()
    browser.get("https://www.telepizza.es/#registrarse")
    time.sleep(5)

    email = browser.find_element_by_id("Email")
    password = browser.find_element_by_id("Password")
    confirm = browser.find_element_by_id("ConfirmPassword")
    telefono = browser.find_element_by_id("FirstPhone")


    email.clear()
    password.clear()
    confirm.clear()
    telefono.clear()


    email.send_keys(correo)
    password.send_keys(Ynombre)
    confirm.send_keys(Ynombre)
    telefono.send_keys(Ynumero)


    login_attempt = browser.find_element_by_xpath("//*[@class='checkbox safari safari537 not_msie']").click()
    login_attempt = browser.find_element_by_xpath("//*[@class='checkbox safari safari537 not_msie']").click()

    for btn in browser.find_elements_by_tag_name('button'):
        if btn.get_attribute('class') == 'btn_submit':
            print(btn.text)
            btn.click()
            break
        
    #Guardamos en txt
    guardar = correo + " " + Ynombre
    f = open ("usuariosE.txt", "a")
    f.write(guardar + '\n')
    f.close()


def iniciosesion(DECISION):
    usuarios = open("usuariosE.txt","r")
    contador = 0
    while(True):
        U = usuarios.readline()
        if not U:
            break
        print(str(contador) + '.- Credenciales:' + U)
        contador = contador + 1
    usuarios.close()


    credencial = int(input("Ingrese un numero de credencial: "))

    usuarios = open("usuariosE.txt","r")
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


    #Iniciamos Sesion
    browser = webdriver.Chrome()
    browser.get("https://www.telepizza.es/#home_login_form")
    time.sleep(5)

    username = browser.find_element_by_id("EmailLogin")
    username.send_keys(S)

    password = browser.find_element_by_xpath("/html/body/ul/li[1]/div/div[2]/fieldset[1]/form/div[2]/span[1]/input[2]").click()
    keyboard.write(C)
    time.sleep(3)

    boton = browser.find_element_by_xpath("/html/body/ul/li[1]/div/div[2]/fieldset[1]/form/div[4]/button").click()

    valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"    

    
    if(DECISION == 0):
        return

    else:
        browser.get("https://www.telepizza.es/usuario/cuenta")

        time.sleep(3)

        nueva = ""
        nueva = nueva.join([choice(valores) for i in range(12)])
        

        act = browser.find_element_by_xpath("/html/body/div[5]/div[1]/form/div[2]/fieldset[2]/div[2]/span[1]/input[2]")
        act.send_keys(nueva)


        new = browser.find_element_by_xpath("/html/body/div[5]/div[1]/form/div[2]/fieldset[2]/div[3]/span[1]/input")
        new.send_keys(nueva)


        confirmar = browser.find_element_by_xpath("/html/body/div[5]/div[1]/form/div[2]/div[2]/button").click()

        
        #Registramos nueva contrasenia
        usuarios = open("usuariosE.txt","r")
        flag = True
        contador = 0
        while(flag):
            U = usuarios.readline()
            if credencial == contador:
                separar = U.split()
                S = separar[0]
                C = nueva
                newline = S + " " + C
                reemplazar_linea('usuariosE.txt',credencial,newline)
                print('NUEVAS CREDENCIALES' + newline)
                flag = False
            contador = contador + 1
            if not U:
                print("Numero no valido")
                break
        usuarios.close()


        #Nos logueamos con las nuevas credenciales
        browser = webdriver.Chrome()
        browser.get("https://www.telepizza.es/#home_login_form")
        time.sleep(5)
        username = browser.find_element_by_id("EmailLogin")
        username.send_keys(S)

        password = browser.find_element_by_xpath("/html/body/ul/li[1]/div/div[2]/fieldset[1]/form/div[2]/span[1]/input[2]").click()
        keyboard.write(C)
        time.sleep(3)

        boton = browser.find_element_by_xpath("/html/body/ul/li[1]/div/div[2]/fieldset[1]/form/div[4]/button").click()

        

def reemplazar_linea(nombre_archivo, numero_linea, reemplazo):
    linea = open(nombre_archivo, 'r').readlines()
    linea[numero_linea] = reemplazo + '\n'
    out = open(nombre_archivo, 'w')
    out.writelines(linea)
    out.close()


def reestablecer():
    usuarios = open("usuariosE.txt","r")
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
    us = open("usuariosE.txt","r")
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
    browser.get("https://www.telepizza.es/usuario/clave")

    na = browser.find_element_by_xpath("/html/body/div[5]/div[2]/span/input")
    na.send_keys(S)
    login_attempt = browser.find_element_by_xpath("/html/body/div[5]/p/a").click()



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
    print("Opcion no valida")