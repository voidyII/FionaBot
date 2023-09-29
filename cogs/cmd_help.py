import discord
from discord.ext import commands

class cmdHelp(commands.Cog):
    # initalises bot variable as self
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        await ctx.send("**__Commands:__**\n.help (shows this message)\n.minecraft (used to do minecraft related things)\n.roll (rolls dice)\n\nFor detailed information about a command type .help followed by the command\nExample: .help minecraft")

    @help.command()
    async def minecraft(self, ctx):
        await ctx.send(f"**__Minecraft Commands:__**\n.minecraft craft [item/specifier] (sends crafting recipe)\n.minecraft info [item] (sends information about item)")
    
    @help.command()
    async def roll(self, ctx):
        await ctx.send(f"**__Dice Rolls:__**\n.roll [die] [amount] (rolls dice certain amount of times)\nDie defaults to d6 without input. Amount defaults to 1 without input\nAvailable Dice:\nd4\nd6\nd8\nd10\nd12\nd20")

async def setup(bot):
    await bot.add_cog(cmdHelp(bot))