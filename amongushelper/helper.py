from redbot.core import commands

class helper(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def map(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("Map!")

    @commands.command()
    async def maptest(self, ctx, map_name:str):
        if map_name == "polus"
            await ctx.send("https://vignette.wikia.nocookie.net/among-us-wiki/images/4/4c/Polus.png")
        elif map_name == "skeld"
            await ctx.send("https://vignette.wikia.nocookie.net/among-us-wiki/images/4/4f/SKELD_MAP.jpg")
        elif map_name == "mira"
            await ctx.send("https://vignette.wikia.nocookie.net/among-us-wiki/images/0/0a/Mirahq.png")
        else:
            await ctx.send("Map not recognised. Please select polus / skeld / mira")