from bs4 import BeautifulSoup


with open('html_file_to_read.html', 'r') as file:
    data = file.read()

soup = BeautifulSoup(data, features='lxml')
# print(soup.meta)
# meta = soup.meta
# print(meta.get('charset'))
# print(meta['charset'])
# div = soup.div
# print(div)

body = soup.body
# print(body)

# it helps to keep check of the track
body['style'] = 'some style'
# print(body.get('style'))
# print(body)
# print(body.get('class'))


# how to get a string from html file
title = soup.title

# print(title)
# print(title.string)

# .replace_with('') replaces the navigable string with custom string

title.string.replace_with('title has been changed')
print(title)
print(title.string)
