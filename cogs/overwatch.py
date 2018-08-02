import discord
import asyncio
import discord
from discord.ext import commands
import overwatch.stats

class Overwatch:
    '''
    Overwatch commands
    '''



@commands.command()
async def overwatchstats(self,ctx, user: str = None, stats):

    stats = overwatch.stats.query('pc', user)
    
    if user == None:
        await ctx.send("You need to use a blizzard username including its tag to search overwatch stats"

    await ctx.send("'''"stats"'''")


