


import os 
import json as js
from bot import bot
import time
main_path = os.getcwd()

def quit_taker() -> None:
    while True:
        try:
            inp = input("///:").strip(" ").lower()

            if inp != "q":
                raise Exception("please try again. you can only enter q")

        except Exception as error:
            print(error)
        else:
            break

def json_folder_maker() -> None:
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

def save_deleter() -> None:
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
                    file.write("NOTE: when you have finished then press ctrl+s after close the temp_file and write 'q' into the terminal\n\n\n")
                    file.write("username: \nemail: \npassword: " )
                os.system(temp_file_path)
                quit_taker()

                
                #* user datas saving
                with open(temp_file_path ,"r+",encoding="utf-8") as file:
                    lines = file.readlines()[-3:]

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
        raise Exception("already there is a user profile in the database")

def user_data_reader() -> list:
    data_file_path = main_path + "/json_files/user_datas.json"
    with open(data_file_path , "r+", encoding="utf-8") as file:
        datas = js.load(file)["active_profile"]
        
    return  [datas["username"],datas["email"],datas["password"]]

def data_writer(data) -> None:

    temp_file_path = main_path + "/json_files/temp_file.txt"

    if type(data) == str:

        with open(temp_file_path,"w",encoding="utf8") as file:
            file.write("NOTE: when you have finished then close the temp_file and write 'q' into the terminal\n\n")
            file.write("RESULT:\n")
            file.write(data + "\n")
        
        os.system(temp_file_path)
        quit_taker()            

    elif type(data) == dict:
        shaped_data = js.dumps(data,indent=4,sort_keys=False)
        with open(temp_file_path,"w",encoding="utf-8") as file:
            file.write("when you have finished then close the temp_file and write 'q' into the terminal\n\n")
            file.write("RESULT:\n")
            file.write(shaped_data)
            
        
        os.system(temp_file_path)
        quit_taker()            




#* first use try except block for functions because sometimes functions send error message. and this mesages should write to temp file