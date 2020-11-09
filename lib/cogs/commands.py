from discord.ext.commands import Cog
from discord.ext.commands import command

class Command(Cog):
    def __init__(self,bot):
        self.bot = bot

    @command(name="hello", aliases=["hola", "h"], hidden=True)
    async def say_hello(self, ctx):
        await ctx.send(f"Hello {ctx.author.mention}!")
        pass

    @Cog.listener()
    async def on_ready(self):
        # await self.bot.stdout.send("Command Cog ready")
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("commands")

def setup(bot):
    bot.add_cog(Command(bot))
