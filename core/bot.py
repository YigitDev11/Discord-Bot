import discord
from discord.ext import commands
from core.logger import logger

class FreshLineBot(commands.Bot):
    def __init__(self):
        # Set access privileges of the bot.
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(
            command_prefix="!",
            intents=intents
        )

        logger.info("FreshLine bot initialized")

    async def setup_hook(self):
        await self.load_extension("cogs.ping") # Load the ping cog
        logger.info("Loaded extension: cogs.ping") # Inform the user
        synced = await self.tree.sync() # Synchronize
        logger.info(f"Synchronized {len(synced)} application command(s).") # Inform the user


    async def on_ready(self):
        assert self.user is not None
        logger.info("=" * 40)
        logger.info(f"Logged in as {self.user}")
        logger.info(f"Bot ID: {self.user.id}")
        logger.info(f"Connected to {len(self.guilds)} guild(s)")
        logger.info("=" * 40)
