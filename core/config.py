from dotenv import load_dotenv
from core.exceptions import ConfigurationError
import os

load_dotenv()

class Config:
    def __init__(self):
        self.TOKEN = os.getenv("DISCORD_TOKEN")
        self.DEBUG = os.getenv("DEBUG", "false").lower()

        if not self.TOKEN:
            raise ConfigurationError(
                "DISCORD_TOKEN is not set in environment."
            )
        if self.DEBUG not in ["true", "false"]:
            raise ConfigurationError(
                "DEBUG must be set to true or false."
            )

config = Config()
