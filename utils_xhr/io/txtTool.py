"""
用于处理txt文件
"""

def _checkTxt(path):
    from utils_xhr.io import _checkFile
    _checkFile(path, suffix='txt')
def readDatas(path='',encoding='utf-8'):
    """
    读取txt数据，并返回一个数组。txt文件中的每个数据需要用回车键隔开。
    :param path: 文件路径
    :param encoding: 读取的编码格式
    :return: []
    """
    _checkTxt(path)
    fp = open(file=path, mode='r', encoding=encoding,)
    arr = fp.readlines()
    fp.close()
    arr=list(map(lambda x:x.strip(),arr))
    return arr
