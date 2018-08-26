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

    @commands.command(name='addtest')
    async def addtest(self, ctx):
        user = ctx.message.author
        role = discord.utils.get(user.server.roles, name="Test")
        await ctx.add_roles(user, role)







def setup(bot):
    bot.add_cog(sudo(bot))
