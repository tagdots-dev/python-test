"""
log level: NOTSET(0) DEBUG (10), INFO (20), WARNING (30), ERROR (40), CRITICAL (50)
loggers  : message with a severity level lower than the logger's level will be discarded before being passed to any handlers
handlers : console (StreamHandler), file (FileHandler)
file     : this is used to estimate approximate log size
"""

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        # '': {  # root logger - if uncomment, bring out underlyging third party calls
        #     'handlers': ['console', 'file'],
        #     'level': 'NOTSET',
        # },
        'default': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'uvicorn.error': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'uvicorn.access': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'json',
            'level': 'DEBUG',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 500000,
            'backupCount': 2,
            'filename': 'app.log',
            'formatter': 'json',
            'level': 'DEBUG',
        },
    },
    'formatters': {
        'plain': {
            'format': '%(asctime)s.%(msecs)03d - %(levelname)s - %(funcName)s - %(filename)s:%(lineno)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'json': {
            'format': '{"_t": "%(asctime)s.%(msecs)03d", "_l": "%(levelname)s", "_f": "%(funcName)s", "_m": "%(filename)s:%(lineno)s", "_d": "%(message)s"}',  # noqa: E501
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
}
