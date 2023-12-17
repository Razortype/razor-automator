from pathlib import Path

from modules.PatternGenerator.services.generator import pattern_handler
from modules.ProcessHandler.services.screen import Monitor

from common.ConfigHandler.reader import DataReader
from common.Logger.logger import generate_logger
from common.Utils.helpers import (
    _path_joiner
)

BASE_PATH = Path(__file__).parent.parent

APP_CONFIG_PATH = _path_joiner(BASE_PATH, "data", "app_config.json")
APP_CONFIG = DataReader.get_config(APP_CONFIG_PATH)

# Paths
PATTER_CONFIG_PATH = _path_joiner(BASE_PATH, *APP_CONFIG.general.directories.patterns_path)
PATTERNS = DataReader.get_config(PATTER_CONFIG_PATH)

LOGGER = generate_logger(
    log_type=APP_CONFIG.general.logger.log_type,
    logger_name="RAZORTYPE",
    log_path=_path_joiner(BASE_PATH, *APP_CONFIG.general.logger.log_path)
)

pattern_handler.enter_patterns(PATTERNS)

monitor = Monitor(pattern_handler)