
import time
import bot
import file_manager



class PANEL:

    def __init__(self,choice_list:list):
        self.choices = choice_list        
        self.bot = None

    def panel(self):
        while True:
            #* if the user doesn't choose an option in the list then an error raise and repeat the process
            try:
                [print(f"{index}: {item}") for index , item in enumerate(self.choices,start=1)]
                inp = input("\nchoose a choice(number): ").strip(" ")
                if inp not in ["1","2","3","4","5","6","7","8","9"]:
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
        
        elif inp == "9":
            self.quit()

    def quit(self):
        print("the app has been quit")

    def Log_in(self):
        #* the app stops to log in again
        if self.bot !=None:
            print("\nbot is already logged in\n")
            self.panel()
        
        #* user's datas getting to log in 
        try:
            file_manager.user_data_taker()
        except Exception as error:
            print(error)

        #* the datas of saved to the file are getting
        try:
            user_datas = file_manager.user_data_reader()
        except :
            print("there is a problem about app. please log in again")
        time.sleep(3)

        #* bot is creating 
        self.bot = bot.bot(username=user_datas[0], email= user_datas[1], password= user_datas[2])
        self.is_log_in = True

        #* if there a problem about driver then the app warns to the user
        try:
            self.bot.log_in()
        except Exception as error:
            if len(str(error)) > 50:
                print("There is a error happend. Please try it later")
            
        self.panel()

    def Log_out(self):
        #* bot's driver closes and the saves deletes
        if self.bot == None:
            print("\nplease first log in\n")
            self.panel()
        else:
            self.bot.driver.close()
            file_manager.save_deleter()
            print("The app is log out")
                    
    def profile_dtl(self):
        #* if the user wants take a look at the the profil

        if self.bot == None:
            print("\nplease first log in\n")
            self.panel()
        
        try:
            detail = self.bot.profile_details()
            file_manager.data_writer(detail)

        except Exception as error:
            print(error)
        
        self.panel()

   #* the functions under this line work with the same logic so i dont write descp to these functions

    def user_srch(self):
        if self.bot == None:
            print("\nplease first log in\n")
            self.panel()
        
        try:
            datas = self.bot.user_search()
        except Exception as error:
            if len(str(error)) > 50:
                print("There is a error happend. Please try it few miuntes later")
                self.panel()
            else:
                print(error)
                self.panel()
        else:    
            file_manager.data_writer(datas)
            self.panel()
    
    def flw_flws(self):
        if self.bot == None:
            print("\nplease first log in\n")
            self.panel()
        
        try:
            datas = self.bot.follows_or_followers()
        except Exception as error:
            if len(str(error)) > 50:
                print("There is a error happend. Please try it few miuntes later")
                self.panel()
            else:
                print(error)
                self.panel()
        else:
            file_manager.data_writer(data = datas)
            self.panel()
        
    def tweet_search(self):
        if self.bot == None:
            print("\nplease first log in\n")
            self.panel()

        try:
            datas = self.bot.search_tweet()
        except Exception as error:
            if len(str(error)) > 50:
                print("There is a error happend. Please try it few miuntes later")
                self.panel()
            else:
                print(error)
                self.panel()
        else:
            file_manager.data_writer(data= datas)
            self.panel()
        
    def daily_twet(self):
        if self.bot == None:
            print("\nplease first log in\n")
            self.panel()
        try:
            self.bot.daily_tweets(writer_func = file_manager.data_writer)
        except Exception as error:
            if len(str(error)) > 50:
                print("There is a error happend. Please try it few miuntes later")
                self.panel()
            else:
                print(error)
                self.panel()
        else:
            self.panel()
        
    def asking_ai(self):
        if self.bot == None:
            print("\nplease first log in\n")
            self.panel()

        try:
            datas = self.bot.ask_grok()
        except Exception as error:
            if len(str(error)) > 50:
                print("There is a error happend. Please try it few miuntes later")
                self.panel()
            else:
                print(error)
                self.panel()
        else:
            file_manager.data_writer(datas)
            self.panel()

#! NOT: if the error lenght bigger 50 character lenght then we assumes there is a problem in the driver.
#! generarlly the problem happens because the network speed is slow and the pages doesn't uploud

if __name__ == "__main__":
    a = PANEL(choice_list=["Log in","Log out","Profile detail","User search","Following or Follower list","Tweet search","Daily tweets","Asking to grok ai","Quit the app"])
    a.panel()

