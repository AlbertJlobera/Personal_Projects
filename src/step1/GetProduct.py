# Import Pandas
import pandas as pd
# Import Selenium libraries
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def getInformationProduct(search):
    # Open Chrome as incognit
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito") 
    # Open chrome
    driver = webdriver.Chrome('../../../chromedriver',options=chrome_options)
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

getInformationProduct('Macbook air 13')