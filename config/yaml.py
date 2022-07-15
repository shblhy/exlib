import yaml
import os
from exlib.config.base import ConfigEngine


class YamlEngine(ConfigEngine):
    from_file = 'yaml_conf_file'
    target = 'yaml_keys'

    def __init__(self, name, from_file='yaml_conf_file', target='yaml_keys'):
        self.name = name
        self.from_file = from_file
        self.target = target

    def init(self, conf):
        self.yaml_path = getattr(conf, self.from_file)
        self._last_yml_time_ = None

    @property
    def _yml_data(self):
        last_yml_time = os.path.getmtime(self.yaml_path)
        if not hasattr(self, '_yml_data_') or last_yml_time != self._last_yml_time_:
            self._yml_data_ = {}
            with open(self.yaml_path) as file:
                self._yml_data_ = yaml.safe_load(file)
            self._last_yml_time_ = os.path.getmtime(self.yaml_path)
        return self._yml_data_

    def _get_value(self, name):
        return self._yml_data.get(name)
