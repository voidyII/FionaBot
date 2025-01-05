import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

def events(bot):
    PREFIX = os.getenv('PREFIX')

    @bot.event
    async def on_message(message):
        # if msg author is bot, return
        if message.author == bot.user:
            return
        
        # stores some message info in variables
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # prints user, message and channel in terminal for debugging purposes
        print(f"{username} wrote {user_message} in {channel}")

        # gives message to handler (commands or no commands)
        if user_message[0] != PREFIX:
            await message.channel.send("test")
        else:
            await bot.process_commands(message)