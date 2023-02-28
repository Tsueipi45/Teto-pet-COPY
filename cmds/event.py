from core.classes import Cog_Extension
from discord.ext import commands
import json

#jfile讀取
with open('settings.json','r',encoding='utF8') as jfile:
    jdata = json.load(jfile)

#歡迎 and 再見
class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self,member,data):
        channel = self.bot.get_channel(int(jdata['Welcome_goodbye_channel']))
        await channel.send(f'歡迎 {member.mention} 來到 一個普通的DC群')
        
        guild = self.bot.get_guild(data.guild_id)
        data.member.add_roles(guild.get_role(686533520109076496))

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(int(jdata['Welcome_goodbye_channel']))
        await channel.send(f'{member.name} 離開了，期望能再次見到您')


#不可以色色        
    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content.endswith("色色") and msg.author != self.bot.user:
            await msg.reply("不可以色色")

#COG運行指令
def setup(bot):
    bot.add_cog(Event(bot))
