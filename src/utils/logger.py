from loguru import logger
from pathlib import Path
from .config import settings

PROJECT_ROOT = Path(__file__).resolve().parents[2]
LOG_DIR = PROJECT_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)

def setup_logger():
    logger.remove()
    logger.add(lambda msg: print(msg, end=""), level=settings.log_level)
    logger.add(str(LOG_DIR / "virtutrip.log"), rotation="10 MB", retention="7 days", level="DEBUG")

setup_logger()