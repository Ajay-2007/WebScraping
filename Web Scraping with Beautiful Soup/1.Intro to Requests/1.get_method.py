import requests


# response = requests.get('https://www.google.com')
# print(response)
# # print(response.content)
# print(response.status_code)
# print(response.headers)
#
#
# for key, value in response.headers.items():
#     print(key + ' : ' + value)

from fake_useragent import UserAgent


ua = UserAgent()

header = {'user-agent': ua.chrome}


# print(ua.chrome)

page = requests.get('https://www.google.com', headers=header)
print(page.content)
page = requests.get('https://www.google.com', headers=header, timeout=3)
print(page.content)



