import logging
from sys import exit
import os
import subprocess

logger = logging.getLogger()
logger.setLevel(logging.INFO)

LOGS_DIRECTORY = os.getenv('LOGS_DIRECTORY')
if not LOGS_DIRECTORY:
    homedir=os.path.expanduser('~')
    print('no environment was found with LOGS_DIRECTORY')
    subprocess.call(["touch", os.path.join(homedir, 'Desktop', "contact_manager_error.txt")])
    exit(1)

logging.basicConfig(filename=LOGS_DIRECTORY,
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
