

"""
İŞLMELER
    1- login
    2- çıkış yap
    3- profile detail
    4- kullanıcı aratma
    5- takip veya taipçi listesi alma
    6- text aratma
    7- ana sayfadsa dolaşma
    8- grok yapay zekasına soru sorma
"""
import time
from bot import bot
import file_manager

file_manager.json_folder_maker()


class PANEL:

    def __init__(self,choice_list:list):
        self.choices = choice_list        
        self.bot = None

    def panel(self):
        while True:
            try:
                [print(f"{index}: {item}") for index , item in enumerate(self.choices,start=1)]
                inp = input("\nchoose a choice(number): ").strip(" ")
                if inp not in ["1","2","3","4","5","6","7","8"]:
                    raise Exception("please choose correctly")

            except Exception as error:
                print("\n",error,"\n")
            else:
                break

        if inp == "1":
            self.Log_in()
        
        elif inp == "2":
            self.Log_out()

        elif inp == "3":
            self.profile_dtl()

        elif inp == "4":
            self.user_srch()

        elif inp == "5":
            self.flw_flws()

        elif inp == "6":
            self.tweet_search()

        elif inp == "7":
            self.daily_twet()

        elif inp == "8":
            self.asking_ai()



    def Log_in(self):
        if self.bot != None:
            print("\nbot is already logged in\n")
            self.panel()

        try:
            file_manager.user_data_taker()
        except Exception as error:
            print(error)

        user_datas = file_manager.user_data_reader()
        time.sleep(3)

        self.bot = bot(username=user_datas[0], email= user_datas[1], password= user_datas[2])
        
        self.bot.log_in()

        self.panel()


    def Log_out(self):
        if self.bot == None:
            print("\nplease first log in\n")
            self.panel()
        else:
            try:
                self.bot.log_out(file_manager.save_deleter)
            except Exception as error:
                print(error)
        print("The app is log out")

    
    def profile_dtl(self):
        if self.bot == None:
            print("\nplease first log in\n")
            self.panel()
        
    
    def user_srch(self):
        if self.bot == None:
            print("\nplease first log in\n")
            self.panel()
        
    
    def flw_flws(self):
        if self.bot == None:
            print("\nplease first log in\n")
            self.panel()
        

    def tweet_search(self):
        if self.bot == None:
            print("\nplease first log in\n")
            self.panel()
        

    def daily_twet(self):
        if self.bot == None:
            print("\nplease first log in\n")
            self.panel()
        

    def asking_ai(self):
        if self.bot == None:
            print("\nplease first log in\n")
            self.panel()
        

a = PANEL(choice_list=["Log in","Log out","Profile detail","User search","Following or Follower list","Tweet search","Daily tweets","Asking to grok ai"])
a.panel()

