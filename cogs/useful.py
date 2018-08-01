import discord
from discord.ext import commands


class useful:
    '''
    Useful commands
    '''

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def says(self, saymsg):
        """Makes me say something"""
        if not saymsg:
            return await self.bot.say('Please provide something for the bot to say.')
        await self.bot.say(saymsg)






# Setup bot
def setup(bot):
    bot.add_cog(useful(bot))
