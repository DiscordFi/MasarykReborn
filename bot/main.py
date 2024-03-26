import discord
import logging
import platform
import os

from discord.ext import commands

# define constants
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if type(DISCORD_TOKEN) != str:
    raise Exception("DISCORD_TOKEN is not set.")

COMMAND_PREFIX = os.getenv("COMMAND_PREFIX")
if type(COMMAND_PREFIX) != str:
    raise Exception("COMMAND_PREFIX is not set.")
elif len(COMMAND_PREFIX) == 0:
    raise Exception("COMMAND_PREFIX is not meant to be empty.")

class Bot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix=COMMAND_PREFIX, intents=discord.Intents.all())
        self.bot_handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
        self.bot_formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")

        discord.utils.setup_logging(handler=self.bot_handler, formatter=self.bot_formatter)

    async def setup_hook(self) -> None:
        # get bot data
        await bot.application_info()

    async def on_ready(self) -> None:
        assert self.user is not None
        # this will sync all commands on ready but is not recommended on production
        #synced = await self.tree.sync()
        ready_string = f"Logged in as {self.user.mention} | {self.user.id}\n"
        ready_string += f"Python {platform.python_version()}\n"
        ready_string += f"discord.py {discord.__version__}\n"
        #ready_string += f"Synced {len(synced)} commands"

        logging.info(ready_string)
        print(ready_string)

bot: Bot = Bot()

bot.run(DISCORD_TOKEN)
