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

maps = {
    "polus" : "https://vignette.wikia.nocookie.net/among-us-wiki/images/4/4c/Polus.png",
    "skeld" : "https://vignette.wikia.nocookie.net/among-us-wiki/images/4/4f/SKELD_MAP.jpg",
    "mira" : "https://vignette.wikia.nocookie.net/among-us-wiki/images/0/0a/Mirahq.png"
}

@commands.command()
def map(self, ctx, map_name: str):
    ctx.send(maps[map_name])
    ctx.send(map_name)