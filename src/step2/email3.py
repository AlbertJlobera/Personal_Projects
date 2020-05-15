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

def send_final_email():

    
    sender_email = os.getenv('emailP')
    receiver_email = os.getenv('email')
    password = os.getenv('PasswordP')


    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login(sender_email,password)
    
    subject = 'Pythonium, ¡Tienes una oferta!'
    
    body = f'''Buenas noticias!\n\nNuestro producto\n {Item}\n\n Se encuentra al siguiente precio {max_price}! un chollazo!, 
si aun sigues interesado te dejo el enlace:\n\n {url}.\n\n\n Ten un buen día!,\n Pythonium,'''

    
    msg = f'Subject:{subject}\n\n{body}'.encode()
    
    
    server.sendmail(
        sender_email,
        receiver_email,
        msg
    )
    
    print('Hey email has been sent!')
    
    server.quit()

def last_email(min_price):
    if (max_price <= min_price):
        send_final_email()


