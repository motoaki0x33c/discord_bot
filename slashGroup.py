import os
import time

import discord
from discord import app_commands

import openAIChat

#interaction.channel.send 為不受限制回傳至聊天室
#interaction.response.send_message 為一定要 10 秒內先回復是否收到

#Angel指令群組 /a
class a(app_commands.Group):
    ### Ai 指令群組 ###
    
    ai = app_commands.Group(name="ai", description="AI 指令集")
    
    #AI聊天 /ai chat
    @ai.command(name="chat", description="輸入文字與 openAI 取得廢文")
    async def chat(self, interaction: discord.Interaction, text: str) -> None:
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print(now, interaction.user, '說：')
        print(text)
        
        await interaction.channel.send('> *' + text + '*')
        await interaction.response.send_message('休蛋幾累 思考中...')
        response = openAIChat.openai_response(text, temperature=0.9, presence_penalty=0.6)
        await interaction.channel.send(str(response))
        
    #AI生圖片 /ai img
    @ai.command(name="img", description="輸入描述給 openAI 生成圖片")
    async def img(self, interaction: discord.Interaction, text: str) -> None:
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print(now, interaction.user, '說：')
        print(text)
        
        await interaction.channel.send('> *' + text + '*')
        await interaction.response.send_message('休蛋幾累 生成中...')
        response = openAIChat.openai_generalIMG(text)
        await interaction.channel.send(str(response))
        
    #AI問答 /ai anwser
    @ai.command(name="anwser", description="輸入文字與 openAI 取得精準問答")
    async def anwser(self, interaction: discord.Interaction, text: str) -> None:
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print(now, interaction.user, '說：')
        print(text)
        
        await interaction.channel.send('> *' + text + '*')
        await interaction.response.send_message('休蛋幾累 思考中...')
        response = openAIChat.openai_response(text)
        await interaction.channel.send(str(response))
        
    #AI程式方面 /ai program
    @ai.command(name="program", description="輸入文字與 openAI 取得程式面向的問答")
    async def program(self, interaction: discord.Interaction, text: str) -> None:
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print(now, interaction.user, '說：')
        print(text)
        
        await interaction.channel.send('> *' + text + '*')
        await interaction.response.send_message('休蛋幾累 思考中...')
        response = openAIChat.openai_response(text, model='code-davinci-002')
        await interaction.channel.send(str(response))
    
    ### 單一指令 ###
    
    #查詢南部公務人員會計職缺 /back_tainan
    @app_commands.command(name="back_tainan", description="查詢南部公務人員會計職缺")
    async def back_tainan(self, interaction: discord.Interaction) -> None:
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print(now, interaction.user, '查詢職缺')
        
        await interaction.response.send_message('連線中...')
        os.chdir("D:\opening_alert")
        os.startfile("runSchedule.bat")
        await interaction.channel.send('查詢完畢')

    #更改機器人狀態 /change_presence
    @app_commands.command(name="change_presence", description="更改機器人狀態")
    async def change_presence(self, interaction: discord.Interaction, text: str) -> None:
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print(now, interaction.user, '更改狀態')
        print(text)
        
        game = discord.Game(text)
        await interaction.client.change_presence(activity=game)
        await interaction.response.send_message('更改完畢')