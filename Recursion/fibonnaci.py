import logging
import os

logging_str = "[%(asctime)s: %(levelname)s: %(module)s:] %(message)s"
log_dir = "logs"
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(filename=os.path.join(log_dir,"running.log"),level=logging.INFO,
format=logging_str,filemode='a')

def fibonacci(n):
    try:
        assert n>=0 and int(n)==n," number should not be negative number or non integer"
        if n in [0,1]:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    except Exception as e:
        return e

logging.info(fibonacci(7))
logging.info(fibonacci(-1))
logging.info(fibonacci(1.5))