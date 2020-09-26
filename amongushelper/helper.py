from redbot.core import commands

class helper(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def map(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("Map!")