import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
from tkinter import *
import datetime
import time
import winsound
from threading import *

import pyjokes

import pywhatkit
import wikipedia

listm={'hi': 'hello!!','hey':'hi',
       'Hello':'Hola',
       'Good morning':'A very good morning','how are you?':'as cool as ice...',
       'good evening':'good evening..chai pee liya?',
       'ok thank you':'My pleasure ',
       'you are a sweet heart neon thanks':'thank you have a nice day',
       'when is your birthday?':'may 6th 2021!! ',
       'Can you help me do simple math?': 'yeah sure!!',
       'cool':'bye!!',
       'Can you help me?': 'obviously,,please tell'}






    
n=0
text=input('')
for n in range(0,100):
    def get_key(text):
        for key,value in listm.items():
            if text == key:
                return value
               
        return "please re enter !"
    print(get_key(text))

    
    print('hey!! I am neon how can i help you today?? I can do so many things-->')
    print('1.send an email?')
    print('2.set an alarm?')
    print('3.Send a whatsapp message')
    print('4.tell you a joke?')
    print('5.play a content from youtube?')
    print('6.Wiki search')
    print('7.tell you the exact time?')
    print('8. exit')
    ch=input()
    if ch=='1':
        
        listener = sr.Recognizer()
        engine=pyttsx3.init()
        email_list ={'aishwarya': 'aishunagesh79@gmail.com','bhavana': '1JT18CS013@jyothyit.ac.in',
            'anushree': '1JT18CS011@jyothyit.ac.in','arpita': '1JT18CS012@jyothyit.ac.in','vaishnavi':'1JT18CS059@jyothyit.ac.in' }

        def talk(text):
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()
        def get_info():
            try:
                with sr.Microphone() as source:
                    print ('listening.....')
                    voice = listener.listen(source)
                    info = listener.recognize_google(voice)
                    print(info)
                    return info.lower()
            except:
                pass
        def send_email(reciever,subject,message):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('aishunagesh12344@gmail.com', 'AISHU12344')
            email=EmailMessage()
            email['from']='aishunagesh12344@gmail.com'
            email['to']= reciever
            email['subject']=subject
            email.set_content(message)
            server.send_message(email)

        def get_email_info():
            talk('kindly specify the destination address')
            name=get_info()
            reciever = email_list[name]
            print(reciever)
            talk('what is the subject?')
            subject = get_info()
            talk( 'what is the body of the email')
            message= get_info()
            send_email(reciever,subject,message)
        get_email_info()
    elif ch=='2':
        root = Tk()


        root.geometry("400x200")



        def Threading():
            t1 = Thread(target=alarm)
            t1.start()


        def alarm():

            while True:

                set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"


                time.sleep(1)


                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                print(current_time, set_alarm_time)


                if current_time == set_alarm_time:
                    print("Time to Wake up")
                    engine=pyttsx3.init()
                    def talk(text):
                        voices = engine.getProperty('voices')
                        engine.setProperty('voice', voices[1].id)
                        engine.setProperty('voice', voices[1].id)
                        engine.say(text)
                        engine.runAndWait()

                    for i in range(0,9):
                            talk('get up get up time is up  !!')
                    talk('good morning ,,,have a nice day!!')




        Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
        Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

        frame = Frame(root)
        frame.pack()

        hour = StringVar(root)
        hours = ('00', '01', '02', '03', '04', '05', '06', '07',
                 '08', '09', '10', '11', '12', '13', '14', '15',
                 '16', '17', '18', '19', '20', '21', '22', '23', '24'
                 )
        hour.set(hours[0])

        hrs = OptionMenu(frame, hour, *hours)
        hrs.pack(side=LEFT)

        minute = StringVar(root)
        minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
                   '08', '09', '10', '11', '12', '13', '14', '15',
                   '16', '17', '18', '19', '20', '21', '22', '23',
                   '24', '25', '26', '27', '28', '29', '30', '31',
                   '32', '33', '34', '35', '36', '37', '38', '39',
                   '40', '41', '42', '43', '44', '45', '46', '47',
                   '48', '49', '50', '51', '52', '53', '54', '55',
                   '56', '57', '58', '59', '60')
        minute.set(minutes[0])

        mins = OptionMenu(frame, minute, *minutes)
        mins.pack(side=LEFT)

        second = StringVar(root)
        seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
                   '08', '09', '10', '11', '12', '13', '14', '15',
                   '16', '17', '18', '19', '20', '21', '22', '23',
                   '24', '25', '26', '27', '28', '29', '30', '31',
                   '32', '33', '34', '35', '36', '37', '38', '39',
                   '40', '41', '42', '43', '44', '45', '46', '47',
                   '48', '49', '50', '51', '52', '53', '54', '55',
                   '56', '57', '58', '59', '60')
        second.set(seconds[0])

        secs = OptionMenu(frame, second, *seconds)
        secs.pack(side=LEFT)

        Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=20)
        exit_button = Button(root, text="Exit", command=root.destroy)
        exit_button.pack(pady=20)

        root.mainloop()
    elif ch=='3':
        contact=input("who is the reciever? please enter the user's number")
        msg=input('enter the message')
        print('enter the hours as in 6 if you want to schedule it to be sent at 6.30')
        hour = int(input())

        print('enter the minutes as in 30 if you want to schedule it to be sent at 6.30')
        mini= int(input())

        pywhatkit.sendwhatmsg(contact, msg, hour , mini)

        
    elif ch=='4':

        listener = sr.Recognizer()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        
       


        def talk(text):
            engine.say(text)
            engine.runAndWait()

        def take_command():
            try:
                with sr.Microphone() as source:
                    print('listening...')
                    voice = listener.listen(source)
                    command = listener.recognize_google(voice)
                    command = command.lower()
                    print(command)
            except:
                pass
            return command
        def joke():
       
            
           
            
            talk(pyjokes.get_joke())
        joke()

        
        
    elif ch=='5':
        
    
       


        def play():
            print('what do you want me to play?')
            song=input('')
            print('playing ' + song)
            pywhatkit.playonyt(song)
        play()
               
        
        
    elif ch=='6':
        print('what do you want to search?')
        pop=input('')
        info = wikipedia.summary(pop, 1)
        print(info)

        
    elif ch=='7':
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        
    elif ch=='8':
        print('bye')
        
        exit(0)
    else:
        exit(0)

    







#get_email_info()


#root.mainloop()





