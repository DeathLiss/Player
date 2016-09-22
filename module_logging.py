import logging
import logging.handlers

#
# 
#

version = '0.01'


# -----------------------------------------------------------------------------
def logRotateTime(logFileName='module_logging.log', logWhen='h', logBkpCount=30, logInterval=14,
                  fileString='%(asctime)s (Стр:%(lineno)d) %(message)s', fileLogLevel=logging.DEBUG,
                  loggerName='filePythonLogger'):
    """Настройка логирования (с ротацией по времени)"""

    # Создаём и настраиваем "корневой" объект
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    # Настраиваем формат сообщения
    fileFormatter = logging.Formatter(fileString)
    streamFormatter = logging.Formatter('%(message)s')

    # Настраиваем вывод в консоль
    streamLogger = logging.StreamHandler()
    streamLogger.setLevel(logging.INFO)
    streamLogger.setFormatter(streamFormatter)

    # Выбираем тип ротации для log-файлов
    if logWhen == 'midnight':
        fileLogger = logging.handlers.TimedRotatingFileHandler(filename=logFileName,
                                                               encoding='utf8',
                                                               when=logWhen,
                                                               backupCount=logBkpCount)
    else:
        fileLogger = logging.handlers.TimedRotatingFileHandler(filename=logFileName,
                                                               encoding='utf8',
                                                               when=logWhen,
                                                               interval=logInterval,
                                                               backupCount=logBkpCount)
    # Настраиваем вывод в log-файл
    fileLogger.setLevel(fileLogLevel)
    fileLogger.setFormatter(fileFormatter)

    # Активируем обработку настроенных выше вариантов логирования
    logger.addHandler(fileLogger)
    logger.addHandler(streamLogger)

    return logger


# -----------------------------------------------------------------------------
def logSyslog(syslogString='python.%(module)s[%(process)s]: %(message)s (Строка:%(lineno)d)',
              sysLogLevel=logging.WARNING, loggerName='syslogPythonLogger'):
    """Настройка логирования (запись в syslog)"""

    # Создаём и настраиваем "корневой" объект
    logger = logging.getLogger(loggerName)  # %(name)s
    logger.setLevel(logging.DEBUG)

    # Настраиваем формат сообщения
    streamFormatter = logging.Formatter('%(message)s')
    syslogFormatter = logging.Formatter(syslogString)

    # Настраиваем вывод в консоль
    streamLogger = logging.StreamHandler()
    streamLogger.setLevel(logging.INFO)
    streamLogger.setFormatter(streamFormatter)

    # Настраиваем вывод в syslog
    sysLogger = logging.handlers.SysLogHandler(address='/dev/log', facility='local0')
    sysLogger.setLevel(sysLogLevel)
    sysLogger.setFormatter(syslogFormatter)

    # Активируем обработку настроенных выше вариантов логирования
    logger.addHandler(sysLogger)
    logger.addHandler(streamLogger)

    return logger

# -----------------------------------------------------------------------------
