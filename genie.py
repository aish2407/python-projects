import datetime
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say(' hi , i am your genie....')
engine.say(' whose command am i obeying today? ')
engine.runAndWait()


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
            if 'genie' in command:
                command = command.replace('genie', '')

                print(command)
    except:
        pass
    return command


def run_genie():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    if 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    if 'help me copy' in command:
        talk('sorry my sultaana ....i am a genie with ethics. and i will not help you at any cost !')
    if 'did god create you' in command:
        talk('NO i am created by 3 beautiful girls aishwarya, vaishnavi and keerthana ......')
    if 'joke' in command:
        talk(pyjokes.get_joke())
    if 'did you eat' in command:
        talk('so kind of you my sultana to think about me ....thank you .....the oppurtunity to serve you always makes me full.....')
    if 'vaishnavi' in command:
        talk(' hello vaishu ,thy wish is my command')
    if 'aishwarya' in command:
        talk(' hello aishu ,thy wish is my command')
    if 'kirthana' in command:
        talk(' hello keerthi ,thy wish is my command')
    else:
        talk('Please say the command ')


while True:
    run_genie()
