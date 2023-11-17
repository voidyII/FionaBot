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

        to_add = {
            "id": moji.channel.id,
            "name": moji.channel.name,
            "type": moji.channel.type
        }

        # print("dic created")

        # # jsfile = open(".\id_file.json", "w")
        # id_file = json.load(open(".\id_file.json", "r"))

        # new_id_file = id_file.append(to_add)
        
        # json.dump(new_id_file, open(".\id_file.json", "w"))
        # id_file.close()

        #I FOUND THIS ON STACKOVERFLOW, THIS IS NOT THE SOLUTION I WANT BUT IT WORKS SOMEHOW
        with open(".\id_file.json", mode="r+") as outfile:
            outfile.seek(0,2)
            pos = outfile.tell()-1
            outfile.seek(pos)
            outfile.write(", {}]".format(json.dumps(to_add)))

        print("write/append succesful")
