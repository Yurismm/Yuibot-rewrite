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



    
# Setup bot
def setup(bot):
    bot.add_cog(useful(bot))
