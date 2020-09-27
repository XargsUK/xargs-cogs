import asyncio, time
from typing import Union
from difflib import get_close_matches

# Discord.py
import discord

# Red
from redbot.core import checks, commands, Config
from redbot.core.bot import Red
from redbot.core.utils.predicates import ReactionPredicate
from redbot.core.utils.menus import start_adding_reactions
# from redbot.core.utils.chat_formatting import humanize_list

class amongushelper(commands.Cog):

	__version__ = "1.0.0"
	__author__ = "xargs"
    
@commands.command()
async def map(self, ctx, map_name:str):
    """Returns the Among Us map resource"""
    if map_name is "polus":
        await ctx.send("Polus")
        await ctx.send("https://vignette.wikia.nocookie.net/among-us-wiki/images/4/4c/Polus.png")
    elif map_name is "skeld":
        await ctx.send("https://vignette.wikia.nocookie.net/among-us-wiki/images/4/4f/SKELD_MAP.jpg")
    elif map_name is "mira":
        await ctx.send("https://vignette.wikia.nocookie.net/among-us-wiki/images/0/0a/Mirahq.png")
    else:
        await ctx.send("Map not recognised. Please select polus / skeld / mira")