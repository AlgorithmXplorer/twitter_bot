
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
        
        self.main_url = "https://x.com/"
        self.email = email
        self.username = username
        self.password = password
        self.is_log_in = False

    def log_in(self):
        #* log in page opens
        log_in_url = self.main_url + "i/flow/login"
        self.driver.get(url = log_in_url)
        self.driver.maximize_window()
        time.sleep(3)

        #*username enters
        email_inp_tag = self.driver.find_element(By.XPATH, "//input[@autocomplete = 'username']") #* this input tag can get email username or number 
        email_inp_tag.send_keys(self.email)
        email_inp_tag.send_keys(Keys.ENTER)
        time.sleep(1.5)

        #!sometimes twitter wants username so try except block must use
        try:
            name_inp_tag = self.driver.find_element(By.XPATH , "//input[@data-testid ='ocfEnterTextTextInput']")
            name_inp_tag.send_keys(self.username)
            name_inp_tag.send_keys(Keys.ENTER)
            time.sleep(1.5)
        except:
            #* if there is no username questiom then just app skip the code
            pass

        #*password enters
        pasword_inp_tag = self.driver.find_element(By.XPATH, "//input[@autocomplete = 'current-password']")
        pasword_inp_tag.send_keys(self.password)
        pasword_inp_tag.send_keys(Keys.ENTER)
        time.sleep(1.5)
        
        self.is_log_in = True
        
        
        






first_bot = bot(email= "tanrininkirbaci36@gmail.com", password= "watchdogs.2007-2025//musty", username= "x_bot_1")
first_bot.log_in()



#todo file manager da username password emial alan func. botdan aldığı verileri dosyaya kaydeden func olucak
    #todo bot oluşturulurken  user datalarını alan func kullanılacak


