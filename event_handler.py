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
            # to be added
            await message.channel.send("test")
        else:
            await bot.process_commands(message)

    @bot.event
    async def on_command_error(ctx, error):
        # if command requiring arg was not provided one
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Are you kidding me??!! How often do I have to tell you to use specifiers for the command?!!! >:V")
        
        # not working/triggered
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("I'm sorry, but that command doesn't seem to exist :/\nIf you're unsure what command to use, type .help and I'll try to help you as best as I can :3")
   