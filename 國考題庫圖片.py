import requests
from bs4 import BeautifulSoup
import urllib.request 
import json

url="https://cougarbot.cc/questions/106-2-2/"
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')
x=0
divs = soup.find_all('div',class_="question-block")
ndiv=divs[90]
#print(ndiv)

cklisk=[]
images = ndiv.find_all('img')
for image in images:
    link = image['src']
    if link.startswith('/api/') == True:
        link=link.replace('/api/get-image/','').replace("/","")
        cklisk.append(link)
if len(cklisk)==0:
    ck1=0
else:
    ck1=cklisk[0] #圖片編號
print(ck1)