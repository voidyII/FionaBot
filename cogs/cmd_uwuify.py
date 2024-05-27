import discord
from discord.ext import commands
from cogfunctions import uwuify_algorithms 

class cmdUwuify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def uwuify(self, ctx, *args):
        return_string = uwuify_algorithms.uwuify_string(args)
        await ctx.send(f"{return_string}")


async def setup(bot):
    await bot.add_cog(cmdUwuify(bot))