import os
import time

import discord
from decouple import config
from discord import app_commands

import autoRespone
import slashGroup


class aClient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)

    #當機器人完成啟動時
    async def on_ready(self):
        await tree.sync()
        print('機器人登入成功，目前登入身份：', self.user)
        
    #當有訊息時
    async def on_message(self, message):
        #排除自己的訊息，避免陷入循環
        if message.author == self.user:
            return
            
        if message.content != '':
            #自動回應字典訊息 ex.笑死
            response = autoRespone.response(message.content)
            if response != '':
                now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                print(now, message.author.name)
                print(message.content)
                await message.channel.send(response)
                

client = aClient()

tree = app_commands.CommandTree(client)

### 載入指令群組 ###
tree.add_command(slashGroup.ai())

##################

### 載入單一指令區塊 ###
#查詢南部公務人員會計職缺
#/back_tainan
@tree.command(name="back_tainan", description="查詢南部公務人員會計職缺")
async def back_tainan(interaction: discord.Interaction) -> None:
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(now, interaction.user, '查詢職缺')
    
    await interaction.response.send_message('連線中...')
    os.chdir("D:\opening_alert")
    os.startfile("runSchedule.bat")
    await interaction.channel.send('查詢完畢')

#更改機器人狀態
#/change_presence
@tree.command(name="change_presence", description="更改機器人狀態")
async def change_presence(interaction: discord.Interaction, text: str) -> None:
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(now, interaction.user, '更改狀態')
    print(text)
    
    game = discord.Game(text)
    await interaction.client.change_presence(activity=game)
    await interaction.response.send_message('更改完畢')

##################


client.run(config('DISCORD_BOT_TOKEN'))