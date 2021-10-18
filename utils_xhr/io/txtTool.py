"""
用于处理txt文件
"""

import os
from warnings import warn


def _checkTxt(path):
    from utils_xhr.io import _checkFile
    _checkFile(path, suffix='txt')
def optionDatas(path='',encoding='utf-8',mode='r',datas=[],isCreateNewFile=False):
    """

    """
    try:
        _checkTxt(path)
    except FileNotFoundError:
        pass
    # 判断文件路径是否存在
    if not os.path.exists(path):
        if isCreateNewFile:
            fp=open(file=path,mode='w')
            fp.close()
        else:
            raise FileExistsError('此文件不存在:'+str(path)+'。建议将方法optinopDatas的参数createNewFile的值置为True以创建文件。')
    if type(datas)!=type([]):
        datas=[datas]
    fp = open(file=path, mode=mode, encoding=encoding)
    if mode=='r':
        arr = fp.readlines()
        fp.close()
        arr = list(map(lambda x: x.strip(), arr))
        return arr
    elif mode=='w':
        datas=map(lambda x:str(x)+'\n',datas)
        fp.writelines(datas)
        fp.close()
    elif mode=='a':
        datas = map(lambda x: str(x) + '\n', datas)
        fp.writelines(datas)
        fp.close()
    return None
def readDatas(path='',encoding='utf-8'):
    """
    读取txt数据，并返回一个数组。txt文件中的每个数据需要用回车键隔开。
    :param path: 文件路径
    :param encoding: 读取的编码格式
    :return: []
    """
    import warnings
    warnings.warn("此方法已经过时，建议替换成optionDatas方法", DeprecationWarning)
    _checkTxt(path)
    fp = open(file=path, mode='r', encoding=encoding,)
    arr = fp.readlines()
    fp.close()
    arr=list(map(lambda x:x.strip(),arr))
    return arr
if __name__ == '__main__':
    # optionDatas(path='tttest.txt',encoding='utf-8',mode='a',arr=['你好','我不好'],createNewFile=False)
    a=optionDatas(path='test.txt',mode='r',datas=[55],isCreateNewFile=True)
    print(a)