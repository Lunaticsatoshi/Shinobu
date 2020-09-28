from discord.ext.commands import Bot as BotBase
from apscheduler.schedulers.asyncio import AsyncIOScheduler

PREFIX = "!"
OWNER_IDS = [572353145963806721]

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        super().__init__(command_prefix=PREFIX, OWNER_ID=OWNER_IDS)

    def run(self, version):
        self.VERSION = version

        with open("./lib/bot/token", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("Running Shinobu...")
        super().run(self.TOKEN, reconnect=True)
    
    async def on_connect(self):
        print("Ara Ara!")

    async def on_disconnect(self):
        print("Ara Ara Sionara!")

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(710051662563115049)
            print("Shinobu ready")
        else:
            print("Shinobu reconnected")

    async def on_message(self, message):
        pass

bot = Bot()