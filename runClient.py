import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

def login_run():
    # takes token and prefix into variables
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    PREFIX = os.getenv('PREFIX')
    OWNERID = os.getenv('OWNER_ID')

    #bot variable
    #intents are all enabled for developement purposes
    bot = commands.Bot(command_prefix=PREFIX, help_command=None, intents=discord.Intents.all(), owner_id = OWNERID)


    # changes presence to 'playing .help'
    @bot.event
    async def on_connect():
        await bot.change_presence(activity=discord.Game(name=".help", type=3))
        print("Playing .help")
    
    #sends login msg in terminal and loads cogs
    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user}")
        cog_path = "./cogs"
        for folder in os.listdir(cog_path):
            for file in os.listdir(f"{cog_path}/{folder}"):
                if file.endswith(".py"):
                    print((f"{folder}.{file[:-3]}"))
                    await bot.load_extension(f"cogs.{folder}.{file[:-3]}")
        print(f"Loaded cogs")

    bot.run(TOKEN)

