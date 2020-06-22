# Creating cleaner and filtered hacker news listing with the help of scraping

# While scraping always check for robots.txt over a website in order to follow ethical measures of web scraping.
# robots.txt announces the parts of website which are dissallowed or allowed.

import requests
from bs4 import BeautifulSoup
import pprint

hn_res = requests.get('https://news.ycombinator.com/news')
hn_soup = BeautifulSoup(hn_res.text, 'html.parser')
news = hn_soup.select('.storylink')
subtext = hn_soup.select('.subtext')

def sort_list_of_dictionaries(list):
  return sorted(list, key = lambda dict: dict['votes'], reverse = True)

def create_custom_hn(news, subtext):
  hn = []
  for idx, item in enumerate(news):
    title = item.getText()
    link = item.get('href', None)

    scores = subtext[idx].select('.score')
    if len(scores):
      votes = int(scores[0].getText().replace(' points', ''))
      if votes >= 100:
        hn.append( { 'title': title, 'link': link, 'votes': votes } )

  return sort_list_of_dictionaries(hn)

pprint.pprint(create_custom_hn(news, subtext))
