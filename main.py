from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import random
import speech_recognition as sr

nltk.download('vader_lexicon')


# Инициализация объекта распознавания речи
recognizer = sr.Recognizer()
# Инициализация анализатора тональности
sia = SentimentIntensityAnalyzer()


def recognize_words():
    all_words = []

    with sr.Microphone() as source:
        print("Говорите...")
        audio = recognizer.listen(source, timeout=3.0, phrase_time_limit=3.0)

    try:
        text = recognizer.recognize_google(
            audio, language="ru-RU", show_all=True)
        print("Распознанные слова:")
        word = random.choice(text["transcript"])
        print("- ", word)
        if "стоп" in word.lower():
            return  # Остановить запись
    except sr.UnknownValueError:
        print("Не удалось распознать речь")
    except sr.RequestError as e:
        print("Ошибка сервиса распознавания речи: {0}".format(e))

    # Продолжить запись
    recognize_words()


def recognize_emotions():
    with sr.Microphone() as source:
        print("Говорите...")
        audio = recognizer.listen(source, timeout=10.0, phrase_time_limit=10.0)

    text = recognizer.recognize_google(audio, language="ru-RU")
    analyzer = SentimentIntensityAnalyzer()

    # Анализ эмоциональной окраски текста
    sentiment_scores = analyzer.polarity_scores(text)

    # Вывод результатов
    print("Анализ эмоциональной окраски для текста:", text)
    print("Позитивность:", sentiment_scores['pos'])
    print("Негативность:", sentiment_scores['neg'])
    print("Нейтральность:", sentiment_scores['neu'])
    print("Общая эмоциональная окраска:", sentiment_scores['compound'])


# Основной цикл программы
while True:
    print("Выберите режим:")
    print("1. Распознавание слов")
    print("2. Распознавание эмоций")
    print("0. Выход")
    choice = input("Введите номер режима: ")

    if choice == "1":
        recognize_words()
    elif choice == "2":
        recognize_emotions()
    elif choice == "0":
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите снова.")
