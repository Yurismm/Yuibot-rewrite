import discord
import asyncio
from discord.ext import commmands

class useful:
    '''
    Useful commands - for server administation and for other uses
    '''
    def __init__(self,bot):
        self.bot = bot

@commmands.command()
async def say(ctx, *, content:str):
    '''Make's Yui say any message you put'''
    await ctx.send(content)


def setup(bot):
    bot.add_cog(useful(bot))