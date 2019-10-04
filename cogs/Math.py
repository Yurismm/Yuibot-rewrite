import discord
from discord.ext import commands

class Math(commands.Cog):
    '''
    Math commands
    '''

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def add(self, ctx, a: int, b: int):
        """Add two numbers to each other"""
        await ctx.send(a+b)

    @commands.command()
    async def multiply(self, ctx, a: int, b: int):
        """Multiply two numbers with each other"""
        await ctx.send(a*b)

    @commands.command()
    async def subtract(self, ctx,a: int,b:int):
        """Subtract two numbers by each other"""
        await ctx.send(a-b)

    @commands.command()
    async def divide(self, ctx,a:int,b:int):
        """Divide two numbers by each other"""
        await ctx.send(a/b)

    @commands.command()
    async def square(self, ctx,a:int):
        """Square a number"""
        await ctx.send(a*a)

    @commands.command()
    async def half(self,ctx,a:int):
        """Half a number"""
        await ctx.send(a/2)


    @commands.command()
    async def double(self,ctx,a:int):
        """Double a number"""
        await ctx.send(a*2)

    @commands.command()
    async def triple(self,ctx,a:int):
        """Triple a number"""
        await ctx.send(a*3)

 










def setup(bot):
    bot.add_cog(Math(bot))
