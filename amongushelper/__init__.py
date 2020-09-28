from .wiki import Wiki

async def setup(bot):
	cog = Wiki(bot)
	bot.add_cog(cog)