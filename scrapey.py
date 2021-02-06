import requests 
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request, urlretrieve
import urllib
import re

html_page = requests.get('https://www.1999.co.jp/eng/image/10522238')
soup = BeautifulSoup(html_page.content, 'html.parser')

images = soup.find_all('img', {'src':re.compile('jpg')})
image_link_list = []

for image in images:
  
  fullImg = 'https://www.1999.co.jp' + image['src']
  image_link_list.append(fullImg)
  

for i in range(len(image_link_list)):
  name = image['src']
  print(name)
  try:
    urllib.request.urlretrieve(image_link_list[i], name)
    print(html_page.status_code)
   
  except:
    # print('stuff not found')
    print(html_page.status_code)

