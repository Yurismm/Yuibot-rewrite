import discord
from discord.ext import commands
from motor.motor_asyncio import AsyncIOMotorClient
import re
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




if not os.environ.get('TOKEN'):
    print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('"'))
