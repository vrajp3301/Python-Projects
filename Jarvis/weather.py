import speech_recognition as sr 
import pyttsx3  
from selenium import webdriver
from time import sleep
webdriver = webdriver.Chrome()
  
r = sr.Recognizer()  
   
def SpeakText(command): 
     
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 
  
def City():
    try: 
        SpeakText("Which city?")
    
        with sr.Microphone() as source2: 
            print("Listening...")
            audio2 = r.listen(source2) 
            MyText = r.recognize_google(audio2) 
            MyText = MyText.lower() 
            webdriver.get("https://www.weather-forecast.com/locations/"+MyText+"/forecasts/latest")
            SpeakText(str(webdriver.find_elements_by_class_name("b-forecast__table-description-content")[0].text))
            # SpeakText(MyText)
            # print("Did you say "+MyText) 
              
    except sr.UnknownValueError: 
        print("unknown error occured") 

def Search():
    
    SpeakText("Which Song?") #SELECTION OF SONG 
    with sr.Microphone() as source2: 
        print("Listening...") 
        audio2 = r.listen(source2) 
        MyText = r.recognize_google(audio2) 
        MyText = MyText.lower() 
        webdriver.get("https://www.youtube.com/results?search_query="+MyText)
        sleep(2)
        x = webdriver.find_element_by_class_name("style-scope ytd-video-renderer").click()
        sleep(2)

