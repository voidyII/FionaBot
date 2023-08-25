import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import message_handler

def client_run():
    # takes token and prefix into variables
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    PREFIX = os.getenv('PREFIX')

    #bot variable
    bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())

    #load cogs
    # for extension in extension_files:
    #     bot.load_extension(extension)
    #     print(f"Loaded {extension}")
    # loads cogs
    # for filename in os.listdir('./cogs'):
    #     if filename.endswith('.py'):
    #         bot.load_extension(f'cogs.{filename[:-3]}')

    #when ready (fully booted) prints login text in terminal
    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user}")

    @bot.event
    async def on_connect():
        for f in os.listdir("./cogs"):
            if f.endswith(".py"):
                await bot.load_extension("cogs."+f[:-3])
        print(f"Loaded cogs")

    #checks if msg received
    # @bot.event
    # async def on_message(message):
    #     # if msg author is client (aka fiona), return
    #     if message.author == bot.user:
    #         return

    #     #puts msg content in string
    #     username = str(message.author)
    #     user_message = str(message.content)
    #     channel = str(message.channel)

    #     #prints message content for debugging purposes
    #     print(user_message)

    #     #if prefix is not present, return
    #     # if user_message[0] == PREFIX:
    #     #     # needs to be changed to functioning return value
            

    #     #write debug msg in terminal
    #     print(f"{username} wrote {user_message} in {channel}")

    #     #wait for msg handler to return response msg
    #     await message_handler.send_msg(message, user_message)

    # #if new member joins, do sth (TBD)
    # @bot.event
    # async def on_member_join(member):
    #     # sth
    #     print("hello")
 
    #starts client
    bot.run(TOKEN)