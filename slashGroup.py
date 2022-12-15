import time

import discord
from discord import app_commands

import openAIChat


#interaction.channel.send 為不受限制回傳至聊天室
#interaction.response.send_message 為一定要 10 秒內先回復是否收到

#Ai 指令群組
class ai(app_commands.Group):
    #/ai chat
    @app_commands.command(name="chat", description="輸入文字與 openAI 取得訊息")
    async def chat(self, interaction: discord.Interaction, text: str) -> None:
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print(now, interaction.user, '說：')
        print(text)
        
        await interaction.response.send_message('休蛋幾累 思考中...')
        response = openAIChat.openai_response(text)
        await interaction.channel.send(str(response))
        
    #/ai img
    @app_commands.command(name="img", description="輸入描述給 openAI 生成圖片")
    async def img(self, interaction: discord.Interaction, text: str) -> None:
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print(now, interaction.user, '說：')
        print(text)
        
        await interaction.response.send_message('休蛋幾累 生成中...')
        response = openAIChat.openai_generalIMG(text)
        await interaction.channel.send(str(response))