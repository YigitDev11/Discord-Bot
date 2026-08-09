import logging
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from core.config import config

# Defining static variables
LOG_DIRECTORY = Path("logs")
LOG_DIRECTORY.mkdir(parents=True, exist_ok=True)
TIMEZONE = ZoneInfo("Europe/Istanbul")
#Create the DailyFileHandler class for special file logging seamlessly.
class DailyFileHandler(logging.FileHandler):
    def _today(self) -> str:
        return datetime.now(TIMEZONE).strftime("%Y-%m-%d")
    def __init__(self, log_directory: Path):
        self.log_directory = log_directory # Setting up the log directory
        self.current_date = self._today() # Detecting today's date
        log_file = self.log_directory / f"{self.current_date}.log" # Setting up the log file

        super().__init__(
            filename=log_file,
            encoding="utf-8"
        )
    def _switch_log_file(self, new_date: str):
        if self.stream:
            self.stream.flush()
            self.stream.close()
        self.current_date = new_date
        log_file = self.log_directory / f"{new_date}.log"
        self.baseFilename = str(log_file)
        self.stream = self._open()
    def emit(self, record):
        today = self._today()
        if today != self.current_date:
            self._switch_log_file(today)
        super().emit(record)


# Create Logger
logger = logging.getLogger("FreshLine.Core")
logger.setLevel(logging.DEBUG if config.DEBUG else logging.INFO)
logger.propagate = False # To prevent repeating logs
# Create Handlers
console_handler = logging.StreamHandler()
file_handler = DailyFileHandler(LOG_DIRECTORY)
# Create Formatter
formatter = logging.Formatter(
    fmt="%(asctime)s -  %(filename)s | %(levelname)s |: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
# Connect Formatter to Handlers
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
# Connect Handler to Logger
if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
logger.info(f"{logger.name} initialized.")
