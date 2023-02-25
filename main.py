import speech_recognition as sr #so jarvis can listen
import pyttsx3 #so jarvis can talk
import pywhatkit
import datetime
import wikipedia
import pyjokes
listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk (text): #function that make jarvis talk
    engine.say(text)
    engine.runAndWait()
def taking_command ():
    try:
        with sr.Microphone() as source :
            talk("How may I help you")
            engine.runAndWait()
            print("listening ...")
            voice =listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            while("jarvis" not in command):
                talk("sorry i didn't understand")
                talk("try again and mention my name")
                engine.runAndWait()
                print("listening ...")
                voice = listner.listen(source)
                command = listner.recognize_google(voice)
            command = command.lower()
            command = command.replace('jarvis', '')
            return command

    except:
        pass
def run_Jarvis():
    command = taking_command()
    print(command)
    if 'play' in command:# playing music
        song = command.replace("play","")# removing jarvis name from the command
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I %M %p")
        talk("the Current time now is"+time)
    elif 'who created you' in command:
        talk('i was created by my father mouhanned ben lazreg')
    elif 'who is'or 'what is' in command:
        person = command.replace('who is','')
        person = command.replace('what is','')
        info = wikipedia.summary(person,1)#give the summary of wikipedia 1st line
        talk(info)
        print(info)
    elif 'i love you ' in command:
        talk('why are you gay ? ')
    elif 'joke' in command:
        joke =pyjokes.get_joke()
        talk(joke)
        print(joke)
    else:
        talk('sorry i did not understand')
talk("Hello Sir")
while(True):
    run_Jarvis()