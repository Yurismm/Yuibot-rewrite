import discord
import asyncio
from discord.ext import commands
import *


class useful:
    '''
    Useful commands
    '''

    def __init__(self, bot):
        self.bot = bot


@commands.command()
async def say(ctx, saymsg : str = None):
    """Makes me say something"""
    if saymsg == None:
        return await ctx.send('Please provide something for the bot to say.')
        
    else: 
        await ctx.send(saymsg)


    
#Setup bot
def setup(bot):
    bot.add_cog(useful(bot))
