from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from time import sleep


class LinkedIn:
    def __init__(self, username='d33ps3curity@gmail.com', password='d33ps3curity'):
        self.driver = webdriver.Chrome('C:\\Users\\d33ps3curity\\Downloads\\chromedriver_win32\\chromedriver.exe')
        main_url = 'https://www.linkedin.com'
        self.username = username
        self.password = password
        self.search_username = "Pranay Kasavaraju"

        self.driver.get(main_url)
        sleep(3)
        self.login()
        self.search_user(self.search_username)
        self.driver.close()


    def login(self):
        log_in_button = self.driver.find_element_by_xpath('//a[@class="nav__button-secondary"]')
        log_in_button.click()

        sleep(3)
        username_input = self.driver.find_element_by_xpath('//input[@id="username"]')
        username_input.send_keys(self.username)

        password_input = self.driver.find_element_by_xpath('//input[@id="password"]')
        password_input.send_keys(self.password)

        submit_button = self.driver.find_element_by_xpath('//button[@class="btn__primary--large from__button--floating"]')
        submit_button.submit()
        sleep(2)


    def search_user(self, search_username):
        sleep(2)
        search_bar = self.driver.find_element_by_xpath('//input[@placeholder="Search"]')
        search_bar.send_keys(search_username)
        search_bar.submit()
        sleep(2)
        get_contact_info = self.driver.find_element_by_xpath('//a[@id="ember49"]')
        get_contact_info.click()
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        email_soup = soup.find('div', class_='pv-contact-info__ci-container t-14')
        print(email_soup.a['href'])


if __name__ == '__main__':
    linkedin_app = LinkedIn()