import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

#jfile讀取
with open('settings.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

#傳送裝置內隨機圖片
class React(Cog_Extension):
    @commands.command()
    async def pic(self, ctx):
        random_pic = random.choice(jdata('pic'))
        pic = discord.file(random_pic)
        await ctx.send(file=pic)

    @commands.command()
    async def url_pic(self, ctx):
        random_pic = random.choice(jdata('url_pic'))
        await ctx.send(random_pic)

#COG運行指令
def setup(bot):
    bot.add_cog(React(bot))