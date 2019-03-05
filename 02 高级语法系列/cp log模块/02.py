'''
1、需求

现在有以下几个日志记录需求：
    1）需求将所有级别的所有日志文件写入磁盘中
    2）all.log文件中记录所有日记信息，日志格什温，日期时间- 日期级别，日志信息
    3）erro.log文件中记录erro及以上级别的日志信息，日期格式为，日期和时间，日志级别-文件名（行号）
日志信息
    4）要求all.log每天凌晨进行日志切割
2、分析
    1）要记录所有级别的日志，因此日志器的有效level需要设置为最低级别的-DEBUG
    2）日志需要被发送到两个不同的目的地，因此需要设置两个handler，另外，两个目的地都是磁盘文件，因此这两个handler都是与filehandler相关的
    3)all.log要求按时间进行切割，因此他需要logging.handler.TimeROotatingFileHandler
    而error.log没有要求日志切割，因此可以使用FileHandle
    4）两个日志晚间格式不同，因此需要对两个handler分别设置各式器
'''
import logging
import logging.handlers
import datetime

# 定义logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG) #设置logger级别

# 为两个不同的文件设置不同的handlers
rf_handler = logging.handlers.TimedRotatingFileHandler('all.log',when='midnight',interval=1
                                                       ,backupCount=7,atTime=datetime.time(0,0,0,0,))
rf_handler.setLevel(logging.INFO)
# backupCount: 表示日志文件的保留个数；
formatter1 = (logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
formatter2 = (logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

rf_handler.setFormatter(formatter1)
f_handler.setFormatter(formatter2)
logger.addHandler(rf_handler)
logger.addHandler(f_handler)


logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')