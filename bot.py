import discord
from discord import file
from discord.ext import commands
import json
import os
from discord import Intents

intents = Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='-',intents = intents)

#機器人準備
@bot.event
async def on_ready():
    print (">>Bot is online<<")

#jfile讀取
with open('settings.json','r',encoding='utF8') as jfile:
    jdata = json.load(jfile)


@bot.event 
async def on_command_error(ctx, error): 
    if isinstance(error, commands.CommandNotFound): 
        em = discord.Embed(title=f"錯誤!!!", description=f"查無此指令", color=ctx.author.color) 
        await ctx.send(embed=em)

#其他py檔案讀取
for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

#-load
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} 已載入')

#-unload
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} 已卸載')
    
#-reload
@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} 已重新載入')

#運轉機器人代號
if __name__ == "__main__":
    bot.run(jdata["TOKEN"])
