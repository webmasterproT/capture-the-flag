```python
import logging
import os
from datetime import datetime

# Define the logging levels
LOG_LEVELS = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL
}

# Define the log format
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Define the directory for log files
LOG_DIR = 'data/logs'
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Define the log file name with a timestamp
LOG_FILE = os.path.join(LOG_DIR, f'log_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')

# Configure the logger
logging.basicConfig(
    level=LOG_LEVELS['DEBUG'],
    format=LOG_FORMAT,
    filename=LOG_FILE,
    filemode='a'
)

# Create a logger object
logger = logging.getLogger(__name__)

def log_action(action, level='INFO'):
    """
    Log an action with the specified level.
    """
    if level in LOG_LEVELS:
        getattr(logger, level.lower())(action)
    else:
        logger.error(f'Invalid log level: {level}')

def log_error(error_msg):
    """
    Log an error message.
    """
    logger.error(error_msg)

def log_info(info_msg):
    """
    Log an informational message.
    """
    logger.info(info_msg)

def get_log_file_path():
    """
    Return the path to the current log file.
    """
    return LOG_FILE

# Example usage:
# log_action("Starting the application", level='INFO')
# log_error("An error occurred")
# log_info("This is an informational message")
```