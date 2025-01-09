from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
from .db_handler import database
import os
import json
import datetime

db_connect = database.connect_db()
db_cursor = db_connect.cursor()
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
scheduled_time = datetime.time(hour=12, minute=00, second=00, tzinfo=datetime.timezone.utc)

class events(commands.Cog):
    # initalises bot variable as self
    def __init__(self, bot):
        self.bot = bot
        self.on_date_check.start()
    
    def cog_unload(self):
        self.on_date_check.cancel()

    # updates the database at 12:00:00 every day (if bot is running during that time)
    @tasks.loop(time=scheduled_time)
    async def on_date_check(self):
        with open(os.path.join(__location__, 'date.json'), "r+") as date_file:
            last_update = json.load(date_file)

        await database.update_guild_all(self, db_cursor)
        db_connect.commit()

        now = datetime.datetime.now()
        time = now.strftime("%Y-%m-%d")
        full_time = now.strftime("%Y-%m-%d %H:%M:%S")

        last_update["last_update"] = time
        last_update["full_last_update"] = full_time

        with open(os.path.join(__location__, 'date.json'), "w") as new_date_file:
            json.dump(last_update, new_date_file)

        print("daily update complete")

    @commands.Cog.listener()
    async def on_ready(self):
        with open(os.path.join(__location__, 'date.json'), "r+") as date_file:
            last_update = json.load(date_file)

        now = datetime.datetime.now()
        time = now.strftime("%Y-%m-%d")
        full_time = now.strftime("%Y-%m-%d %H:%M:%S")

        if last_update.get("last_update") < time:
            await database.update_guild_all(self, db_cursor)
            db_connect.commit()

            last_update["last_update"] = time
            last_update["full_last_update"] = full_time

            with open(os.path.join(__location__, 'date.json'), "w") as new_date_file:
                json.dump(last_update, new_date_file)

            print("on_ready complete")

        else: print("No on_ready update needed")
        
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await database.add_guild(self, guild, db_cursor)
        db_connect.commit()

        print("finished adding guild")

    @commands.Cog.listener()
    async def on_guild_update(self, guild_pre, guild_post):
        await database.update_guild_on_update(self, guild_post, db_cursor)
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