import discord
from discord.ext import commands

class cmdHelp(commands.Cog):
    # initalises bot variable as self
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        # needs proper formatting
        await ctx.send("**__Commands:__**\n.help - shows this message\n.help [command] - shows help message relating to command")

async def setup(bot):
    await bot.add_cog(cmdHelp(bot))