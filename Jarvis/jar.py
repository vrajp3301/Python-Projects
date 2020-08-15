import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pytautogui
from weather import City,Search

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!!")   

    else:
        speak("Good Evening Sir!!")  

    speak("Please tell me how may I help you?")       

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abc@gmail.com','') #sender-mail and password
    server.sendmail('xyz@gmail.com', to, content) #receiver-mail
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=10)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'please exit' in query :
            exit()

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        
        elif 'open netflix' in query:
            code = 'C:\\Users\\ADMIN\\Desktop\\Python\\netflix.py'
            os.startfile(code)

        elif 'open my twitter account' in query:
            code = 'C:\\Users\\ADMIN\\Desktop\\Python\\twitter.py'
            os.startfile(code)
        
        elif 'open twitter' in query:
            code = 'C:\\Users\\ADMIN\\Desktop\\Python\\Jarvis\\twitter_bot.py'
            os.startfile(code)
        elif 'take screenshot' in query:
            ss = pyautogui.screenshot()
            ss.save(r'C:\Users\ADMIN\Desktop\Python\screenshot.jpg')
            
        elif 'tell me weather' in query:
            City()
         
        elif 'play song on youtube' in query:
            Search()
            
        elif 'play music' in query:
            music_dir = 'F:\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[5]))
 
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'email to jack' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "abc@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")   
