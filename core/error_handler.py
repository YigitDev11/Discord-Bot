import discord
from discord import app_commands
from discord.ext import commands

from core.exceptions import PermissionDenied, InvalidArgument
from core.logger import logger

class GlobalErrorHandler:
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def _respond(self, interaction: discord.Interaction, message: str) -> None:
        if interaction.response.is_done():
            await interaction.followup.send(message, ephemeral=True)
        else:
            await interaction.response.send_message(message, ephemeral=True)

    async def handle_app_command_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError) -> None:
        original_error = self._unwrap_error(error)

        if isinstance(original_error, PermissionDenied):
            logger.warning(f"Permission denied for user {interaction.user.id}")
            await self._respond(interaction, "❌ You don't have permission to use this command.")
            return

        if isinstance(original_error, InvalidArgument):
            logger.warning(f"Invalid argument from user {interaction.user.id}")
            await self._respond(interaction, "❌ The provided argument is invalid.")
            return

    def _unwrap_error(self, error: Exception) -> Exception:
        if isinstance(error, app_commands.CommandInvokeError):
            return error.original

        return error
