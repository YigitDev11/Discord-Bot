from core.bot import FreshLineBot
from core.config import config
from core.logger import logger

logger.info("Starting the bot...")

bot = FreshLineBot()
try:
    bot.run(str(config.TOKEN))

except KeyboardInterrupt:
    logger.info("The bot is stopped by the user.")

except Exception as e:
    logger.exception(f"An unexpected error occured: {e}")
