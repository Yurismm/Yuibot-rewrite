import discord
import math
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

    @commands.command()
    async def square(self, ctx,a:int):
        await ctx.send(a*a)

    @commands.command()
    async def squareroot(self,ctx,x:int)
        await ctx.send(math.sqrt(x))







def setup(bot):
    bot.add_cog(Math(bot))