# importing libraries
import logging
import os

logging_str = "[%(asctime)s: %(levelname)s: %(module)s:] %(message)s"
log_dir = "logs"
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(filename=os.path.join(log_dir,"running.log"),level=logging.INFO,
format=logging_str,filemode='a')


def Factorial(n):
    try:
        assert n>=0 and int(n)==n, "The number must be an positive integer only!"
        if n in [0,1]:
            return 1
        else:
            return n * Factorial(n-1)
    except Exception as e:
        return e


logging.info(Factorial(3))
logging.info(Factorial(4))
logging.info(Factorial(5))
logging.info(Factorial(-9))
print("Hello, World!")
