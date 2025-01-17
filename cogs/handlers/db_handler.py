import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import mysql.connector
import datetime

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_ROOT_USER')
DB_PASSWORD = os.getenv('DB_ROOT_PASSWORD')

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

        print("db connected")
        
        return mydb
    
    # adds guild to database (guild registry)
    async def add_guild(self, guild, cursor):
        bot = self.bot
        guild = await bot.fetch_guild(guild.id, with_counts=True)
        cursor.execute("USE active_data")

        created = guild.created_at.strftime("%Y-%m-%d %H:%M:%S")
        now = datetime.datetime.now()
        time = now.strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute(f"INSERT INTO active_guilds VALUES({guild.id}, '{guild.name}', {guild.owner_id}, '{created}', {guild.approximate_member_count}, '{time}');")
        print(f"added guild with id {guild.id} to table active_guilds")

    async def update_guild_on_update(self, guild_to_update, cursor):
        bot = self.bot
        guild_new = await bot.fetch_guild(guild_to_update.id, with_counts=True)

        now = datetime.datetime.now()
        update_time = now.strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("USE active_data")
        cursor.execute(f"UPDATE active_guilds \
                        SET guild_name='{guild_new.name}', owner_id={guild_new.owner_id}, member_count={guild_new.approximate_member_count}, last_update='{update_time}' \
                        WHERE guild_id={guild_new.id}")
        

    async def update_guild_all(self, cursor):
        bot = self.bot
        cursor.execute("USE active_data")
        cursor.execute("SELECT guild_id FROM active_guilds")
        
        guilds_to_update = cursor.fetchall()
        current_guilds = bot.guilds

        now = datetime.datetime.now()
        update_time = now.strftime("%Y-%m-%d %H:%M:%S")

        for guild in current_guilds:
            for elems in guilds_to_update:
                if guild.id in elems:
                    continue
                else:
                    await database.add_guild(self, guild, cursor)
        
        for elem in guilds_to_update:
            for id in elem:
                guild_updated = await bot.fetch_guild(id, with_counts=True)
                cursor.execute(f"UPDATE active_guilds \
                                SET guild_name='{guild_updated.name}', owner_id={guild_updated.owner_id}, member_count={guild_updated.approximate_member_count}, last_update='{update_time}' \
                                WHERE guild_id={id}")

    def remove_guild(guild, cursor):
        cursor.execute(f"USE active_data")
        cursor.execute(f"DELETE FROM active_guilds WHERE guild_id={guild.id}")
        print(f"removed guild with id {guild.id} from table active_guilds")

async def setup(bot):
    await bot.add_cog(database(bot))