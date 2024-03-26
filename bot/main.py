import discord
import logging
import platform
import os

from discord.ext import commands

def test_dotenv() -> None:
    if type(os.getenv("DISCORD_TOKEN")) != str:
        raise Exception("DISCORD_TOKEN is not set.")
    if type(os.getenv("PREFIX")) != str:
        raise Exception("PREFIX is not set.")

test_dotenv()

class Bot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix=os.getenv("PREFIX"), intents=discord.Intents.all())
        self.bot_handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
        self.bot_formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")

        discord.utils.setup_logging(handler=self.bot_handler, formatter=self.bot_formatter)

    async def setup_hook(self) -> None:
        # get bot data
        await bot.application_info()

    async def on_ready(self) -> None:
        # this will sync all commands on ready but is not recommended on production
        #synced = await self.tree.sync()
        ready_string = f"Logged in as {self.user.mention} | {self.user.id}\n"
        ready_string += f"Python {platform.python_version()}\n"
        ready_string += f"discord.py {discord.__version__}\n"
        #ready_string += f"Synced {len(synced)} commands"

        logging.info(ready_string)
        print(ready_string)

bot: Bot = Bot()

bot.run(os.getenv("DISCORD_TOKEN"))
