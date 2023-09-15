import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import random
import smtplib
import psutil #for cpu and battery details
import pyautogui #pip install pyautogui for taking screenshots
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
    print("I am Hazel, your personal voice assistant. Please tell me how may I help you")
    speak("I am Hazel, your personal voice assistant. Please tell me how may I help you")
           

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)  
        speak("Say that again please...")  
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shashank.sahu15729@gmail.com', 'xxxxxxxxxxxxx')
    server.close()

def screenshot():
    img=pyautogui.screenshot()
    img.save('C:\\Users\\Lenovo\\Pictures\\Screenshots\\ss.png')

def joke():
    speak('Here is a joke')
    print('Here is a joke')
    speak(pyjokes.get_joke())

def cpu():
    usage=str(psutil.cpu_percent())
    print('CPU is at '+usage)
    speak('CPU is at '+usage)
    battery=psutil.sensors_battery
    print('Battery is at'+str(battery))
    speak('Battery is at' + str(battery))
    #speak(battery.percent)   




if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            print("Opening youtube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            print("Opening google")

        elif 'open spotify' in query:
            webbrowser.open("spotify.com")  
            print("Opening spotify") 


        elif 'play songs' in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir,random.choice(songs)))

        elif 'tell me a joke' in query:
            joke()
            
        elif 'take screenshots' in query:
            screenshot()
            print('Taking screenshot')
            speak('Done')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open word' in query:
            speak('Opening MS word')
            path="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(path)

        elif 'write a note' in query:
            print('what should I write?')
            speak('What should I write?')
            notes=takeCommand()
            file=open('notes.txt','w')

        elif 'locate' in query:
            query=query.replace('where is','')
            location=query
            print('User asked to locate'+location)
            speak('Here is'+location)
            webbrowser.open_new_tab('https://www.google.com/maps/place/'+location)
            
        elif 'cpu' in query:
            cpu()


        elif 'stop' in query:
            speak('Exiting Hazel')
            quit()

        elif 'email to shashank' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "shashank.sahu3110@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                print("Sorry. I am not able to send this email") 
                speak("Sorry. I am not able to send this email")    
