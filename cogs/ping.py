import discord
from discord.ext import commands
from discord import app_commands

# Define the Ping class
class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @app_commands.command(
        name = "ping",
        description = "Monitors the delay of the bot."
    )
    async def ping(self, interaction: discord.Interaction):
        gateway_latency = round(self.bot.latency * 1000)

        if gateway_latency < 100:
            color = discord.Color.green()
            status = "🟢 Excellent"

        elif gateway_latency < 250:
            color = discord.Color.gold()
            status = "🟡 Good"

        else:
            color = discord.Color.red()
            status = "🔴 Experiencing Delays"

        embed = discord.Embed(
            title = "🏓 Pong!",
            description = "The bot is operational.",
            color = color
        )
        embed.add_field(
            name = "Gateway Latency",
            value = f"`{gateway_latency} ms`",
            inline = False
        )
        embed.add_field(
            name = "Connection Health",
            value = status,
            inline = False
        )
        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Ping(bot))
