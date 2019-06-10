import logging
LOG_FORMAT = "%(asctime)s-%(levelname)s-%(message)s"
# 设置logging
logging.basicConfig(level=logging.DEBUG,format=LOG_FORMAT,filename="my log")
logging.debug("this is debig")
logging.info("this is info")
logging.warning("this is warning")
logging.error("this is error")
logging.critical("this is critical")
