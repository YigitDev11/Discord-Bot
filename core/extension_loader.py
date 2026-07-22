from pathlib import Path
from discord.ext import commands
from core.logger import logger

async def load_extensions(bot: commands.Bot):
    for file in Path("cogs").glob("*.py"):
        if file.stem == "__init__":
            continue
        extension = f"cogs.{file.stem}"
        await bot.load_extension(extension)
        logger.info(f"Loaded extension: {extension}")
