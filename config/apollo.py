import json
import types
from .base import Config
from ..libs.apollo_client import ApolloClient


def get_value(name, format='str', value=None):
    """
        返回yige property,动态从apollo获取值
    :param name:
    :param format:
    :param value: 默认值
    :return:
    """
    def get(self):
        r = self.client.get_value(name, namespace=self.namespace)
        parsers = {
            'json': lambda x: json.loads(x) if x else None,
            'int': lambda x: int(x) if x else None,
            'float': lambda x: int(x) if x else None
        }
        if format in parsers:
            return parsers[format](r)
        return r if r is not None else value
    return property(get)


class ApolloConfig(Config):
    def _get_value(self, name, format='str', value=None):
        r = self.client.get_value(name, namespace=self.namespace)
        parsers = {
            'json': lambda x: json.loads(x) if x else None,
            'int': lambda x: int(x) if x else None,
            'float': lambda x: int(x) if x else None
        }
        if format in parsers:
            return parsers[format](r)
        return r if r is not value else value

    def __init__(self, app_id, server, auth):
        self.namespace = 'quant.dev'
        self.client = ApolloClient(app_id=app_id,
                                   config_server_url=server,
                                   authorization=auth)
        self.set_dynamic_property()

    def set_dynamic_property(self):
        """
            动态绑定property，以确保属性是从配置中心获取最新而非缓存。
        :return:
        """
        for key in self.apollo_keys:
            if '__' in key:
                key, format = key.split('__')
            else:
                format = 'str'
            setattr(ApolloConfig, key, get_value(key, format))

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.stopped = True
