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
    async def map(self, ctx, map_name:str=None):
        if map_name == None
            await ctx.send("No map specified. Please select polus / skeld / mira")
        if map_name == "polus"
            await ctx.send("https://vignette.wikia.nocookie.net/among-us-wiki/images/4/4c/Polus.png")
        elif map_name == "skeld"
            await ctx.send("https://vignette.wikia.nocookie.net/among-us-wiki/images/4/4f/SKELD_MAP.jpg")
        elif map_name == "mira"
            await ctx.send("https://vignette.wikia.nocookie.net/among-us-wiki/images/0/0a/Mirahq.png")
        else:
            await ctx.send("Map name ", map_name, " not recognised.")
