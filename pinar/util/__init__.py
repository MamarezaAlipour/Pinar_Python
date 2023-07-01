"""
init util
"""
import logging
from pint import UnitRegistry

from .config import *
from .constants import *
from .coordinates import *
from .save import *

ureg = UnitRegistry()

class log_level:
    """Context manager that sets all loggers with names starting with
    name_prefix (default is "") to a given specified level.

    Examples
    --------
    Set ALL loggers temporarily to the level 'WARNING'
    >>> with log_level(level='WARNING'):
    >>>     ...

    Set all the pinar loggers temporarily to the level 'ERROR'
    >>> with log_level(level='ERROR', name_prefix='pinar'):
    >>>     ...

    """

    def __init__(self, level, name_prefix=""):
        self.level = level
        self.loggers = {
            name: (logger, logger.level)
            for name, logger in logging.root.manager.loggerDict.items()
            if isinstance(logger, logging.Logger) and name.startswith(name_prefix)
            }
        if name_prefix == "":
            self.loggers[""] = (logging.getLogger(), logging.getLogger().level)

    def __enter__(self):
        for logger, _ in self.loggers.values():
            logger.setLevel(self.level)

    def __exit__(self, exception_type, exception, traceback):
        for logger, previous_level in self.loggers.values():
            logger.setLevel(previous_level)
