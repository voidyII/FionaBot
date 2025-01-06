import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from .db_handler import database

class events(commands.Cog):
    # initalises bot variable as self
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        database.add_guild(guild)
        print("finished adding guild")

    # currently just a debug listener, TODO: expand functionality
    @commands.Cog.listener()
    async def on_message(self, message):
        bot = self.bot
        PREFIX = os.getenv('PREFIX')

        # if msg author is bot, return
        if message.author == bot.user:
            return
        
        # stores some message info in variables
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # prints user, message and channel in terminal for debugging purposes 
        print(f"{username} wrote {user_message} in {channel}")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # if command requiring arg was not provided one
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Are you kidding me??!! How often do I have to tell you to use specifiers for the command?!!! >:V")
        
        # not working/triggered
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("I'm sorry, but that command doesn't seem to exist :/\nIf you're unsure what command to use, type .help and I'll try to help you as best as I can :3")

async def setup(bot):
    await bot.add_cog(events(bot))