from .base import ConfigEngine, parse
from ..libs.apollo_client import ApolloClient


class ApolloEngine(ConfigEngine):
    target = 'apollo_keys'

    def init(self, conf):
        self._conf_ = conf
        self.client = ApolloClient(app_id=conf.apollo_app_id,
                                   config_server_url=conf.apollo_app_server,
                                   authorization=conf.apollo_app_auth)
        self.namespace = conf.apollo_namespace or 'application'

    def _get_value(self, name):
        return self.client.get_value(name, namespace=self.namespace)
