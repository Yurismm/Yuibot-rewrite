from discord.ext import commands
from time import time
import discord


class Osu:
    def __init__(self, bot):
        self.bot = bot
        self.baseurl = 'https://lemmmy.pw/osusig/sig.php?'

    @commands.guild_only()
    @commands.command(aliases=['osu'])
    async def osustats(self, ctx, *, osuplayer: str = None):
        if not osuplayer:
            embed = discord.Embed(
                description="**" + ctx.author.name +
                "** you need to tell me a username!",
                color=0xff0000)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=0x00ff00)
            embed.set_author(
                name=f"{osuplayer}'s Stats",
                url=f"https://osu.ppy.sh/u/{osuplayer}",
                icon_url="https://s.ppy.sh/images/head-logo.png")
            embed.set_footer(text="Osu stats")
            query = (
                f'colour=hexff66aa&uname={osuplayer}&pp=1&countryrank'
                '&flagshadow&flagstroke&opaqueavatar&avatarrounding=5&'
                f'onlineindicator=undefined&xpbar&xpbarhex&random={time()}')

            embed.set_image(url=f'{self.baseurl}{query}')
            print(f'{self.baseurl}{query}')
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Osu(bot))