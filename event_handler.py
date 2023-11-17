import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import json
import message_handler

def client_run():
    # takes token and prefix into variables
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    PREFIX = os.getenv('PREFIX')

    #bot variable
    bot = commands.Bot(command_prefix=PREFIX, help_command=None, intents=discord.Intents.all())

    #sends login msg in terminal and loads cogs
    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user}")
        for f in os.listdir("./cogs"):
            if f.endswith(".py"):
                await bot.load_extension("cogs."+f[:-3])
        print(f"Loaded cogs")

    # changes presence to 'playing .help'
    @bot.event
    async def on_connect():
        await bot.change_presence(activity=discord.Game(name=".help", type=3))
        print("Playing .help")

    # error handling tests
    # @bot.event
    # async def on_command_error(ctx, error):
    #     if isinstance(error, commands.MissingRequiredArgument):
    #         await ctx.send("Are you kidding me??!! How often do I have to tell you to use specifiers for the command?!!! >:V")
        
    #     # not working/triggered
    #     if isinstance(error, commands.CommandNotFound):
    #         await ctx.send("I'm sorry, but that command doesn't seem to exist :/\nIf you're unsure what command to use, type .help and I'll try to help you as best as I can :3")

    #     if isinstance(error, commands.BadArgument):
    #         await ctx.send("Awwhh, did you make a typo? Better fix that up real quick and send it again :3<3")
    
    #if member joins, greets them
    @bot.event
    async def on_member_join(member):
        chnl = await bot.fetch_channel(1142502285042253834)
        await chnl.send(f"Omg omg, hiiiii {member.mention}!!! <3<3")

    # workflow for user message
    @bot.event
    async def on_message(message):
        # if msg author is bot (aka fiona), return
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
            await message_handler.send_msg(message, user_message)
        else:
            await bot.process_commands(message)

    @bot.event
    async def on_reaction_add(reaction, user):
        msg_file = open(".\cogfunctions\msg_roles.json", "r")
        msg_dat = json.load(msg_file)
        
        if user.id == bot.user.id:
            return

        # for entry in msg_dat:
        #     if entry.get["chnl_id"] != reaction.message.channel.id:
        #         return
        #     if reaction.emoji ==


 
    #starts client
    bot.run(TOKEN)