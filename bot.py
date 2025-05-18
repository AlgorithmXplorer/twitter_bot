
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

    def follows_or_followers(self) -> dict:
        if not self.is_log_in:
            raise Exception("bot did not log in")

        #* name ,count and follower or following choice getting
        def name_taker() -> str:
            while True:
                try:
                    name = input("enter an username: ").strip(" ")
                    if len(name) > 15:
                        raise ValueError("usernames character long max be fifteen character")
                    elif len(name) <= 0:
                        raise ValueError("please enter an username correctly")
                    
                except ValueError as error:
                    print(error)
                else:
                    return name
        user_name = name_taker()

        def choice_taker():
            while True:
                try:
                    choices = ["following","followers"]
                    choice = input(f"1){choices[0]} \n2){choices[1]} \nwhich one(number): ")
                    if choice !="1" and choice != "2":
                        raise ValueError("please enter a choice correctly")
                except ValueError as error:
                    print(error)

                else:
                    return choice
        choice = choice_taker()

        def count_taker() -> int:
            while True:
                try:
                    count = int(input("enter a count: "))
                    if count > 1000 or count < 0:
                        raise OverflowError("app does not bring that much user")

                except ValueError:
                    print("please enter a count correctly")
                except OverflowError as error:
                    print(error)
                else:
                    return count 
        count = count_taker()


        #* url making and entering 
        if choice == "1":
            new_url = self.main_url + user_name + "/" + "following"
            
        elif choice == "2":
            new_url = self.main_url + user_name + "/" + "followers"
        
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

    def user_search(self) -> dict:
        if not self.is_log_in :
            raise Exception("bot did not log in")
        
        #*return to main page
        self.driver.get(self.main_url)

        #*username taking
        def name_taker() -> str:
            while True:
                try:
                    name = input("enter an username: ").strip(" ")
                    if len(name) > 15:
                        raise ValueError("usernames character long max be fifteen character")
                    elif len(name) <= 0:
                        raise ValueError("please enter an username correctly")
                    
                except ValueError as error:
                    print(error)
                else:
                    return name
        name = name_taker()
        time.sleep(1.5)

        #*data sending to search input
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

    def search_tweet(self) -> dict:
        if self.is_log_in == False:
            raise Exception("bot did not log in")
        
        #*return to main page
        self.driver.get(self.main_url)
        time.sleep(1.5)
        
        #* topic and tweet count taking
        def topic_taker() -> str:
            while True:
                try:
                    topic = input("what will search: ").lower().strip(" ")
                    if topic == "":
                        raise ValueError("please enter a topic")
                except ValueError as error:
                    print(error)
                else:
                    return topic
        topic = topic_taker()

        def count_taker() -> int:
            while True:
                try:
                    count = int(input("enter a count: "))
                    if count > 1000 or count < 0:
                        raise OverflowError("app does not bring that much tweet")

                except ValueError:
                    print("please enter a count correctly")
                except OverflowError as error:
                    print(error)
                else:
                    return count        
        count = count_taker()



        #* searching the topic with hashtag
        inp_tag = self.driver.find_element(By.XPATH ,"//input[@data-testid='SearchBox_Search_Input']")
        inp_tag.send_keys(f"#{topic}")
        inp_tag.send_keys(Keys.ENTER)
        time.sleep(6)

        def tweet_taker()->dict:
            tweets = {}
            text_list = self.driver.find_elements(By.XPATH , "//div[@data-testid='tweetText']")
            name_list = self.driver.find_elements(By.XPATH , "//div[@data-testid ='User-Name' ]")
            
            for text_div , name_div in zip(text_list,name_list):
                #*tweet text datas getting
                text_span_tags =text_div.find_elements(By.CSS_SELECTOR , ".css-1jxf684.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3")
                text = "  //  ".join([ span.text for span in text_span_tags if len(span.text) >2])
                
                #* the user who owns tweet
                username = name_div.find_element(By.CSS_SELECTOR , ".css-1jxf684.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3")
                
                tweets.update({username.text : text})
            return tweets
        
        def scroll_func():
            first_height = self.driver.execute_script("return document.scrollingElement.scrollHeight")
            
            scroling = self.driver.execute_script(f"window.scrollTo(0,{first_height})")

            last_height =  self.driver.execute_script("return document.scrollingElement.scrollHeight")

            if last_height == first_height:
                raise ValueError("all tweets are appeared")
            
        def main(tweet_func , scroler , count:int) -> dict:
            tweets = {}
            while True:
                tweet_list = tweet_func()
                tweets.update(tweet_list)

                if len(tweets) > count:
                    return tweets
                try:
                    scroler()
                except ValueError as error:
                    print(error)
                    return tweets
                time.sleep(1.5)

        #*slicng
        first_list = main(tweet_func=tweet_taker , scroler= scroll_func, count=count)
        last_list ={}
        for name,text in first_list.items():
            last_list.update({name:text})
            if len(last_list) == count:
                return last_list
        
    def daily_tweets(self) -> None:
        if not self.is_log_in:
            raise Exception("bot did not log in")
        
        self.driver.get(url= self.main_url)
        time.sleep(3)

        #* tweet taker func 
        def inner():
            tweets = {}
            #* tweets taking
            text_div_tags = self.driver.find_elements(By.XPATH , "//div[@data-testid = 'tweetText']")
            username_div_tags = self.driver.find_elements(By.XPATH , "//div[@data-testid = 'User-Name']")
            
            #* username and tweet text taking
            for text_div , username_div in zip(text_div_tags , username_div_tags):
                username = username_div.find_element(By.CSS_SELECTOR , ".css-1jxf684.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3")

                text_list = text_div.find_elements(By.CSS_SELECTOR , ".css-1jxf684.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3")
                text = "   ".join([span.text for span in text_list if len(span.text) > 2])

                tweets.update({username.text :  text})
            return tweets
        
        def scroller():
            scroll_bar_height = self.driver.execute_script("return document.scrollingElement.scrollHeight")
            
            self.driver.execute_script(f"window.scrollTo(0,{scroll_bar_height})")
            time.sleep(4.5)

        def user_choice_getting():
            while True:
                user_choice = input("do you want more tweet? (y/n): ").lower().strip(" ")
                if user_choice not in ["y","n"]:
                    print("please enter your choice correctly")
                else:
                    return user_choice
        
        tweets = inner()
        print(tweets)
        
        while True:
            if user_choice_getting() == "n":
                break
            else:
                scroller()
                new_tweets = inner()
                print(new_tweets)
        
    def ask_grok(self) -> str:
        if not self.is_log_in:
            raise Exception("bot did not log in")

        self.driver.get(url = self.main_url)
        time.sleep(1.5)

        #* entering to grok page
        self.driver.get(url= "https://x.com/i/grok")
        time.sleep(1.5)

        def question_getting():
            while True:
                question = input("what are you going to ask grok: ").strip(" ").lower()
                if question == "":
                    print("please write the question correctly")
                else:
                    return question

        def waiting():
            strs = [".",". .",". . ."]

            for i in range(2):
                print(strs[0])
                time.sleep(0.5)

                print(strs[1])
                time.sleep(0.5)

                print(strs[2])
                time.sleep(0.5)

                print(strs[1])
                time.sleep(0.5)

        def asking(question:str):
            
            ask_bar = self.driver.find_element(By.XPATH , "//textarea[@autocapitalize='sentences']")
            #* entering the question to grok
            ask_bar.send_keys(question)
            time.sleep(0.5)
            ask_bar.send_keys(Keys.ENTER)
        
            waiting()
            

            #* returning the answer
            answer_span = self.driver.find_element(By.CSS_SELECTOR, ".css-146c3p1.r-bcqeeo.r-1ttztb7.r-qvutc0.r-37j5jr.r-a023e6.r-16dba41.r-1adg3ll.r-a8ghvy.r-p1pxzi")
            return_data = f"Question: {question}\nGROK:  {answer_span.text}\n\n"
            return return_data


        question = question_getting()

        while True:
            try:
                answer = asking(question=question)
            except:
                waiting()
            else:
                return answer


    #* grok limiti doldu 2 saat sonra tekrar gel        

        

first_bot = bot(email= "tanrininkirbaci36@gmail.com", password= "watchdogs.2007-2025//musty", username= "x_bot_1")

first_bot.log_in()
time.sleep(4.5)

#* user follower or follows getting
# liste = first_bot.follows_or_followers()
# print(len(liste))
# print(liste)

#* user searching
# users = first_bot.user_search()
# print(users)

#* tweet searching
# tweets = first_bot.search_tweet()
# print(tweets)
# print(len(tweets))

#* daily tweets taking
# daily_tweets = first_bot.daily_tweets()

#* asking to grok ai
# x = first_bot.ask_grok()
# print(x)



#todo file manager da username password emial alan func. botdan aldığı verileri dosyaya kaydeden func olucak
    #todo bot oluşturulurken  user datalarını alan func kullanılacak

#todo panelde olucak seçenekler
"""
- log in
- search (tweet) 
- user searching (eğer öyle bir kullanıcı varsa linkini atıcak)
- followers - follows 
- daily tweets
- maybe grok question

"""
