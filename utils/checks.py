from discord.ext import commands


class DevError(commands.CheckFailure):
    pass


def is_dev():
    """ Checks whether a user is a developer of the bot """
    dev_list = [('mariobob#8342', 293159670040887297), ('Yuriii#6518', 358970589697933314), ('MendtheMiner#0605', 341650948432592897), ('MrSoka#9106', 325278718937530368)]

    async def predicate(ctx):
        if ctx.author.id not in (x[1] for x in dev_list):
            raise DevError('User not in developer list.')
        return True
    return commands.check(predicate)
