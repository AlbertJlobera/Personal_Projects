# Import pandas
import pandas as pd
# Import smtplib for the email
import smtplib
# Import .env variables
import os
import dotenv
from dotenv import load_dotenv
load_dotenv()
# Import variables needed
from GetInfoProduct import url, Item, max_price
from sentimentanalisi import sentiment_changed

def send_mail():
    product = pd.read_csv('../../Email_2.csv')
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
