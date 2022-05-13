import yaml
from exlib.config.base import ConfigEngine


class YamlEngine(ConfigEngine):
    from_file = 'yaml_conf_file'
    target = 'yaml_keys'

    def __init__(self, name, from_file='yaml_conf_file', target='yaml_keys'):
        self.name = name
        self.from_file = from_file
        self.target = target

    def init(self, conf):
        self._yml_data_ = {}
        yaml_path = getattr(conf, self.from_file)
        with open(yaml_path) as file:
            self._yml_data_ = yaml.safe_load(file)

    def _get_value(self, name):
        return self._yml_data_.get(name)
