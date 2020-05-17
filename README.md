<h1><span style="color: #2c32af">Pythonium, el robot que te avisa de las ofertas en Amazon</span></h1>


<h2>Solo tienes que indicarle el producto que quieres y él te mandará un email avisándote con la oferta</h2>

<p>¿Cuánto tiempo has pasado en Amazon actualizando la página del producto que tanto te gusta para ver si el precio bajaba?<br><br>
  Si la respuesta es <i>mucho</i>, tienes que conocer a <span style="color: #2c32af"> Pythonium</span>. <br><br> 
Pythonium nace con el propósito de ahorrarte tiempo y avisarte cuando <strong>el producto que tú le indiques esté en oferta.</strong><br><br>
  
  <figure class="wp-block-image size-large is-resized"><img src="https://github.com/AlbertJlobera/Personal_Projects/blob/master/IMG/pythonium.png" alt="" width="521" height="346"/></figure>
  
<h3>¿Te preguntas cómo funciona?</h3><br> 
-Dile el nombre del producto que te interesa<br>
-El robot te enviará un email con los 5 mejores que encuentre en Amazon<br>
-Tú le especificarás cuál quieres y cuál es el precio máximo que pagarías por él<br>
-En un segundo email, Pythonium te adjuntará un archivo con todas sus características y se quedará revisando cada hora el precio del producto<br>
-En cuanto el precio alcance la cifra máxima que has indicado, te mandará un nuevo email avisándote de la oferta<br>
  
 <h3>¿Te preguntas cómo interactuar con él?</h3><br>
 El sistema de Pythonium utiliza <strong>dos pipelines</strong> diferentes:
 <br>
 <strong>Primer Pipeline:</strong> <i>main.py</i>
 <br>
 Aquí es donde escribirás el producto que quieres que busque, tu nombre para que el robot pueda dirigirse a ti y un email de contacto:<br><br>
 <i><strong>python3 main.py --item</strong> <'nombre del producto deseado'><strong> --user</strong> <'Tu nombre'><strong> --email</strong> <'tu email'> </i><br><br>
  
  <strong>Segundo Pipeline:</strong> <i>main2.py</i><br>
  En este archivo tendrás que indicarle a Pythonium el número del índice del producto (lo verás en el archivo adjunto), el precio máximo que pagarías por él, tu nombre y un email de contacto.
  <br><br>
  <i><strong>python3 main2.py --index</strong> <'numero del producto deseado del 0 al 4'><strong> --precio</strong> <'precio mínimo interesado'><strong> --user</strong> <'tu nombre'><strong> --email</strong> <'tu email'> </i><br>Pythonium te enviará un tercer email cuando el precio baje, y no hará falta hacer uso de otro parámetro, ya que automáticamente se formulará con una condición.<br>
    Si tienes cualquier duda puedes revisar los parámetros con -h o --help, te recordará los comandos a seguir y su función.<br><br>
  
  <h3> ¿Cómo se ha creado? </h3>
  <strong>Python:</strong><br>
  - <i>Pandas<br>
  - Numpy</i><br><br>


<strong>Selenium</strong><br>
- <i>pyvirtualdisplay <br>
- time <br>
- webdriver<br>
- selenium.webdriver.common.by<br>
- selenium.webdriver.support <br>
- selenium.webdriver.support.ui import WebDriverWait</i><br><br>
  
<strong>Email</strong><br>
- <i>email.mime.multipart<br>
- email.mime.text<br>
- mimetypes<br>
- email.mime.image <br>
- email import encoders<br>
- email.mime.base <br>
- smtplib</i><br><br>

<strong>Googletrans</strong><br>
- <i>googletrans</i><br><br>

<strong>Machine learning "NLTK"</strong><br>
- <i>nltk<br>
- nltk.stem <br>
- nltk.sentiment.vader <br>
- nltk.download("vader_lexicon")</i><br><br>

<strong>Variable .env</strong><br>
- <i>os<br>
- dotenv<br>
- dotenv <br>
load_dotenv()</i><br><br>

<strong>Pipeline</strong><br>
- <i>argparse</i><br><br><br>


  <figure class="wp-block-image size-large is-resized"><img src="https://github.com/AlbertJlobera/Personal_Projects/blob/master/IMG/gif-pythonium.gif" alt="" width="521" height="346"/></figure>
