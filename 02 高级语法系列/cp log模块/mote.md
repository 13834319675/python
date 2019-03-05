# log  
https://www.cnblogs.com/yyds/p/6901864.html
- loging
- longing模块提供模块级别的函数记录日志
- 包括四大组件

## 1、日志相关的概念

- 日志
- 日志的级别（level）
    - 不同的用户吧关注不同的程序信息
    - DEBUG
    - INFO
    - NUTICE
    - WARNING
    - ERROR
    - CRITICAL
    - ALERT
    - EMERGENCY
- IO 操作，不需要频繁操作
- log的自作用
    - 调试
    - 了解软件的运行情况
    - 分析定位问题
- 日志信息
    - time
    - 地点
    - level
    - 内容
- 成熟的第三方日志
    - log4f
    - log4php
    - logging
## logging模块
   
- 日志级别
    - 级别可自定义
    - DEBUG
    - INFO
    - WARNING
    - ERROR
    - CRITICAL
- 初始化/写日志实例需要制定级别，只有当级别等于或者高于制定级别时才被记录
- 使用方式
    - 直接使用logging（封装了其他组件）
    - logging四大组件直接定义
    
# 2.1 logging模块级别的日志
- 使用以下几个函数
    - logging.debug(msg,*args,**kwargs) 创建一条严重级别为dubug的日志记录
    - logging.info(msg,*atgs,**kwargs) 创建一天严重级别为info的日志记录
    - logging.warning(msg,*args,**kwargs) 创建一天严重级别为warning的日志记录
    - logging.error(mag,*args,**kwargs) 创建一条严重级别为error的日志记录
    - logging.critical(mag,*args,**kwargs) 创建一条严重级别为critical的日志记录
    - logging.log(msg,*args,**kwargs) 创建一条严重级别为level的日志记录
    - logging.basicconfig(**kwargs) 对root logger进行一次性配置
    
- logging.basicconfig (**kwargs) 对root。logger进行一次性配置

    - 只在第一次调用的时候起作用
    - 不配做logger则使用默认值
        - 输出，sys.stderr
        - 级别：WARNING
        - 格式
        
- level：log_name:content
- 案例01
- format参数        
    - asctime  %（asctime）s 日志事件发生的时间-人类可读的时间，如2019年2月28日13:53:23
    - created  %（created）f 日志事件发生的时间- 时间戳，就是当时调用的time.time的返回值
    - relativecreated %（relativecreated）d 日志事件发生的时间，相对于longing模块加时间的相对毫秒数（目前还不知道干嘛用的）
    = msecs %（msecs）d  日志时间发生的毫秒部分
    - levelname %（levelname）s  法日志记录的文职形式的日志级别（"DEBUG","INFO","WARNING","ERROR","CRITICAL"） 
    - leveno %(leveno)s  该日志记录的数字形式的日志级别（10，20,30）
    - message %（message）s 日志记录的文本内容，通过msg%args计算得到
    - name %（name）s 锁使用的日志器名称，默认是root，因为默认使用的是rootlogger
    - pathname %（pathname）s  调用日志记录函数的源码文件的全部路径
    - filename %（filename）s  pathname的文件名部分，包含文件后缀
    - module %（module）s filename的名称部分，不包含后缀
    - linneno %（lineno）d 调用日志记录函数的源代码所在的行号
    - funcname %（funcname）s 调用日志记录函数的函数名
    - process %（process）d  进程ID
    - processName %（processName）s 进程名称，python3.1新增
    - thread %（thread）d 线程ID
    - threadName %（threadName）s  线程名称
# 2.2 logging模块的处理流程

- 四大组件
    - 日志器（logger）：产生入职的一个借口
    - 处理器（handler）：把产生的日志文件发送到相应的目的地
    - 过滤器（filter）：更精确的控制那些日志输出
    - 各式器（formatter）：对输出信息进行格式化
- logger
    - 产生一个日志
    - 操作
            
    - logger.setlevel() ,设置日志器会处理的消息最低产生的级别
    - logger.addHandler()和logger.removeHandler()  为改logger对象添加和移除一个handler对象
    - logger.addFilter()和logger.removeFilter() 对该logger对象添加和移除一个filter对象
    - logger.debug() 产生一个debug级别的日志，同理 info，error等
    - logger.exception() 创建类似于logger.error的日志信息
    - logger.log(),获取一个明确的日志level 参数类创建一个日志记录

- 如何得到一个日志对象
    - 实例化
    - logging.getlogger()
- Handler
    - handler对象负责发送相关的信息到指定目的地。Python的日志系统有多种Handler可以使用。
    有些Handler可以把信息输出到控制台，有些Logger可以把信息输出到文件，还有些 Handler可以把信息发送到网络上。
    如果觉得不够用，还可以编写自己的Handler。可以通过addHandler()方法添加多个多handler
    - 把log发送到指定位置
    - 方法
        - setlevel # Handler.setLevel(lel):指定被处理的信息级别，低于lel级别的信息将被忽略
        - setFormat # Handler.setFormatter()：给这个handler选择一个格式
        - addFilter，removeFilter # Handler.addFilter(filt)、Handler.removeFilter(filt)：新增或删除一个filter对象
    - 不需要直接使用，Handler是基类
                   
    - logging.StreamHandler 将日志消息发送到输出的Stream，如std.out.std.err或者任何file-like对象
    - logging.FileHandler  将日志晚间消息发送到磁盘文件，默认情况下文件大小会无限增长
        - FileHandler(filename[,mode]) filename是文件名，必须指定一个文件名。
        mode是文件的打开方式。参见Python内置函数open()的用法。默认是’a'，即添加到文件末尾。
    - logging.handlers.RotatingFileHandler  将日志消息发送到磁盘文件，并支持日志文件被大小切割
    - logging.handlers.TimeRoatingfileHandlter 将日志发送到磁盘文件，并支持日志文件按时间切割
        - TimedRotatingFileHandler( filename [,when [,interval [,backupCount]]])
        - 其中filename参数和backupCount参数和RotatingFileHandler具有相同的意义。
        - interval是时间间隔。
        - when参数是一个字符串。表示时间间隔的单位，不区分大小写。它有以下取值：
        - S 秒
        - M 分
        - H 小时
        - D 天
        - W 每星期（interval==0时代表星期一）
        - midnight 每天凌晨
    - logging.handlers.HTTPHandler 将日志文件消息以GET 或者POST的方式发送给一个HTTP服务器
    - logging.handlers.SMTPHandler 将日志文件发送给一个指定的emall地址
    - logging.NullHandler 该Handler实例会忽略error messages，通常被想使用logging的library开发者使用来
    避免'No handlers could be found for logger XXX'信息的出现。

- format类
    - 直接实例化
    - 可以继承format添加特殊内容
    - 三个参数
        - fmt  指定消息格式化字符串，如果不指定改参数则默认使用
               ‘%Y-%m-%d %H-%M-%S’
        - datefmt 指定日期格式化字符串，如果不指定改参数则默认使用
               "%Y-%m-%d %H:%M:%S"
        - style：Python 3.2新增的参数，可取值为 '%', '{'和 '$'，如果不指定该参数则默认使用'%' 
        
    - filter类
        - 可以被Handler和loger使用
        - 控制传递关来信息的具体内容
        - 案例02