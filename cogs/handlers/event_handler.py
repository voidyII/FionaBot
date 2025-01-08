import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import datetime
from .db_handler import database

db_connect = database.connect_db()
db_cursor = db_connect.cursor()

class events(commands.Cog):
    # initalises bot variable as self
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    old_date = '2025-01-08 00:42:26'

    # @commands.Cog.listener()
    # async def on_ready(self):
    #     db_cursor = database.connect_db()

    if old_date < datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
        async def daily_guild_update(self, guild):
            await database.update_guild_all(self, guild, db_cursor)
            db_connect.commit()
            print("daily guild updates done")

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await database.add_guild(self, guild, db_cursor)
        db_connect.commit()
        print("finished adding guild")

    @commands.Cog.listener()
    async def on_guild_update(self, guild_pre, guild_post):
        await database.update_guild_one(self, guild_post, db_cursor)
        db_connect.commit()
        print(f"updated guild with id {guild_post.id}")
    
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        database.remove_guild(guild, db_cursor)
        db_connect.commit()
        print("finished removing guild")

    # currently just a debug listener, TODO: expand functionality
    @commands.Cog.listener()
    async def on_message(self, message):
        bot = self.bot

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