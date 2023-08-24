import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import rsp_minecraft

def bot_commands():
    # load_dotenv()
    # TOKEN = os.getenv('TOKEN')
    # PREFIX = os.getenv('PREFIX')
    # OWNER = os.getenv('OWNER_ID')

    # bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())
    # # bot.owner_id(OWNER)

    # @bot.group()
    async def minecraft(ctx):
        # , *, message: str
        # message = user_message
        # await ctx.send("YES <333")
        print(f"{ctx.author} invoked minecraft command")

    # @minecraft.command()
    async def recipe(ctx, arg):
        recipe_to_send = rsp_minecraft.recipes(arg)
        await ctx.send(file=recipe_to_send)