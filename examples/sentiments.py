from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
seq = sia.polarity_scores("Fuck you!")

print(seq)
