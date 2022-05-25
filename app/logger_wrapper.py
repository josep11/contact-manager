import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)
log_filename = f"/tmp/contactmanager.log"
logging.basicConfig(filename=log_filename,
                    encoding="utf-8", level=logging.DEBUG)


""" 
from app.app_config import AppConfig
home = os.path.expanduser("~")

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# -------------------------------- #
# -------- BEGIN CONFIG ---------- #
# -------------------------------- #
DEBUG_LOG_FILENAME = "debug.log"
# -------------------------------- #
# --------- END CONFIG ----------- #
# -------------------------------- #

# https://docs.python.org/3/howto/logging.html
# create logs directory if not exists
PROD_LOG_FILENAME = f"{AppConfig.APP_NAME.lower()}.log"
log_file_dir = home + f"/Library/Logs/{AppConfig.APP_NAME}/"
log_file = log_file_dir + PROD_LOG_FILENAME
try:
    os.makedirs(log_file_dir)
except FileExistsError as e:
    pass

if AppConfig.isDev:
    logging.basicConfig(filename=DEBUG_LOG_FILENAME,
                        encoding="utf-8", level=logging.DEBUG)
else:
    logging.basicConfig(
        filename=log_file, encoding="utf-8", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
    )
 """
