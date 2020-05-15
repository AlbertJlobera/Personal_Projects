# Import Pandas
import pandas as pd
# Import Selenium libraries
from pyvirtualdisplay import Display
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Import googletrans to conver reviews to english language due nltk just accept english
from googletrans import Translator
# Import nltk for sentiment analysis
from nltk.stem import SnowballStemmer
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download("vader_lexicon")
# Import smtplib for the email
import smtplib
# Import .env variables
import os
import dotenv
from dotenv import load_dotenv
load_dotenv()



def infoProduct(index,min_price):
    # Load csv Email_1
    df = pd.read_csv('../Email_1.csv')
    # Extract item chosen by index and save it into a new variable item_chosed
    item_chosen = df.loc[index,'Item']
    # Extract price  of the item chosen by index and save it into a new variable item_chosed
    price_chosen = df.loc[index,'Price']
    # Active Selenium with incognit 
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    # Open Chrome to Amazon
    driver = webdriver.Chrome('../chromedriver',options=chrome_options)
    driver.get("https://www.amazon.es/")
    sleep(3)
    # Select search bar and type the full name of the item chosen 
    driver.find_element_by_xpath("//input[@id=\"twotabsearchtextbox\"]")\
        .send_keys(item_chosen)
    sleep(2)
    driver.find_element_by_xpath("//input[contains(@type,'submit')]")\
        .click()
    sleep(2)
    # Select sort items by price max to min
    driver.find_element_by_class_name("a-dropdown-prompt")\
        .click()
    sleep(2)
    driver.find_element_by_id("s-result-sort-select_2")\
        .click()
    sleep(2)

    # Click on the firt item found
    driver.find_element_by_class_name('a-link-normal.a-text-normal')\
        .click()
    sleep(2)
    # Open full reviews 
    driver.find_element_by_class_name('a-expander-prompt')\
        .click()
    sleep(2)
    # Start Scraping information from there
    # Get reviews
    
    review = driver.find_elements_by_class_name('cr-original-review-content')# reviews to do the nltk
    # Get item_description
    item_description = driver.find_element_by_id('productTitle') # full description of the item
    # Get Price
    price = driver.find_element_by_id('priceblock_ourprice') # Actual price
    # Get table information column one
    column1 = driver.find_elements_by_class_name('label')
    # Get table information column two
    column2 = driver.find_elements_by_class_name('value')
    # Save url
    
    url = driver.current_url

    # Preparing data from Selenium to str or float.
    # Get str item description
    
    Item = item_description.text
    # Modify type to float as max_price
    price = price.text
    price = price.strip(' €')
    price = price.replace('.','')
    price = price.replace(',','.')
    
    max_price = float(price)
    # Get first column
    column_1 = [c.text for c in column1]
    # Get second column
    column_2 = [c.text for c in column2]
    # Preparing DataFrame of the two columns informations
    df = {'Characteristics': column_1,'Information':column_2}
    df = pd.DataFrame.from_dict(df, orient='index')
    df = df.transpose()
    # Set index to Characteristics to get just two columns in our DataFrame
    product = df.set_index(['Characteristics'])
    # Save csv to Email_2.csv
    product.to_csv('Email_2.csv', index=False)

    # Get Sentiment Analizer
    
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
    
    sentiment_changed = {'Negativo':sentiment['neg'],'Neutro':sentiment['neu'],'Positivo':sentiment['pos']}
    # Make persantatge of the sentiment for each group

    sentiment_changed = {'Positivo':round(sentiment_changed['Positivo']*100/1,2),'Neutro':round(sentiment_changed['Neutro']*100/1,2),'Negativo':round(sentiment_changed['Negativo']*100/1,2)}

    # Send second Email

    product = pd.read_csv('Email_2.csv')
    # Preparing env variables
    sender_email = os.getenv('emailP')
    receiver_email = os.getenv('email')
    password = os.getenv('PasswordP')

    # Connecting to the server
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login(sender_email,password)
    # Subject of the email
    subject = 'Pythonium, detalles del artículo'
    # Body of the email
    body = f'''Buenos días!\n\nVoy a recordarte el nombre y especificaciones generales del producto escogido: 
    \n{Item}\nPrecio actual: {max_price}.\n\n
    Segun mi sistema de sentimiento, las valoraciones tienen un % de:\n
    {sentiment_changed}\n\n\nEnlace al producto:\n {url}
    
    Te adjunto una tabla con los datos técnicos del producto para que le eches un ojo:\n\n\n{product}\n\n 
    Cuando baje al precio deseado te lo recordaré.\n\n Ten un buen día!,\n Pythonium,'''

    
    msg = f'Subject:{subject}\n\n{body}'.encode()
    
    
    server.sendmail(
        sender_email,
        receiver_email,
        msg
    )
    
    server.quit()
    print('Hey, email has been sent!')
    
    while True:
        sleep(60 * 60)

        # Run Selenium without browser

        display = Display(visible=0, size=(800, 600))\
        .display.start()

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        # Open Chrome to Amazon
        driver = webdriver.Chrome('../chromedriver',options=chrome_options)
        driver.get(url)
        sleep(3)
        # Get Price
        price2 = driver.find_element_by_id('priceblock_ourprice') # Actual price
        # Modify type to float as max_price
        price1 = price2.text
        price1 = price1.strip(' €')
        price1 = price1.replace('.','')
        price1 = price1.replace(',','.')
    
        max_price1 = float(price1)

        # Condition if the price goes down third email will be sent
        if (max_price1 <= min_price):


            # Send third email

            sender_email = os.getenv('emailP')
            receiver_email = os.getenv('email')
            password = os.getenv('PasswordP')


            server = smtplib.SMTP('smtp.gmail.com',587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            
            server.login(sender_email,password)
            
            subject = 'Pythonium, ¡Tienes una oferta!'
            
            body = f'''Buenas noticias!\n\nNuestro producto\n {Item}\n\n Se encuentra al siguiente precio {max_price1}!  
            si aun sigues interesado te dejo el enlace:\n\n {url}.\n\n\n Ten un buen día!,\n Pythonium,'''

            
            msg = f'Subject:{subject}\n\n{body}'.encode()
            
            
            server.sendmail(
                sender_email,
                receiver_email,
                msg
            )
            
            print('Hey email has been sent!')
            
            server.quit()






