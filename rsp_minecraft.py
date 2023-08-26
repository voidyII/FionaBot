import discord

def recipes(material):
    match material:
        # Workbench
        case "workbench": return discord.File("./recipe_img/CraftingTable/craft_workbench.png")

        # Brewing

        # Building Blocks
        case "planks": return discord.File("./recipe_img/CraftingTable/Building Blocks/craft_planks.gif")

        # Combat

        # Decoration Blocks
        case "chest": return discord.File("./recipe_img/CraftingTable/Decoration Blocks/craft_chest.png")
        case "fence": return discord.File("./recipe_img/CraftingTable/Decoration Blocks/craft_fence.gif")
        case "furnace": return discord.File("./recipe_img/CraftingTable/Decoration Blocks/craft_furnace.png")
        case "shulkerBox": return discord.File("./recipe_img/CraftingTable/Decoration Blocks/craft_shulkerbox.png")
        case "torch": return discord.File("./recipe_img/CraftingTable/Decoration Blocks/craft_torch.png")

        # Food

        # Materials
        case "stick": return discord.File("./recipe_img/CraftingTable/Materials/craft_stick.png")

        # Redstone

        # Tools
        case "axe": return discord.File("./recipe_img/CraftingTable/Tools/craft_axes.gif")
        case "brush": return discord.File("./recipe_img/CraftingTable/Tools/craft_brush.png")
        case "bucket": return discord.File("./recipe_img/CraftingTable/Tools/craft_bucket.png")
        case "clock": return discord.File("./recipe_img/CraftingTable/Tools/craft_clock.png")
        case "compass": return discord.File("./recipe_img/CraftingTable/Tools/craft_compass.png")
        case "fishing rod": return discord.File("./recipe_img/CraftingTable/Tools/craft_fisingrod.png")
        case "flint&steel": return discord.File("./recipe_img/CraftingTable/Tools/craft_flintandsteel.png")
        case "hoe": return discord.File("./recipe_img/CraftingTable/Tools/craft_hoes.gif")
        case "pickaxe": return discord.File("./recipe_img/CraftingTable/Tools/craft_pickaxes.gif")
        case "recoveryCompass": return discord.File("./recipe_img/CraftingTable/Tools/craft_recoverycompass.png")
        case "shears": return discord.File("./recipe_img/CraftingTable/Tools/craft_shears.png")
        case "shovel": return discord.File("./recipe_img/CraftingTable/Tools/craft_shovels.gif")
        case "spyglass": return discord.File("./recipe_img/CraftingTable/Tools/craft_spyglass.png")

        # Transportation

        # Misc
        case "map": return discord.File("./recipe_img/CraftingTable/Tools/craft_map.png")
        