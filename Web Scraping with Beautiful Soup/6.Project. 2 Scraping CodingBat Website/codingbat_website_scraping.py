
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pandas as pd


user_agent = UserAgent()
headers = {'user-agent': user_agent.chrome}
main_url = 'https://codingbat.com/java'
page = requests.get(main_url, headers=headers)
soup = BeautifulSoup(page.content, 'lxml')

base_url = 'https://codingbat.com'

all_divs = soup.find_all('div', class_='sum')

all_links = [base_url + div.a['href'] for div in all_divs]

for link in all_links:
    inner_page = requests.get(link, headers=headers)
    inner_soup = BeautifulSoup(inner_page.content, 'lxml')
    div = inner_soup.find('div', class_='tabc')
    # for td in div.table.find_all('td'):
    #     print(base_url + td.a['href'])
    # break
    question_links = [base_url + td.a['href'] for td in div.table.find_all('td')]


    # for question_link in question_links:
    #     print(question_link)
     
    data = {}

    for question_link in question_links:
        final_page = request.get(question_link)
        final_soup = BeautifulSoup(final_page.content, 'lxml')
        indent_div = final_soup.find('div', class_='indent')
        problem_statement = indent_div.table.div.string

        siblings_of_statement = indent_div.table.div.next_siblings

        for sibling in siblings_of_statement:
            if sibling is not None:
                # print(sibling) 
                data[question_link] = sibling

    data = list(data.items())

    data = pd.DataFrame(data)

    data_csv = pd.to_csv('Codingbat_question_scraping.csv')


