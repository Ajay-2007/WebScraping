from selenium import webdriver
import requests


driver = webdriver.Chrome('C:\\Users\\d33ps3curity\\Downloads\\chromedriver_win32\\chromedriver.exe')

driver.get('https://www.google.com')

# search tag using id, class

search_bar = driver.find_element_by_class_name('gLFyf')

# search bar

search_bar.send_keys('I want to learn web scraping')

# submit the form
search_bar.submit()


# close the driver
driver.close()