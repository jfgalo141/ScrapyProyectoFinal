from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

#ltyqqmemymvkishplk@kvhrw.com
#prueba1234
#añadir try, returns para controlar los errores, minimizar la web e intentar crear un csv con toda la info del usuario registrado y con las cookies para que no tenga que estar siempre iniciando sesion
#meter tor
#Guardar datos en csv
class Scrapy:
    browser = None
    initial_path = '/Users/fernando_cg/Desktop/ScrapyProyectoFinal/drivers/mac/chromedriver'
    def __init__(self):
        options=webdriver.ChromeOptions().add_argument('--disable-extensions-')
        self.browser = webdriver.Chrome(self.initial_path ,chrome_options=options)

    
    def init_screen(self):
        
        self.browser.get('https://www.linkedin.com/uas/login?fromSignIn=true&trk=cold_join_sign_in')
        
        WebDriverWait(self.browser,5).until(
            EC.element_to_be_clickable((By.XPATH,
            "//button[@action-type='ACCEPT']"
            ))).click()
        #time.sleep(5)
        #self.browser.find_element_by_xpath("//button[@action-type='ACCEPT']").click()
    
    def entrar(self,user,password):
        #Poner aqui una excepcion y arreglar el input
        while True:
            try:
                stateCode = None
                self.browser.find_element_by_xpath("//input[@type='text']").send_keys(user)
                self.browser.find_element_by_xpath("//input[@type='password']").send_keys(password)
                time.sleep(1)
                self.browser.find_element_by_xpath("//button[@type='submit']").click()
                
                if(self.browser.current_url == "https://www.linkedin.com/feed/?trk=homepage-basic_signin-form_submit"):
                    stateCode = True
                else:
                    stateCode = False
                return stateCode
            except:
                self.browser.refresh()
                time.sleep(5)

    def buscar(self,trabajo,ubicacion):
        url = "https://www.linkedin.com/jobs/"
        self.browser.get(url)
        self.browser.find_element(By.XPATH,"//input[@class='jobs-search-box__text-input jobs-search-box__keyboard-text-input']").send_keys(trabajo)
        if(len(ubicacion)>0):
            self.browser.find_element(By.XPATH,"//input[@class='jobs-search-box__text-input']").send_keys(ubicacion)
        self.browser.find_element(By.XPATH,"//button[@type='button']").click()
    
    def filtrar(filtros):
        print("hola")

    
    
s = Scrapy()
s.init_screen()
print(s.entrar("ltyqqmemymvkishplk@kvhrw.com", "prueba1234"))
s.buscar("java","sevilla")