import discord
from discord.ext import commands
import rsp_minecraft

class cmdMinecraft(commands.Cog):
    # initalises bot variable as self
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    # minecraft command group
    @commands.group()
    async def minecraft(self, ctx):
        print("minecraft command invoked")

    # craft command (sends recipe)
    @minecraft.command()
    async def craft(self, ctx, arg):
        recipe_to_send = rsp_minecraft.recipes(arg)

        await ctx.send(f"Here's the recipe you wanted!! :3",file=recipe_to_send)
        print(f"sent {arg} recipe")

    # does not work
    @minecraft.command()
    async def help(self, ctx, arg):
        print(arg)
        await ctx.send(f"Soon I will be able to list all the possible commands you can do with .minecraft! Just you wait, it's going to be great :PP")

async def setup(bot):
    await bot.add_cog(cmdMinecraft(bot))