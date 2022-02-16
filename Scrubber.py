from bs4 import BeautifulSoup
import requests
import nltk
import random

WIKI_HOME = "https://en.wikipedia.org"
request = requests.get(WIKI_HOME)
soup = BeautifulSoup(request.content, 'html.parser')

english_vocab = set(w.lower() for w in nltk.corpus.words.words())


def getFullLink(link: str) -> str:
  if link[0:4] == 'http':
    return link
  return WIKI_HOME + link

def isEnglish(text: str) -> bool:
  if text is None:
    return False
  text_vocab = set(w.lower() for w in text if w.lower().isalpha())
  return len(text_vocab.difference(english_vocab)) == 0

def getTextFromSubLink(soup):
  links = dict()
  for link in soup.find_all('a'):
    if (isEnglish(link.string)):
      links[link.string] = getFullLink(link.get('href'))

  randomNumber = random.randint(1, 1000)
  key = list(links.keys())[randomNumber % len(links.keys())]

  print(f'{key}: {links[key]}')

  request = requests.get(links[key])

  soup = BeautifulSoup(request.content, 'html.parser')

  print(soup.get_text())

def getImages(soup):
  imgs = set()
  for link in soup.find_all('img'):
    imgs.add(link.get('src'))

  return imgs

getImages(soup)
