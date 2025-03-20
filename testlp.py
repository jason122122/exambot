# for y1 in range(2):
#     year=89+y1
#     for t1 in range(2):
#         for t2 in range(2):
#             print(year,t1,t2)



# import json
# import random
# with open('題目/11011.json','r', encoding='utf8') as file:
#     qdata =json.load(file)
# #print(qdata)
# yel=[]
# idl=[]
# typel=[]
# ql=[]
# qimgl=[]

# Al=[]
# Bl=[]
# Cl=[]
# Dl=[]
# anl=[]

# for i in range(len(qdata)):
#     yel.append(qdata[i]["year"])
#     idl.append(qdata[i]["id"])
#     typel.append(qdata[i]["type"])
#     ql.append(qdata[i]["question"])
#     qimgl.append(qdata[i]["qimg"])
#     Al.append(qdata[i]["A"])
#     Bl.append(qdata[i]["B"])
#     Cl.append(qdata[i]["C"])
#     Dl.append(qdata[i]["D"])
#     anl.append(qdata[i]["answer"])
# rnb = random.randint(0,len(ql)-1)
# #rnb=75
# body=""
# body+="{} {}\n{}\n(A){}\n(B){}\n(C){}\n(D){}".format(yel[rnb],typel[rnb],ql[rnb],Al[rnb],Bl[rnb],Cl[rnb],Dl[rnb])
# print(body)
# if qimgl[rnb]!=str(0):
#     print(qimgl[rnb])

# import random
# def allc():  
#     global b
#     b=random.randint(0,100)
# allc()
# print(b)
# allc()
# print(b)
adict={'1': 2, '2': 1}
che=1
tol="作答紀錄:\n"
for i in range(5):
    cc=adict.get("{}".format(i+1))
    if str(cc)=="None":
        cc="X"
    elif str(cc)=="1":
        cc="A"
    elif str(cc)=="2":
        cc="B"
    elif str(cc)=="3":
        cc="C"
    elif str(cc)=="4":
        cc="D"
    print(cc)


print(adict)