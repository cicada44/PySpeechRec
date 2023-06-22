from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
seq = sia.polarity_scores(
    "You're great of all time! I'm glad to see so amazing person!")

print(seq)
