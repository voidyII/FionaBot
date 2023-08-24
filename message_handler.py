# import discord
import os
import response_handler
import cmd_handler

# sends response
async def send_msg(message, user_message):
    PREFIX = os.getenv('PREFIX')
    if user_message[0] != PREFIX:
        response = response_handler.handle_all(user_message)
        await message.channel.send(response)
    else:
        response = cmd_handler.bot_commands()
