"""定义了交互文件的io工具
1.csv交互工具  module csvTool
2.txt交互工具  module txtTool
"""
import os
from utils_xhr.io import csvTool
from utils_xhr.io import txtTool
from utils_xhr.io.fileTool import replaceFileSign
__all__=['csvTool','txtTool','replaceFileSign']

def _checkFile(path,suffix=''):
    """
    检查该路径是否存在，同时检查路径后缀是否等于suffix

    :param path: 文件的路径
    :suffix: 文件的后缀，默认为空。当path路径后缀不为suffix的后缀的时候，会报错
    """
    if path==None:
        raise FileNotFoundError('path路径为空,请设置查找路径!!!')
    path = str(path)
    if path == "":
        raise FileNotFoundError('path路径为空,请设置查找路径!!!')
    if not os.path.exists(path):
        raise FileNotFoundError('文件:'+path+'。不存在该文件,请检查路径正确。')
    if suffix!='' and not path.endswith(suffix):
        raise TypeError('数据类型错误,要求类型为:'+suffix+'。但是文件:'+path+"不是该类型")