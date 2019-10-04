import discord
from discord.ext import commands
import traceback
import subprocess
import textwrap
from contextlib import redirect_stdout
import inspect
from utils.checks import *
import io
import json
import os


class developer(commands.Cog):
    '''
    developer commands
    '''

    def __init__(self, bot):
        self.bot = bot

    def cleanup_code(self, content):
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])
        return content.strip('`\n')

    @commands.command(name='eval')
    @is_dev()
    async def _eval(self, ctx, *, body):
        """Evaluates python code"""
        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            '_': self.bot._last_result,
            'source': inspect.getsource,
            'session': self.bot.session
        }

        env.update(globals())

        body = self.cleanup_code(body)
        stdout = io.StringIO()
        err = out = None

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        def paginate(text: str):
            '''Simple generator that paginates text.'''
            # Untested function rewrite, sorry if it's broken -Jamu
            cur = 0
            pages = []
            while cur <= len(text):
                pages.append(text[cur:1980])
                cur += 1980
            return pages

        try:
            exec(to_compile, env)
        except Exception as e:
            err = await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
            return await ctx.message.add_reaction('\u2049')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            err = await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            if ret is None:
                if value:
                    try:

                        out = await ctx.send(f'```py\n{value}\n```')
                    except:
                        paginated_text = paginate(value)
                        for page in paginated_text:
                            if page == paginated_text[-1]:
                                out = await ctx.send(f'```py\n{page}\n```')
                                break
                            await ctx.send(f'```py\n{page}\n```')
            else:
                self.bot._last_result = ret
                try:
                    out = await ctx.send(f'```py\n{value}{ret}\n```')
                except:
                    paginated_text = paginate(f"{value}{ret}")
                    for page in paginated_text:
                        if page == paginated_text[-1]:
                            out = await ctx.send(f'```py\n{page}\n```')
                            break
                        await ctx.send(f'```py\n{page}\n```')

        if out:
            await ctx.message.add_reaction('\u2705')  # tick
        elif err:
            await ctx.message.add_reaction('\u2049')  # x
        else:
            await ctx.message.add_reaction('\u2705')

#test

    @commands.command(name='exec')
    @is_dev()
    async def _exec(self, ctx, *, code):
        """Executes code."""
        e = discord.Embed(color=0x00ff00, title='Running code')
        e.description ='Please wait...'
        msg = await ctx.send(embed=e)
        lol = subprocess.run(f"{code}", cwd='/Users/Administrator/Desktop/Yuibot-rewrite', stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        err = lol.stderr.decode("utf-8")
        res = lol.stdout.decode("utf-8")
        em = discord.Embed(color=0x00ff00, title='Ran on the Command Prompt!')
        if len(res) > 1850 or len(err) > 1850:
            em.description = f"Ran on the Command Line ```{code}``` Output: \nThe process details are too large to fit in a message."
            await msg.edit(embed=em)
        else:
            em.description = f"Ran on the Command Line: ```{code}``` Output: \n\n```{err or res}```"
            await msg.edit(embed=em)


# Setup bot
def setup(bot):
    bot.add_cog(developer(bot))
