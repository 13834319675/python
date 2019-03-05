import logging

LOG_FORMAT = "%(asctime)s====%(levelname)s----%(message)s"
logging.basicConfig(filename='logpy.log',level=logging.DEBUG,format=LOG_FORMAT)

logging.debug('This is a debug log!')
logging.info('This is a info log!')
logging.warning('This is a waining log!')
logging.error('This is a erroe log!')
logging.critical('This is a critical!')

#另外一种写法
logging.log(logging.DEBUG, "This is a debug log.")
logging.log(logging.INFO, "This is a info log.")
logging.log(logging.WARNING, "This is a warning log.")
logging.log(logging.ERROR, "This is a error log.")
logging.log(logging.CRITICAL, "This is a critical log.")

