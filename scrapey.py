import requests 
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request, urlretrieve
import urllib
import re
import os 

html_page = requests.get('https://www.1999.co.jp/eng/image/10700202')
soup = BeautifulSoup(html_page.content, 'html.parser')

images = soup.find_all('img', {'src':re.compile('jpg')})
image_link_list = []

for image in images:
  fullImg = 'https://www.1999.co.jp' + image['src']
  image_link_list.append(fullImg)

for i in range(len(image_link_list)):
  path = '/Users/jjarrett/webscraper/img'
  name = str(i) + '.jpg'
  location = os.path.join(path, name)
  try:
    urllib.request.urlretrieve(image_link_list[i], location)
    print('grabbing images...')

  except:
    print(html_page.status_code)

