from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

#ltyqqmemymvkishplk@kvhrw.com
#prueba1234
#añadir try, returns para controlar los errores, minimizar la web e intentar crear un csv con toda la info del usuario registrado y con las cookies para que no tenga que estar siempre iniciando sesion
class Scrapy:
    browser = None
    initial_path = '/home/atom/Desktop/Mis_cosas/Programacion/linkedinScrapping/drivers/linux/driverChromeLinuxFer'
    def __init__(self):
        options=webdriver.ChromeOptions().add_argument('--disable-extensions-')
        self.browser = webdriver.Chrome(self.initial_path ,chrome_options=options)

    
    def init_screen(self):
        
        self.browser.get('https://www.linkedin.com')
        
        WebDriverWait(self.browser,5).until(
            EC.element_to_be_clickable((By.XPATH,
            "//button[@action-type='ACCEPT']"
            ))).click()
        #time.sleep(5)
        #self.browser.find_element_by_xpath("//button[@action-type='ACCEPT']").click()
    
    def entrar(self,user,password):
        #Poner aqui una excepcion y arreglar el input
        stateCode = None
        self.browser.find_element_by_xpath("//input[@type='text']").send_keys(user)
        self.browser.find_element_by_xpath("//input[@type='password']").send_keys(password)
        time.sleep(1)
        self.browser.find_element_by_xpath("//button[@data-tracking-control-name='homepage-basic_signin-form_submit-button']").click()
        
        if(self.browser.current_url == "https://www.linkedin.com/feed/?trk=homepage-basic_signin-form_submit"):
            stateCode = 0
        else:
            stateCode = 1
        

        return stateCode
        
    
s = Scrapy()
s.init_screen()
print(s.entrar("ltyqqmemymvkishplk@kvhrw.com", "prueba1234"))