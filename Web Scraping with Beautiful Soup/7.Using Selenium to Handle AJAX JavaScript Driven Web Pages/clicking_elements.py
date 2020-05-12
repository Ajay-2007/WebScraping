from selenium import webdriver
from time import sleep



driver = webdriver.Chrome('C:\\Users\\d33ps3curity\\Downloads\\chromedriver_win32\\chromedriver.exe')

driver.get('https://www.instagram.com/')
sleep(5)

login_button = driver.find_element_by_link_text('Sign up')
login_button.click()

sleep(5)



driver.close()
