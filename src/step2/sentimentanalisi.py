# Import variable reviews from GetInfoProduct
from GetInfoProduct import review
# Import googletrans to conver reviews to english language due nltk just acept english
from googletrans import Translator
# Import nltk for sentiment analysis
from nltk.stem import SnowballStemmer
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download("vader_lexicon")

def sentiment():
    
    # Convert selenium type to str of review varibale
    reviews = [''.join(r.text.split('\n')) for r in review]
    reviews = ''.join(reviews)
    # Translate to english
    trans = Translator()
    t = trans.translate(reviews)
    text = t.text

    # Extract sentiment analysis from the total reviews
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    # Modify the dictionary to make it clear
    global sentiment_changed
    sentiment_changed = {'Negativo':sentiment['neg'],'Neutro':sentiment['neu'],'Positivo':sentiment['pos']}
    # Make persantatge of the sentiment for each group

    sentiment_changed = {'Positivo':round(sentiment_changed['Positivo']*100/1,2),'Neutro':round(sentiment_changed['Neutro']*100/1,2),'Negativo':round(sentiment_changed['Negativo']*100/1,2)}
sentiment()