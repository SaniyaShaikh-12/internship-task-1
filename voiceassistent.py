#Create a custom voice assistant using Python to personalize and automate tasks according to your needs. 
# Python's versatility makes it an excellent choice for scripting and development, allowing you to build a voice assistant that can compete with the likes of Siri, 
# Alexa, and Google Assistant.



import speech_recognition as sr           #understand  voice 
import pyttsx3                           #Talk back to you         
import datetime                          # To get current time
import webbrowser                       #search the web

engine = pyttsx3.init()            # Start the speech engine
        
#Set voice (0 = male, 1 = female usually)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change index to switch voice  # 1 for female voice

def speak(text):
    engine.say(text)       # Queue up what to say
    engine.runAndWait()    # Speak it out loud

def greet_user():
    hour = datetime.datetime.now().hour     # Get current hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your assistant. How can I help you today?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')     #recognize_google() converts voice to text.
        print(f"User said: {query}") 
    except Exception as e:
        print("Say that again please...")
        return "None"                                                    #If there's an error or silence, it returns "None"
    return query.lower()

def perform_task(query):                                        #we can add more conditions for: Opening specific websites,Playing music,Reading news Or connecting with other Python scripts


    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("https://www.youtube.com")

    elif 'open google' in query:
        webbrowser.open("https://www.google.com")

    elif 'time' in query:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {current_time}")

    else:
        speak("Sorry, I didn’t understand that command.")
if __name__ == "__main__":                                         #This keeps the assistant running in a loop. It listens for commands and acts based on what you say.
    greet_user()
    while True:
        command = take_command()
        if command == "none":
            continue
        perform_task(command)
