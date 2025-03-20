import requests
from bs4 import BeautifulSoup
import urllib.request 
import json

# year=109
# t1=1
# t2=1
for y1 in range(16):
    year=98+y1
    for t1 in range(2):
        for t2 in range(2):
            with open('題目/{}{}{}.json'.format(year,t1+1,t2+1), 'r', encoding='utf8') as file:
                qfile = json.load(file)
            tplist=[]
            for tt in range(len(qfile)):
                idd=qfile[tt]["id"]
                #print(idd)
                #idd=12872
                url2="https://cougarbot.cc/question-view/{}/".format(idd)
                r2 = requests.get(url2)
                soup2 = BeautifulSoup(r2.text,'html.parser')
                x=0
                divs2 = soup2.find('div',id="show-explain")
                #print(divs2.text) 
                awall=divs2.text #詳解

                cklisk=[]
                images = soup2.find_all('img')
                for image in images:
                    link = image['src']
                    if link.startswith('/api/') == True:
                        link=link.replace('/api/get-image/','').replace("/","")
                        if link not in cklisk:
                            cklisk.append(link)
                if len(cklisk)==0:
                    ck2=0
                else:
                    ck2=cklisk[0] #圖片編號
                #print(ck2)
                tplist.append({"id":str(idd),"aimg":str(ck2),"awall":str(awall)})
            with open('詳解/A{}{}{}.json'.format(year,t1+1,t2+1),'w', encoding='utf8') as file: #存檔
                json.dump(tplist,file)
            print("{}{}{}done!".format(year,t1+1,t2+1))
#print(tplist)
year=114
t1=0
for t2 in range(2):
    with open('題目/{}{}{}.json'.format(year,t1+1,t2+1), 'r', encoding='utf8') as file:
        qfile = json.load(file)
    tplist=[]
    for tt in range(len(qfile)):
        idd=qfile[tt]["id"]
        #print(idd)
        #idd=12872
        url2="https://cougarbot.cc/question-view/{}/".format(idd)
        r2 = requests.get(url2)
        soup2 = BeautifulSoup(r2.text,'html.parser')
        x=0
        divs2 = soup2.find('div',id="show-explain")
        #print(divs2.text) 
        awall=divs2.text #詳解

        cklisk=[]
        images = soup2.find_all('img')
        for image in images:
            link = image['src']
            if link.startswith('/api/') == True:
                link=link.replace('/api/get-image/','').replace("/","")
                if link not in cklisk:
                    cklisk.append(link)
        if len(cklisk)==0:
            ck2=0
        else:
            ck2=cklisk[0] #圖片編號
        #print(ck2)
        tplist.append({"id":str(idd),"aimg":str(ck2),"awall":str(awall)})
    with open('詳解/A{}{}{}.json'.format(year,t1+1,t2+1),'w', encoding='utf8') as file: #存檔
        json.dump(tplist,file)
    print("{}{}{}done!".format(year,t1+1,t2+1))

