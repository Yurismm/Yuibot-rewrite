import discord
from discord.ext import commands
import random, asyncio, aiohttp

class economy():
    def __init__(self, bot):
        self.bot = bot

    async def on_command_error(self, message,  error):
        if isinstance(error, commands.CommandOnCooldown):
            await discord.abc.Messageable.send(message.channel, error)              
        
    

        
    @commands.command()
    async def openaccount(self, ctx):
        """"Create a bank account, if you already have one it will get reset"""
        self.bot.db.economy.update_one( { "_id": ctx.author.id }, { "$set": { "money": 0 } }, upsert=True )
        await ctx.send("Created an account")

    @commands.command(aliases=['bal'])
    async def balance(self, ctx):
        """"See your current balance"""
        user = await self.bot.db.economy.find_one({ "_id": ctx.author.id })
        await ctx.send(f"{ctx.author.mention} | Your balance: **{user['money']}**:dollar: ")     
                               
                    
                         
def setup(bot):
    bot.add_cog(economy(bot))