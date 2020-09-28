import asyncio
import time
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
        "polus":"https://vignette.wikia.nocookie.net/among-us-wiki/images/4/4c/Polus.png",
        "skeld":"https://vignette.wikia.nocookie.net/among-us-wiki/images/4/4f/SKELD_MAP.jpg",
        "mira":"https://vignette.wikia.nocookie.net/among-us-wiki/images/0/0a/Mirahq.png"
    }

    @commands.command()
    async def map(self, ctx, map_name):
        await ctx.send(self.maps.get(map_name, f"{map_name} isn't a recognised map. Try Polus, Skeld or Mira"))

    wikis = {
        "crewmate":"https://among-us.fandom.com/wiki/Crewmate",
        "imposter":"https://among-us.fandom.com/wiki/Impostor",
        "use":"https://among-us.fandom.com/wiki/Use",
        "report":"https://among-us.fandom.com/wiki/Report",
        "kill":"https://among-us.fandom.com/wiki/Kill",
        "sabotage":"https://among-us.fandom.com/wiki/Sabotage",
        "vent":"https://among-us.fandom.com/wiki/Vent",
        "security":"https://among-us.fandom.com/wiki/Security",
        "doorlog":"https://among-us.fandom.com/wiki/Doorlog",
        "vitals":"https://among-us.fandom.com/wiki/Vitals",
        "tasks":"https://among-us.fandom.com/wiki/Tasks"
    }

    @commands.command()
    async def wiki(self, ctx, wiki_name):
        await ctx.send(self.wikis.get(wiki_name.lower(), f"I can't find a wiki for {wiki_name}. I have actions (kill, report etc) and roles (crewmate/imposter)."))