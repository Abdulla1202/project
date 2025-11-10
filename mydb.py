import json

class Database:
    def add_data(self , name,email,password):
        with open(r"F:\PYTHON VS\campusx\NlpApp\db.json","r") as rf:
            data = json.load(rf)

        
        if email in data:
            return 0
        else:
            data[email] = [name, password]  # ✅ dictionary
            with open(r"F:\PYTHON VS\campusx\NlpApp\db.json","w") as wf:
                json.dump(data,wf)
            return 1
        

    def check_user(self,email,password):
        with open(r"F:\PYTHON VS\campusx\NlpApp\db.json","r") as rf:
            data = json.load(rf)

        if email in data:
            if data[email][1] == password:
             return 1
            else:
             return 0  

        else:
           return 0      