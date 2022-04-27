from .base import ConfigEngine, parse, get_property
from redis import Redis

REDIS_KEYS = [
    "host",
    "port",
    "db",
    "password",
    "socket_timeout",
    "socket_connect_timeout",
    "socket_keepalive",
    "socket_keepalive_options",
    "connection_pool",
    "unix_socket_path",
    "encoding",
    "encoding_errors",
    "charset",
    "errors",
    "decode_responses",
    "retry_on_timeout",
    "retry_on_error",
    "ssl",
    "ssl_keyfile",
    "ssl_certfile",
    "ssl_cert_reqs",
    "ssl_ca_certs",
    "ssl_ca_path",
    "ssl_ca_data",
    "ssl_check_hostname",
    "ssl_password",
    "ssl_validate_ocsp",
    "ssl_validate_ocsp_stapled",
    "ssl_ocsp_context",
    "ssl_ocsp_expected_cert",
    "max_connections",
    "single_connection_client",
    "health_check_interval",
    "client_name",
    "username",
    "retry",
    "redis_connect_func"
]


class RedisEngine(ConfigEngine):
    target = 'redis_keys'
        
    def init(self, conf):
        kwargs = {key: getattr(conf, f'redis_{key}') for key in REDIS_KEYS if hasattr(conf, f'redis_{key}')}
        self.client = Redis(**kwargs)

    def _get_value(self, name):
        return self.client.get(name)


class RedisHashEngine(RedisEngine):
    target = 'redis_hash_keys'

    def _get_value(self, name):
        f1, f2 = name.split('--')
        return self.client.hget(f1, f2)
