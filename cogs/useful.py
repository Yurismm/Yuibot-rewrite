import discord
from discord.ext import commands

class Math:
    '''
    Math commands
    '''

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def afk(ctx):
        '''@user is AFK: reason'''
        async def add(self,ctx,a:int):
            await ctx.send(ctx.author.name'is AFK:' a)
