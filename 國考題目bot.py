import discord
from discord.ext import commands ,tasks 
from discord.ui import Select ,View ,Button
from discord import app_commands
import json
import random
import os
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)
bot.remove_command("help")

TOKEN = os.getenv("DISCORD_TOKEN")
@bot.event
async def on_ready():
    print(">> bot on <<")
    synced = await bot.tree.sync()

@bot.tree.command(name="挑科國考隨機題目",description="隨機題目")
@app_commands.choices(題目類型=[
  discord.app_commands.Choice(name='生物化學', value=1),
  discord.app_commands.Choice(name='解剖學', value=2),
  discord.app_commands.Choice(name='組織學', value=3),
  discord.app_commands.Choice(name='胚胎學',value=4),
  discord.app_commands.Choice(name="微生物學",value=5),
  discord.app_commands.Choice(name="免疫學",value=6),
  discord.app_commands.Choice(name="寄生蟲學",value=7),
  discord.app_commands.Choice(name="公共衛生學",value=8),
  discord.app_commands.Choice(name="藥理學",value=9),
  discord.app_commands.Choice(name="病理學",value=10),
  discord.app_commands.Choice(name="生理學",value=11)
])
async def 挑科國考隨機題目(interaction:discord.Interaction,題目類型:discord.app_commands.Choice[int]):
  us=interaction.user
  with open('題目/allquestion.json','r', encoding='utf8') as file:
    qdata =json.load(file)
  #print(qdata)
  yel=[]
  idl=[]
  typel=[]
  ql=[]
  qimgl=[]

  Al=[]
  Bl=[]
  Cl=[]
  Dl=[]
  anl=[]

  for i in range(len(qdata)):
    if qdata[i]["type"]==題目類型.name:
      yel.append(qdata[i]["year"])
      idl.append(qdata[i]["id"])
      typel.append(qdata[i]["type"])
      ql.append(qdata[i]["question"])
      qimgl.append(qdata[i]["qimg"])
      Al.append(qdata[i]["A"])
      Bl.append(qdata[i]["B"])
      Cl.append(qdata[i]["C"])
      Dl.append(qdata[i]["D"])
      anl.append(qdata[i]["answer"])
  def allc():  
    global embed ,rnb
    rnb = random.randint(0,len(ql)-1)
    #rnb=75
    embed=discord.Embed(color=0x0080ff,title="{} {}".format(yel[rnb],typel[rnb]),description=ql[rnb])
    if qimgl[rnb]!=str(0):
      #print(qimgl[rnb])
      file_path = "圖片/{}.png".format(qimgl[rnb])  # 本地圖片路徑
      file = discord.File(file_path, filename="image.jpg")
      embed.set_image(url="attachment://image.jpg")
    embed.add_field(name="(A)", value=Al[rnb], inline=False)  
    embed.add_field(name="(B)", value=Bl[rnb], inline=False)  
    embed.add_field(name="(C)", value=Cl[rnb], inline=False)  
    embed.add_field(name="(D)", value=Dl[rnb], inline=False)  
  allc()
  
  next=Button(label="下一題",style=discord.ButtonStyle.green)
  a=Button(label="答案",style=discord.ButtonStyle.green)
  k=Button(label="結束",style=discord.ButtonStyle.red)
  async def  callback1(interaction):
    if us==interaction.user:
        allc()
        await interaction.response.edit_message(embed=embed)
    else :
      await interaction.response.send_message("<a:noU:1096707079345020938>",ephemeral=True)
  async def  callback2(interaction):
    if us==interaction.user:
        ans=anl[rnb]
        ans=ans.replace("1","A").replace("2","B").replace("3","C").replace("4","D")
        embed.add_field(name="正確答案 為({})".format(ans), value="若詳解跑掉請見 https://cougarbot.cc/question-view/{}/".format(idl[rnb]), inline=False) 
        await interaction.response.edit_message(embed=embed)
    else :
      await interaction.response.send_message("<a:noU:1096707079345020938>",ephemeral=True)
  async def  callback11(interaction):
    if us==interaction.user:
        await interaction.response.edit_message(delete_after=0.1)
    else :
        await interaction.response.send_message("<a:noU:1096707079345020938>",ephemeral=True)
  view=View(timeout=None)
  view.add_item(a)
  view.add_item(next)
  view.add_item(k)
  next.callback=callback1
  a.callback=callback2
  k.callback=callback11
  await interaction.channel.send(embed=embed,view=view)


  
@bot.tree.command(name="國考隨機題目",description="隨機題目")
async def 國考隨機題目(interaction:discord.Interaction):
  us=interaction.user
  with open('題目/allquestion.json','r', encoding='utf8') as file:
    qdata =json.load(file)
  #print(qdata)
  yel=[]
  idl=[]
  typel=[]
  ql=[]
  qimgl=[]

  Al=[]
  Bl=[]
  Cl=[]
  Dl=[]
  anl=[]

  for i in range(len(qdata)):
      yel.append(qdata[i]["year"])
      idl.append(qdata[i]["id"])
      typel.append(qdata[i]["type"])
      ql.append(qdata[i]["question"])
      qimgl.append(qdata[i]["qimg"])
      Al.append(qdata[i]["A"])
      Bl.append(qdata[i]["B"])
      Cl.append(qdata[i]["C"])
      Dl.append(qdata[i]["D"])
      anl.append(qdata[i]["answer"])
  def allc():  
    global embed ,rnb
    rnb = random.randint(0,len(ql)-1)
    #rnb=75
    embed=discord.Embed(color=0x0080ff,title="{} {}".format(yel[rnb],typel[rnb]),description=ql[rnb])
    if qimgl[rnb]!=str(0):
      #print(qimgl[rnb])
      file_path = "圖片/{}.png".format(qimgl[rnb])  # 本地圖片路徑
      file = discord.File(file_path, filename="image.jpg")
      embed.set_image(url="attachment://image.jpg")
    embed.add_field(name="(A)", value=Al[rnb], inline=False)  
    embed.add_field(name="(B)", value=Bl[rnb], inline=False)  
    embed.add_field(name="(C)", value=Cl[rnb], inline=False)  
    embed.add_field(name="(D)", value=Dl[rnb], inline=False)  
  allc()

  next=Button(label="下一題",style=discord.ButtonStyle.green)
  a=Button(label="答案",style=discord.ButtonStyle.green)
  k=Button(label="結束",style=discord.ButtonStyle.red)
  async def  callback1(interaction):
    if us==interaction.user:
        allc()
        await interaction.response.edit_message(embed=embed)
    else :
      await interaction.response.send_message("<a:noU:1096707079345020938>",ephemeral=True)
  async def  callback2(interaction):
    if us==interaction.user:
        ans=anl[rnb]
        ans=ans.replace("1","A").replace("2","B").replace("3","C").replace("4","D")
        embed.add_field(name="正確答案 為({})".format(ans), value="若詳解跑掉請見 https://cougarbot.cc/question-view/{}/".format(idl[rnb]), inline=False) 
        await interaction.response.edit_message(embed=embed)
    else :
      await interaction.response.send_message("<a:noU:1096707079345020938>",ephemeral=True)
  async def  callback11(interaction):
    if us==interaction.user:
        await interaction.response.edit_message(delete_after=0.1)
    else :
        await interaction.response.send_message("<a:noU:1096707079345020938>",ephemeral=True)
  view=View(timeout=None)
  view.add_item(a)
  view.add_item(next)
  view.add_item(k)
  next.callback=callback1
  a.callback=callback2
  k.callback=callback11
  await interaction.channel.send(embed=embed,view=view)


@bot.tree.command(name="模擬試題",description="模擬考")
@app_commands.choices(年分=[
  discord.app_commands.Choice(name='98', value=1),
  discord.app_commands.Choice(name='99', value=2),
  discord.app_commands.Choice(name='100', value=3),
  discord.app_commands.Choice(name='101',value=4),
  discord.app_commands.Choice(name="102",value=5),
  discord.app_commands.Choice(name="103",value=6),
  discord.app_commands.Choice(name="104",value=7),
  discord.app_commands.Choice(name="105",value=8),
  discord.app_commands.Choice(name="106",value=9),
  discord.app_commands.Choice(name="107",value=10),
  discord.app_commands.Choice(name="108",value=11),
  discord.app_commands.Choice(name="109",value=12),
  discord.app_commands.Choice(name="110",value=13),
  discord.app_commands.Choice(name="111",value=14),
  discord.app_commands.Choice(name="112",value=15),
  discord.app_commands.Choice(name="113",value=16),
  discord.app_commands.Choice(name="114",value=17)
],
月份=[
   discord.app_commands.Choice(name='寒假', value=1),
   discord.app_commands.Choice(name='暑假', value=2)
],
部分=[
   discord.app_commands.Choice(name='醫學一', value=1),
   discord.app_commands.Choice(name='醫學二', value=2)
]
)
async def 模擬試題(interaction:discord.Interaction,年分:discord.app_commands.Choice[int],月份:discord.app_commands.Choice[int],部分:discord.app_commands.Choice[int]):
  us=interaction.user
  try:
    with open('題目/{}{}{}.json'.format(年分.name,月份.value,部分.value),'r', encoding='utf8') as file:
      qdata =json.load(file)
  except:
     await interaction.response.send_message("沒有此檔案")
  adict={}
  yel=[]
  idl=[]
  typel=[]
  ql=[]
  qimgl=[]
  replist=[]
  unlist=[]
  wrglist=[]
  for i in range(100):
      replist.append(i+1)
  Al=[]
  Bl=[]
  Cl=[]
  Dl=[]
  anl=[]
  x=0
  for i in range(len(qdata)):
    yel.append(qdata[i]["year"])
    idl.append(qdata[i]["id"])
    typel.append(qdata[i]["type"])
    ql.append(qdata[i]["question"])
    qimgl.append(qdata[i]["qimg"])
    Al.append(qdata[i]["A"])
    Bl.append(qdata[i]["B"])
    Cl.append(qdata[i]["C"])
    Dl.append(qdata[i]["D"])
    anl.append(qdata[i]["answer"])
  def allc(x):  
    global embed ,rnb
    if x==-1:
        x=99
    elif x==100:
        x=0
    rnb=x
    embed=discord.Embed(color=0x0080ff,title="{} {}".format(yel[rnb],typel[rnb]),description="{}.{}".format(x+1,ql[rnb]))
    if qimgl[rnb]!=str(0):
      #print(qimgl[rnb])
      file_path = "圖片/{}.png".format(qimgl[rnb])  # 本地圖片路徑
      file = discord.File(file_path, filename="image.jpg")
      embed.set_image(url="attachment://image.jpg")
    embed.add_field(name="(A)", value=Al[rnb], inline=False)  
    embed.add_field(name="(B)", value=Bl[rnb], inline=False)  
    embed.add_field(name="(C)", value=Cl[rnb], inline=False)  
    embed.add_field(name="(D)", value=Dl[rnb], inline=False)  
  allc(0)

  last=Button(label="上一題",style=discord.ButtonStyle.green)
  a=Button(label="A",style=discord.ButtonStyle.green)
  b=Button(label="B",style=discord.ButtonStyle.green)
  c=Button(label="C",style=discord.ButtonStyle.green)
  d=Button(label="D",style=discord.ButtonStyle.green)
  e=Button(label="不確定",style=discord.ButtonStyle.blurple)
  next=Button(label="下一題",style=discord.ButtonStyle.green)
  k=Button(label="交卷",style=discord.ButtonStyle.red)
  aw=Button(label="答案",style=discord.ButtonStyle.green)
  async def  callback1(interaction):
    if us==interaction.user:
        allc(rnb-1)
        await interaction.response.edit_message(embed=embed)
    else :
      await interaction.response.send_message("<a:noU:1096707079345020938>",ephemeral=True)
  async def  callback2(interaction):
    if us==interaction.user:
        allc(rnb+1)
        await interaction.response.edit_message(embed=embed)
    else :
      await interaction.response.send_message("<a:noU:1096707079345020938>",ephemeral=True)
  async def  callback3(interaction):
    if us==interaction.user:
        che=rnb+1
        adict["{}".format(che)] = 1
        if che in replist:
          replist.remove(che)  
        replist.sort()
        tol="尚未作答題目:"
        for i in range(len(replist)):
              tol+=" {}".format(replist[i])
        tol+="\n不確定題目:"
        for i in range(len(unlist)):
            tol+=" {}".format(unlist[i])
        await interaction.response.edit_message(content=f'```{tol}```')
    else :
      await interaction.response.send_message("<a:noU:1096707079345020938>",ephemeral=True)
  async def  callback4(interaction):
    if us==interaction.user:
        che=rnb+1
        adict["{}".format(che)] = 2
        if che in replist:
          replist.remove(che)  
        replist.sort()
        tol="尚未作答題目:"
        for i in range(len(replist)):
              tol+=" {}".format(replist[i])
        tol+="\n不確定題目:"
        for i in range(len(unlist)):
            tol+=" {}".format(unlist[i])
        await interaction.response.edit_message(content=f'```{tol}```')
    else :
      await interaction.response.send_message("<a:noU:1096707079345020938>",ephemeral=True)
  async def  callback5(interaction):
    if us==interaction.user:
        che=rnb+1
        adict["{}".format(che)] = 3
        if che in replist:
          replist.remove(che)  
        replist.sort()
        tol="尚未作答題目:"
        for i in range(len(replist)):
              tol+=" {}".format(replist[i])
        tol+="\n不確定題目:"
        for i in range(len(unlist)):
            tol+=" {}".format(unlist[i])
        await interaction.response.edit_message(content=f'```{tol}```')
    else :
      await interaction.response.send_message("<a:noU:1096707079345020938>",ephemeral=True)
  async def  callback6(interaction):
    if us==interaction.user:
        che=rnb+1
        adict["{}".format(che)] = 4
        if che in replist:
          replist.remove(che)  
        replist.sort()
        tol="尚未作答題目:"
        for i in range(len(replist)):
              tol+=" {}".format(replist[i])
        tol+="\n不確定題目:"
        for i in range(len(unlist)):
            tol+=" {}".format(unlist[i])
        await interaction.response.edit_message(content=f'```{tol}```')
    else :
      await interaction.response.send_message("<a:noU:1096707079345020938>",ephemeral=True)
  async def  callback7(interaction):
    if us==interaction.user:
        che=rnb+1
        if che not in unlist:
          unlist.append(che)  
        else:
          unlist.remove(che)
        unlist.sort()
        replist.sort()
        tol="尚未作答題目:"
        for i in range(len(replist)):
            tol+=" {}".format(replist[i])
        tol+="\n不確定題目:"
        for i in range(len(unlist)):
            tol+=" {}".format(unlist[i])
        await interaction.response.edit_message(content=f'```{tol}```')
    else :
      await interaction.response.send_message("<a:noU:1096707079345020938>",ephemeral=True)
  async def  callback8(interaction):
    if us==interaction.user:
        
        tol="作答紀錄:\n"
        for i in range(100):
          cc=adict.get("{}".format(i+1))
          if str(cc)=="None":
                wrglist.append(i+1)
                cc="X"
          elif str(cc)=="1":
                if str(cc) not in anl[i]:
                   wrglist.append(i+1)   
                cc="A"
          elif str(cc)=="2":
                if str(cc) not in anl[i]:
                  wrglist.append(i+1)  
                cc="B"
          elif str(cc)=="3":
                if str(cc) not in anl[i]:
                    wrglist.append(i+1)  
                cc="C"
          elif str(cc)=="4":
                if str(cc) not in anl[i]:
                  wrglist.append(i+1)  
                cc="D"
          tol+=str(cc)
          if i  % 10 == 4:
                tol+=" "
          elif i % 10 == 9:
                tol+="\n"

        tol+="\n得分:{}".format(100-len(wrglist))
        tol+="\n回答錯誤題號:\n"
        for i in range(len(wrglist)):
          tol+="{} ".format(wrglist[i])
          if i % 10 == 9:
                tol+="\n"

        view.remove_item(a)
        view.remove_item(b)
        view.remove_item(c)
        view.remove_item(d)
        view.remove_item(e)
        view.remove_item(k)
        view.add_item(aw)
        await interaction.response.edit_message(content=f'```{tol}```',view=view)
    else :
      await interaction.response.send_message("<a:noU:1096707079345020938>",ephemeral=True)
  async def  callback9(interaction):
    if us==interaction.user:
        ans=anl[rnb]
        ans=ans.replace("1","A").replace("2","B").replace("3","C").replace("4","D")
        embed.add_field(name="正確答案 為({})".format(ans), value="若詳解跑掉請見 https://cougarbot.cc/question-view/{}/".format(idl[rnb]), inline=False) 
        await interaction.response.edit_message(embed=embed)
  view=View(timeout=None)
  view.add_item(e)
  view.add_item(a)
  view.add_item(b)
  view.add_item(c)
  view.add_item(d)
  view.add_item(last)
  view.add_item(next)
  view.add_item(k)
  last.callback=callback1
  next.callback=callback2
  a.callback=callback3
  b.callback=callback4
  c.callback=callback5
  d.callback=callback6
  e.callback=callback7
  k.callback=callback8
  aw.callback=callback9
  await interaction.channel.send(embed=embed,view=view)

bot.run(TOKEN)