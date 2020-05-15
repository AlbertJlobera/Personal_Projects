# Import Pandas
import pandas as pd
# Import Numpy
import numpy as np
# Import variebles .env
import os
import dotenv
from dotenv import load_dotenv
load_dotenv()
# Import smtplib for email function
import smtplib
# Import Selenium libraries
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes


def getInformationProduct(search):

    # Using Selenium

    # Open Chrome as incognit
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito") 
    # Open chrome
    driver = webdriver.Chrome('../../chromedriver',options=chrome_options)
    # Go to Amazon
    driver.get("https://www.amazon.es/")
    sleep(3)
    # Click on search items and write the item into it
    driver.find_element_by_xpath("//input[@id=\"twotabsearchtextbox\"]")\
        .send_keys(search)
    sleep(2)
    driver.find_element_by_xpath("//input[contains(@type,'submit')]")\
        .click()
    sleep(2)
    # Click on sort product per expensive to cheaper
    driver.find_element_by_class_name("a-dropdown-prompt")\
        .click()
    sleep(2)
    driver.find_element_by_id("s-result-sort-select_2")\
        .click()
    sleep(2)
    # Start scraping information from there:

    # Get all items name:
    item = driver.find_elements_by_class_name("a-size-base-plus.a-color-base.a-text-normal")
    # Get all prices:
    price = driver.find_elements_by_class_name("a-price-whole")
    # Get all images:
    image = driver.find_elements_by_class_name('s-image')
    # Save current url in url variable:
    url = driver.current_url

    # Scraping.
    # Items:
    Items=[items.text for items in item]
    # Price (we need to convert the selenium type to float)
    numero=[i.get_attribute("innerHTML") for i in price if (i.get_attribute("innerHTML") != "null")]
    Price = [e.replace('.','') for e in numero]
    Price = [e.replace(',','.') for e in Price if type(e) == str]        
    Price = [float(e) for e in Price if type(e) == str]
    # Preparing DataFrame, if length is not equal, give me a null instead
    df = {'Item':Items,'Price':Price}
    df = pd.DataFrame.from_dict(df, orient='index')
    df = df.transpose()
    # Save csv file as df.items.csv no new index needed.
    df.to_csv('df.items.csv',index=False)

    # Cleaning Dataset:

    # Load csv as df
    df = pd.read_csv('df.items.csv')
    # Drop nulls
    df.dropna(inplace=True)
    # Sort values by Price max to min to extract the fifth expensive products
    df.sort_values(by=['Price'], ascending=False,inplace=True)
    # Reset index
    df.reset_index(drop=True,inplace=True)
    # Create a new DataFrame with the fifth first products as five_products
    five_products = df.head(5)
    # Save CSV as products_ready.csv no index
    five_products.to_csv('products_ready.csv',index=False)

    # Sending first email:

    # Extract csv
    df = pd.read_csv('products_ready.csv')
    # Select Price and Item columns
    df_email = df[['Price','Item']]
    # Save csv to Email_1.csv, no index needed
    df_email.to_csv('../Email_1.csv',index=False)
    df_email = df[['Price','Item']]
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
    subject = 'Soy Pythonium, encantado de conocerte'
    # Body of the email
    body = f'''Buenos día,\nAquí tienes el producto que me pediste, 
    te mando una lista de los cinco productos más caros que he econtrado.
    \nDime cual quieres indicando el número que te aparece delante de cada artículo, van del 0 al 4, 
    necesitaría tambien el precio al cual estarías interesado.\n\n\n{df_email}\n\n\n Te avisaré cuando el precio baje, 
    si no me indicas un precio estimado te avisaré cuando baje, aun que sea solo un poco :).\n\n
        Recuerda que me encontrarás en tu terminal con el comando ......\n\nTen un buen día!,\nPythonium'''
    
    msg = f'Subject:{subject}\n\n{body}'.encode("utf-8")
    # ----------------Attached---------
    fileToSend = "Email_1.csv"
  
    ctype, encoding = mimetypes.guess_type(fileToSend)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"

    maintype, subtype = ctype.split("/", 1)

    if maintype == "text":
        fp = open(fileToSend)
    # Note: we should handle calculating the charset
    attachment = MIMEText(fp.read(), _subtype=subtype)
    fp.close()
    attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
    msg.attach(attachment)
    # ------------------Attached----------
    server.sendmail(
        sender_email,
        receiver_email,
        msg,
        
    )
    
    server.quit()

getInformationProduct('macbook air 13')