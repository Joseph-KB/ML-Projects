import logging
import os
from datetime import datetime


#log file creation -- Folder with .log extension is created
LOG_FILE=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

# path for logfile -- "logs" is the folder name and path for loggings
#logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
logs_path=os.path.join(os.getcwd(),"logs")
# make directory even if file exists
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)