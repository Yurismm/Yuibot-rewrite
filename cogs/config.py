import discord
from discord.ext import commands

class config(commands.Cog):
    '''
    Configuration commands
    '''

    def __init__(self, bot):
        self.bot = bot
        self.db = self.bot.db

    async def save_prefix(self, prefix, guildID, ctx):
        await self.bot.db.config.update_one({"_id": ctx.guild.id}, {"$set": {"prefix": prefix}}, upsert=True)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def prefix(self, ctx, prefix=None):
        """Change Prefix of the server"""
        guildID = str(ctx.guild.id)
        if not prefix:
            return await ctx.send('Please provide a prefix for this command to work')
        try:
            await self.save_prefix(prefix, guildID, ctx)
            await ctx.send(f'Prefix `{prefix}` successfully saved (re-run this command to replace it)')
        except Exception as e:
            await ctx.send(f'Something went wrong\nError Log: `str({e})`')


        


# Setup bot
def setup(bot):
    bot.add_cog(config(bot))
