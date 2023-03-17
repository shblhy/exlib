import os
import sys
import argparse
import pickle
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


def get_parser():
    parser = argparse.ArgumentParser(description='请输入参数')
    parser.add_argument('-t', '--tag_id', default=datetime.now().strftime('%Y%m%d%H%M%S'), required=False)
    parser.add_argument('-e', '--episode', type=int, default=3, required=False)
    return parser


class StraBase:
    def __init__(self, tag_id, source_dir):
        """

        :param tag_id: 用一个id来区分多次运行的日志等
        :param source_dir: 源内容
        """
        self.tag_id = tag_id
        self.source_dir = source_dir

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
