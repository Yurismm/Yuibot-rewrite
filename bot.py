import discord
from utils.checks import *
from discord.ext import commands
from motor.motor_asyncio import AsyncIOMotorClient
import re
import json
import logging
import random
from random import randint
import inspect
import traceback
import os
from discord.ext.commands import errors
import aiohttp
import sys
import time


bot = commands.Bot(command_prefix='$')

startup_extensions = [
#    'cogs.useful',
#    'cogs.config',
    'cogs.developer',
    'cogs.Math',
    'cogs.osu',
    "pas has a small dick"
]



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


@bot.event
async def on_command_error(ctx, error):
    trace = ''.join(
        traceback.format_exception(type(error), error, error.__traceback__))
    erroremb = discord.Embed(
        description=f'```py\n{trace}\n```',
        color=discord.Color.red(),
        timestamp=ctx.message.created_at)
    erroremb.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    erroremb.add_field(name='Message Content', value=ctx.message.content)
    erroremb.add_field(name="Server ID", value=ctx.guild.id)
    erroremb.add_field(name="Server", value=ctx.guild)
    erroremb.add_field(
        name='Location', value=f'#{ctx.channel.name} ({ctx.channel.id})')

    await bot.get_channel(697460379265269891).send(embed=erroremb)


@bot.event
async def on_guild_join(guild):
    channel = bot.get_channel(697407857661837322)
    embed = discord.Embed(
        title='New Server!',
        description=f'Server Name: {guild.name} | Server Num {len(bot.guilds)}',
        color=discord.Color.green())
    embed.set_thumbnail(url=guild.icon_url)
    embed.set_footer(text=f"Server ID: {guild.id}")
    embed.set_author(
        name=f"Owner: {guild.owner} | ID: {guild.owner.id}",
        icon_url=guild.owner.avatar_url)
    await channel.send(embed=embed)


@bot.event
async def on_guild_remove(guild):
    channel = bot.get_channel(697407857661837322)
    embed = discord.Embed(
        title='Removed from Server',
        description=f'Server Name: {guild.name} | Server Num {len(bot.guilds)}',
        color=discord.Color.red())
    embed.set_thumbnail(url=guild.icon_url)
    embed.set_footer(text=f"Server ID: {guild.id}")
    embed.set_author(
        name=f"Owner: {guild.owner} | ID: {guild.owner.id}",
        icon_url=guild.owner.avatar_url)
    await channel.send(embed=embed)


@bot.command()
async def invite(ctx):
    colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
    colour = int(colour, 16)
    embed = discord.Embed(
        description=
        "https://discordapp.com/oauth2/authorize?client_id=456910763504697363&scope=bot&permissions=8",
        color=colour)
    embed.set_author(name="Use this link to invite Yui to your server!")
    embed.set_footer(text="Invite Link")
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    print("----------------")
    print("Logged in as:")
    print("Name : {}".format(bot.user.name))
    print("ID : {}".format(bot.user.id))
    print("Py Lib Version: %s" % discord.__version__)
    print("----------------")

    await bot.change_presence(status=discord.Status.idle)


@bot.command()
@is_dev()
async def presence(ctx, Type=None, *, thing=None):
    """Change the bots presence"""
    if Type is None:
        await ctx.send(
            'Usage: &presence [game/stream] [msg] OR &presence clear')
    else:
        if Type.lower() == 'stream':
            await bot.change_presence(
                activity=discord.Streaming(
                    name=thing, url='https://www.twitch.tv/monstercat'))
            await ctx.send(f'I am now streaming {thing}!')
        elif Type.lower() == 'game':
            await bot.change_presence(activity=discord.Game(name=thing))
            await ctx.send(f'I am now playing {thing}!')
        elif Type.lower() == 'clear':
            await bot.change_presence(activity=None)
            await ctx.send("Stopped playing/streaming")
        else:
            await ctx.send(
                'Usage: &presence [game/stream] [msg] OR &presence clear')


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
            print('Loaded extension: {}'.format(extension))
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

with open ("data/token.txt") as f:
  bot.run(f.read())