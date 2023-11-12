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
    async def d4(self, ctx, arg=None):
        if arg == None:
            rolld4 = roll_dice.d4()
            await ctx.send(f"You rolled a `{rolld4}`!!^^")
        else:
            arg = int(arg)
            while arg > 0:
                rolld4 = roll_dice.d4()
                await ctx.send(f"You rolled a `{rolld4}`!!^^")
                arg = arg-1

    @roll.command()
    async def d6(self, ctx, arg=None):
        if arg == None:
            rolld6 = roll_dice.d6()
            await ctx.send(f"You rolled a `{rolld6}`!!^^")
        else:
            arg = int(arg)
            while arg > 0:
                rolld6 = roll_dice.d6()
                await ctx.send(f"You rolled a `{rolld6}`!!^^")
                arg = arg-1 
    
    @roll.command()
    async def d8(self, ctx, arg=None):
        if arg == None:
            rolld8 = roll_dice.d8()
            await ctx.send(f"You rolled a `{rolld8}`!!^^")
        else:
            arg = int(arg)
            while arg > 0:
                rolld8 = roll_dice.d8()
                await ctx.send(f"You rolled a `{rolld8}`!!^^")
                arg = arg-1

    @roll.command()
    async def d10(self, ctx, arg=None):
        if arg == None:
            rolld10 = roll_dice.d10()
            await ctx.send(f"You rolled a `{rolld10}`!!^^")
        else:
            arg = int(arg)
            while arg > 0:
                rolld10 = roll_dice.d10()
                await ctx.send(f"You rolled a `{rolld10}`!!^^")
                arg = arg-1
        
    @roll.command()
    async def d12(self, ctx, arg=None):
        if arg == None:
            rolld12 = roll_dice.d12()
            await ctx.send(f"You rolled a `{rolld12}`!!^^")
        else:
            arg = int(arg)
            while arg > 0:
                rolld12 = roll_dice.d12()
                await ctx.send(f"You rolled a `{rolld12}`!!^^")
                arg = arg-1
    
    @roll.command()
    async def d20(self, ctx, arg=None):
        if arg == None:
            rolld20 = roll_dice.d20()
            await ctx.send(f"You rolled a `{rolld20}`!!^^")
        else:
            arg = int(arg)
            while arg > 0:
                rolld20 = roll_dice.d20()
                await ctx.send(f"You rolled a `{rolld20}`!!^^")
                arg = arg-1

    @roll.command()
    async def d100(self, ctx, arg=None):
        if arg == None:
            rolld100 = roll_dice.d100()
            await ctx.send(f"You rolled a `{rolld100}`!!^^")
        else:
            arg = int(arg)
            while arg > 0:
                rolld100 = roll_dice.d100()
                await ctx.send(f"You rolled a `{rolld100}`!!^^")
                arg = arg-1

async def setup(bot):
    await bot.add_cog(cmdRoll(bot))