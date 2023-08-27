import discord
from discord.ext import commands
import rcp_minecraft

class cmdMinecraft(commands.Cog):
    # initalises bot variable as self
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    # minecraft command group
    @commands.group(invoke_without_command=True)
    async def minecraft(self, ctx):
        await ctx.send("You forgot to specify what I should do, dummy!! >:/")

    # craft command (sends recipe)
    @minecraft.group(invoke_without_command=True)
    async def craft(self, ctx, arg):
        recipe_to_send = rcp_minecraft.recipes(arg)
        await ctx.send(f"Here's the recipe you wanted!! :3",file=recipe_to_send)
        print(f"sent {arg} recipe")

    @craft.command()
    async def dye(self, ctx, arg):
        dye_recipe_to_send = rcp_minecraft.colors(arg)
        await ctx.send(f"Here's the recipe you wanted!! :3",file=dye_recipe_to_send)

async def setup(bot):
    await bot.add_cog(cmdMinecraft(bot))