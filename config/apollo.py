from .base import Config
from ..libs.apollo_client import ApolloClient
from werkzeug.local import LocalProxy


class ApolloConfig(Config):
    def _get_value(self, name, value=None):
        r = self.client.get_value(name)
        return r if r is not value else value

    def __init__(self, app_id, server, auth):
        self.client = ApolloClient(app_id=app_id,
                                   config_server_url=server,
                                   authorization=auth)
        for key in self.apollo_keys:
            setattr(self, key, LocalProxy(lambda : self._get_value(key)))

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.stopped = True
