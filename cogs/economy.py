import discord
from discord.ext import commands
import random, asyncio, aiohttp

class economy():
    def __init__(self, bot):
        self.bot = bot

    async def on_command_error(self, message,  error):
        if isinstance(error, commands.CommandOnCooldown):
            await discord.abc.Messageable.send(message.channel, error)              
        
    async def is_registered(self, user):
        x = await self.db.economy.find_one({"user": user.id})
        if x is None:
            return False
        else:
            return True


    @commands.command(aliases=['register', 'openbank'])
    async def openaccount(self, ctx):
        '''Opens a bank account for the economy!'''
        registered = await self.is_registered(ctx.author)
        if registered:
            return await ctx.send("You already have a bank account!")
        await self.db.economy.update_one({"user": ctx.author.id}, {"$set": {"money": 0}}, upsert=True)
        await ctx.send("Your bank account is now open!")

    @commands.command(aliases=['bal'])
    async def balance(self, ctx):
        """"See your current balance"""
        user = await self.bot.db.economy.find_one({ "_id": ctx.author.id })
        await ctx.send(f"{ctx.author.mention} | Your balance: **{user['money']}**:dollar: ")     

    @commands.command()
    @commands.cooldown(1, 120, commands.BucketType.user)                  
    async def work(self, ctx):
        """work for some money"""
        x = random.randint(100, 1000)
        user = await self.bot.db.economy.find_one( { "_id": ctx.author.id } )
        current = user['money']
        self.bot.db.economy.update_one( { "_id": ctx.author.id}, { "$set": { "money": current + x} })
        await ctx.send(f"You have earned {x} :dollar:")                       
              
    @commands.command()
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def daily(self, ctx):
        """Get your daily cash"""
        x = random.randint(500, 10000)
        user = await self.bot.db.economy.find_one( { "_id": ctx.author.id } )
        current = user['money']
        self.bot.db.economy.update_one( { "_id": ctx.author.id}, { "$set": { "money": current + x} })
        await ctx.send(f"Your daily gave you {x}:dollar:!\n`Come back in 24 hours and claim your next daily!`")                                
                    
                         
def setup(bot):
    bot.add_cog(economy(bot))