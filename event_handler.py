import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import message_handler
import cmd_handler

def client_run():
    # takes token and prefix into variables
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    PREFIX = os.getenv('PREFIX')

    #bot variable
    bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())

    #when ready (fully booted) prints login text in terminal
    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user}")

    #checks if msg received
    @bot.event
    async def on_message(message):
        # if msg author is client (aka fiona), return
        if message.author == bot.user:
            return

        #puts msg content in string
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        #prints message content for debugging purposes
        print(user_message)

        #if prefix is not present, return
        if user_message[0] == PREFIX:
            # needs to be changed to functioning return value
            await cmd_handler.bot_commands()

        #write debug msg in terminal
        print(f"{username} wrote {user_message} in {channel}")

        #wait for msg handler to return response msg
        await message_handler.send_msg(message, user_message)

    #if new member joins, do sth (TBD)
    @bot.event
    async def on_member_join(member):
        # sth
        print("hello")
 
    #starts client
    bot.run(TOKEN)