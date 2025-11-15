import os
import sys
import logging
from datetime import datetime

log_dir = "logs"
logging_str = "[%(asctime)s] %(lineno)d - %(levelname)s - %(message)s"

log_filepath = os.path.join(log_dir, f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    format=logging_str,
    level=logging.INFO,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logging = logging.getLogger("summarizerlogger")
