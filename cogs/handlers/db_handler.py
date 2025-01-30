import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import mysql.connector
import datetime

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_FIONA_USER')
DB_PASSWORD = os.getenv('DB_FIONA_PASSWORD')
DB_NAME = os.getenv('DB_FIONA_NAME')

class database(commands.Cog):
    # initalises bot variable as self
    def __init__(self, bot):
        self.bot = bot

    def connect_db():
        mydb = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )

        print("db_server connected")
        
        return mydb
    
    # adds guild to database (guild registry)
    async def add_guild(self, id, cursor):
        bot = self.bot
        guild = await bot.fetch_guild(id, with_counts=True)
        cursor.execute(f"CREATE TABLE g{guild.id} (user_id int(13))")

        created = guild.created_at.strftime("%Y-%m-%d %H:%M:%S")
        now = datetime.datetime.now()
        time = now.strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute(f"INSERT INTO guilds_overview VALUES ({guild.id}, '{guild.name}', {guild.owner_id}, '{created}', {guild.approximate_member_count}, '{time}', '{time}');")
        print(f"added guild with id {guild.id} to table guilds_overview")

    async def update_guild_on_update(self, guild_to_update, cursor):
        bot = self.bot
        guild_new = await bot.fetch_guild(guild_to_update.id, with_counts=True)

        now = datetime.datetime.now()
        update_time = now.strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute(f"USE {DB_NAME}")
        cursor.execute(f"UPDATE guilds_overview \
                        SET guild_name='{guild_new.name}', owner_id={guild_new.owner_id}, member_count={guild_new.approximate_member_count}, last_update='{update_time}' \
                        WHERE guild_id={guild_new.id}")
        

    async def update_guild_all(self, cursor):
        bot = self.bot
        cursor.execute(f"USE {DB_NAME}")
        cursor.execute("SELECT guild_id FROM guilds_overview")
        
        db_guild_list = cursor.fetchall()
        bot_guilds = bot.guilds

        now = datetime.datetime.now()
        update_time = now.strftime("%Y-%m-%d %H:%M:%S")
        
        #current guild in database
        guilds_to_update = []
        for guilds in db_guild_list:
            for elem in guilds:
                guilds_to_update.append(elem)

        #current guilds that bot is part of
        current_bot_guilds = []
        for guild in bot_guilds:
            current_bot_guilds.append(guild.id)

        #if no guilds in database, add all current bot guilds and return
        if guilds_to_update == []:
            print("debug")
            for id in current_bot_guilds:
                await database.add_guild(self, id, cursor)
            return

        #filter current bot guilds to only new ones
        for elem in guilds_to_update:
            current_bot_guilds = list(filter(lambda item: item != elem, current_bot_guilds))

        #add the new guilds to database
        for id in current_bot_guilds:
            await database.add_guild(self, id, cursor)
        
        #update all other guilds
        for id in guilds_to_update:
            guild_updated = await bot.fetch_guild(id, with_counts=True)
            cursor.execute(f"UPDATE guilds_overview \
                            SET guild_name='{guild_updated.name}', owner_id={guild_updated.owner_id}, member_count={guild_updated.approximate_member_count}, last_update='{update_time}', full_last_update='{update_time}' \
                            WHERE guild_id={id}")

    def remove_guild(id, cursor):
        cursor.execute(f"USE {DB_NAME}")
        cursor.execute(f"DROP TABLE g{id}")
        cursor.execute(f"DELETE FROM guilds_overview WHERE guild_id={id}")
        print(f"removed guild with id {id} from table guilds_overview")

async def setup(bot):
    await bot.add_cog(database(bot))