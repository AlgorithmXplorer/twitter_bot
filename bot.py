
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
        time.sleep(5)

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

    def follows_or_followers(self,user_name:str , choice:str , count=None) -> dict:
        if not self.is_log_in:
            raise Exception("bot did not log in")


        #* url making and entering 
        if choice == "following":
            new_url = self.main_url + user_name + "/" + choice
            
        elif choice == "followers":
            new_url = self.main_url + user_name + "/" + choice
        
        self.driver.get(new_url)
        time.sleep(6)

        follow_list = {}
        
        #* an inner function for getting user
        def inner():
            users_div_tag_list = self.driver.find_elements(By.XPATH , "//div[@data-testid='cellInnerDiv']")
            
            inner_follow_list = {}
            
            url_list = [] 
            username_list = []

            for user_div in users_div_tag_list:
                try:
                    username_span_tag = user_div.find_element(By.CSS_SELECTOR , ".css-1jxf684.r-dnmrzs.r-1udh08x.r-1udbk01.r-3s2u2q.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3")
                    username_list.append(username_span_tag.text)
                
                    user_url_tag = user_div.find_element(By.CSS_SELECTOR, ".css-175oi2r.r-1wbh5a2.r-dnmrzs.r-1ny4l3l.r-1loqt21")
                    url_list.append(user_url_tag.get_attribute("href"))
                except:
                    continue
                
            for url,username in zip(url_list,username_list):
                inner_follow_list.update({username : url})
            
            return inner_follow_list
        
        #* if count data doesn't come then just inner function works
        #* but if there is a count data then app scrolls with twitter scrollbar
        if count != None:
            follow_list = inner()
            
            while True:

                #* scrolling with java code
                scroll_height = self.driver.execute_script("return document.documentElement.scrollHeight")
                self.driver.execute_script(f"window.scrollTo(0,{scroll_height})")
                last_height = self.driver.execute_script("return document.documentElement.scrollHeight")

                #* take the new user datas to follow_list (user data update)  
                new_list = inner()        
                follow_list.update(new_list)

                list_count = len(follow_list)
                
                #* loop controls
                if list_count >= count:
                    break
                                
                if last_height == scroll_height:
                    if list_count < count:
                        raise Exception("there are not that many users")
                    
                time.sleep(3)


            #*slicing 
            result = {}
            i=1
            for name,url in follow_list.items():
                result.update({name:url})
                
                if i == count:
                    break
                i+=1

            return result
                
        else:
            follow_list = inner()
            return follow_list

    def user_search(self,name) -> dict:
        if not self.is_log_in :
            raise Exception("bot did not log in")
        
        #*data sending to search input
        self.driver.get(self.main_url)
        time.sleep(1.5)
        inp_tag = self.driver.find_element(By.XPATH , "//input[@data-testid='SearchBox_Search_Input']")
        inp_tag.send_keys(f"#{name}")
        inp_tag.send_keys(Keys.ENTER)
        time.sleep(6)

        #* users page opens
        list_of_butons =  self.driver.find_elements(By.XPATH ,"//div[@class='css-175oi2r r-14tvyh0 r-cpa5s6 r-16y2uox']") 
        users_div = list_of_butons[2]
        users_div.find_element(By.CSS_SELECTOR ,".css-1jxf684.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3").click()
        time.sleep(6)

        #* Retrieving users
        all_user_div_tags = self.driver.find_elements(By.XPATH ,"//div[@data-testid='cellInnerDiv']")
        users = {}
        
        for div_tag in all_user_div_tags:
            #* Retrieving username 
            username_span = div_tag.find_element(By.CSS_SELECTOR , ".css-1jxf684.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3")

            #* Retrieving user url 
            url_a_tag =div_tag.find_element(By.CSS_SELECTOR , ".css-175oi2r.r-1wbh5a2.r-dnmrzs.r-1ny4l3l.r-1loqt21")

            users.update({username_span.text : url_a_tag.get_attribute("href")})
        return users


first_bot = bot(email= "tanrininkirbaci36@gmail.com", password= "watchdogs.2007-2025//musty", username= "x_bot_1")

first_bot.log_in()
time.sleep(4.5)

# liste = first_bot.follows_or_followers(user_name="Ebonivonn",choice="following")

# users = first_bot.user_search(name="ebo")
# print(users)


time.sleep(1000)





#todo file manager da username password emial alan func. botdan aldığı verileri dosyaya kaydeden func olucak
    #todo bot oluşturulurken  user datalarını alan func kullanılacak

#todo panelde olucak seçenekler
"""
- log in
- search (twweet) 
- user searching (eğer öyle bir kullanıcı varsa linkini atıcak)
- followers - follows 
- maybe grok question

"""
