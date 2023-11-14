import discord
from discord.ext import commands

class cmdAdmin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def rolemsg(self, ctx):
        # 1143667808820002937
        # ctx.author
        print('lol')


async def setup(bot):
    await bot.add_cog(cmdAdmin(bot))