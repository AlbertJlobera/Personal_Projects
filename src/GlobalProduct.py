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
from email.mime.image import MIMEImage



def getInformationProduct(search,user,email_user):

    # Using Selenium

    # Open Chrome as incognit
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito") 
    # Open chrome
    driver = webdriver.Chrome('../chromedriver',options=chrome_options)
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
    # Drop nulls
    df.dropna(inplace=True)

    # Sort values by Price max to min to extract the fifth expensive products
    df.sort_values(by=['Price'], ascending=False,inplace=True)
    # Reset index
    df.reset_index(drop=True,inplace=True)
    # Create a new DataFrame with the fifth first products as five_products
    df = df.head(5)
    # Save csv as Products to attach in the next email
    df.to_csv('src/CSV/Products.csv')

    # Send email with csv atatched

    # Preparing env variables
    sender_email = os.getenv('emailP')
    receiver_email = email_user
    password = os.getenv('PasswordP')

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = email_user
    msg["Subject"] = f"Pythonium: Tus TOP 5 [{search}]"
    html =f"""\
    <html>
    <head></head>
    <body>
        <h3>¡Hola, {user}!</h3>
        <p>¡Muchas gracias por encargarme mi primera misión!<br> 
        He estado investigando en <i>Amazon</i> sobre: <strong><span style="color: #2c32af">{search}</span></strong><br>
        Después de una búsqueda exhaustiva, he seleccionado<strong> los 5 mejores</strong> y te los adjunto en este email.<br>
        Recuerda indicarme el <strong>número del artículo</strong> que más te guste y el <strong>precio máximo</strong> que pagarías por él.<p><br><br>
        Seguimos en contacto,<br><br>
        
        <h3><span style="color: #2c32af">Pythonium</span></h3>
        </p>

    </body>
    </html>
    """
    
    part2 = MIMEText(html, 'html')
    msg.attach(part2)
    fileToSend = 'src/CSV/Products.csv'
    ctype, encoding = mimetypes.guess_type(fileToSend)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"

    maintype, subtype = ctype.split("/", 1)

    if maintype == "html":
        fp = open(fileToSend)
        # Note: we should handle calculating the charset
        attachment = MIMEText(fp.read(), _subtype=subtype)
        fp.close()
    else:
        fp = open(fileToSend, "rb")
        attachment = MIMEBase(maintype, subtype)
        attachment.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(attachment)
    fp = open('IMG/pythonium.png', 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)
    attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
    msg.attach(attachment)

    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(sender_email,password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

    server.quit()

