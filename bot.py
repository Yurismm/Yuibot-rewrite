import discord
from discord.ext import commands
from motor.motor_asyncio import AsyncIOMotorClient
import re
import json
import logging
import os
import aiohttp
import sys

db = AsyncIOMotorClient(os.environ.get('MONGODB'))


async def getprefix(bot, message):
    if isinstance(message.channel, discord.DMChannel): return "*"
    x = await db.yui.prefix.find_one({"id": str(message.guild.id)})
    pre = x['prefix'] if x is not None else '*'
    match = re.match(f"<@!?{bot.user.id}> ", message.content)
    return match.group() if match else pre

bot = commands.Bot(command_prefix=getprefix)
bot.db = db.yui
logging.basicConfig(level=logging.ERROR)
bot.session = aiohttp.ClientSession(loop=bot.loop)

def dev_check(id):
    with open('data/devs.json') as f:
        devs = json.load(f)
        if id in devs:
            return True
        return False

@bot.command()
async def ping(ctx):
    '''Pong! Get the bot's response time'''
    em = discord.Embed(color=discord.Color(value=0x00ff00))
    em.title = "Pong!"
    em.description = f'{bot.ws.latency * 1000:.4f} ms'
    await ctx.send(embed=em)



@bot.command()
async def presence(ctx, Type=None, *, thing=None):
    """Change the bots presence"""
    if not dev_check(ctx.author.id):
        return await ctx.send("You cannot use this because you are not a developer.")
    if Type is None:
        await ctx.send('Usage: *presence [game/stream] [msg]')
    else:
      if Type.lower() == 'stream':
        await bot.change_presence(activity=discord.Game(name=thing,type=1, url='https://www.twitch.tv/a'), status='online')
        await ctx.send(f'I am now streaming {thing}!')
      elif Type.lower() == 'game':
        await bot.change_presence(activity=discord.Game(name=thing))
        await ctx.send(f'I am now playing {thing}!')
      elif Type.lower() == 'clear':
        await bot.change_presence(activity=None)
        await ctx.send('I am not playing anything anymore')
      else:
        await ctx.send('Usage: *presence [game/stream] [msg]')


if not os.environ.get('TOKEN'):
    print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('"'))
