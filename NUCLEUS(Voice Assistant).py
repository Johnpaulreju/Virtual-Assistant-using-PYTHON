    #___________________________ modules used to creat the Assistant _______________________________

# this module is used to get the voice for the Assistant
import pyttsx3
# this module is used to send sms for security purpose
from twilio.rest import Client
# this module is used to recognise the user voice
import speech_recognition as sr
# this module is used to get access to social media like Whatsapp, Youtube and Etc.
import pywhatkit as kit
#this module is used to get time to do some work
import threading
# this module is used to get date & time
import datetime
# this module is used to search things in wikipedia
import wikipedia
# This module is used to open other browser instead of the default one
import webbrowser
# this module is used to get access the computer 
import os
# this module is used to draw any shape user want
import turtle
# this module is used to get random number or anything
import random
# this module is used to convert strings to Python datatypes
import json
# this module is used  to send HTTP requests using Python
import requests
# this module is used to run new applications
import subprocess
# this module is used to get jokes online
import pyjokes
# this module is used to store a list of email used to send E-mails
import smtplib
#this module is used to get basic information regarding any phonenumber
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
# this module is used to get access to online dictionary
from PyDictionary import PyDictionary
dictionary=PyDictionary()
# this module is used to open a provided URl
from urllib.request import urlopen 
# these three module are used to get access to the volume of the system
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from email.message import EmailMessage
import time
# here we can set the default browser for our assistant by selecting path
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

#engine that convert text to speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[2].id)
engine.setProperty('voices',voices[2].id)

#giving access to the speaker
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
   IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#for keep waiting
def background_calculation():
    # here goes some long calculation
    time.sleep(random() * 5 * 60)

def main():
    thread = threading.Thread(target=background_calculation)
    thread.start()

#giving access to send mail
def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "bcaproject2k21@gmail.com"
    msg['from'] = user
    password = "sirrfnmvsmgyycsq"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

#otp
onetimepass = random.randint(1111,9999)
#code not to change the name of assistant
def sec():    
    account_sid = 'AC96e4c1d4b2def1046a50ea8396942ffc'
    auth_token = 'a1b4e5d55cd50649796487ca17997a6d'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            body='****THREAT****----->\nThe user is trying to Change the assistant name\nThe otp to Change is ==>'+str(onetimepass),
            from_='+13344012740',
            to='+917742521023 '
        )
    print(message.sid)
    return

#to get the user name as the sir
def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("hello")
    speak(uname)
    speak("I am Your assistant! How Can I Help you Sir")
uname =("john")

#to wish the user according to the time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")
    elif hour>=0 and hour<18:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening sir")
    speak(" I am nucleus!  Speed 1 terahertz!  memory 1 zeta byte.! ")

#to take command from the user
def takeCommand():    
    
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
        print("say that again please...")
        return "None"
    return query
#providing security
def mainsec():
    speak("Sir can yu say the entry password")
    password=takeCommand()
    if password=="it's me":
        return
    elif password=="its me":
        return
    elif password=="it's me":
        return
    else:
        exit()
#giving default name to assistant
assname = ("nucleus") 

#----------------------------------calling the assistant--------------------------
if __name__ == "__main__":
    #starts with security
    mainsec()
    #starts with wishing
    wishMe()
    #after wishing calls user name
    username()
    while True:
    #if 2:
        #storing user said in lower case in query
        query = takeCommand().lower() 
        
        #code to search user said in wikipedia
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query= query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        
        #code to listen to music from computer
        elif 'play music' in query:
            n = random.randint(0,6)
            speak('Playing music...')
            music_dir = 'C:\\Users\\p c m\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[n]))
        
        #code to open YouTube
        elif  'youtube' in query:
            speak('searching in youtube...')
            query= query.replace("youtube", "")
            kit.playonyt("" + query)

        #code to get basic info of phNo.
        elif  'phone' in query:
            speak('Which number you want to search sir...')
            Num = takeCommand()
            speak('searching in N.I.A database Sir!...')
            ph = phonenumbers.parse("+91"+Num)
            ge = geocoder.description_for_number(ph, 'en')
            ca = carrier.name_for_number(ph, 'en')
            speak("phone number is from"+ge)
            speak("and carrier of phone is"+ca)
            print(geocoder.description_for_number(ph, 'en'))
            print(carrier.name_for_number(ph, 'en'))
            print(timezone.time_zones_for_number(ph))
        
        #code to talk to user, if user say fine or good
        elif  'fine' in query or "good" in query:
            speak('Thats great sir') 
        
        #code to cntrol volume of the system
        elif  'volume' in query:
            speak('Sir! Do you want to increase or decrease the volume')
            query = takeCommand()
            #code to increase volume
            if 'increase' in query or 'raise' in query:
                volume.SetMasterVolumeLevel(-0.0, None) #max volume
                speak("volume has been increased to max level sir!")
                speak("is that ok for you")
                query = takeCommand()
                if 'yes' in query or 'ya' in query or 'fine' in query or 'great' in query:
                    speak("ok sir!")
                elif 'no' in query or 'not that much' in query or 'nope' in query or 'decrease little bit' in query:
                    speak("volume has been decreased to 90 percent sir")
                    volume.SetMasterVolumeLevel(-2.0, None) #90% volume
                elif 'increase little bit' in query:
                    speak("sorry sir! volume can't be further increase")
                else:
                    speak("sir i'm not able to hear you so i'm not changing the volume further")
            #code to decrease volume
            elif 'decrease' in query or 'lower' in query:
                volume.SetMasterVolumeLevel(-12.0, None) #45% volume
                speak("volume has been decreased to 45 precent sir!")
                speak("is that ok for you")
                query = takeCommand()
                if 'yes' in query or 'ya' in query or 'fine' in query or 'great' in query:
                    speak("ok sir!")
                elif 'no' in query or 'not that much' in query or 'nope' in query or 'increase little bit' in query:
                    volume.SetMasterVolumeLevel(-8.0, None) #59% volume
                    speak("volume has been increased to 59 precent sir!")
                elif 'decrease little bit' in query:
                    
                    speak("sorry sir! volume cannot be decrease more than this level")
                else:
                    speak("sir i'm not able to hear you so i'm not changing the volume further")
            else:
                pass
        
        #code to talk to user, if user say hi, hello etc
        elif 'hello' in query or "hi" in query or "hey" in query or "hai" in query:
            speak('how are you')
        
        #code to send email
        elif 'email' in query:
            try:
                speak("Whom do you want to send Email sir")
                e_person = takeCommand()
                speak("What should I say?")
                content = takeCommand()    
                email_alert("MESSAGE FROM JOHN", ""+str(content), ""+str(e_person))
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")
        
        #code to talk to user, if user say how are you
        elif 'how are you' in query:
            speak("I am fine, Thank you")
        
        #code to search words in dictionary
        elif 'meaning' in query or 'what do you mean by' in query or 'dictionary' in query:
            speak("Which word do u want to find the meaning sir")
            query= str(takeCommand())
            dictionary=PyDictionary()          
            word = dictionary.meaning(query) 
            A=len(word)
            print(len(word))                
            print(word) 
            speak("the meaning  is" + str(word)) 
  
        #code to get the weather report of any place user want
        elif "weather" in query:
            api_key="1b2498d6cf39c59086eb63888e86fce7"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                R = (y["temp"]) - 273.15
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n Temperature in Celsius unit is " +
                      str(R) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description is " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n Temperature in Celsius unit is " +
                      str(R) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
    
        #code to get top 5 news
        elif "news" in query:
            try:
                url = ('https://newsapi.org/v2/top-headlines?''sources=bbc-news&''apiKey=968f006f678f4ae393ec3a3b04014ad7')
                response = requests.get(url)
                text = response.text
                my_json = json.loads(text)
                for i in range(0, 6):
                    speak(my_json['articles'][i]['title'] )
                    print(my_json['articles'][i]['title'] )
            except Exception as e:                 
                print(str(e))
        
        #code to send whatsapp message to anyone using voice
        elif 'message' in query:
            speak("you have to open the chrome to send message! Should i open the chrome for you")
            query = takeCommand()
            if "yes" in query or "yeah" in query or "open" in query:
                webbrowser.get(chrome_path).open("www.google.com" )
                speak("do you want to send someone individual or a group")
                query = takeCommand()
                if "individual" in query:
                    try:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        speak("whom do u want to send the message! tell me the number sir")
                        phno = takeCommand()
                        speak("what do you want me to send ")
                        message = takeCommand()
                        kit.sendwhatmsg("+91" +phno, "" +message,11,39 )
                        speak("message has been sent")
                    except Exception as e:
                        print(e)
                        speak("I am not able to send this message")  
                #elif "group" in query:
                    #try:
                        #speak("which group do u want me to send the message sir")
                        #group = takeCommand()
                        #speak("what do you want me to send ")
                        #message = takeCommand()
                        #kit.sendwhatmsg_to_group()
                        #speak("message has been sent")
                    #except Exception as e:
                        #print(e)
                        #speak("I am not able to send this message")
                else:
                    speak("i am not able to understand")
            else:
                speak("you will not be able to send message! sorry")

        #code to open google and search    
        elif 'google' in query:
            speak('opening google...')
            query= query.replace("google", "")
            kit.search("" + query)

        #code to listen joke from online
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        #code to talk to user, if user ask 'who am i'
        elif "who i am" in query:
            speak("If you talk then definately you are a human.")
 
        #code to talk to user'
        elif "why you came to world" in query:
            speak("Thanks to John. further It's a secret")
        
        #code to talk to user, if user ask about love
        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
        
        #code to mark or open any location from google map
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.get(chrome_path).open("https://www.google.co.in/maps/place/" + location )

        ##code to talk to user, if user ask 'who are you' 
        elif "who are you" in query:
            speak("I am your virtual assistant created by John")
        
        #code to recall assistant for the service
        elif "nucleus" in query:
            wishMe()
            speak("Ready for your service ")
            speak(uname)
        
        #code to talk
        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister john")  
        
        #code to write a note
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
        #code to show the saved note 
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r") 
            print(file.read())
            speak(file.read(6))
       
       #code to change the default name of the assistant
        elif "change name" in query:
            sec()
            speak("Can you please tell the otp you recived in authorized phone sir! ")
            
            aotp = takeCommand()
            if aotp==onetimepass:
                speak("O T P Verified sir")
                speak("you can change the name sir")
                assname=takeCommand()
                speak("Thanks for naming me")
            else:
                speak("unauthorized person detected")
                exit()
        
        #code to respone the user ask command
        elif "what is your name" in query or "What 's your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)
        
        #code to open stackoverflow
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        #code to ask the user if he/she want any help
        elif 'ok' in query:
            speak('Do you need any help sir')
        
        #code to do is the respone is no help
        elif 'no help' in query:
            speak('Do you want me to exit or quit')
            if 'ya' in query:
                exit()
        
        #code to draw shape for user
        elif 'draw' in query:
            speak('want do you want me to draw')
            speak('a square, a rectangle, a circle, a cylinder')
            query=takeCommand()
            if 'square' in query:
                turtle.forward(50)
                turtle.left(90)
                turtle.forward(50)
                turtle.left(90)
                turtle.forward(50)
                turtle.left(90)
                turtle.forward(50)
                turtle.left(90)
            elif 'rectangle' in query:
                turtle.forward(100)
                turtle.left(90)
                turtle.forward(50)
                turtle.left(90)
                turtle.forward(100)
                turtle.left(90)
                turtle.forward(50)
                turtle.left(90)
            elif 'circle' in query:
                r = 50
                turtle.circle(r)
            elif 'cylinder' in query:
                height = 200
                radius = 40
                turtle.forward(height)
                turtle.circle(radius)
                turtle.setheading(90)
                turtle.penup()
                turtle.forward(2*radius)
                turtle.pendown()
                turtle.setheading(180)
                turtle.forward(height)
                turtle.circle(radius, extent=180)  
                turtle.done()

        #code to hiberante the system    
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call(["shutdown", "/l"])

        #code to ask the assistant what is the time 
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is{strTime}")

        #code to off/exit the assistant services    
        elif "exit" in query or "quit" in query:
            speak('Have a nice day! sir')
            exit()
 