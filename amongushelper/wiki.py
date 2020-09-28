import asyncio
from operator import truediv
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


class Wiki(commands.Cog):
    __version__ = "1.0.0"
    __author__ = "xargs"





    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=424914245973442562, force_registration=True)
        defaul_guild = {
			'wikis':{}
			}

        self.config.register_guild(**defaul_guild)

		# Using this to gain data accessing performance via RAM
        self.wikis = {}
        self.lockcommand = {}

    @commands.group(aliases=['w'], invoke_without_command=True)
    @commands.guild_only()
    async def wiki(self, ctx: commands.Context, *, wiki_name:str=None):
        """Returns a wiki as requested by a user"""
        member: discord.Member = ctx.author

        #---- Returns available wikis if user didn't pass a wiki_name ---- 
        if wiki_name is None:
            return await self.send_wiki_list(ctx)
        
        #---- Checks if the bot has permission to mention ----
        if not ctx.channel.permissions_for(ctx.me).mention_everyone:
            return await ctx.send('I require the "Mention Everyone" permission to execute that command.')
        
        #------------Locking command at guild level to disable spam ping---------
        if self.lock_command(ctx):
            return await ctx.send('Someone else is current using this command. Please wait and retry soon.')
        
        #-----------------------Check if wiki is in list-------------------------
        wikis = await self.get_wikis(ctx)
        wiki_name = wiki_name if wiki_name in wikis else await self.find_wiki_name(ctx,wiki_name)

        if wiki_name is None:
            # Couldn't find the wiki or a close match in the list.
            self.unlock_command(ctx)
            return await self.send_wiki_list(ctx)
        
        #---------------------Get wiki_resource from wiki-------------------------
        wiki_resource = wikis.get(wiki_name).get('wiki_resource')

        if wiki_resource is None:
            # if the wiki resource isn't set
            self.unlock_command(ctx)
            return await ctx.send(f'While there\'s a wiki entry for {wiki_name}, there\'s no resource associated with it.')

    @wiki.command()
    @checks.guildowner_or_permissions(administrator=True)
    async def add(self, ctx: commands.Context, wiki_name, *, wiki_resource):
        """Adds a wiki name to a corresponding wiki resource"""
        wikis = await self.get_wikis(ctx)
        if wiki_name in wikis:
            return await ctx.send(f'There\'s already an entry for {wiki_name}.')
        
        await self.add_wiki(ctx, wiki_name, wiki_resource)
        await ctx.tick()

    @wiki.command(name='del', aliases=['delete'])
    @checks.guildowner_or_permissions(administrator=True)
    async def delete(self, ctx: commands.Context, *, wiki_name:str):
        """Adds a wiki name to a corresponding wiki resource"""
        wikis = await self.get_wikis(ctx)
        if wiki_name not in wikis:
            return await ctx.send(f'{wiki_name} isn\'t in the list.')
        
        await self.del_wiki(ctx, wiki_name)
        await ctx.tick()
    
    @wiki.command()
    @checks.guildowner_or_permissions(administrator=True)
    async def cleardata(self, ctx: commands.Context):
        """This will remove all the saved data"""
        await self.config.clear_all()
        self.wikis = {}
        await ctx.tick()

    async def find_wiki_name(self, ctx, wiki_name):
        wikis = await self.get_wikis(ctx)
        match = get_close_matches(wiki_name, wikis.keys(), 1, 0.3)
        if not match:
            # No match found, list of wikis returned instead
            return
        
        msg = await ctx.send(f'I can\'t find a wiki called {wiki_name}. Did you mean`{match[0]}`?')
        start_adding_reactions(msg, ReactionPredicate.YES_OR_NO_EMOJIS)

        try: #waiting for reaction
            pred = ReactionPredicate.yes_or_no(msg, ctx.author)
            await ctx.bot.wait_for("reaction_add", check=pred, timeout=15)
        except asyncio.TimeoutError:
            await ctx.send("You didn\'t react in time, cancelled.")

        try: # Delete reactions from question message
            if ctx.channel.permissions_for(ctx.me).manage_messages:
                await msg.clear_reactions()
        except:
                pass

        if pred.result is not True:
            return # User didn't responded with tick
            
        wiki_name = match[0]
        return wiki_name
    
    async def send_wiki_list(self, ctx):
        wikis = await self.get_wikis(ctx)

        #---------------------Check if there is a list of wikis------------------
        if wikis is None:
            return await ctx.send("There are currently no wikis on the list.")

        #---------------------Create a game list message------------------------
        name_wikis = [n for n in wikis.keys()]
        await ctx.send('>>> **Wiki List:**\n' + '\n'.join(name_wikis))

    async def send_setting_wikis(self, ctx):
        wikis = await self.get_wikis(ctx)
    
        #---------------------Check if there is a list of wikis------------------
        if wikis is None:
            return await ctx.send("There are currently no wikis on the list.")

        #---------------------Create a wiki info message------------------------
        txt = '>>> **Wiki settings list**\n'
        for wiki_name, info in wikis.items():
            wiki_resource = info['wiki_resource']
            txt += f'`{wiki_name}` | {wiki_resource}\n'
        await ctx.send(txt)

    def lock_command(self,ctx):
        guild_id = str(ctx.guild.id)
        if self.lockcommand.get(guild_id, False):
            return True
        self.lockcommand.update({guild_id:True})
        return False
    
    def unlock_command(self, ctx):
        guild_id = str(ctx.guild.id)
        self.lockcommand.update({guild_id:False})
    

    #==============================Caching Function=============================
	#-----------------------------------Wikis-----------------------------------
    async def get_wikis(self, ctx):
        guild_id = str(ctx.guild.id)
        wikis = self.wikis.get(guild_id)
        if wikis is None:
            guild_group = self.config.guild(ctx.guild)
            wikis = await guild_group.wikis()
            self.wikis.update({guild_id:wikis})
        return wikis

    async def add_wiki(self, ctx, wiki_name, wiki_resource):
        guild_id = str(ctx.guild.id)
        wikis = await self.get_wikis(ctx)

        wikis[wiki_name] = {
            'wiki_resource':wiki_resource
        }

        await self.config.guild(ctx.guild.id).wikis.set(wikis)
        self.wikis.update({guild_id:wikis})

    async def del_wiki(self, ctx, wiki_name):
        guild_id = str(ctx.guild.id)
        wikis = await self.get_wikis(ctx)

        try:
            del wikis[wiki_name]
        except KeyError:
            pass

        await self.config.guild(ctx.guild).wikis.set(wikis)
        self.wikis.update({guild_id:wikis})