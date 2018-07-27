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

    @commands.command()
    async def square(self, ctx,a:int):
        await ctx.send(a*a)

    @commands.command()
    async def half(self,ctx,a:int):
        await ctx.send(a/2)


    @commands.command()
    async def double(self,ctx,a:int):
        await ctx.send(a*2)

    @commands.command()
    async def urAnus(self,ctx,a:int)
        await ctx.send(a*8/6*4/3*33/4*9/2-3)
        
   








def setup(bot):
    bot.add_cog(Math(bot))