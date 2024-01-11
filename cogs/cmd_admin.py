import discord
from discord.ext import commands
import json

class cmdAdmin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    # @commands.has_role("Developer")
    async def role(self, ctx, arg):

        role_file = open(".\cogfunctions\msg_roles.json", "r")
        role_dat = json.load(role_file)

        #needs handling if role doesnt exist
        for roleitem in role_dat:
            if roleitem.get("cmd_name") == arg:
                role_id = roleitem.get("role_id")
                role_name = roleitem.get("role_name")
                role = discord.utils.get(ctx.guild.roles, id=role_id, name=role_name)
                user = ctx.message.author
                await user.add_roles(role)
                #personality sucks
                await ctx.send(f"Yayy, you now have the {role_name} role :D")
                break
            else: continue
        
        # arg_list = []
        # index = len(arg_list)
        # arg_list.insert(index, args)

        # await ctx.message.delete()

        # moji = await  ctx.channel.send(
        #     "React to this message with one of the following Emojis to get a role assigned:\n"
        #     f"\{arg_list[0][0]}: {arg_list[0][1]}\n"
        #     f"\{arg_list[0][2]}: {arg_list[0][3]}"
        #     )
        
        # i=0
        # while i < len(arg_list[0])-1:
        #     emoji = arg_list[0][i]
        #     await moji.add_reaction(emoji)
        #     i = i + 2

        # def rolesList(list):
        #     i = 1
        #     while i < len(list[0])-1:
        #         role = list[0][i]
 
        # roleargs = {"role1": arg_list[0][1], "role2": arg_list[0][3]}

        # reac = await moji.channel.fetch_message(moji.id)
        # reac_list = reac.reactions
        # print(reac_list)
            
        # i=0
        # k=1
        # while i < len(reac.reactions)-1:
        #     emoji = f"emoji{k}"
        #     reac_dic = {}
        #     reac_dic.update(emoji = reac_list[i])
        #     i = i + 2
        #     k = k + 1

        # print(reac_dic)

        # to_add = {
        #     "guild": moji.channel.guild.name,
        #     "guild_id": moji.channel.guild.id,
        #     "chnl": moji.channel.name,
        #     "chnl_id": moji.channel.id,
        #     "type": moji.channel.type,
        #     "msg_id": moji.id,
        #     "roles": roleargs,
        #     #"emoji": reac_dic
        # }

        # print("dic created")

        # # my code for the version found on sof
        # with open(".\cogfunctions\msg_roles.json", "r+") as id_dat:
        #     id_dat.seek(0, 2)
        #     dat_pos = id_dat.tell()-3
        #     id_dat.seek(dat_pos)
        #     new_dat = ",\n    {}\n]".format(json.dumps(to_add))
        #     id_dat.write(new_dat)

        # #I FOUND THIS ON STACKOVERFLOW, THIS IS NOT THE SOLUTION I WANT BUT IT WORKS SOMEHOW
        # # with open(".\id_file.json", mode="r+") as outfile:
        # #     outfile.seek(0,2)
        # #     pos = outfile.tell()-1
        # #     outfile.seek(pos)
        # #     outfile.write(", {}]".format(json.dumps(to_add)))

        # print("write/append succesful")
    
    @commands.command()
    async def rolerm(self, ctx, arg):
        role_file = open(".\cogfunctions\msg_roles.json", "r")
        role_dat = json.load(role_file)
        
        for roleitem in role_dat:
            if roleitem.get("cmd_name") == arg:
                role_id = roleitem.get("role_id")
                role_name = roleitem.get("role_name")
                user = ctx.message.author
                user_roles = ctx.message.author.roles
                role = discord.utils.get(ctx.guild.roles, id=role_id, name=role_name)
                if role in user_roles:
                    await user.remove_roles(role)
                    #fiona personality sucks here
                    await ctx.send("You now don't have that role anymore :(")
                    break
                else:
                    #personality sucks
                    await ctx.send("You're trying to remove a role you don't even have!! >:(")
            else: continue

async def setup(bot):
    await bot.add_cog(cmdAdmin(bot))