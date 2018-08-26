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
        guild.create_role(name="Test")

    @commands.command(name='givetest')
    async def givetest(self, ctx):
        role = discord.utils.get(ctx.guild.roles, name="Test")
        user = ctx.message.author
        await user.add_roles(role)







def setup(bot):
    bot.add_cog(sudo(bot))
