# Sentiment analysis
"""
we have imported textblob library which inherits lexicon list of negative & positive words
like, positive- good,nice & negative words- bad ,adverse etc.
"""
from textblob import TextBlob
print("Enter views")
x = str(input())
feedback = TextBlob(x)
y = feedback.sentiment.polarity

# checking polarity & subjectivity of sentence with if else
if y < 0:
    print("Negative")
elif y == 0:
    print("Neutral")
elif 0 < y <= 1:
    print("Positive")
