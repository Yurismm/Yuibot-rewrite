import discord
from discord.ext import commands



class useful:
    '''
    Useful Commands
    '''
    def __init__(self, bot):
        self.bot = bot


        @bot.command()
        async def say(saymsg):
            """Makes me say something"""
            if not saymsg:
                return await ctx.send('Please provide me with something to say.')
            await bot.say(saymsg)


def setup(bot):
    bot.add_cog(Fun(bot))
