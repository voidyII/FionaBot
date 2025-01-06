import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import mysql.connector

class database(commands.Cog):
    # initalises bot variable as self
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    # adds guild to database (guild registry and own table)
    def add_guild(guild):
        print(guild.id)
        print(f"nothing added")

async def setup(bot):
    await bot.add_cog(database(bot))