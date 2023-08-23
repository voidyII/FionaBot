import discord
from dotenv import load_dotenv
import os
import message_handler

def login_msg():
    # takes token and prefix into variables
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    PREFIX = os.getenv('PREFIX')

    #client variable
    client = discord.Client(intents=discord.Intents.all())

    #when ready (fully booted) prints login text in terminal
    @client.event
    async def on_ready():
        print(f"Logged in as {client.user}")

    #checks if msg received
    @client.event
    async def on_message(message):
        # if msg author is client (aka fiona), return
        if message.author == client.user:
            return

        #puts msg content in string
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        #if prefix is not present, return
        if user_message[0] != PREFIX:
            return

        #write debug msg in terminal
        print(f"{username} wrote {user_message} in {channel}")

        #wait for msg handler to return response msg
        await message_handler.send_msg(message, user_message)

    #if new member joins, do sth (TBD)
    @client.event
    async def on_member_join(member):
        # sth
        print("hello")
 
    #starts client
    client.run(TOKEN)