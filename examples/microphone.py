# -----------------------------------------------------------------------------
#
# Trivial example of using microphone in speech_recognition in Python3
#
# -----------------------------------------------------------------------------

import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak...")
    audio = recognizer.listen(source, 5, 5)

text = recognizer.recognize_google(audio, language="ru-RU")

print(text)
