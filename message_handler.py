# import discord
import response_handler

async def send_msg(message, user_message):
    response = response_handler.handle_all(user_message)
    await message.channel.send(response)
