import discord
from discord.ext import commands

class Math:
    '''
    Math commands
    '''

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def add(self, ctx, a: int, b: int):
        await ctx.send(a+b)

    @commands.command()
    async def multiply(self, ctx, a: int, b: int):
        await ctx.send(a*b)

    @commands.command()
    async def subtract(self, ctx,a: int,b:int):
        await ctx.send(a-b)

    @commands.command()
    async def divide(self, ctx,a:int,b:int):
        await ctx.send(a/b)




def setup(bot):
    bot.add_cog(Math(bot))