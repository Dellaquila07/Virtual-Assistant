import speech_recognition
import pyttsx3
import datetime
import wikipedia
import pywhatkit

audio = speech_recognition.Recognizer()
machine = pyttsx3.init()

def execute_commands():
    """This method will listen and execute commands"""
    try:
        with speech_recognition.Microphone() as source:
            voice = audio.listen(source)
            command = audio.recognize_google(voice, language="pt-BR")
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", "")
                machine.say(command)
                machine.runAndWait()

        return command

    except:
        print("Algo errado não está certo")


def user_command():
    """This method will check which command the user wants to be executed"""
    command = execute_commands()
    if 'horas' in command:
        hour = datetime.datetime.now().strftime("%H:%M")
        machine.say("Agora são ", hour)
        machine.runAndWait()
    elif "procure por" in command:
        find = command.replace("procure por", "")
        wikipedia.set_lang("pt")
        result = wikipedia.summary(find, 2)
        machine.say(result)
        machine.runAndWait()
    elif "toque" in command:
        music = command.replace("toque", "")
        result = pywhatkit.playonyt(music)
        machine.say("Tocando", music)
        machine.runAndWait()

user_command()
