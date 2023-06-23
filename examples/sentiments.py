# -----------------------------------------------------------------------------
#
# Trivial example for sentiment scores using SIA in nltk in Python3
#
# -----------------------------------------------------------------------------

from nltk.sentiment import SentimentIntensityAnalyzer

# Initialization sia
sia = SentimentIntensityAnalyzer()

text = "You're great of all time! I'm glad to see so amazing person!"
seq = sia.polarity_scores(text)

print(seq)
