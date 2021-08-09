#文件赋值
import os
def replaceFileSign(path,signs=[('@value@','value')],encoding='utf-8'):
    """
    替换文件中的sign。
    警告: 此举会把文件中字符清除掉。
    :param path: 替换的文件路径
    :param signs: 替换标签。将文件中的标签替换成新的数据、如:sign=[('@value@','value')]。将文件中的@value@替换成value
    :param encoding: 编码规则
    """
    fp = open(file=path, mode='r', encoding=encoding)
    lines = fp.readlines()
    for i in range(len(lines)):
        for sign in signs:
            if sign[0] in lines[i]:
                lines[i] = lines[i].replace(sign[0],sign[1])
    fpw = open(file=path, mode='w', encoding=encoding)
    fpw.writelines(lines)
    fpw.close()
    fp.close()
    return

