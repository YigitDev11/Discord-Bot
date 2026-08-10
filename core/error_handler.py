import discord
from discord import app_commands
from discord.ext import commands

from core.exceptions import PermissionDenied
from core.logger import logger

class GlobalErrorHandler:
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def handle_app_command_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError) -> None:
        original_error = self._unwrap_error(error)
        if isinstance(original_error, PermissionDenied):
            logger.warning(f"Permission denied for user {interaction.user.id}")
            await interaction.response.send_message("❌ You don't have permission to use this command.", ephemeral=True)
            return
    def _unwrap_error(self, error: Exception) -> Exception:
        if isinstance(error, app_commands.CommandInvokeError):
            return error.original

        return error
