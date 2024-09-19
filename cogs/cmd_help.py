import discord
from discord.ext import commands

class cmdHelp(commands.Cog):
    # initalises bot variable as self
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        await ctx.send("**__Commands:__**\n.help (shows this message)\n.minecraft (used to do minecraft related things)\n.roll (rolls dice)\n.coinflip (flips a coin)\n.role (does role related things)\n\nFor detailed information about a command type .help followed by the command\nExample: .help minecraft")

    @help.command()
    async def minecraft(self, ctx):
        await ctx.send(f"**__Minecraft Commands:__**\n.minecraft craft [item/specifier] (sends crafting recipe)\n.minecraft info [item] (sends meta information about item)")
    
    @help.command()
    async def roll(self, ctx):
        await ctx.send(f"**__Dice Rolls:__**\n.roll [die] [amount] (rolls dice certain amount of times)\nDie defaults to d6 without input. Amount defaults to 1 without input\nAvailable Dice:\nd4\nd6\nd8\nd10\nd12\nd20\nd100")

    @help.command()
    async def coinflip(self, ctx):
        await ctx.send(f"**__Coinflip__**\n.coinflip (flips a coin)\n\nseriously idiot! what were you expecting??! >:(")

    @help.command()
    async def role(self, ctx):
        await ctx.send(f"**__Role Commands:__**\n.role [rolename] (adds role to user)\n.rolerm [rolename] (removes role from user)\n\n__List of Roles:__\nMinecraft (invoked with 'minecraft')\nDungeons & Dragons (invoked with 'dnd')\nMagic: The Gathering (invoked with 'mtg')\nSplatoon (invoked with 'sploon')\nBot Tester (invoked with 'bottester')")

    @help.command()
    async def uwuify(self, ctx):
        await ctx.send(f"**__Uwuifier__**\n.uwuify [text to uwuify] (uwuifies the given text)")

async def setup(bot):
    await bot.add_cog(cmdHelp(bot))