#Library for performing speech recognition, with support for several engines and APIs, online and offline. Speech recognition engine/API support: CMU Sphinx (works offline)
import speech_recognition as sr
#pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline and is compatible with both Python 2 and 3
import pyttsx3
#pywhatkit is a Python library for sending WhatsApp messages at a certain time, it has several other features too.
#Following are some features of pywhatkit module:
#    Send WhatsApp messages.
#    Play a YouTube video.
#    Perform a Google Search.
#    Get information on particular topic.
import pywhatkit
#The datetime module supplies classes for manipulating dates and times.
import datetime as dt
#Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia.Search Wikipedia, get article summaries, get data like links and images from a page, and more
import wikipedia as wiki
#One line jokes for programmers (jokes as a service)
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
