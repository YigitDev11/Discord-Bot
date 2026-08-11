import discord
from discord import app_commands
from discord.ext import commands

from core.logger import logger
from core.exceptions import APIError, ConfigurationError, CooldownError, DatabaseError, ExternalServiceError, InternalError, NotFoundError, PermissionDenied, InvalidArgument

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

        # ===User Errors===

        if isinstance(original_error, PermissionDenied):
            logger.warning(f"Permission denied for user {interaction.user.id}")
            await self._respond(interaction, "❌ You don't have permission to use this command.")
            return

        if isinstance(original_error, InvalidArgument):
            logger.warning(f"Invalid argument from user {interaction.user.id}")
            await self._respond(interaction, "❌ The provided argument is invalid.")
            return

        if isinstance(original_error, CooldownError):
            logger.warning(f"Command cooldown triggered for user {interaction.user.id}")
            await self._respond(interaction, "⏳ This command is on cooldown. Please try again later.")
            return

        if isinstance(original_error, NotFoundError):
            logger.warning(f"Requested resource not found for user {interaction.user.id}")
            await self._respond(interaction, "❌ The requested resource could not be found.")
            return

        # ===Service Errors===

        if isinstance(original_error, APIError):
            logger.error(f"API Error while handling command for user {interaction.user.id}: {original_error}")
            await self._respond(interaction, "❌ Something went wrong while communicating with a service.")
            return

        if isinstance(original_error, DatabaseError):
            logger.error(f"Database error while handling command for user {interaction.user.id}: {original_error}")
            await self._respond(interaction, "❌ Something went wrong while accessing the database.")
            return

        if isinstance(original_error, ExternalServiceError):
            logger.error(f"External service error while handling command for user {interaction.user.id}: {original_error}")
            await self._respond(interaction, "❌ An external service is currently unavailable.")
            return

        # ===System Errors===

        if isinstance(original_error, ConfigurationError):
            logger.error(f"Configuration error while handling command for user {interaction.user.id}: {original_error}")
            await self._respond(interaction, "❌ The Bot is currently experencing a configuration problem.")
            return

        if isinstance(original_error, InternalError):
            logger.error(f"Internal error while handling command for user {interaction.user.id}: {original_error}")
            await self._respond(interaction, "❌ An internal error occurred while processing your request.")
            return

        # ===Unknown Errors===

        logger.exception(f"UNhandled application command error for user {interaction.user.id}: {original_error}")
        await self._respond(interaction, "❌ An unexpected error occurred while processing your request.")
        return

    def _unwrap_error(self, error: Exception) -> Exception:
        if isinstance(error, app_commands.CommandInvokeError):
            return error.original

        return error
