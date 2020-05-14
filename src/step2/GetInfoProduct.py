# Import Pandas
import pandas as pd
# Import Selenium libraries
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def infoProduct(indexnumer):
    # Load csv Email_1
    df = pd.read_csv('../../Email_1.csv')
    # Extract item chosen by index and save it into a new variable item_chosed
    item_chosen = df.loc[indexnumer,'Item']
    # Extract price  of the item chosen by index and save it into a new variable item_chosed
    price_chosen = df.loc[indexnumer,'Price']
    # Active Selenium with incognit 
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    # Open Chrome to Amazon
    driver = webdriver.Chrome('../../../chromedriver',options=chrome_options)
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
    global review # global variable
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
    global url # global variable
    url = driver.current_url

    # Preparing data from Selenium to str or float.
    # Get str item description
    global Item # global variable
    Item = item_description.text
    # Modify type to float as max_price
    price = price.text
    price = price.strip(' €')
    price = price.replace('.','')
    price = price.replace(',','.')
    global max_price #global variable
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

infoProduct(0)

