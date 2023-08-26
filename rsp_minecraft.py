import discord

def recipes(material):
    match material:
        case "pickaxe": return discord.File("./recipe_img/CraftingTable/Tools/craft_pickaxes.gif")
        case "planks": return discord.File("./recipe_img/CraftingTable/Building Blocks/craft_planks.gif")
        case "torch": return discord.File("./recipe_img/CraftingTable/Decoration Blocks/craft_torch.png")
        case "stick": return discord.File("./recipe_img/CraftingTable/Materials/craft_stick.png")