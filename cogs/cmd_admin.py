import discord
from discord.ext import commands
import json

class cmdAdmin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    @commands.has_role("Developer")
    async def rolemsg(self, ctx, *args):

        arg_list = []
        index = len(arg_list)
        arg_list.insert(index, args)

        await ctx.message.delete()

        moji = await  ctx.channel.send(
            "React to this message with one of the following Emojis to get a role assigned:\n"
            f"\{arg_list[0][0]}: {arg_list[0][1]}\n"
            f"\{arg_list[0][2]}: {arg_list[0][3]}"
            )
        
        i=0
        while i < len(arg_list[0])-1:
            emoji = arg_list[0][i]
            await moji.add_reaction(emoji)
            i = i + 2

        roleargs = {"role1": arg_list[0][1], "role2": arg_list[0][3]}

        reac = await moji.channel.fetch_message(moji.id)
        reac_list = reac.reactions
        print(reac_list)

        #for reaction in reac_list:
            

        i=0
        k=1
        while i < len(reac.reactions)-1:
            emoji = f"emoji{k}"
            reac_dic = {}
            reac_dic.update(emoji = reac_list[i])
            i = i + 2
            k = k + 1

        print(reac_dic)

        to_add = {
            "guild": moji.channel.guild.name,
            "guild_id": moji.channel.guild.id,
            "chnl": moji.channel.name,
            "chnl_id": moji.channel.id,
            "type": moji.channel.type,
            "msg_id": moji.id,
            "roles": roleargs,
            #"emoji": reac_dic
        }

        print("dic created")

        # my code for the version found on sof
        with open(".\cogfunctions\msg_roles.json", "r+") as id_dat:
            id_dat.seek(0, 2)
            dat_pos = id_dat.tell()-3
            id_dat.seek(dat_pos)
            new_dat = ",\n    {}\n]".format(json.dumps(to_add))
            id_dat.write(new_dat)

        #I FOUND THIS ON STACKOVERFLOW, THIS IS NOT THE SOLUTION I WANT BUT IT WORKS SOMEHOW
        # with open(".\id_file.json", mode="r+") as outfile:
        #     outfile.seek(0,2)
        #     pos = outfile.tell()-1
        #     outfile.seek(pos)
        #     outfile.write(", {}]".format(json.dumps(to_add)))

        print("write/append succesful")

async def setup(bot):
    await bot.add_cog(cmdAdmin(bot))