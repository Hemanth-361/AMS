from textblob import TextBlob

def sentiment_analysis(text):
    analysis = TextBlob(text)
    
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

# Example usage:
text = "i will love this game!"
print(sentiment_analysis(text))
