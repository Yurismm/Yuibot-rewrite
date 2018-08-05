import discord
from discord.ext import commands

class animals():
    def __init__(self, bot):
        self.bot = bot


@commands.command()
async def cat(ctx,src,self):
    src="http://thecatapi.com/api/images/get?format=src&type=gif"
    embed = discord.Embed(color = 0xf76ce4)
    embed.set_author(name = "A cat...Nothing serious")
    embed.set_image(url = src)
    embed.set_footer(text="Cat why not")
    await ctx.send (embed = embed)















def setup(bot):
    bot.add_cog(animals(bot))