import discord
import asyncio
import nekos
from discord.ext import commands


class rule34:
    '''
    Rule34 commands
    '''

    def __init__(self, bot):
        self.bot = bot

@commands.command()
async def lewd(self, ctx, lewd):

    if ctx.channel.is_nsfw():
    ctx.send("You can't use this command, Put the bot in a nsfw channel, and you will be able to use this command")

    else:
        lewd = img('lewdk')
        embed = discord.Embed(color = 0xf76ce4)
        embed.set_author(name = "From Neko Life")
        embed.set_image(url = lewd)
        embed.set_footer(text='Made By Tom')
        await ctx.send(embed)








def setup(bot):
    bot.add_cog(rule34(bot))
