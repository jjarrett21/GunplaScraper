import requests 
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials, firestore, storage
from urllib.request import urlopen, Request, urlretrieve
from google.cloud import client
import urllib
import re
import os 

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'storageBucket' : 'g-reader-5aafb.appspot.com'

})

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='/Users/jjarrett/gcloud_key_pair.json'


link = input("Please enter link \n")
html_page = requests.get(link)
soup = BeautifulSoup(html_page.content, 'html.parser')

image_div = soup.find_all('div', {'id':'imgAll' })[0]
image_link_list = []

db = firestore.client()
bucket = storage.bucket()


for img in image_div.find_all('img', { 'src':re.compile('jpg')}):
  fullImg = 'https://www.1999.co.jp' + img['src']
  image_link_list.append(fullImg)


for i in range(len(image_link_list)):
  path = '/Users/jjarrett/webscraper/img'
  name = str(i) + '.jpg'
  location = os.path.join(path, name)
  blob = bucket.blob(name)
  try:
    urllib.request.urlretrieve(image_link_list[i], location)
    blob.upload_from_filename(location)
    print('grabbing images...')

  except:
    print(html_page.status_code)

