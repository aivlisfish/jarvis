import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 125)

def tts(texttospeak):
    engine.say(texttospeak)
    engine.runAndWait()

def continuous_recognition():
    r = sr.Recognizer()
    run = True
    with sr.Microphone() as source:
        print("Listening...")
        while run:
            try:
                audio = r.listen(source)
                text = format(r.recognize_google(audio))
                print(text)
                if ('Jarvis' in text):
                    if ('exit' in text) or ('shut down' in text):
                        run = False
                    if 'clip that' in text:
                        tts('Clipped to Downloads folder')
                    if 'remove his balls' in text:
                        tts('Registering him for sack removal')
            except sr.UnknownValueError:
                print("Nothing said")
            except sr.RequestError as e:
                print("Could not request results; {}".format(e))

if __name__ == "__main__":
    continuous_recognition()