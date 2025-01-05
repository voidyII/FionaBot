import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import event_handler

def login_run():
    # takes token and prefix into variables
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    PREFIX = os.getenv('PREFIX')

    #bot variable
    #intents are all enabled for developement purposes
    bot = commands.Bot(command_prefix=PREFIX, help_command=None, intents=discord.Intents.all())

    # changes presence to 'playing .help'
    @bot.event
    async def on_connect():
        await bot.change_presence(activity=discord.Game(name=".help", type=3))
        print("Playing .help")
    
    #sends login msg in terminal and loads cogs
    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user}")
        for f in os.listdir("./cogs"):
            if f.endswith(".py"):
                await bot.load_extension("cogs."+f[:-3])
        print(f"Loaded cogs")

    event_handler.events(bot)

    bot.run(TOKEN)

