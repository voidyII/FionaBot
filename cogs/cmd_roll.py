import discord
from discord.ext import commands
from cogfunctions import roll_dice

class cmdRoll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.group(invoke_without_command=True)
    async def roll(self, ctx):
        rolld6 = roll_dice.d6()
        await ctx.send(f"You rolled a `{rolld6}`!!^^")

    @roll.command()
    async def d4(self, ctx):
        rolld4 = roll_dice.d4()
        await ctx.send(f"You rolled a `{rolld4}`!!^^")

    @roll.command()
    async def d6(self, ctx):
        rolld6 = roll_dice.d6()
        await ctx.send(f"You rolled a `{rolld6}`!!^^")
    
    @roll.command()
    async def d8(self, ctx):
        rolld8 = roll_dice.d8()
        await ctx.send(f"You rolled a `{rolld8}`!!^^")

    @roll.command()
    async def d10(self, ctx):
        rolld10 = roll_dice.d10()
        await ctx.send(f"You rolled a `{rolld10}`!!^^")

    @roll.command()
    async def d12(self, ctx):
        rolld12 = roll_dice.d12()
        await ctx.send(f"You rolled a `{rolld12}`!!^^")
    
    @roll.command()
    async def d20(self, ctx):
        rolld20 = roll_dice.d20()
        await ctx.send(f"You rolled a `{rolld20}`!!^^")

async def setup(bot):
    await bot.add_cog(cmdRoll(bot))