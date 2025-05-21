

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
            self.Log_out

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
        pass
    
    def Log_out(self):
        pass
    
    def profile_dtl(self):
        pass
    
    def user_srch(self):
        pass
    
    def flw_flws(self):
        pass

    def tweet_search(self):
        pass

    def daily_twet(self):
        pass

    def asking_ai(self):
        pass

a = PANEL(choice_list=["Log in","Log out","Profile detail","User search","Following or Follower list","Tweet search","Daily tweets","Asking to grok ai"])
a.panel()

