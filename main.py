import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime as dt
import wikipedia as wiki
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voice_rate = 175
engine.setProperty('rate', voice_rate)
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)


def introduce():
    engine.say('Hello')
    engine.say('My name is Alexa your virtual assistant.')
    engine.say('What can I do for you today?')
    engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace('alexa', '')
                print(command)
    except Exception as e:
        print(e)
    return command


def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        print('Playing' + song)
        talk('Playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command and 'what' in command:
        time = dt.datetime.now().strftime('%I.%M %p')
        print(time)
        talk('Current time is' + time)
    elif 'search' in command and 'wikipedia' in command:
        search = command.replace('search', '').replace('on', '').replace('wikipedia', '')
        info = wiki.summary(search, 1)
        print(info)
        talk(info)
    elif 'joke' in command and 'tell' in command:
        joke = pyjokes.get_joke()
        talk(joke)
        print(joke)
    else:
        talk('I am sorry I did not catch you.')
        talk('Could you say it again?')

# MAIN


introduce()
while True:
    run_alexa()
