# Import Pandas
import pandas as pd
# Import variebles .env
import os
import dotenv
from dotenv import load_dotenv
load_dotenv()
# Import smtplib for email function
import smtplib

# Extract csv
df = pd.read_csv('products_ready.csv')
# Select Price and Item columns
df_email = df[['Price','Item']]
# Save csv to Email_1.csv, no index needed
df_email.to_csv('Email_1.csv',index=False)

def send_mail():

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
    
    msg = f'Subject:{subject}\n\n{body}'.encode()
    
    
    server.sendmail(
        sender_email,
        receiver_email,
        msg
    )
    
    print('Hey email has been sent!')
    
    server.quit()
    
send_mail()