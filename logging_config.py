import os
import sys

from loguru import logger

sink = "app.log"
if 'LOG_SINK' in os.environ and os.environ['LOG_SINK'] == 'stdout':
    sink = sys.stdout

log_level = "INFO"
if 'LOG_LEVEL' in os.environ:
    log_level = str.upper(os.environ['LOG_LEVEL'])

logger.add(sink, rotation="20 MB", level=log_level)
