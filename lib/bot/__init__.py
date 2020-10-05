from discord.ext.commands import Bot as BotBase
from discord.ext.commands import CommandNotFound
from discord import Embed
from glob import glob
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime 
from asyncio import sleep
from ..db import db

PREFIX = "!"
OWNER_IDS = [572353145963806721]
COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]

class Ready(object):
    def __init__(self):
        for cog in COGS:
            setattr(self, cog, False)
    def ready_up(self, cog):
        setattr(self, cog, True)
        print(f"{cog} cog is ready")

    def all_ready(self):
        return all([getattr(self, cog) for cog in COGS])

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.cogs_ready = Ready()
        self.guild = None
        self.scheduler = AsyncIOScheduler()
        db.autosave(self.scheduler)

        super().__init__(command_prefix=PREFIX, OWNER_ID=OWNER_IDS)

    def setup(self):
        for cog in COGS:
            self.load_extension(f"lib.cogs.{cog}")
            print(f"{cog} cog Loaded")

    def run(self, version):
        self.VERSION = version
        print("running setup")
        self.setup()

        with open("./lib/bot/token", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("Running Shinobu...")
        super().run(self.TOKEN, reconnect=True)
    
    async def on_connect(self):
        print("Ara Ara!")

    async def on_disconnect(self):
        print("Ara Ara Sionara!")

    async def on_error(self, err, *args, **kwargs):
        if err == 'on_command_error':
            await args[0].send("Somthing went wrong.")
        channel = self.get_channel(710051662563115052)
        await channel.send("An error Occurrred")
        raise 

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            pass
        elif hasattr(exc, "original"):
            raise exc.original
        else:
            raise exc

    async def rules_reminder(self):
        self.stdout.send("Remember to follow the rules")

    async def on_ready(self):
        if not self.ready:
            self.guild = self.get_guild(710051662563115049)
            self.stdout = self.get_channel(710051662563115052)
            self.scheduler.start()
            self.scheduler.add_job(self.rules_reminder, CronTrigger(day_of_week=0, hour=12))

            # embed = Embed(title="Ara Ara!!", description="Shinobu is now here", colour=0xFF0000, timestamp=datetime.utcnow())
            # embed.add_field(name="Name", value="Value",inline=False)
            # embed.set_author(name="LunaticSatoshi", icon_url=self.guild.icon_url)
            # embed.set_thumbnail(url=self.guild.icon_url)
            # embed.set_image(url=self.guild.icon_url)
            # embed.set_footer(text="This is a footer")
            # await channel.send(embed=embed)
            while not self.cogs_ready.all_ready():
                await sleep(0.5)
            self.ready = True
            print("Shinobu ready")
            await self.stdout.send("Now Online")
        else:
            print("Shinobu reconnected")

    async def on_message(self, message):
        pass

bot = Bot()