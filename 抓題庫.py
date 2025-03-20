import requests
from bs4 import BeautifulSoup
import urllib.request 
import json
'''
for y1 in range(16):
    year=98+y1
    for t1 in range(2):
        for t2 in range(2):
            #print(year,t1,t2)

            url="https://cougarbot.cc/questions/{}-{}-{}/".format(year,t1+1,t2+1)
            r = requests.get(url)
            soup = BeautifulSoup(r.text,'html.parser')
            x=0
            divs = soup.find_all('div',class_="question-block")

            temporylist=[]
            #print(len(divs))
            for k in range(len(divs)):
                ndiv=divs[k]
                #print(ndiv)

                questionq=ndiv.find('div',class_="question-Q") 
                #print(questionq.text)   #題目
                qq=questionq.text

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

                choices = ndiv.find('div',class_="question-A")
                #print(choices)
                allchoice = choices.find_all("li")
                chlist=[]
                for i in range(len(allchoice)):
                    #print(allchoice[i].text) #選項
                    chlist.append(allchoice[i].text)
                aw=""
                answers= choices.find_all("li",class_="primary-color")
                for i in range(len(answers)):
                    #print(answers[i].text) #正確答案
                    p=chlist.index(answers[i].text)
                    p=p+1
                    aw+=str(p)
                    #print(aw)
                
                qtype=""
                tagss = ndiv.find('div',class_="question-tag") #題目類型
                if "生物化學"in tagss.text:
                    qtype="生物化學"
                if "解剖學"in tagss.text:
                    qtype="解剖學"
                if "組織學"in tagss.text:
                    qtype="組織學"
                if "胚胎學"in tagss.text:
                    qtype="胚胎學"
                if "微生物學"in tagss.text:
                    qtype="微生物學"
                if "免疫學"in tagss.text:
                    qtype="免疫學"
                if "寄生蟲學"in tagss.text:
                    qtype="寄生蟲學"
                if "公共衛生學"in tagss.text:
                    qtype="公共衛生學"
                if "藥理學"in tagss.text:
                    qtype="藥理學"
                if "病理學"in tagss.text:
                    qtype="病理學"
                if "生理學"in tagss.text:
                    qtype="生理學"
                #print(qtype)

                idgets = ndiv.find('a')
                #print(idgets.get('id'))  #<class 'bs4.element.Tag'> 得到 collect-5833 詳解網址 https://cougarbot.cc/question-view/5833/
                idd=idgets.get('id')
                idd=idd.replace('collect-','')

            
                temporylist.append({"year":str("{}-{}-{}".format(year,t1+1,t2+1)),"id":str(idd),"type":str(qtype),"question":str(qq),"qimg":str(ck1),"A":str(chlist[0]),"B":str(chlist[1]),"C":str(chlist[2]),"D":str(chlist[3]),"answer":str(aw)})

            # print(temporylist)
            with open('題目/{}{}{}.json'.format(year,t1+1,t2+1),'w', encoding='utf8') as file: #存檔
                json.dump(temporylist,file)
            print("{}{}{}done!".format(year,t1+1,t2+1))
'''

year=114
t1=0
for t2 in range(2):
    #print(year,t1,t2)

    url="https://cougarbot.cc/questions/{}-{}-{}/".format(year,t1+1,t2+1)
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    x=0
    divs = soup.find_all('div',class_="question-block")

    temporylist=[]
    #print(len(divs))
    for k in range(len(divs)):
        ndiv=divs[k]
        #print(ndiv)

        questionq=ndiv.find('div',class_="question-Q") 
        #print(questionq.text)   #題目
        qq=questionq.text

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

        choices = ndiv.find('div',class_="question-A")
        #print(choices)
        allchoice = choices.find_all("li")
        chlist=[]
        for i in range(len(allchoice)):
            #print(allchoice[i].text) #選項
            chlist.append(allchoice[i].text)
        aw=""
        answers= choices.find_all("li",class_="primary-color")
        for i in range(len(answers)):
            #print(answers[i].text) #正確答案
            p=chlist.index(answers[i].text)
            p=p+1
            aw+=str(p)
            #print(aw)
        
        qtype=""
        tagss = ndiv.find('div',class_="question-tag") #題目類型
        if "生物化學"in tagss.text:
            qtype="生物化學"
        if "解剖學"in tagss.text:
            qtype="解剖學"
        if "組織學"in tagss.text:
            qtype="組織學"
        if "胚胎學"in tagss.text:
            qtype="胚胎學"
        if "微生物學"in tagss.text:
            qtype="微生物學"
        if "免疫學"in tagss.text:
            qtype="免疫學"
        if "寄生蟲學"in tagss.text:
            qtype="寄生蟲學"
        if "公共衛生學"in tagss.text:
            qtype="公共衛生學"
        if "藥理學"in tagss.text:
            qtype="藥理學"
        if "病理學"in tagss.text:
            qtype="病理學"
        if "生理學"in tagss.text:
            qtype="生理學"
        #print(qtype)

        idgets = ndiv.find('a')
        #print(idgets.get('id'))  #<class 'bs4.element.Tag'> 得到 collect-5833 詳解網址 https://cougarbot.cc/question-view/5833/
        idd=idgets.get('id')
        idd=idd.replace('collect-','')

    
        temporylist.append({"year":str("{}-{}-{}".format(year,t1+1,t2+1)),"id":str(idd),"type":str(qtype),"question":str(qq),"qimg":str(ck1),"A":str(chlist[0]),"B":str(chlist[1]),"C":str(chlist[2]),"D":str(chlist[3]),"answer":str(aw)})

    # print(temporylist)
    with open('題目/{}{}{}.json'.format(year,t1+1,t2+1),'w', encoding='utf8') as file: #存檔
        json.dump(temporylist,file)
    print("{}{}{}done!".format(year,t1+1,t2+1))