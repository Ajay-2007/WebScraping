from bs4 import BeautifulSoup


def read_file():
    with open('html_file_to_read.html', 'r') as file:
        data = file.read()
        return data

html_file = read_file()
# print(html_file)
soup = BeautifulSoup(html_file, 'lxml')
print(soup)

# soup prettify
print(soup.prettify())