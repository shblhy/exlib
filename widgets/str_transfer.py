import re


def transfer_underline(name):
    """驼峰转下划线"""
    pattern = re.compile(r'([A-Z]{1})')
    res = re.sub(pattern, '_' + r'\1', name).lower()
    while res.startswith('_'):
        res = res[1:]
    while res.endswith('_'):
        res = res[-1:]
    return res


def transfer_hump(name, ignore_first=True):
    """下划线转驼峰"""
    res = []
    for index, n in enumerate(name.split('_')):
        if ignore_first and index == 0:
            res.append(n)
        else:
            res.append(f'{n[0].upper()}{n[1:]:}')
    return ''.join(res)