import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import urllib.request
import re
import calendar
import datetime


# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice
engine.setProperty('rate', 120)  # 1 for female and 0 for male voice



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    r.energy_threshold = 250
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didnt understand")
        return "None"
    return query


if __name__ == '__main__':

    speak("Amigo assistance activated ")
    # speak("How can i help you")
    while True:
        speak("How can i help you")
        query = take_command().lower()
        
        if 'wikipedia' in query:

            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif "who is" in query:
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)

        
        elif "can you do" in query:
            speak("here are some tasks that i can perform ")
            flag=0
            while True:
                if(flag==1):
                    break
                print("1.play songs on youtube\n2.open spotity\n3.open file explorer\n4.tell me current time\n5.show me calendar\n6.exit")
                speak("tell me the number of task you want to perform")
                query=take_command().lower()
                if(query=="first"):
                    speak("say the name of the song you want to play")
                    query=take_command().lower()
                    new_query=query.replace(" ","+")
                    html = urllib.request.urlopen("https://www.youtube.com/results?search_query={q}".format(q=new_query))
                    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                    webbrowser.open("https://www.youtube.com/watch?v={video}".format(video=video_ids[0]))
                    flag=1
                elif(query=="second"):
                    webbrowser.open("spotify.com")
                    flag=1
                elif(query=="third"):
                    os.startfile("c:")
                    flag=1
                elif(query=="fourth"):
                    now=datetime.datetime.now()
                    time=now.strftime("%H:%M:%S")
                    print(time)
                    speak(time)
                elif(query=="fifth"):
                    print(calendar.month(2022,11))
                    flag=1
                elif(query=="sixth" or query=="six"):
                    flag=1
                elif(query=="thank you"):
                    speak("my pleasure ")
                    exit(0)
                else:
                    speak("didnt understand say it again")


            # os.startfile(r"C:\Users\hp\OneDrive\Desktop\Aarambh-Hai-Prachand(PagalWorld).mp3")
        elif "hello" in query:
            speak("hey glad to hear this from you ,how can i help you")

        elif "open file manager" in query:
            speak("opening file manager")
            os.startfile("c:")
            
        elif 'who are you' in query:
            speak("I am Amigo developed by Ashish yadav ")
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")
        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")
        # elif 'open whatsapp' or 'whatsapp' in query:
        #      speak("opening whatsapp")
        #      webbrowser.open("https://www.whatsapp.com/")
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")
        elif 'thank you' in query:
            speak("my pleasure ")
            exit(0)