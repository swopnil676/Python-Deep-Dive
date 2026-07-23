# Voice Assistant :

    # primary
# import pyttsx3
# engine = pyttsx3.init()
# text = input("Say something : ")
# engine.say(text)
# engine.runAndWait()


    # optimized
import pyttsx3

def speak(text, rate=150, volume=1.0):
    engine = pyttsx3.init()

    # Set speech properties
    engine.setProperty('rate', rate)      # speed of speech
    engine.setProperty('volume', volume)  # volume (0.0 to 1.0)

    engine.say(text)
    engine.runAndWait()

# Input
text = input("Say something: ").strip()

# Safety check
if text:
    speak(text)
else:
    print("No text entered!")