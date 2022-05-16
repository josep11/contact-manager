import logging
import os
from app.app_config import AppConfig

home = os.path.expanduser("~")

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# -------------------------------- #
# -------- BEGIN CONFIG ---------- #
# -------------------------------- #
DEBUG_LOG_FILENAME = "debug.log"
PROD_LOG_FILENAME = "editpasteapp.log"
# -------------------------------- #
# --------- END CONFIG ----------- #
# -------------------------------- #

# https://docs.python.org/3/howto/logging.html
log_file_dir = home + f"/Library/Logs/{AppConfig.APP_NAME}/"  # create logs directory if not exists
log_file = log_file_dir + PROD_LOG_FILENAME
try:
    os.makedirs(log_file_dir)
except FileExistsError as e:
    pass

if AppConfig.isDev:
    logging.basicConfig(filename=DEBUG_LOG_FILENAME, encoding="utf-8", level=logging.DEBUG)
else:
    logging.basicConfig(
        filename=log_file, encoding="utf-8", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
    )
