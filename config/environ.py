import os
from .base import ConfigEngine, get_property, parse


class EnvironEngine(ConfigEngine):
    target = 'environ_keys'

    def _get_value(self, name):
        return os.environ.get(name)
