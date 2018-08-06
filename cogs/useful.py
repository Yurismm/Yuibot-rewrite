import discord
import asyncio
from discord.ext import commands


class useful:
    '''
    Useful commands
    '''

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(ctx, saymsg : str = None):
        """Makes me say something"""
        if saymsg == None:
            return await ctx.send('Please provide something for the bot to say.')
        await ctx.send(saymsg)

    @bot.command(pass_context=True)
    async def arole(ctx, *args):
        member = ctx.message.author.id
        input = ' '.join(args)
        role = get(member.server.roles, name=input)
        &eval await guild.get_member(member).add_roles(discord.utils.get(ctx.guild.roles, name =role))


    @bot.command(pass_context=True)
    async def rrole(ctx, *args):
        member = ctx.message.author.id
        input = ' '.join(args)
        role = get(member.server.roles, name=input)
        &eval await guild.get_member(member).remove_roles(discord.utils.get(ctx.guild.roles, name =role))
 
    @commands.command()
    async def ex(args, message, client, invoke):

     try:
         ammount = int(args[0]) + 1 if len(args) > 0 else 2
     except:
      await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), descrition="Please enter a valid value for message ammount!"))
         retur

     cleared = 0
     failed = 0
                                                                                
     async for m in client.logs_from(message.channel, limit=ammount):
         try:
             await client.delete_message(m)
             cleared += 1
         except:

             failed += 1
   pass
 
     failed_str = "\n\nFailed to clear %s message(s)." % failed if failed > 0 else ""
     returnmsg = await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.blue(), description="Cleared %s message(s).%s" % (cleared, failed_str)))
     await asyncio.sleep(4)
     await client.delete_message(returnmsg)
    
# Setup bot
def setup(bot):
    bot.add_cog(useful(bot))
