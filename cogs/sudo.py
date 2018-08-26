import discord
from discord.ext import commands


class sudo:
    '''
    Developer only commands to make a server suffer
    '''

    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def roleme(self, ctx):
        author = ctx.message.author
        await ctx.create_role(author.server, name="Test 12")





def setup(bot):
    bot.add_cog(sudo(bot))
