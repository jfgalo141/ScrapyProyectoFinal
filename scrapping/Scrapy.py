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
    table = pd.DataFrame(columns=["titulo","empresa","lugar","tipo"])
    initial_path = '/Users/fernando_cg/Desktop/ScrapyProyectoFinal/drivers/mac/chromedriver'
    filters ={
        "lugar":{
            "presencial":"/html/body/div[3]/div/div/div[2]/ul/li[6]/fieldset/div/ul/li[1]/label",
            "remoto":"/html/body/div[3]/div/div/div[2]/ul/li[6]/fieldset/div/ul/li[2]/label",
            "hibrido":"/html/body/div[3]/div/div/div[2]/ul/li[6]/fieldset/div/ul/li[3]/label"
        }
    }
    def __init__(self):
        options=webdriver.ChromeOptions().add_argument('--disable-extensions-')
        self.browser = webdriver.Chrome(self.initial_path ,chrome_options=options)

    
    def init_screen(self):
        
        self.browser.get('https://www.linkedin.com/uas/login?fromSignIn=true&trk=cold_join_sign_in')
        
        WebDriverWait(self.browser,5).until(
            EC.element_to_be_clickable((By.XPATH,
            "//button[@action-type='ACCEPT']"
            ))).click()
        time.sleep(1)
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

    def filtrar(self,filtros):
        #WebDriverWait(self.browser,5).until(
        #EC.element_to_be_clickable((By.XPATH,"/html/body/div[7]/aside/div[1]/header/div[3]/button[2]/li-icon/svg"))).click()

        WebDriverWait(self.browser,5).until(
        EC.element_to_be_clickable(
            (By.XPATH,"/html/body/div[7]/aside/div[1]/header/div[2]/button/h2/span[1]"))).click()
        
        WebDriverWait(self.browser,5).until(
        EC.element_to_be_clickable(
            (By.XPATH,"/html/body/div[7]/div[3]/div[3]/section/div/div/div/div/div/button"))).click()

        for filter in filtros:
            WebDriverWait(self.browser,5).until(
            EC.element_to_be_clickable(
                (By.XPATH,self.filters[filter][filtros[filter]]))).click()
        
        WebDriverWait(self.browser,5).until(
        EC.element_to_be_clickable(
            (By.XPATH,"/html/body/div[3]/div/div/div[3]/div/button[2]/span"))).click()
   
    def anuncio(self):
        #/html/body/div[7]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[1]/div/div
        jobs = self.browser.find_elements(By.CLASS_NAME,"job-card-container")
        for i in jobs:
            datos = []
            contador = 0
            for line in i.text.splitlines():
                if contador <4:
                    datos.append(line)
                else:
                    break

            self.saveTable(datos[0],datos[1],datos[2],datos[3])
            self.saveCsv()
            

    def scrapping(self):
        #"/html/body/div[7]/div[3]/div[3]/div[2]/div/section[2]/div 
        time.sleep(3)
        titulo = self.browser.find_element(By.XPATH,"/html/body/div[7]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[2]/a/h2").text
        lugarRemoto = self.browser.find_element(By.XPATH,"/html/body/div[7]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[2]/div[1]/span[1]/span[2]").text
        tipoDeJornada = self.browser.find_element(By.XPATH,"/html/body/div[7]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/ul/li[1]/span").text
        url = self.browser.current_url
        self.saveTable(titulo,lugarRemoto,tipoDeJornada,url)
        self.saveCsv()

    def saveTable(self,titulo,lugarRemoto,tipoDeJornada,url):
        data =pd.DataFrame([[titulo,lugarRemoto,tipoDeJornada,url]],columns=["titulo","empresa","lugar","tipo"])
        self.table = self.table.append(data)

    def saveCsv(self):
        self.table.to_csv("./data/offerts.csv",index=False)
    
s = Scrapy()
s.init_screen()
s.entrar("jytizjltoohjfxnquk@nvhrw.com", "prueba1234")
#eoivzjagqtvundoxpp@kvhrs.com
#xiwir15359@spruzme.com
#ltyqqmemymvkishplk@kvhrw.com
#jytizjltoohjfxnquk@nvhrw.com
#hacer que se guarde un csv con las solicitudes de la cuenta
s.buscar("java","sevilla")
time.sleep(2)
s.filtrar({"lugar":"presencial"})
time.sleep(4)
s.anuncio()