from selenium import webdriver
from bs4 import BeautifulSoup
from xlsxwriter import Workbook
import requests
import shutil
from time import sleep
import os


class App:
    def __init__(self, username='raikar_ajay', password='D33pS3curity', target_username='dataminer2060',
                 path='C:\\users\\d33ps3curity\\downloads\\instaPhotos'):

        print(os.path.exists(path))
        input('stop for now')
        self.username = username
        self.password = password
        self.target_username = target_username
        self.path = path
        self.driver = webdriver.Chrome('C:\\Users\\d33ps3curity\\Downloads\\chromedriver_win32\\chromedriver.exe')
        self.main_url = 'https://www.instagram.com'
        self.driver.get(self.main_url)
        self.error = False

        self.login()
        if self.error is False:
            self.close_dialog_box()
            self.open_target_profile()
        if self.error is False:
            self.scroll_down()

        if self.error is False:
            if not os.path.exists(path):
                os.mkdir(path)

        sleep(3)
        self.driver.close()

        # write login function

    def write_captions_to_excel_file(self, images, caption_path):
        print('writing to excel')
        # workbook = Workbook(caption_path + '/captions.xlsx')
        workbook = Workbook(os.path.join(caption_path, 'captions.xlsx'))
        worksheet = workbook.add_worksheet()
        row = 0
        worksheet.write(row, 0, 'Image name')  # 3 --> row number, column number, value
        worksheet.write(row, 1, 'Caption')

        row += 1
        for index, image in enumerate(images):
            filename = 'image_' + str(index) + '.jpg'
            try:
                caption = image['alt']
            except KeyError:
                caption = 'No caption exists for this image'
            worksheet.write(row, 0, filename)
            worksheet.write(row, 1, caption)
            row += 1
        workbook.close()

    def download_captions(self, images):
        captions_folder_path = os.path.join(self.path, 'captions')
        if not os.path.exists(captions_folder_path):
            os.mkdir(captions_folder_path)
        self.write_captions_to_excel_file(images, captions_folder_path)
        '''
        for index, image in enumerate(images):
            try:
                caption = image['alt']
            except KeyError:
                caption = 'No caption exists for this image'

            file_name = 'caption_' + str(index) + '.txt'
            file_path = os.path.join(captions_folder_path, file_name)
            link = image['src']
            with open(file_path, 'wb') as file:
                file.write(str('link:' + str(link) + '\n' + 'caption:' + caption).encode())
        '''

    def downloading_images(self):
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        all_images = soup.find_all('img')
        self.download_captions(all_images)
        print('Length of all images', len(all_images))
        for index, image in enumerate(all_images):
            filename = 'image_' + str(index) + '.jpg'
            # image_path = self.path + '/' + filename
            image_path = os.path.join(self.path, filename)
            link = image['src']
            print('Downloading image', index)
            response = requests.get(link, 'lxml')
            try:
                with open(image_path, 'wb') as file:
                    shutil.copyfileobj(response.raw, file)  # shutil --> parameter(source - destination)
            except Exception as e:
                print(e)
                print('Could not download the image number', index)
                print('Image link-->', link)

            print(image['src'])

    def login(self):
        try:
            # log_in_button = self.driver.find_element_by_xpath('//div[@id="react-root"]/p[@class="izU2O"]')
            # log_in_button = self.driver.find_element_by_class_name('jKUp7')
            try:
                sleep(2)
                username_input = self.driver.find_element_by_xpath('//input[@class="_2hvTZ pexuQ zyHYP"]')
                username_input.send_keys(self.username)
                password_input = self.driver.find_element_by_xpath("//input[@class='_2hvTZ pexuQ zyHYP']")
                password_input.send_keys(self.password)
                password_input.submit()
            except Exception:
                print('Some exception occured while trying to find username and password field')
                self.error = True

        except Exception:
            self.error = True
            print('Unable to find login button')
        # log_in_button.click()

        # input('Stop for now')

    def scroll_down(self):
        try:
            no_of_posts = self.driver.find_element_by_xpath('//span[@class="-nal3"]')
            no_of_posts = str(no_of_posts.text).replace(',', '')  # 15,483 -> 15483
            self.no_of_posts = int(no_of_posts)
            if self.no_of_posts > 12:
                no_of_scrolls = (self.no_of_posts / 12) + 3
            try:
                for value in range(no_of_scrolls):
                    # print(value)
                    self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                    sleep(1)
            except Exception as e:
                self.error = True
                print(e)
                print('Some error occured while trying to scroll down')
        except Exception:
            print('Could not find no of posts while trying to scroll')
            self.error = True

    def open_target_profile(self):
        try:
            sleep(2)
            search_bar = self.driver.find_element_by_xpath('//input[@class="XTCLo x3qfX"]')
            search_bar.send_keys(self.target_username)
            target_profile_url = self.main_url + '/' + self.target_username + '/'
            self.driver.get(target_profile_url)
            sleep(3)
        except Exception:
            self.error = True
            print('Could not find search bar')

    def close_dialog_box(self):
        try:
            sleep(2)
            close_btn = self.driver.find_element_by_xpath('//button[@class="aOOlW HoLwm"]')
            close_btn.click()
            sleep(1)
        except Exception:
            pass


if __name__ == '__main__':
    app = App()

