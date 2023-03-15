import os
import sys
import argparse
import pickle
from config import conf
from datetime import datetime

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
    source_dir = conf.source_dir

    def reset(self):
        raise NotImplemented

    def run(self):
        raise NotImplemented

    def load_pkl(self, file_name):
        file_path = os.path.join(self.source_dir, file_name)
        with open(file_path, 'rb') as f:
            obj = pickle.load(f)
            f.close()
        return obj

    def save(self, content, file_name, cover=False):
        """
            保存文件 如果存在同名文件，默认不覆盖，而是在文件名中加入时间(精确到秒)，继续保存
        :param content:
        :param file_name:
        :param cover:
        :return:
        """
        file_path = os.path.join(self.source_dir, file_name)
        if not cover:
            if os.path.exists(file_path):
                new_file_name = _change_file_name(file_name)
                file_path = os.path.join(self.source_dir, new_file_name)
        with open(file_path, 'rb') as f:
            f.write(content)
            f.close()
        return file_path


def _change_file_name(file_name):
    t = datetime.now().strftime('%Y%m%d%H%M%S')
    if '.' in file_name:
        names = file_name.split('.')
        return '.'.join(names[:-1]) + t + '.' + '.'.join(names[-1:])
    else:
        return file_name + t
