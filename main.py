from textblob import TextBlob
from googletrans import Translator
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# import nltk
import speech_recognition as sr

# Download AI model to recognize special lexicon
# nltk.download('vader_lexicon')


# Initialization object speech recognition
recognizer = sr.Recognizer()
# Initialization analyser key
sia = SentimentIntensityAnalyzer()


def translate_russian_to_english(sentence):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(sentence, src='ru', dest='en')
    return translation.text


def recognizeSpeech(timelimit):

    with sr.Microphone() as source:
        print("Speak...")
        audio = recognizer.listen(source, timelimit, timelimit)

    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        print("Recognized text:")
        print(text)

    except sr.UnknownValueError:
        print("Can't recognize speech")
    except sr.RequestError as e:
        print("Error while trying to recognize words: {0}".format(e))


def recognizeEmotions(timelimit):

    with sr.Microphone() as source:
        print("Speak...")
        audio = recognizer.listen(source, timelimit, timelimit)

    # Make the natural english text from russian
    russian_text = recognizer.recognize_google(audio, language="ru-RU")
    native_text = translate_russian_to_english(russian_text)

    analyzer = SentimentIntensityAnalyzer()

    # Analyze of emotional keys
    sentiment_scores = analyzer.polarity_scores(native_text)

    # Output results
    print("Analys emotional coloring for text:")
    print("Positive:", sentiment_scores['pos'] * 100, '%')
    print("Negative:", sentiment_scores['neg'] * 100, '%')
    print("Neutral:", sentiment_scores['neu'] * 100, '%')
    print("General emotional:", sentiment_scores['compound'] * 100, '%')


while True:
    print("Mode:")
    print("1. Words recognition")
    print("2. Santiments recognition")
    print("0. Exit")
    choice = input("Input number of mode: ")

    if choice == "1":
        recognizeSpeech(int(input("Time to record: ")))
    elif choice == "2":
        recognizeEmotions(int(input("Time to record: ")))
    elif choice == "0":
        break
    else:
        print("Incorrect choice. Please, make the choice again.")
