from selenium import webdriver
from time import sleep



driver = webdriver.Chrome('C:\\Users\\d33ps3curity\\Downloads\\chromedriver_win32\\chromedriver.exe')

# driver.get('https://www.instagram.com')
#
# sleep(2)
# login_button = driver.find_element_by_xpath("//div[@class='gr27e']//p[@class='izU2O']/a")
# login_button.click()
#
# sleep(5)


driver.get('https://www.google.com')
sleep(2)
search_bar = driver.find_element_by_xpath('//input[@class="gLFyf gsfi"]')
search_bar.send_keys('valid xpath expression')
search_bar.submit()
sleep(5)


driver.close()