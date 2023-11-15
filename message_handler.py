#import discord
import response_handler
import json

# sends response
async def send_msg(message, user_message):
    user_message = user_message.lower()
    if user_message != "rolemsg":
        response = response_handler.handle_all(user_message)
        await message.channel.send(response)
    else:
        moji = await  message.channel.send("test")
        await moji.add_reaction('💻')

        dic = {
            "id": moji.channel.id,
            "name": moji.channel.name
        }

        print("dic created")

        id_file = open(".\id_file.json", "w")

        if id_file
        json.dump(dic, id_file)
        id_file.close()

        print("write/append succesful")
