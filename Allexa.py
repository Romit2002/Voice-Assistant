import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else :
        speak("good evening")
    speak("Hello Everyone I am Allexa")

def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
        

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query  


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'open google' in query:
            webbrowser.open('https://www.google.com/')

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        if 'wikipedia' in query:
            speak("Searching Results")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("Sir!! According to wikipedia")
            print(results)
            speak(results)

        elif 'i am sad' in query:
            speak("Playing Good songs to fresh your mind")    
            webbrowser.open("https://www.youtube.com/watch?v=N3yxZsSzbdc&list=RDN3yxZsSzbdc&start_radio=1")

        if 'open iiit kota website' in query:
            webbrowser.open("https://iiitkota.ac.in")
        elif 'who is romit' in query:
            print("Romit is an undergraduate student of Indian Institute of Information Technology Kota")
            speak("Romit is an undergraduate student of Indian Institute of Information Technology  Kota")