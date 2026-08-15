import discord
from discord.ext import commands
from discord import app_commands

from core.metadata import GEN_DESCRIPTION, NAME, GENERATION, VER_DESCRIPTION, VERSION, MAIN_DESCRIPTION

class Info(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name = "info",
        description = "Informs the user with general information about this bot."
    )

    async def info(self, interaction: discord.Interaction):
        novum_red = discord.Color.from_str("#8B0000")
        embed = discord.Embed(
            title = f"Name: {NAME}",
            description = MAIN_DESCRIPTION,
            color = novum_red
        )
        embed.add_field(
            name = f"Generation: {GENERATION}",
            value = GEN_DESCRIPTION
        )
        embed.add_field(
            name = f"Version: {VERSION}",
            value = VER_DESCRIPTION
        )

        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Info(bot))
