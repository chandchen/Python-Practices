from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re
import datetime
import random
import os

random.seed(datetime.datetime.now())


def save_image(soup):
    try:
        image_links = soup.find('table', {'class': 'infobox'}).find('img')
        image_url = "https:" + image_links.attrs['src']

        root = "D://pics//wiki//"
        path = root + image_url.split('/')[-1]
        try:
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                res = requests.get(image_url)
                with open(path, 'wb') as f:
                    f.write(res.content)
                    f.close()
                    print("File Saved Success")
            else:
                print("File Existed")
        except:
            print("Crawler Fails")
    except:
        print("File Saved Fails")


def get_link(article_url):
    url = 'https://en.wikipedia.org' + article_url
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')

    save_image(soup)

    return soup.find('div', {'id': 'bodyContent'}).findAll('a',
                               href=re.compile('^(/wiki/)((?!:).)*$'))

info = input("Please Enter Information You Want to Search: ")

links = get_link('/wiki/' + info)
while len(links) > 0:
    new_article = links[random.randint(0, len(links)-1)].attrs['href']
    print(new_article)
    links = get_link(new_article)
