import discord
import asyncio
from discord.ext import commands


class useful:
    '''
    Useful commands
    '''

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(ctx, saymsg):
        """Makes me say something"""
        if not saymsg:
            return await ctx.send('Please provide something for the bot to say.')
        await ctx.send(saymsg)

    @bot.command(pass_context=True)
    async def arole(ctx, *args):
        member = ctx.message.author.id
        input = ' '.join(args)
        role = get(member.server.roles, name=input)
        &eval await guild.get_member(member).add_roles(discord.utils.get(ctx.guild.roles, name =role))


    @bot.command(pass_context=True)
    async def arole(ctx, *args):
        member = ctx.message.author.id
        input = ' '.join(args)
        role = get(member.server.roles, name=input)
        &eval await guild.get_member(member).remove_roles(discord.utils.get(ctx.guild.roles, name =role))

# Setup bot
def setup(bot):
    bot.add_cog(useful(bot))
