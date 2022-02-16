from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import pandas as pd

class Scrapy:
    browser = None
    initial_path = '/home/atom/Desktop/Mis_cosas/Programacion/linkedinScrapping/drivers/driverChromeLinuxFer'
    def __init__(self):
        options=webdriver.ChromeOptions().add_argument('--disable-extensions-')
        self.browser = webdriver.Chrome(self.initial_path ,chrome_options=options)

    
    def init_screen(self):
        
        self.browser.get('https://www.linkedin.com')
    
s = Scrapy()
s.init_screen()
