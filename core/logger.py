import logging
from core.config import config

# Create Logger
logger = logging.getLogger("FreshLine")
logger.setLevel(logging.DEBUG if config.DEBUG else logging.INFO)
# Create Handler
handler = logging.StreamHandler()
# Create Formatter
formatter = logging.Formatter(
    fmt="%(asctime)s -  %(filename)s | %(levelname)s |: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
# Connect Formatter to Handler
handler.setFormatter(formatter)
# Connect Handler to Logger
logger.addHandler(handler)

logger.info("Logger initialized.")
