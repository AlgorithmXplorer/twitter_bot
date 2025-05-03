
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


class bot:
    
    def __init__(self,username:str , email:str , password:str):
        self.option = Options()
        self.option.add_experimental_option("prefs",{"intl.accept_languages" : "en"})
        self.driver = webdriver.Chrome(options= self.option)
        self.action = ActionChains(driver=self.driver)
        
        self.email = email
        self.username = username
        self.password = password

    


