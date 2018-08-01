import discord
from discord.ext import commands

class Math:
    '''
    Math commands
    '''

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def afk(self,ctx,a:int):
        '''@user is AFK: reason'''
        await ctx.send(ctx.author.name'is AFK:' a)
