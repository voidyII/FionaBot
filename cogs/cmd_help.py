import discord
from discord.ext import commands

class cmdHelp(commands.Cog):
    # initalises bot variable as self
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        await ctx.send("I am not able to help you right now, I'm sooo sorryyyy!!! :/")

    @help.command()
    async def minecraft(self, ctx):
        await ctx.send(f"Soon I will be able to list all the possible commands you can do with .minecraft! Just you wait, it's going to be great :PP")

async def setup(bot):
    await bot.add_cog(cmdHelp(bot))