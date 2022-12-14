import os
import time

import discord
from decouple import config

import autoRespone
import openAIChat

#調用 event 函式庫
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
#當機器人完成啟動時
async def on_ready():
    print('機器人登入成功，目前登入身份：', client.user)

@client.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入循環
    if message.author == client.user:
        return
        
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    if message.content != '':
        #自動回應字典訊息
        response = autoRespone.response(message.content)
        if response != '':
            print(str(now) + ' ' + str(message.author.name))
            print(message.content)
            await message.channel.send(response)

        #更改機器人狀態
        if message.content.startswith('Angel正在玩'):
            target = message.content.split(" ",2)
            if len(target) > 1:
                game = discord.Game(target[1])
                await client.change_presence(activity=game)

        #查詢南部公務人員會計職缺
        if message.content.startswith('回台南'):
            print(str(now) + ' ' + str(message.author.name))
            print(message.content)
            await message.channel.send('連線中...')
            os.chdir("D:\opening_alert")
            os.startfile("runSchedule.bat")
        
        #呼叫openAI生成文字
        if message.content.startswith('87AI:'):
            print(str(now) + ' ' + str(message.author.name))
            print(message.content)
            await message.channel.send('休蛋幾累 思考中...')
            response = openAIChat.openai_response(message.content.split("87AI:")[1])
            await message.channel.send(str(response))
        
        #呼叫openAI生成圖片
        if message.content.startswith('IMG87AI:'):
            print(str(now) + ' ' + str(message.author.name))
            print(message.content)
            await message.channel.send('休蛋幾累 生成中...')
            response = openAIChat.openai_generalIMG(message.content.split("IMG87AI:")[1])
            await message.channel.send(str(response))


@client.event
#錯誤訊息
async def on_error(event, *args, **kwargs):
    error_msg = args[0] #Gets the message object
    print('error:')
    print(error_msg)

client.run(config('DISCORD_BOT_TOKEN'))
