import discord
from discord.ext import commands


class Useful:
    '''
    Useful commands
    '''

    def __init__(self,bot):
        self.bot = bot





def setup(bot):
    bot.add_cog(Useful(bot))
