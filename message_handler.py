#import discord
import response_handler

# sends response
async def send_msg(message, user_message):
    user_message = user_message.lower()
    response = response_handler.handle_all(user_message)
    await message.channel.send(response)       