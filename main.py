from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from translate import Translator
import speech_recognition as sr

# Download AI model to recognize special lexicon
nltk.download('vader_lexicon')


# Initialization object speech recognition
recognizer = sr.Recognizer()
# Initialization analyser key
sia = SentimentIntensityAnalyzer()

# Function to recognize speech


def recognizeSpeech():

    with sr.Microphone() as source:
        print("Speak...")
        audio = recognizer.listen(source, timeout=5.0, phrase_time_limit=5.0)

    try:
        text = recognizer.recognize_google(
            audio, language="ru-RU")
        print("Recognized words:")
        print(text)

    except sr.UnknownValueError:
        print("Can't recognize speech")
    except sr.RequestError as e:
        print("Error while trying to recognize words: {0}".format(e))


def recognizeEmotions():
    with sr.Microphone() as source:
        print("Speak...")
        audio = recognizer.listen(source, timeout=3.0, phrase_time_limit=3.0)

    text = recognizer.recognize_google(audio, language="ru-RU")
    analyzer = SentimentIntensityAnalyzer()

    # Analyze of emotional keys
    sentiment_scores = analyzer.polarity_scores(text)

    # Output results
    print("Analys emotional coloring for text:", sentiment_scores)
    print("Positive:", sentiment_scores['pos'])
    print("Negative:", sentiment_scores['neg'])
    print("Neutral:", sentiment_scores['neu'])
    print("General emotional:", sentiment_scores['compound'])


# Основной цикл программы
while True:
    print("Mode:")
    print("1. Words recognition")
    print("2. Santiments recognition")
    print("0. Exit")
    choice = input("Input number of mode: ")

    if choice == "1":
        recognizeSpeech()
    elif choice == "2":
        recognizeEmotions()
    elif choice == "0":
        break
    else:
        print("Incorrect choice. Please, make the choice again.")
