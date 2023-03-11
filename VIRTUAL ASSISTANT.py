

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import smtplib
from PyDictionary import PyDictionary
import pytrends
import requests
from bs4 import BeautifulSoup
import proverb
from tkinter import messagebox, filedialog
from tkinter.ttk import*
from time import strftime




from pytube import YouTube
import urllib3
from translate import Translator
import random
import webbrowser
import gnewsclient
import os
import mysql.connector
from tkinter import*
from tkinter.scrolledtext import *

from tkinter import messagebox
from deep_translator import GoogleTranslator



#sql connecti
'''sql=mysql.connector.connect(host="localhost",user="root",password="pugazhmukilansql",database="virtual_assistant")'''

    
#audio
engine = pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)

def talk(auido):
    engine.say(auido)
    engine.runAndWait()
    
    
# window tkinter
root=Tk()
root.geometry("730x920")
root.title("virtual assistance")
root.resizable(0,0)
root.config(bg="black")

#main title label

Label(root,text="VIRTUAL ASSISTANT",bg="darkcyan",fg="white",font="arial 18 bold",width=70).pack()

def greeting():
    CurrentHour= int(datetime.datetime.now().hour)
    if CurrentHour >= 0 and CurrentHour < 12:
        talk('Good Morning!')
        print("GOOD MORNING!")
        
    elif CurrentHour >= 12 and CurrentHour < 18:
        talk('Good Afternoon!')
        print("GOOD AFTERNOON!")
        
    elif CurrentHour >= 18 and CurrentHour != 0:
        talk('Good Evening!')
        print("GOOD EVENING!")
        
greeting()
 ###### help #####3

def help():
    l=["this virtual assistant can do numerous things such as: ","tell you meaning for a word   :   eg:'meaning of personification'","tell you the distance between two place  :   eg: ' distance between chennai and mumbai'"
    ,"play you tube videos   :   eg: 'playing drawing videos in you tube'","helps to order things in amazon   :   eg : 'order mobile phones' ","can send automated whatsapp messages and e mails ",
    "will give you information about the thing you asl   :   eg : 'what is computer or how to make good study plan'","will give you daily news by clicking the button in the top 'news'",
    "will show you the direction for the partivcular place  :  eg :'take me to delhi' ","will open the website you want  :   eg : 'open youtube'","will show you the nearest gas station and restarunts"
    ]
    p=[]
    for i in l:
        p.append(i+"\n\n")

    w=Tk()
    w.geometry("730x920")
    w.title("virtual assistance user manual  window")
    w.resizable(0,0)
    w.config(bg="black")
    text = ScrolledText(w, width=80, height=55, wrap=WORD,font="arial 10 bold") # create text zone
    text.place(x=13,y=230) # pack it in the entire window
    text.insert(1.0,p)
Button(root,text="manual",fg="black",bg="cyan",font="arial 10 bold",width="10",command=help).place(x=240,y=103)
        

#####google####
def google():
    try:
        print("-------------------------")
        print("opening google")
        print("-------------------------")
        talk("opening google")
        webbrowser.open("www.google.co.in")
    except:
        talk("can't able to open google")
        print("can't able to open google")
        
Button(root,text="GOOGLE",fg="black",bg="cyan",font="arial 10 bold",width="10",command=google).place(x=20,y=60)


######whatsapp###
def whatsapp():
    win=Tk()
    win.geometry("500x400")
    win.title("whatsapp sender")
    win.config(bg="black")
    win.resizable(0,0)
    label1=Label(win,text="WHATSAPP SENDER",fg="black",bg="cyan",font="arial 10 bold",width=50)

    label1.pack()
    
    enumber=Entry(win,width=40)
    enumber.place(x=170,y=50)
    label2=Label(win,text="enter number with\n country code \n eg(+91xxxxxxxxxx)",font="arial 8 bold", fg="black",bg="cyan",)
    
    label2.place(x=10,y=40)
    
    emessage=Entry(win,width=50)
    emessage.place(x=160,y=100)
    Label(win,text="message",font="arial 10 bold", fg="black",bg="cyan",).place(x=10,y=100)
    
    ehour=Entry(win,width=50)
    ehour.place(x=160,y=145)
    Label(win,text="enter hours\n (railway time)",font="arial 9 bold", fg="black",bg="cyan",).place(x=10,y=140)
    
    eminutes=Entry(win,width=40)
    eminutes.place(x=160,y=195)
    Label(win,text="enter the minutes\n (railway time)",font="arial 9 bold", fg="black",bg="cyan",).place(x=10,y=190)
     
    def send():
        re=Label(win,text="your message will be sent in few seconds",fg="black",bg="yellow",)
        re.place(x=100,y=280)
        root.after(2000, re.destroy)
        
        try:
            pywhatkit.sendwhatmsg(enumber.get(), emessage.get(), int(ehour.get()), int(eminutes.get()))
            re1=Label(win,text="your message has been sent successfully!",fg="black",bg="yellow",)
            re1.place(x=100,y=280)
            root.after(2000, re1.destroy)
        except:
            re2=Label(win,text="oops! message cannot be sent ...kindly check your internet",fg="black",bg="yellow",)
            re2.place(x=100,y=280)
            root.after(3000, re2.destroy)
          

        
        
    Button(win,text="SEND",fg="white",bg="green",font="arial 10 bold",command=send).place(x=200,y=230)

Button(root,text="WHATSAPP",fg="black",bg="cyan",font="arial 10 bold",width="10",command=whatsapp).place(x=150,y=60)

####news####
def newsall():
    def newssports():
        
        win=Tk()
        
        win.geometry("740x860")
        win.resizable(0,0)
        win.config(bg="lightblue")
        win.title("NEWS")
        Label(win,text=" SPORTS NEWS",font="arial 30 bold",bg="black",fg="white",width=500).pack()
        def cricket():
            url='https://sportstar.thehindu.com/'+"cricket"
            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')
            headlines = soup.find('body').find_all('h2')
            count=0
            for x in headlines:
                l=[]      
                count=0 
                nu=1     
                for x in headlines:
                                
                    l.append("\n"+str(nu)+" : "+str(x.text.strip())+"\n")
                    nu+=1
                        
                    count=count+1
                    if count==10:
                        break
                
            print(l)
            label1=Label(win,text="CRICKET NEWS",bg="green",fg="white",font="arial 13 bold",width="60")
            label1.place(x=30,y=210)
            """Label(root,text=i+"\n",font="arial 15 bold",bg="white",fg="black",height=30).place(x=4,y=250)"""
            text = ScrolledText(win, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
            text.place(x=18,y=260) # pack it in the entire window
            text.insert(1.0, l)
        
                
            
        
        def football():
            url='https://sportstar.thehindu.com/'+"football"
            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')
            headlines = soup.find('body').find_all('h2')
            count=0
            for x in headlines:
                l=[]      
                count=0 
                nu=1     
                for x in headlines:
                                
                    l.append("\n"+str(nu)+" : "+str(x.text.strip())+"\n")
                    nu+=1
                        
                    count=count+1
                    if count==10:
                        break
                    
            print(l)

            
                    
            label1=Label(win,text="FOOTBALL NEWS",bg="green",fg="white",font="arial 13 bold",width="60")
            label1.place(x=30,y=210)       
            """Label(root,text=i+"\n",font="arial 15 bold",bg="white",fg="black",height=30).place(x=4,y=250)"""
            text = ScrolledText(win, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
            text.place(x=18,y=260) # pack it in the entire window
            text.insert(1.0, l)

        def tennis():
            url='https://sportstar.thehindu.com/'+"tennis"
            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')
            headlines = soup.find('body').find_all('h2')
            count=0
            for x in headlines:
                l=[]      
                count=0 
                nu=1     
                for x in headlines:
                                
                    l.append("\n"+str(nu)+" : "+str(x.text.strip())+"\n")
                    nu+=1
                        
                    count=count+1
                    if count==10:
                        break
                    
            print(l)

            
                    
            label1=Label(win,text="TENNIS NEWS",bg="green",fg="white",font="arial 13 bold",width="60")
            label1.place(x=30,y=210)       
            """Label(root,text=i+"\n",font="arial 15 bold",bg="white",fg="black",height=30).place(x=4,y=250)"""
            text = ScrolledText(win, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
            text.place(x=18,y=260) # pack it in the entire window
            text.insert(1.0, l)

        def basketball():
            url='https://sportstar.thehindu.com/'+"basketball"
            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')
            headlines = soup.find('body').find_all('h2')
            count=0
            for x in headlines:
                l=[]      
                count=0 
                nu=1     
                for x in headlines:
                                
                    l.append("\n"+str(nu)+" : "+str(x.text.strip())+"\n")
                    nu+=1
                        
                    count=count+1
                    if count==10:
                        break
                    
            print(l)

            
                    
            label1=Label(win,text="BASKETBALL NEWS",bg="green",fg="white",font="arial 13 bold",width="60")
            label1.place(x=30,y=210)       
            """Label(root,text=i+"\n",font="arial 15 bold",bg="white",fg="black",height=30).place(x=4,y=250)"""
            text = ScrolledText(win, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
            text.place(x=18,y=260) # pack it in the entire window
            text.insert(1.0, l)


        bcricket=Button(win,text="CRICKET",bg="orange",fg="black",font="arial 9 bold",width=20,command=cricket)
        bcricket.place(x=61,y=150 ) 
        bfootball=Button(win,text="FOOTBALL",bg="orange",fg="black",width=20,font="arial 9 bold",command=football)
        bfootball.place(x=203,y=150 )
        btennis=Button(win,text="TENNIS",bg="orange",fg="black",width=20,font="arial 9 bold",command=tennis)
        btennis.place(x=352,y=150 )
        bbasketball=Button(win,text="BASKETBALL",bg="orange",fg="black",width=20,font="arial 9 bold",command=basketball)
        bbasketball.place(x=494,y=150 )



   
    
    def news():
    
        
        """city=input("enter the city name:")"""
        city=Entry(root1,width=80,)
        city.place(x=180,y=150)
        Label(root1,text="city name",font="arial 15 bold",bg="orange",fg="white").place(x=50,y=150)
        

        
        line=Entry(root1,width=80,)
        line.place(x=180,y=190)
        Label(root1,text="no.of lines",font="arial 15 bold",bg="orange",fg="white").place(x=50,y=190)
                

        
        
            
                
        def getnews():
            try:
                url='https://timesofindia.indiatimes.com/city/'+city.get()
                response = requests.get(url)

                soup = BeautifulSoup(response.text, 'html.parser')
                headlines = soup.find('body').find_all('figcaption')
                
                l=[]      
                count=0 
                nu=1     
                for x in headlines:
                            
                    l.append("\n"+str(nu)+" : "+str(x.text.strip())+"\n")
                    nu+=1
                    
                    count=count+1
                    if count==int(line.get()):
                        
                    
                        break

                print(l)
                
                
                
                for i in l: 
                    
                
                    """Label(root,text=i+"\n",font="arial 15 bold",bg="white",fg="black",height=30).place(x=4,y=250)"""
                    text = ScrolledText(root1, width=70, height=30, wrap=WORD,font="arial 10 bold") # create text zone
                    text.place(x=18,y=260) # pack it in the entire window
                    text.insert(1.0, l)

            except:
                    text = ScrolledText(root1, width=70, height=30, wrap=WORD,font="arial 10 bold") # create text zone
                    text.place(x=18,y=260) # pack it in the entire window
                    text.insert(1.0, "can't able to get the news for this city ")
                
        Button(root1,text="DONE",font="arial 10 bold",fg="white",bg="green",command= getnews).place(x=350,y=220)

            
        


    root1=Tk()
    root1.geometry("700x790")
    root1.resizable(0,0)
    root1.config(bg="lightblue")
    root1.title("NEWS")
    Label(root1,text="NEWS",font="arial 30 bold",bg="black",fg="white",width=500).pack()
    Button(root1,text="SPORTS NEWS",font="arial 10 bold",fg="white",bg="orange",padx=2,command= newssports).place(x=70,y=70)
    Button(root1,text="GENERAL NEWS",font="arial 10 bold",fg="white",bg="orange",padx=2,command=news ).place(x=500,y=70)

Button(root,text="NEWS",font="arial 10 bold",fg="black",bg="cyan",width=10 ,command=newsall).place(x=570,y=60)


#########time####################
'''time = datetime.datetime.now().strftime('%I:%M %p')
Label(root,text="TIME : "+time,font="arial 10 bold",bg="black",fg="white").place(x=25,y=110)'''
def time():
    string=strftime("%H:%M:%S:%p")
    label.config(text="TIME : "+string)
    label.after(1000,time)
     
label=Label(root,font=("ds-digital bold",10),background="black",foreground="white")
label.place(x=25,y=110)
time()

###########date##################
date = datetime.datetime.now().strftime("%b %d %Y")
Label(root,text="DATE : "+date,font="arial 10 bold",bg="black",fg="white").place(x=560,y=110)

#############translator###################
def trans():
    def language():
        langtext=entrytext.get()
    
        
        lang=entrylang.get()
        
            
       
        
        translation = GoogleTranslator(source='auto', target=lang).translate(langtext)
        a=translation

        
        text = ScrolledText(root2, width=60, height=15, wrap=WORD,font="arial 10 bold") # create text zone
        text.place(x=20,y=340) # pack it in the entire window
        text.insert(1.0, a)
    
        
            

        

        

    root2=Tk()
    root2.title("translator")
    root2.geometry("620x700")
    root2.resizable(0,0)
    root2.config(bg="black")
    title=Label(root2,text="LANGUAGE TRANSLATOR",bg="lightblue",fg="black",width="30")
    title.config(font=("areial",30))
    title.pack()

    labelplain1=Label(root2,bg="black",fg="black",width=30)
    labelplain1.pack()
    labelentry=Label(root2,text="enter the text you want to translate",bg="yellow",fg="black",width=30)
    labelentry.config(font=("areial",10))
    labelentry.pack()
    labelplain2=Label(root2,bg="black",fg="black",width=30)
    labelplain2.pack()
    entrytext=Entry(root2,bg="lightblue",fg="black",width=40)
    entrytext.pack()
    labelplain3=Label(root2,bg="black",fg="black",width=30)
    labelplain3.pack()
    labellang=Label(root2,text="enter the language to which you want to translate",bg="yellow",fg="black",width=45)
    labellang.pack()
    labelplain4=Label(root2,bg="black",fg="black",width=30)
    labelplain4.pack()

    entrylang=Entry(root2,bg="lightblue",fg="black",width=40)
    entrylang.pack()
    labelplain5=Label(root2,bg="black",fg="black",width=30)
    labelplain5.pack()


    buttontrans=Button(root2,text="translate",bg="green",fg="white",width=15,command=language)
    buttontrans.pack()
    labelplain6=Label(root2,bg="black",fg="black",width=30)
    labelplain6.pack()
Button(root,text="TRANSLATOR",width=11,fg="black",bg="cyan",font="arial 10 bold",command=trans).place(x=430,y=60) 

###### weather#######

#########todolist###########
def todolist():
    
    def newTask():
        task = my_entry.get()
        if task != "":
            lb.insert(END, task)
            file=open("task.txt","a")
            file.write(task)
            file.write("\n")
            file.close()
            my_entry.delete(0, "end")
        else:
            messagebox.showwarning("warning", "Please enter some task.")

    def deleteTask():
        
        lb.delete(ANCHOR)
        g=lb.size()
        
        z=lb.get ( 0, last=g )
        file=open("task.txt","w")
        for i in z:
            file.write(i)
            
        
    
        
        
        
            
            
        file.close()
            
        
    ws = Tk()
    ws.geometry('500x450')
    ws.title('To-Do-List')
    ws.config(bg='black')
    ws.resizable(0,0)

    frame = Frame(ws)
    frame.pack(pady=20)

    lb = Listbox(
        frame,
        width=25,
        height=8,
        font=('Times', 18),
        bd=0,
        fg='black',
        highlightthickness=0,
        selectbackground='#a6a6a6',
        
        
    )
    lb.pack(side=LEFT, fill=BOTH)
    task_list = []
    file=open("task.txt","r")
    h=file.readlines()
    for i in h:
        task_list.append(i)
    file.close()

    

    for item in task_list:
        lb.insert(END, item)

    sb = Scrollbar(frame)
    sb.pack(side=RIGHT, fill=BOTH)

    lb.config(yscrollcommand=sb.set)
    sb.config(command=lb.yview)

    #entering the task
    my_entry = Entry(
            ws,
            font=('times', 24)
            )

    my_entry.pack(pady=20)



    addTask_btn = Button(
        ws,
        text='Add Task',
        font=('times 14'),
        bg='#c5f776',
        padx=12,
        pady=9,
        command=newTask
    )
    addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

    delTask_btn = Button(
        ws,
        text='Delete Task',
        font=('times 14'),
        bg='#ff8b61',
        padx=12,
        pady=9,
        command=deleteTask
    )
    delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


    ws.mainloop()

   

    
Button(root,text="To-Do-List",font="arial 10 bold",fg="black",bg="cyan",width=10 ,command=todolist).place(x=380,y=103)
#######email##############
def sendmail():
    root3=Tk()
    root3.geometry("650x550")
    root3.resizable(0,0)
    root3.title ("EMAIL SENDER")
    root3.config(bg="black")
    Label(root3,text="EMAIL SENDER",fg="black",bg="cyan",font="arial 15 bold",width=60).pack()  
    
      
    your_mailid=Entry(root3,width=50)
    your_mailid.place(x=210,y=60)
    Label(root3,text="your mail id",bg="cyan",fg="black",font="arial 10 bold",width=15).place(x=20,y=60)
    
    your_mail_password=Entry(root3,width=50)
    your_mail_password.place(x=210,y=120)
    Label(root3,text="your mail password",bg="cyan",fg="black",font="arial 10 bold",width=15).place(x=20,y=120)
    
    mail_sub=Entry(root3,width=50)
    mail_sub.place(x=210,y=170)
    Label(root3,text="mail subject",bg="cyan",fg="black",font="arial 10 bold",width=15).place(x=20,y=170)
    
    mail_content=Entry(root3,width=50)
    mail_content.place(x=210,y=230)
    Label(root3,text="content",bg="cyan",fg="black",font="arial 10 bold",width=15).place(x=20,y=230)
    
    recivers_mail_id=Entry(root3,width=50)
    recivers_mail_id.place(x=210,y=290)
    Label(root3,text="recivers mail id",bg="cyan",fg="black",font="arial 10 bold",width=15).place(x=20,y=290)
    

    
    def send():
        try:
            
            
            pywhatkit.send_mail(your_mailid.get(),your_mail_password.get(),mail_sub.get(),mail_content.get(),recivers_mail_id.get())
            Label(root3,text="message sent successfully !",bg="black",fg="green",font="arial 10 bold").place(x=200,y=400)
        except:
            Label(root3,text="cant able to send the message! \n        CHECK       \n  1) two step verification if off\n 2) inputs are correct",fg="red",bg="yellow",font="arial 10 bold",width=25).place(x=180,y=400)
    Button(root3,text="SEND",font="arial 10 bold",bg="green",fg="white",width=10,command=send).place(x=270,y=350)
    
    
Button(root,text="EMAIL",font="arial 10 bold",fg="black",bg="cyan",width=10 ,command=sendmail).place(x=290,y=60)

###running the main program####
def run_alexa():
    try:
        #play you tube videos
        if 'play'in command:
            song= command.replace('song','')
        
            
            text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
            text.place(x=13,y=230) # pack it in the entire window
            text.insert(1.0,"playing video")
            talk('playing video')
            pywhatkit.playonyt(song)

       
        #chatbot   
        elif "hey" == command:
            l="hey how is it going"
            print(l)
            text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
            text.place(x=13,y=230) # pack it in the entire window
            text.insert(1.0,l)            
            talk("hey how it is going")
        elif 'it is going well' == command:
            l="super"
            print(l)
            text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
            text.place(x=13,y=230) # pack it in the entire window
            text.insert(1.0,l) 
            print(l)      
            talk("super")

        elif 'thanks' == command:
            l="welcome"
                
            text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
            text.place(x=13,y=230) # pack it in the entire window
            text.insert(1.0,l)
            print(l)
            talk("welcome")
        elif 'thanks for this help' == command:
            l="welcome"
                
            text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
            text.place(x=13,y=230) # pack it in the entire window
            text.insert(1.0,l)
            print(l)
            talk("welcome")
        
        elif 'how are you' == command:
            l="i am fine thanks for asking"
            text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
            text.place(x=13,y=230) # pack it in the entire window
            text.insert(1.0,l) 
            print(l)       
            talk("i am fine thanks for asking")
            
        elif 'how about you' == command:
            l="i am fine thanks for asking"
            
            text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
            text.place(x=13,y=230) # pack it in the entire window
            text.insert(1.0,l)
            talk("i am fine thanks for asking")
            print(l)
        
        elif 'what is your name' == command:
            l='my name is jarvis what is your name'
            text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
            text.place(x=13,y=230) # pack it in the entire window
            text.insert(1.0,l)    
            talk("my name is jarvis what is your name")
            print(l)
                
        elif 'your name' == command:
            l="my name is jarvis"
            text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
            text.place(x=13,y=230) # pack it in the entire window
            text.insert(1.0,l)
            talk("my name is jarvis")
            print(l)

        elif 'my name is ' in command:
            l="oh fine nice name "
            text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
            text.place(x=13,y=230) # pack it in the entire window
            text.insert(1.0,l)
            talk("oh fine nice name")
            print(l)


            

            


            
            


        elif 'you are not replying properly' == command:
            l='sorry i will improve myself '
            text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
            text.place(x=13,y=230) # pack it in the entire window
            text.insert(1.0,l)
            talk("sorry i will imporve")
            print(l)
            
        elif 'why are you replying properly' == command:
            l='sorry i will improve myself '
            text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
            text.place(x=13,y=230) # pack it in the entire window
            text.insert(1.0,l)
            talk("sorry i will imporve")
            print(l)
            
        elif 'you are not replying well' == command:
            l='sorry i will improve myself '
            text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
            text.place(x=13,y=230) # pack it in the entire window
            text.insert(1.0,l)
            
        elif 'you need to be developed more' == command:
            l='thanks for this feedback'
            text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
            text.place(x=13,y=230) # pack it in the entire window
            text.insert(1.0,l)
            talk(l)
            print(l)
            
        elif 'you need to be develop more' == command:
            l='thanks for this feedback'
            text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
            text.place(x=13,y=230) # pack it in the entire window
            text.insert(1.0,l)
            talk(l)
            print(l)
            
        elif 'what can you do' in command:
            
            
            l=["actually i will do many things as i am programmed for that  the list are:\n","play you tube videos and songs\n","ask quetsions with what\n",
               "send automated whatsapp messages\n","say  you time and date\n","can say you some infromation from wikipedia\n",
               "can tell you todays headlines from times of india news\n","say meaning of the words you give\n"]
            text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
            text.place(x=13,y=230) # pack it in the entire window
            text.insert(1.0,l,)
            
       
        #open you tube
        elif "open youtube"  == command:
           
           
           



            try:
                text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
                text.place(x=13,y=230) # pack it in the entire window
                text.insert(1.0,"opening youtube")                
                talk("opening you tube")
                webbrowser.open("www.youtube.com")
            except:
                text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
                text.place(x=13,y=230) # pack it in the entire window
                text.insert(1.0,"can't able to open")
                print("can't able to open")
         #open google maps       
        elif "open googlemaps"  == command:
               
           
           



            try:
                text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
                text.place(x=13,y=230) # pack it in the entire window
                text.insert(1.0,"opening googlemaps")                
                talk("opening googlemaps")
                webbrowser.open("https://www.google.com/maps/")
            except:
                text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
                text.place(x=13,y=230) # pack it in the entire window
                text.insert(1.0,"can't able to open")
                print("can't able to open")
                talk("can't able to open")
        #open google classroom
        elif "open googleclassroom" == command:
               
           
           



            try:
                text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
                text.place(x=13,y=230) # pack it in the entire window
                text.insert(1.0,"opening googleclassroom")                
                talk("opening googleclassroom")
                webbrowser.open("https://edu.google.com/products/classroom/")
            except:
                text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
                text.place(x=13,y=230) # pack it in the entire window
                text.insert(1.0,"can't able to open")
                print("can't able to open")
        #open whatsapp web        
        elif "open whatsapp" == command:
               
           
           



            try:
                text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
                text.place(x=13,y=230) # pack it in the entire window
                text.insert(1.0,"opening whatsapp")                
                talk("opening whatsapp")
                webbrowser.open("https://web.whatsapp.com/")
            except:
                text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
                text.place(x=13,y=230) # pack it in the entire window
                text.insert(1.0,"can't able to open")
                print("can't able to open")
        #open gmail        
        elif "open gmail" == command:
               
           
           



            try:
                text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
                text.place(x=13,y=230) # pack it in the entire window
                text.insert(1.0,"opening gmail ")                
                talk("opening gmail")
                webbrowser.open("https://mail.google.com/mail/u/0/")
            except:
                text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
                text.place(x=13,y=230) # pack it in the entire window
                text.insert(1.0,"can't able to open")
                print("can't able to open")
        #order things in amazon
        elif "order"in command:
            word=command.replace('order' , " ")
            webbrowser.open("https://www.amazon.in/s?k="+word+"&ref=nb_sb_noss_2")
            
            text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
            text.place(x=13,y=230) # pack it in the entire window
            text.insert(1.0,"getting to the amazon")
            talk ("opening the respective page in amazon")
            
            
            
                
                
      
        #roll dice

        elif command =="roll a dice":
            dice=['1','2','3','4','5','6']
            throw=random.choice(dice)
            
            text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
            text.place(x=13,y=230) # pack it in the entire window
            text.insert(1.0,"the number you have got is",throw)
            print("the number you have got is ",throw)
            talk("the number you have got it ",throw)
        #time    
        elif 'time' in command:
            try:

                time = datetime.datetime.now().strftime('%I:%M %p')
                text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
                text.place(x=13,y=230) # pack it in the entire window
                text.insert(1.0,time)              
                
                talk(time)
               
               
                
            except:
                print("cant able to show the time sorry!...")
            
         #tells the meaning of the words   
        elif 'meaning of' in command:
            dict=PyDictionary()
            word=command.replace('meaning of' ,'')
            try:
                l=dict.meaning(word)
                text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
                text.place(x=13,y=230) # pack it in the entire window
                text.insert(1.0,l)
                
               
               
                
    
                
                
            except:
               
                text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold" ,fg="red") # create text zone
                text.place(x=13,y=230) # pack it in the entire window
                text.insert(1.0,"can't able to find the meaning of this word")


                    
                
       
            
        #distance between the two places
        elif "distance between" in command:
            try:
                word=command.replace(" ","+")
                word2="search?q="+word
                word3=word2.replace(" ","")
                            
                url="https://www.google.com/"+word3
                response = requests.get(url)

                soup = BeautifulSoup(response.content, 'html.parser')
                headlines = soup.find('body').find_all('span')
                l=[]
                for i in headlines:
                    

                    l.append(i.text.strip())
                print(l)
                p=[]
                
            
                text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
                text.place(x=13,y=230) # pack it in the entire window
                for i in l[9:12]:
                    text.insert(1.0,i)
                '''   p.append("\n"+i+"\n")
                print(p)'''
                
                
            except:
                l="can't able to find the distance....."
                text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
                text.place(x=13,y=230) # pack it in the entire window
                text.insert(1.0,"can't able to understand.....")
                talk(l)

        elif 'take me to'in command:
            try:
                word=command.replace("take me to","")
                word2="your location/"+word+"/"
                url="https://www.google.com/maps/dir/"+word2
                webbrowser.open(url)
                talk("taking you to",word)
            except:
                
                text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
                text.place(x=13,y=230) # pack it in the entire window
                text.insert(1.0," sorry can't able to direct you to the location")
                
                talk("sorry can't able to direct you to the location")


        elif 'whatsapp' == command :
            whatsapp()

        elif "news"  == command:
            newsall()

        elif "email"  == command:
            sendmail()

        elif "translator" == command:
            trans()

        elif "to do list"  == command:
            todolist()
        elif "restaurants near me"  in command:
            try:
                text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
                text.place(x=13,y=230) # pack it in the entire window
                text.insert(1.0,"showing the restaurants near you")                
                talk("showing the restaurants near you")
                webbrowser.open("https://www.google.com/maps/search/Restaurants/data=!3m1!4b1")
            except:
                text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
                text.place(x=13,y=230) # pack it in the entire window
                text.insert(1.0,"can't able to open")
                print("can't able to open")
 
        elif "hotels near me"   in command:
            try:
                text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
                text.place(x=13,y=230) # pack it in the entire window
                text.insert(1.0,"showing the hotels near you")                
                talk("showing the hotels near you")
                webbrowser.open("https://www.google.com/maps/search/Hotels/data=!4m2!2m1!6e3")
            except:
                text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
                text.place(x=13,y=230) # pack it in the entire window
                text.insert(1.0,"can't able to open")
                print("can't able to open")

        elif "gas near me" in command:
            try:
                text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
                text.place(x=13,y=230) # pack it in the entire window
                text.insert(1.0,"showing the gas near you")                
                talk("showing the gas near you")
                webbrowser.open("https://www.google.com/maps/search/Gas/data=!3m1!4b1")
            except:
                text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
                text.place(x=13,y=230) # pack it in the entire window
                text.insert(1.0,"can't able to open")
                print("can't able to open")

        #accessing the to do list through command
        

        
       


        #gives information
        elif  'who is' or'what is' or'want info about' in command:

            try:
                url="https://www.google.com/search?q="+command
                response = requests.get(url)

                soup = BeautifulSoup(response.text, 'html.parser')
                temp = soup.find("body").find_all("li")
                l=[]
                for i in temp:
                    a=i.getText()

                    l.append(a)

                a=[]

                for j in l[8::]:
                    a.append(j)
                    a.append("\n")

                
                if a==[]:
                    #trying anither method to get the information

                    #note some problem inthis code need to checked
                    url="https://www.google.com/search?q="+command
                    response = requests.get(url)

                    soup = BeautifulSoup(response.text, 'html.parser')
                    temp = soup.find("body").find_all("span")
                    '''temp1=temp.find(_class="hgKElc")'''
                    d=[]
                    for i in temp:
                        a=i.getText()

                        d.append(a)

                    g=[]

                    for j in d:
                        g.append(j)
                        g.append("\n")
                        #printing the text
                    '''g=temp.getText()'''

                    text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold",fg="black") # create text zone
                    text.place(x=13,y=230) # pack it in the entire window
                    text.insert(1.0,g)
                    print("second attempt")
                    print(g)

                    if g==[]:
                        #wikipedia search inforamation
                        io= command.replace('who is'and'want info about'and'what is','')
                                
                                
                            
                        spe = wikipedia.summary(io, sentences = 10)
                        text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold",fg="black") # create text zone
                        text.place(x=13,y=230) # pack it in the entire window
                        text.insert(1.0,spe)
                        print("wiki attempt") 
                        print(spe)  
                    else:
                        pass                         



                            
                           
                    
                        
                    '''pywhatkit.info(io)'''
                else:
                    text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold",fg="black") # create text zone
                    text.place(x=13,y=230) # pack it in the entire window
                    text.insert(1.0,a)
                    print(a)
            except:
                target1 = io

                                
                text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold",fg="red") # create text zone
                text.place(x=13,y=230) # pack it in the entire window
                text.insert(1.0,"directing to the respective page for you search")
                pywhatkit.search(target1)



  

            
     
                

        else:
            l="can't able to understand....."
            text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
            text.place(x=13,y=230) # pack it in the entire window
            text.insert(1.0,"can't able to understand command.....")
            talk(l)
            
    except:
        l="can't, able to understand....."
        text = ScrolledText(root, width=75, height=30, wrap=WORD,font="arial 10 bold") # create text zone
        text.place(x=13,y=230) # pack it in the entire window
        text.insert(1.0,"can't able to understand.....")
        talk(l)       

       
           

            
                
                                
            
        







    

        
        
  
#command entry ways
#text input
def textcommand(*args):
    global command
    command=commandentry.get()
    Label(root,text=command,fg="black",bg="white",width=70,font="arial 10 bold").place(x=10,y=170)
   


    com=command
        
    
    print(command)
    run_alexa()
    commandentry.delete(0,END)
#speech input
def speak():
    try:
        listener= sr.Recognizer()
        
        with sr.Microphone() as source:
            print ("listening")
                        
            voice= listener.listen(source)
            global command
            c= listener.recognize_google(voice)
            command=c.lower() 
            Label(root,text=command,fg="black",bg="white",width=70,font="arial 10 bold").place(x=10,y=170)
            print(command)

        


       
            
        
            run_alexa()
    except:
        print("speech recogoniton failed")

#command entery
commandentry=Entry(root,width=70,font="arial 10 bold")

commandentry.bind("<Return>", textcommand)
commandentry.place(x=22,y=850,height=43)


#incon if the mic 
photo = PhotoImage(file = "mic.png")

Button(root,image=photo,bd=0,command=speak).place(x=660,y=840,height=61,width=62)  




        
        
            

#display command in the label


root.mainloop() 

