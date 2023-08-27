import discord

def recipes(material):
    match material:
        # Workbench
        case "workbench": return discord.File("./recipe_img/CraftingTable/craft_workbench.png")

        # Brewing
        case "blazepowder": return discord.File("./recipe_img/CraftingTable/Brewing/craft_blazepowder.png")
        case "brewingstand": return discord.File("./recipe_img/CraftingTable/Brewing/craft_brewingstand.png")
        case "cauldron": return discord.File("./recipe_img/CraftingTable/Brewing/craft_cauldron.png")
        case "fermentedSpiderEye": return discord.File("./recipe_img/CraftingTable/Brewing/craft_fermentedspidereye.png")
        case "glassbottle": return discord.File("./recipe_img/CraftingTable/Brewing/craft_glassbottle.png")
        case "blazepowder": return discord.File("./recipe_img/CraftingTable/Brewing/craft_glisteringmelon.png")
        case "blazepowder": return discord.File("./recipe_img/CraftingTable/Brewing/craft_magmacream.png")

        # Building Blocks
        case "planks": return discord.File("./recipe_img/CraftingTable/Building Blocks/craft_planks.gif")

        # Decoration Blocks
        case "chest": return discord.File("./recipe_img/CraftingTable/Decoration Blocks/craft_chest.png")
        case "fence": return discord.File("./recipe_img/CraftingTable/Decoration Blocks/craft_fence.gif")
        case "furnace": return discord.File("./recipe_img/CraftingTable/Decoration Blocks/craft_furnace.png")
        case "shulkerBox": return discord.File("./recipe_img/CraftingTable/Decoration Blocks/craft_shulkerbox.png")
        case "torch": return discord.File("./recipe_img/CraftingTable/Decoration Blocks/craft_torch.png")

        # Redstone

        #Transportation
        case "activatorrail": return discord.File("./recipe_img/CraftingTable/Transportation/craft_activatorrail.png")
        case "boat": return discord.File("./recipe_img/CraftingTable/Transportation/craft_boat.png")
        case "boatxchest": return discord.File("./recipe_img/CraftingTable/Transportation/craft_boatwithchest.png")
        case "carrotstick": return discord.File("./recipe_img/CraftingTable/Transportation/craft_carrotonastick.png")
        case "detectorrail": return discord.File("./recipe_img/CraftingTable/Transportation/craft_detectorrail.png")
        case "furnaceminecart": return discord.File("./recipe_img/CraftingTable/Transportation/craft_furnaceminecart.png")
        case "minecart": return discord.File("./recipe_img/CraftingTable/Transportation/craft_minecart.png")
        case "minecartxhopper": return discord.File("./recipe_img/CraftingTable/Transportation/craft_minecartwithhopper.png")
        case "minecartxtnt": return discord.File("./recipe_img/CraftingTable/Transportation/craft_minecartwithtnt.png")
        case "poweredrail": return discord.File("./recipe_img/CraftingTable/Transportation/craft_poweredrail.png")
        case "rail": return discord.File("./recipe_img/CraftingTable/Transportation/craft_rail.png")
        case "chestminecart": return discord.File("./recipe_img/CraftingTable/Transportation/craft_storageminecart.png")
        case "warpedfungusstick": return discord.File("./recipe_img/CraftingTable/Transportation/craft_warpedfungusonastick.png")

        # Food
        case "bread": return discord.File("./recipe_img/CraftingTable/Food/craft_bread.png")
        case "cake": return discord.File("./recipe_img/CraftingTable/Food/craft_cake.png")
        case "cookie": return discord.File("./recipe_img/CraftingTable/Food/craft_cookie.png")
        case "goldenapple": return discord.File("./recipe_img/CraftingTable/Food/craft_goldenapple.png")
        case "goldencarrot": return discord.File("./recipe_img/CraftingTable/Food/craft_goldencarrot.png")
        case "honeybottle": return discord.File("./recipe_img/CraftingTable/Food/craft_honeybottle.png")
        case "mushroomstew": return discord.File("./recipe_img/CraftingTable/Food/craft_mushroomstew.png")
        case "pumpkinpie": return discord.File("./recipe_img/CraftingTable/Food/craft_pumpkinpie.png")
        case "rabbitstew": return discord.File("./recipe_img/CraftingTable/Food/craft_rabbitstew.png")
        case "suspiciousstew": return discord.File("./recipe_img/CraftingTable/Food/craft_suspiciousstew.png")

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

        # Combat
        case "arrow": return discord.File("./recipe_img/CraftingTable/Combat/craft_arrow.png")
        case "boots": return discord.File("./recipe_img/CraftingTable/Combat/boots.gif")
        case "bow": return discord.File("./recipe_img/CraftingTable/Combat/craft_bow.png")
        case "chestplate": return discord.File("./recipe_img/CraftingTable/Combat/craft_chestplates.gif")
        case "crossbow": return discord.File("./recipe_img/CraftingTable/Combat/craft_crossbow.png")
        case "helmets": return discord.File("./recipe_img/CraftingTable/Combat/craft_helmets.gif")
        case "leggings": return discord.File("./recipe_img/CraftingTable/Combat/craft_leggings.gif")
        case "shield": return discord.File("./recipe_img/CraftingTable/Combat/craft_shield.png")
        case "spectralarrow": return discord.File("./recipe_img/CraftingTable/Combat/craft_spectralarrow.png")
        case "swords": return discord.File("./recipe_img/CraftingTable/Combat/craft_swords.gif")
        case "tippedarrow": return discord.File("./recipe_img/CraftingTable/Combat/craft_tippedarrow.png")

        # Brewing
        case "blazepowder": return discord.File("./recipe_img/CraftingTable/Brewing/craft_blazepowder.png")
        case "brewingstand": return discord.File("./recipe_img/CraftingTable/Brewing/craft_brewingstand.png")
        case "cauldron": return discord.File("./recipe_img/CraftingTable/Brewing/craft_cauldron.png")
        case "fermentedSpidereye": return discord.File("./recipe_img/CraftingTable/Brewing/craft_fermentedspidereye.png")
        case "glassbottle": return discord.File("./recipe_img/CraftingTable/Brewing/craft_glassbottle.png")
        case "glisteringMelon": return discord.File("./recipe_img/CraftingTable/Brewing/craft_glisteringmelon.png")
        case "magmacream": return discord.File("./recipe_img/CraftingTable/Brewing/craft_magmacream.png")

        # Materials
        case "bonemeal": return discord.File("./recipe_img/CraftingTable/Materials/craft_bonemeal.png")
        case "bowl": return discord.File("./recipe_img/CraftingTable/Materials/craft_bowl.png")
        case "goldingot": return discord.File("./recipe_img/CraftingTable/Materials/craft_goldingot.png")
        case "ironnugget": return discord.File("./recipe_img/CraftingTable/Materials/craft_ironnugget.png")
        case "leather": return discord.File("./recipe_img/CraftingTable/Materials/craft_leather.png")
        case "melonseeds": return discord.File("./recipe_img/CraftingTable/Materials/craft_melonseeds.png")
        case "netheriteingot": return discord.File("./recipe_img/CraftingTable/Materials/craft_netheriteingot.png")
        case "pumpkinseeds": return discord.File("./recipe_img/CraftingTable/Materials/craft_pumpkinseeds.png")
        case "stick": return discord.File("./recipe_img/CraftingTable/Materials/craft_stick.png")
        case "sugar": return discord.File("./recipe_img/CraftingTable/Materials/craft_sugar.png")

        # Misc
        case "beacon": return discord.File("./recipe_img/CraftingTable/Misc/craft_beacon.png")
        case "book": return discord.File("./recipe_img/CraftingTable/Misc/craft_book.png")
        case "book&quill": return discord.File("./recipe_img/CraftingTable/Misc/craft_bookandquill.png")
        case "bucket": return discord.File("./recipe_img/CraftingTable/Misc/craft_bucket.png")
        case "composter": return discord.File("./recipe_img/CraftingTable/Misc/craft_composter.png")
        case "Endereye": return discord.File("./recipe_img/CraftingTable/Misc/craft_eyeofender.png")
        case "firecharge": return discord.File("./recipe_img/CraftingTable/Misc/craft_firecharge.png")
        case "fireworkRocket": return discord.File("./recipe_img/CraftingTable/Misc/craft_fireworkrocket.gif")
        case "fireworkStar": return discord.File("./recipe_img/CraftingTable/Misc/craft_fireworkstar.gif")
        case "horsearmor": return discord.File("./recipe_img/CraftingTable/Misc/craft_horsearmor.png")
        case "map": return discord.File("./recipe_img/CraftingTable/Tools/craft_map.png")
        case "paper": return discord.File("./recipe_img/CraftingTable/Misc/craft_paper.png")

def colors(color):
    match color:
        case "black": return discord.File("./recipe_img/CraftingTable/Dyes/craft_blackdye.gif")
        case "blue": return discord.File("./recipe_img/CraftingTable/Dyes/craft_bluedye.gif")
        case "brown": return discord.File("./recipe_img/CraftingTable/Dyes/craft_browndye.png")
        case "cyan": return discord.File("./recipe_img/CraftingTable/Dyes/craft_cyandye.gif")
        case "gray": return discord.File("./recipe_img/CraftingTable/Dyes/craft_graydye.png")
        case "lightblue": return discord.File("./recipe_img/CraftingTable/Dyes/craft_lightbluedye.gif")
        case "lightgrey": return discord.File("./recipe_img/CraftingTable/Dyes/craft_lightgraydye.gif")
        case "lime": return discord.File("./recipe_img/CraftingTable/Dyes/craft_limedye.png")
        case "magenta": return discord.File("./recipe_img/CraftingTable/Dyes/craft_magenatdye.gif")
        case "orange": return discord.File("./recipe_img/CraftingTable/Dyes/craft_orangedye.gif")
        case "pink": return discord.File("./recipe_img/CraftingTable/Dyes/craft_pinkdye.gif")
        case "purple": return discord.File("./recipe_img/CraftingTable/Dyes/craft_purpledye.png")
        case "red": return discord.File("./recipe_img/CraftingTable/Dyes/craft_reddye.gif")
        case "white": return discord.File("./recipe_img/CraftingTable/Dyes/craft_whitedye.gif")
        case "yellow": return discord.File("./recipe_img/CraftingTable/Dyes/craft_yellowdye.gif")
        