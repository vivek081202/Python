# Sentiment analysis for brand new iphone 13
"""
we have imported textblob library which inherits lexicon list of negative & positive words
like, positive- good,nice & negative words- bad ,adverse etc.
"""
from textblob import TextBlob
print("Enter your views about Iphone 13")
x = str(input())
feedback = TextBlob(x)
y = feedback.sentiment.polarity

# checking polarity & subjectivity of sentence with if else
if y < 0:
    print("Thanks for your feedback! We will improve our product according to your specifications & features")
elif y == 0:
    print("Thanks for your feedback!")
elif 0 < y <= 1:
    print("Thanks for your feedback! We are glad that you liked out product")
