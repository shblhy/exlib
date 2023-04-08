
def find_str_index(substr, str, time):
    # 找字符串substr在str中第time次出现的位置
    times = str.count(substr)
    if (times == 0) or (times < time):
        pass
    else:
        i = 0
        index = -1
        while i < time:
            index = str.find(substr, index + 1)
            i += 1
        return index
