import discord
from discord import app_commands
from discord.ext import commands

from core.extension_loader import load_extensions
from core.error_handler import GlobalErrorHandler
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
        self.error_handler = GlobalErrorHandler(self)
        self.tree.on_error = self.on_tree_error

        logger.info("FreshLine bot initialized")

    async def setup_hook(self):
        await load_extensions(self) # Load the cogs automatically
        synced = await self.tree.sync() # Synchronize
        logger.info(f"Synchronized {len(synced)} application command(s).") # Inform the user

    async def on_ready(self):
        assert self.user is not None
        logger.info("=" * 40)
        logger.info(f"Logged in as {self.user}")
        logger.info(f"Bot ID: {self.user.id}")
        logger.info(f"Connected to {len(self.guilds)} guild(s)")
        logger.info("=" * 40)

    async def on_tree_error(
        self,
        interaction: discord.Interaction,
        error: app_commands.AppCommandError
    ) -> None:
        await self.error_handler.handle_app_command_error(interaction,error)
