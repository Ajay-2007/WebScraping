from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup


# make a webdriver object

driver = webdriver.Chrome('C:\\Users\\d33ps3curity\\Downloads\\chromedriver_win32\\chromedriver.exe')

# open some page using get method   - url   -> parameters
driver.get('https://www.facebook.com')

soup = BeautifulSoup(driver.page_source, 'lxml')
print(soup.prettify())

driver.close()