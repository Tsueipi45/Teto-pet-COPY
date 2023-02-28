import discord
from discord.ext.commands import Cog
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument
from core.classes import Cog_Extension
import math
from math import factorial

class Math (Cog_Extension):
    
#-add
    @commands.command(pass_context=True)
    async def add(self,ctx,a: int,b: int):
        em = discord.Embed(title=f'{a} 加 {b} 的值', description=f'{a} + {b} = {a+b}', color=ctx.author.color)
        await ctx.send (embed = em) 
    @add.error
    async def clear_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            em = discord.Embed(title=f'錯誤', description=f'請給我正確數量的數字', color=ctx.author.color)
            await ctx.send (embed = em)

#-minus
    @commands.command(pass_context=True)
    async def minus(self,ctx,a: int,b: int):
        em = discord.Embed(title=f'{a} 減 {b} 的值', description=f'{a} - {b} = {a-b}', color=ctx.author.color)
        await ctx.send (embed = em) 
    @minus.error
    async def clear_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            em = discord.Embed(title=f'錯誤', description=f'請給我正確數量的數字', color=ctx.author.color)
            await ctx.send (embed = em)

#-times
    @commands.command(pass_context=True)
    async def times(self,ctx,a: int,b: int):
        em = discord.Embed(title=f'{a} 乘以 {b} 的值', description=f'{a} x {b} = {a*b}', color=ctx.author.color)
        await ctx.send (embed = em) 
    @times.error
    async def clear_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            em = discord.Embed(title=f'錯誤', description=f'請給我正確數量的數字', color=ctx.author.color)
            await ctx.send (embed = em)

#-divide
    @commands.command(pass_context=True)
    async def divide(self,ctx,a: int,b: int):
        em = discord.Embed(title=f'{a} 除以 {b} 的值', description=f'{a} / {b} = {a/b}', color=ctx.author.color)
        await ctx.send (embed = em) 
    @divide.error
    async def clear_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            em = discord.Embed(title=f'錯誤', description=f'請給我正確數量的數字', color=ctx.author.color)
            await ctx.send (embed = em)

#-calculate
    @commands.command(pass_context=True)
    async def calculate(self,ctx, *,calculate):
        await ctx.send(eval(calculate))

#-factorial
    @commands.command(pass_context=True)
    async def factorial(self,ctx, *,a: int):
        if a > 25:
            await ctx.send(f'數字太大了,我會爆炸！')
        else:
            await ctx.send(f'{a} 的階乘值為: {factorial(a)}')
    @factorial.error
    async def clear_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            em = discord.Embed(title=f'錯誤', description=f'請給我一個數字', color=ctx.author.color)
            await ctx.send (embed = em)


def setup(bot):
    bot.add_cog(Math(bot))
