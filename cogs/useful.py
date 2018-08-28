import discord
import asyncio
from discord.ext import commmands

class useful:
    '''
    Useful commands - for server administation and for other uses
    '''
    def __init__(self,bot):
        self.bot = bot

@commmands.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    return await ctx.send(mesg)
