from discord.ext.commands import Cog

class Command(Cog):
    def __init__(self,bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        # await self.bot.stdout.send("Command Cog ready")
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("commands")

def setup(bot):
    bot.add_cog(Command(bot))
