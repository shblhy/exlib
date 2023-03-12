import sys
import argparse

"""
{
    'key1': '_must_',
    'key2': '<default_value>'
}
[(k, dict),
(k, dict),
]
"""
#  python xxx.py --episode=11


def expand(user_params):
    params = []
    for k, v in user_params.items():
        _values = {'default': v}
        item = [f'--{k}', _values]
        params.append(item)
    return params


def get_parser(params):
    sys.argv.pop()
    parser = argparse.ArgumentParser()
    for k, v in params:
        parser.add_argument(k, **v)
    return parser


class StraBase:
    def reset(self):
        raise NotImplemented

    def reset(self):
        raise NotImplemented
