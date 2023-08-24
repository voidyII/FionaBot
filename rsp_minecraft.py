import discord

def recipes(material):
    match material:
        case "pickaxe": return discord.File("D:\downloads\images\MinecraftRecipes\CraftingTable\Tools\craft_pickaxes.gif")