
#region #todo user data geter function 
#* kullancı username email ve şifre giricek. bu bilgileri geçici bir txt dosyası açıcaz ve oraya yazıcak
#* yazılan bilgileri bir json dosyasına kaydedeğiz
#* bu json dosyası içindeki dicti aşağıdaki gibi olucak.
"""
{
"active_profile":None / {bilgiler}
}
"""
#* kullanıcı bu işlemleri login dediği zaman olucak.
#* bu data işlemleri bittikten sonra bota gereken bilgileri burda yazdığımız fonksiyon çıktı edicek

#todo yani burda ayzılan fonksiyonun amacı:
"""
kullanıcı login dediği ilk önce dataları yazdığımız json dosyasına bakıcak
eğerki active profile None ise bir txt dosyası çalıştıracak ve bilgileri alıcak. ayrıca txt dosyasında not olarak işi bittiğinde terminale q girmesini isteyeceğiz.
bilgileri aldıktan dosya silinecek ve json dosyasına kaydedecek
ve bu kaydetme işlemi sonrası yine json dosyasındaki veriyi okuayak verileri bota gönderecek.
"""
#endregion

#region #* data writer
#* bottan alınan tüm veriler anlık olarak txt dosyalarında gösteren bir fonksiyon olucak
#* bu fonksiyon aldığı bir dicti yada listeyi anlık olarak bir txt dosyasına yazıcak ve txt dosyasında not olarak işi bittiğinde terminale q giilmesi istenecek.
#* botun her bir fonksiyonun çıktısı bu txt dosyasına datayı yazdıran fonksiyon ile olucak

#todo yani oluşturulcak bu fonksyion bot tarafından aldığı verileri anlık olarak bir txt dosyasında gösterecek
#endregion

#todo daily tweet bringer fonksiyonu direk parametre olarak alarak kendi içinde yazdırıcak


import os 
import json as js
from bot import bot
import time

def quit_taker():
    while True:
        try:
            inp = input("///:").strip(" ").lower()

            if inp != "q":
                raise Exception("please try again. you can only enter q")

        except Exception as error:
            print(error)
        else:
            break

main_path = os.getcwd()

def json_folder_maker():
    #* this function first checks is there a folder . if there is a folder then the function just skips
    #! BUT THERE İS NOT A FOLDRER THEN:
    #* creates a folder. and creates two file in this folder.
    #* first one of created files for Temporary file second one for user datas
    #* first file is txt file second is json 

   

    def inner(path):
        #* folder maing
        os.mkdir(path +"/json_files")

        #* files making
        with open(path +"/json_files/temp_file.txt","a",encoding="utf-8") as file:
            pass

        with open(path +"/json_files/user_datas.json","a",encoding="utf-8") as file:
            js.dump({'active_profile':None},file,indent=4,sort_keys=False)

    #* if there is a folder then app is skiping the inner function 
    if os.path.exists("json_files"):
        pass
    else:
        inner(main_path)

def save_deleter():
    #*this function for log outing

    data_file_path = main_path + "/json_files/user_datas.json"
    with open(data_file_path,"r+",encoding="utf-8") as file:
        datas = js.load(file)
    datas["active_profile"] = None
    with open( data_file_path  , "w" , encoding="utf-8") as file:
        js.dump(datas ,file,indent=4,sort_keys=False)


def user_data_taker():
    data_file_path = main_path + "/json_files/user_datas.json"
    temp_file_path = main_path + "/json_files/temp_file.txt"

    with open(data_file_path , "r+", encoding="utf-8") as file:
        datas = js.load(file)
    
    if datas["active_profile"] == None:
        while True:
            #* if user changes the texts in the file then the app Warns the user
            try:
                #* user datas taking
                with open(temp_file_path ,"w",encoding="utf-8") as file:
                    file.write("username: \nemail: \npassword: \n\n\nwhen you have finished then press ctrl+s after close the temp_file and write 'q' into the terminal" )
                os.system(temp_file_path)
                quit_taker()

                
                #* user datas saving
                with open(temp_file_path ,"r+",encoding="utf-8") as file:
                    lines = file.readlines()[:3]

                username = lines[0].split(": ")[1].strip(" ").strip("\n")
                email = lines[1].split(": ")[1].strip(" ").strip("\n")
                password = lines[2].split(": ")[1].strip(" ").strip("\n")

                datas["active_profile"] = {"username":username,"email":email,"password":password}

                with open(data_file_path ,"w",encoding="utf-8") as file:
                    js.dump(datas , file , indent=4 , sort_keys=False) 
            except:
                print("PLEASE DONT CHANGE ANY TEXT İN THE TEMP FİLE")
            else:
                break
    else:
        raise Exception("already there is a user profile")
#* panelde login seçeneği seçilirse bu fonksiyon çaışıcak
#* hata da gelse gelmesede sonuç olarak user data json dosyası okunacak ve veriler bota gönderilecek
#* ve bu json dosyasında active_profile varsa botun is_log_in attribute'u  True olucak.
#* kullanıcıda zorunu olarak 



# save_deleter()
# user_data_taker()


def data_writer(str_data = None , dict_data = None):
    #* eğerki gelen veri dicti ise ilk önce json modülü ile indent verilir ardından txt dosyasına yazdırılır
    #* gelen veri str ise direk txt dosyasına yazdırılacak

    pass


# x_bot = bot()

