import discord
from discord.ext import commands


class sudo:
    '''
    Developer only commands to make a server suffer
    '''

    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(name='roleme')
    async def roleme(self, ctx):
        guild = ctx.guild
        await guild.create_role(name="Test")






def setup(bot):
    bot.add_cog(sudo(bot))
