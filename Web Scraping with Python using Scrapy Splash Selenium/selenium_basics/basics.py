from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from shutil import which

chrome_options = Options()
chrome_options.add_argument("--headless")

chrome_path = which("chromedriver")

driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)

driver.get("https://duckduckgo.com")

search_bar = driver.find_element_by_id("search_form_input_homepage")
search_bar.send_keys("My User Agent")
# search_bar.submit()

# search_btn = driver.find_element_by_id("search_button_homepage")
# search_btn.click()
# driver.find_elements_by_class_name()

# driver.find_elements_by_tag_name("h1")
# driver.find_elements_by_xpath()
# driver.find_elements_by_css_selector()
search_bar.send_keys(Keys.ENTER)

print(driver.page_source)

driver.close()
