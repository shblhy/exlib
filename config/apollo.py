from .base import ConfigEngine
from ..libs.apollo_client import ApolloClient


class ApolloEngine(ConfigEngine):
    target = 'apollo_keys'
    APOLLO_CLIENT_INIT_KEYS = ['env', 'ip', 'timeout', 'cycle_time', 'cache_file_path']

    def init(self, conf):
        self._conf_ = conf
        params = self.get_params(conf)
        self.client = ApolloClient(app_id=conf.apollo_app_id,
                                   config_server_url=conf.apollo_app_server,
                                   authorization=conf.apollo_app_auth,
                                   **params)
        self.namespace = conf.apollo_namespace or 'application'

    def get_params(self, conf):
        params = {}
        for attr in ApolloEngine.APOLLO_CLIENT_INIT_KEYS:
            attr_name = f'apollo_{attr}'
            if hasattr(conf, attr_name):
                params[attr] = getattr(conf, attr_name)
        return params

    def _get_value(self, name):
        return self.client.get_value(name, namespace=self.namespace)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.stopped = True
