from bs4 import BeautifulSoup
import requests as request

WIKI_HOME = "https://en.wikipedia.org"

WATERLOO_TEST = "https://en.wikipedia.org/wiki/Waterloo"




test = request.get(WATERLOO_TEST)

soup = BeautifulSoup(test.content, 'html.parser')

# print(soup.prettify())
# print(soup.get_text())
# n = 0
# for link in soup.find_all('a'):
#     if n == 5:
#         break
#     href = link.get('href')
#     if not href is None and href.startswith('/wiki/'):
#         n += 1
#         print(link.get('title'), "  :  ", link.get('href'))


# text = soup.get_text()
# print(text)

# with open('output.txt', 'w') as file:
    # file.writelines(text)

