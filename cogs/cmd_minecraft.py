import discord
from discord.ext import commands
import rcp_minecraft
import json

class cmdMinecraft(commands.Cog):
    # initalises bot variable as self
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    # minecraft command group
    @commands.group(invoke_without_command=True)
    async def minecraft(self, ctx):
        await ctx.send("You forgot to specify what I should do, dummy!! >:/")

    @minecraft.command()
    async def info(self, ctx, arg):
        item_file = open("D:\Coding\FionaBot\item_data.json")
        item_dat = json.load(item_file)
        for item in item_dat:
            if item.get("fiona_item_name") == arg:
                if item.get("obtainable") == True:
                    obtain = "yes"
                else: obtain = "no"

                if item.get("image") != None:
                    img = discord.File(item.get("image"))
                    name = item.get("name")
                    id = item.get("item_id")
                    stack = item.get("stack")
                    await ctx.send(f"**Item Info:**\n", file=img)
                    await ctx.send(f"Name: {name}\nItem ID: {id}\nStackability: {stack}\nObtainable: {obtain}")
                else:
                    name = item.get("name")
                    id = item.get("item_id")
                    stack = item.get("stack")
                    await ctx.send(f"**Item Info:**\nName: {name}\nItem ID: {id}\nStackability: {stack}\nObtainable: {obtain}")

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
    
    @craft.command()
    async def cut(self, ctx, arg):
        cutblock_recipe_to_send = rcp_minecraft.cut(arg)
        await ctx.send(f"Here's the recipe you wanted!! :3",file=cutblock_recipe_to_send)

    @craft.command()
    async def chiseled(self, ctx, arg):
        chiseledblock_recipe_to_send = rcp_minecraft.chiseled(arg)
        await ctx.send(f"Here's the recipe you wanted!! :3",file=chiseledblock_recipe_to_send)

    @craft.command()
    async def polished(self, ctx, arg):
        polishedblock_recipe_to_send = rcp_minecraft.polished(arg)
        await ctx.send(f"Here's the recipe you wanted!! :3",file=polishedblock_recipe_to_send)

    @craft.command()
    async def block(self, ctx, arg):
        block_recipe_to_send = rcp_minecraft.block(arg)
        await ctx.send(f"Here's the recipe you wanted!! :3",file=block_recipe_to_send)

async def setup(bot):
    await bot.add_cog(cmdMinecraft(bot))