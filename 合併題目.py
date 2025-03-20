
import json
temporylist=[]
for y1 in range(16):
    year=98+y1
    for t1 in range(2):
        for t2 in range(2):
            with open('題目/{}{}{}.json'.format(year,t1+1,t2+1), 'r', encoding='utf8') as file:
                qfile = json.load(file)
                for i in range(len(qfile)):
                    idd=qfile[i]["id"]
                    qtype=qfile[i]["type"]
                    qq=qfile[i]["question"]
                    ck1=qfile[i]["qimg"]
                    aa=qfile[i]["A"]
                    bb=qfile[i]["B"]
                    cc=qfile[i]["C"]
                    dd=qfile[i]["D"]
                    aw=qfile[i]["answer"]
                    temporylist.append({"year":str("{}-{}-{}".format(year,t1+1,t2+1)),"id":str(idd),"type":str(qtype),"question":str(qq),"qimg":str(ck1),"A":str(aa),"B":str(bb),"C":str(cc),"D":str(dd),"answer":str(aw)})
year=114
t1=0
for t2 in range(2):
    with open('題目/{}{}{}.json'.format(year,t1+1,t2+1), 'r', encoding='utf8') as file:
        qfile = json.load(file)
        for i in range(len(qfile)):
            idd=qfile[i]["id"]
            qtype=qfile[i]["type"]
            qq=qfile[i]["question"]
            ck1=qfile[i]["qimg"]
            aa=qfile[i]["A"]
            bb=qfile[i]["B"]
            cc=qfile[i]["C"]
            dd=qfile[i]["D"]
            aw=qfile[i]["answer"]
            temporylist.append({"year":str("{}-{}-{}".format(year,t1+1,t2+1)),"id":str(idd),"type":str(qtype),"question":str(qq),"qimg":str(ck1),"A":str(aa),"B":str(bb),"C":str(cc),"D":str(dd),"answer":str(aw)})
with open('題目/allquestion.json','w', encoding='utf8') as file: #存檔
    json.dump(temporylist,file)
print("allquestion done!")