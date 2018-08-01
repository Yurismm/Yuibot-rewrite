import discord
from discord.ext import commands


class useful:
    '''
    Useful commands
    '''

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, saymsg):
        """Makes me say something"""
        if not saymsg:
            return await ctx.send('Please provide something for the bot to say.')
        await ctx.send(saymsg)






# Setup bot
def setup(bot):
    bot.add_cog(useful(bot))
