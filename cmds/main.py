import discord
from discord.ext.commands import Cog
from discord.ext import commands
from discord.ext.commands.converter import PartialMessageConverter
from discord.ext.commands.errors import MissingRequiredArgument
from core.classes import Cog_Extension
import random

class Main (Cog_Extension):

#-ping
    @commands.command(pass_context=True)
    async def ping(self,ctx):
        await ctx.send(f'延遲為: {round(self.bot.latency*1000)}(毫秒)')
        await ctx.send(f'The PING is: {round(self.bot.latency*1000)}(ms)')

#-say
    @commands.command(pass_context=True)
    async def say(self,ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)
    @say.error
    async def clear_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("請告訴我要說些什麼")

#-purge
    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def purge(self,ctx, amount: int):
        await ctx.channel.purge(limit=amount+1)
        await ctx.message.delete()
        await ctx.send(f'已刪除 {amount} 個訊息. 操縱者: {ctx.author.mention}.', delete_after = 15)

    @purge.error
    async def clear_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("你沒有權限執行這個動作")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("請給我一個數字")

#-choose
    @commands.command(pass_context=True)
    async def choose(self,ctx, *options):
        random_option = random.choice(options)
        em = discord.Embed(title=f'選項有 : {options}', description=f'我選的是 : {random_option}', color=ctx.author.color)
        await ctx.send (embed = em) 

#-flip a coin
    @commands.command(pass_context=True)
    async def flip(self,ctx):
        coin = ("正面","反面")
        random_coin = random.choice(coin)
        em = discord.Embed(title=f'擲硬幣', description=f'硬幣落地時朝上的是: {random_coin}', color=ctx.author.color)
        await ctx.send (embed = em) 

#-COG運行指令
def setup(bot):
    bot.add_cog(Main(bot))
