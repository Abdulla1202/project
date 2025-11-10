from  tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:

    def __init__(self):
        # create database object
        self.dbo = Database()
        self.apio = API()



        # login ka gui load krna 
        self.root = Tk() # gui ka object bna diya // gui banaya
        self.root.title("NLP Application")
        self.root.iconbitmap("campusx/resorses/abdulla.ico")
        self.root.geometry("350x600")
        self.root.config(bg="#574A47")
        self.login_gui()
        self.root.mainloop() # gui ko screen pe hold kr ke rakhta h  // gui screen pe rkha
    def login_gui(self):
       self.clear()
       haeding =  Label(self.root,text="NLP App")
       haeding.pack(pady=(20,20))
       haeding.config(font=("Courier",24,'bold'),bg="#574A47",fg="white")

       lable1 = Label(self.root,text="Enter Your Email")
       lable1.pack(pady=(10,10))
       self.email_entry = Entry(self.root,width=30)
       self.email_entry.pack(pady=(10,10),ipady=4)

       lable2 = Label(self.root,text="Enter Your Password")
       lable2.pack(pady=(10,10))
       self.password_entry = Entry(self.root,width=30, show="*")
       self.password_entry.pack(pady=(10,10),ipady=4)

       login_btn = Button(self.root,text="login", width=20,height=2, command = self.perform_login)
       login_btn.pack(pady=(20,20),ipady=2,ipadx=6)

       lable3 = Label(self.root,text="Not a user? Sign Up")
       lable3.pack(pady=(20,10))

       
       redirect_btn = Button(self.root,text="Register now" , command=self.register_gui)
       redirect_btn.pack(pady=(20,20))
        

    def register_gui(self):
       self.clear()
       haeding =  Label(self.root,text="NLP App")
       haeding.pack(pady=(20,20))
       haeding.config(font=("Courier",24,'bold'),bg="#574A47",fg="white")

       lable0 = Label(self.root,text="Enter Your Name")
       lable0.pack(pady=(10,10))
       self.name_entry = Entry(self.root,width=30)
       self.name_entry.pack(pady=(10,10),ipady=4)

       lable1 = Label(self.root,text="Enter Your Email")
       lable1.pack(pady=(10,10))
       self.email_entry = Entry(self.root,width=30)
       self.email_entry.pack(pady=(10,10),ipady=4)

       lable2 = Label(self.root,text="Enter Your Password")
       lable2.pack(pady=(10,10))
       self.password_entry = Entry(self.root,width=30, show="*")
       self.password_entry.pack(pady=(10,10),ipady=4)

       ragister_btn = Button(self.root,text="Ragister", width=20,height=2, command=self.perform_ragistetion)
       ragister_btn.pack(pady=(20,20),ipady=2,ipadx=6)

       lable3 = Label(self.root,text="Already a member")
       lable3.pack(pady=(20,10))

       
       redirect_btn = Button(self.root,text="Login now" , command=self.login_gui)
       redirect_btn.pack(pady=(20,20))
      


    def clear(self):
         #clear the screen of gui
        for i in self.root.pack_slaves():
            i.destroy()
    
    def perform_ragistetion(self):
        # fech data from the gui
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        response = self.dbo.add_data(name,email,password)

        if response:
           messagebox.showinfo("Success","user registered successfully")
        else:
              messagebox.showerror("Error","Email already exists")



    def perform_login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        response = self.dbo.check_user(email,password)

        if response:
           messagebox.showinfo("Success","Login successfully") 
           self.home_gui()
        else:
           messagebox.showerror("Error","Invalid email or password")    

               
    def home_gui(self):
        self.clear()
        haeding =  Label(self.root,text="NLP App")
        haeding.pack(pady=(20,20))
        haeding.config(font=("Courier",24,'bold'),bg="#574A47",fg="white")

        sentiment_btn = Button(self.root,text="Sentiment Analysis", width=20,height=2 , command=self.sentiment_gui)
        sentiment_btn.pack(pady=(20,20))

        ner_btn = Button(self.root,text="Named Entity Recognition", width=20,height=2)
        ner_btn.pack(pady=(20,20))

        emotion_btn = Button(self.root,text="Emotion Detection", width=20,height=2)
        emotion_btn.pack(pady=(20,20))

        logout_btn = Button(self.root,text="Logout", width=10,height=2, command=self.login_gui)
        logout_btn.pack(pady=(10,10))
   
    def sentiment_gui(self):
        self.clear()
        haeding1 =  Label(self.root,text="NLP App")
        haeding1.pack(pady=(30,30))
        haeding1.config(font=("Courier",24,'bold'),bg="#574A47",fg="white")

        haeding2 =  Label(self.root,text="Sentiment Analysis")
        haeding2.pack(pady=(10,10))
        haeding2.config(font=("Courier",14),bg="#574A47",fg="white")

        lable1 = Label(self.root,text="Enter Your Text")
        lable1.pack(pady=(10,10))

        self.sentiment_entry = Text(self.root,width=30,height=10)
        self.sentiment_entry.pack(pady=(10,10))

        analyze_btn = Button(self.root,text="Analyze Sentiment", width=20,height=2,command=self.analyze_sentiment)
        analyze_btn.pack(pady=(20,20),ipady=2,ipadx=6)

        self.sentiment_result = Label(self.root,text="",bg="#574A47",fg="white")
        self.sentiment_result.pack(pady=(10,10))
        self.sentiment_result.configure(font=("Courier",14))

        back_btn = Button(self.root,text="Back", width=20,height=2, command=self.home_gui)
        back_btn.pack(pady=(20,20),ipady=2,ipadx=6)


   # def analyze_sentiment(self):
      # text = self.sentiment_entry.get()
      # result = self.apio.sentiment_analysis(text)
      # print(result)

    def analyze_sentiment(self):
     text = self.sentiment_entry.get("1.0", "end-1c")
     result = self.apio.sentiment_analysis(text)
     self.sentiment_result.config(text=f"Sentiment: {result['sentiment']}")
    


    def ner_gui(self):
        self.clear()
        haeding1 =  Label(self.root,text="NLP App")
        haeding1.pack(pady=(30,30))
        haeding1.configure(font=("Courier",24,'bold'),bg="#574A47",fg="white")

        haeding2 =  Label(self.root,text="Named Entity Recognition")
        haeding2.pack(pady=(10,10))
        haeding2.configure(font=("Courier",14),bg="#574A47",fg="white") 


        lable1 = Label(self.root,text="Enter Your Text")
        lable1.pack(pady=(10,10))   

        self.ner_entry = Text(self.root,width=30,height=10)
        self.ner_entry.pack(pady=(10,10))

        analyze_btn = Button(self.root,text="Analyze NER", width=20,height=2)
        analyze_btn.pack(pady=(20,20))

        self.ner_result = Label(self.root,text="",bg="#574A47",fg="white")
        self.ner_result.pack(pady=(10,10))  

        back_btn = Button(self.root,text="Back", width=20,height=2, command=self.home_gui)
        back_btn.pack(pady=(20,20))


    def analyze_emotion(self):
     text = self.sentiment_entry.get("1.0", "end-1c")
     result = self.apio.emotion_detection(text)
     self.sentiment_result.config(text=f"Emotion: {result['emotion']}")
    







nlp = NLPApp()        