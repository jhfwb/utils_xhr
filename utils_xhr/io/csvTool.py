"""定义了交互csv的工具
核心方法：
    1. function **optionCsv**：读取，添加，书写csv文件
    2. function **getCsvHeader**：获取csv的数据头
    3. function **popLastData**：弹出csv的最后一个数据
"""
import csv
import os




def getCsvHeader(path='',encoding='utf-8'):
    """获得csv文件的行文件
    :param path: 需要读取的csv文件的路径。
    :param encoding: 以什么编码形式读取文件。
    :return: []
    """
    _isCsvFile(path)
    with open(path, 'r',encoding=encoding) as fp:
        # encoding是读取时候的解码规则
        line=fp.readline()
        arr=line[0:len(line)-1].split(',')
        return arr
def _readCsvFileByAllEncodingToArr(path='',status=['ANSI','gbk','utf-8']):
    """
    读取csv文件，无论这个csv文件是哪种编码。
    将其转化成数组格式
    """
    if len(status)==0:
        raise UnicodeDecodeError('utf-8,gbk,ANSI这三种编码格式都无法解析')
    encoding=status.pop()
    with open(file=path, mode='r', encoding=encoding) as fp:
        try:
            # encoding是读取时候的解码规则
            readers = csv.DictReader(fp)
            return list(readers)
        except UnicodeDecodeError:
            fp.close()
            return _readCsvFileByAllEncodingToArr(path=path,status=status)
def _isCsvFile(path):
    from utils_xhr.io import _checkFile
    _checkFile(path,suffix='csv')
def popLastData(path='',isPop=False,encoding='utf-8'):
    """弹出/获得 一个csv文件的最后一个数据

    :param path: csv的文件路径
    :param isPop: 是否删除文件的最后一个数据，默认不删除。
    :param encoding: 编码
    usage:
        >>> from utils_xhr.io import csvTool
        >>> csvTool.popLastData(path='../test.csv',isPop=True)
    当isPop为True的时候，弹出文件末尾的数据
    当isPop为False的时候，获得文件末尾的数据
    """
    _isCsvFile(path)
    arr=optionCsv(path=path,mode='r',encoding=encoding)
    if len(arr)==0:
        raise ZeroDivisionError('无法弹出数据，因为该文件:'+path+',数据为空')
    if isPop==False:
        return arr[len(arr) - 1]
    else:
        data=arr[len(arr) - 1]
        del arr[len(arr) - 1]
        optionCsv(path=path,datas=arr,mode='w',encoding=encoding)
        return data

def optionCsv(path='',datas=[],mode="a",encoding='utf-8',isCreateFile=False):
    """操作csv文件

    usage:
        >>> from utils_xhr.io import csvTool
        >>> # 读取文件
        >>>  csvTool.optionCsv(path='../test.csv',mode='r')
        >>> #写入文件
        >>>  csvTool.optionCsv(path='../test.csv',mode='w',datas =[{'name':'张三','age':'12'}],encoding='utf-8')
        >>> #为文件添加数据
        >>>  csvTool.optionCsv(path='../test.csv',mode='a',datas=[{'name':'李四','age':'121'}],encoding='utf-8')

    mode模式介绍:
     * r 读取模式,根据csv文件路径读取datas数据。此时必要参数为path，mode
     * a 添加模式,根据csv文件路径添加datas数据。此时必要参数为path，mode，datas
     * w 写入模式,根据csv文件路径覆写datas数据。此时必要参数为path，mode，datas

    :param path: 操作的csv文件的路径
    :param datas: 数据集。格式必须如此[{name:'张三',age:'19'},{name:'李四',age:'12'}]
    :param mode: 模式。共有r,a,w三种模式
    :param encoding: 编码。1.utf-8  2.ANSI  3.gbk
    :param isCreateFile: 当该文件不存在的时候，是否创建该文件。默认不创建。
    :return: None
    """
    if isCreateFile:
        if not path.endswith('csv'):
            raise FileExistsError(path+'文件后缀名错误！不为.csv')
    else:
        _isCsvFile(path=path)
    if not os.path.exists(path):
        if isCreateFile:
            f = open(path, "a")
            f.close()
        else:
            raise FileNotFoundError("找不到该文件:"+path)
    if mode=='r':
        return _readCsvFileByAllEncodingToArr(path=path,status=['ANSI','gbk','utf-8'])
    if mode=='w':
        if len(datas)==0:
            with open(path, 'w', encoding=encoding, newline="") as fp:
                # encoding是读取时候的解码规则
                fp.write('')
                fp.close()
                return
        headers = list(datas[0].keys())
        with open(path, 'w', encoding=encoding, newline="") as fp:
            # encoding是读取时候的解码规则
            writer = csv.DictWriter(fp, headers)
            writer.writeheader()
            writer.writerows(datas)
    if mode=='a':#弹性添加
        #判断文件存不存在
        if os.path.exists(path):
            #判断是否有header
            oldArr=[]
            with open(path, 'r', encoding=encoding) as fp:
                # encoding是读取时候的解码规则
                readers = csv.DictReader(fp)
                oldArr=list(readers)
            fp.close()
            newDatas=oldArr+datas
            optionCsv(path=path, mode='w', encoding=encoding, datas=newDatas)
        else:
            optionCsv(path=path,mode='w',encoding=encoding,datas=datas)
        pass
    pass
def changeExeclToCsvFile(path="",encoding='utf-8'):
    """
    #将csv文件转成excel文件。目前只能转换第一个表格
    :param path:需要转换的文件的路径
    :param encoding:读取的excel文件的编码，写入编码默认和读取编码一直
    :return: None
    """
    from utils_xhr.io.excelTool import optionExecl
    datas=optionExecl(path=path, mode='r')
    optionCsv(path=path.replace('.xlsx','.csv'), encoding=encoding, mode='w',datas=datas,isCreateFile=True)
def changeCsvToExcelFile(path="",encoding='utf-8'):
    """
    #将csv文件转成excel文件
    :param path:
    :param encoding:
    :return:
    """
    from utils_xhr.io.excelTool import optionExecl
    datas = optionCsv(path=path, mode='r',encoding=encoding)
    optionExecl(path=path.replace('.csv','.xlsx'),mode='w',datas=datas,isCreateFile=True)

def readCsvData_arrDict(path,encoding='utf-8'):
    """
    根据path路径,读取csv文件。并以list的数组形式返回
    数组中的每一项都是字典的形式（dict）
    :param str path: csv文件的读取路径
    :param str encoding:以什么样的编码读取数据
    :return:list数组，数组中每一项为字典
    """
    with open(path, 'r', encoding=encoding) as fp:
        # encoding是读取时候的解码规则
        readers = csv.DictReader(fp)
        return list(readers)
def readCsvData_arrArr(path,encoding='utf-8'):
    """
    根据path读取csv文件。并以list的数组形式返回。
    数组中的每一项都是数组的形式

    :param path:csv的路径
    :return:list数组，数组中每一项为数组
    """
    with open(path, 'r', encoding=encoding) as fp:
        # encoding是读取时候的解码规则
        reader = csv.reader(fp)
        return list(reader)
def writeCsvData_arrDict(path,arr,encoding='utf-8'):
    """
    以数组的形式写入。数组内部必须是字典形式
    :param path:文件的写入路径
    :param arr: 写入的内容
    :return: 返回该数组
    """
    headers =list(arr[0].keys())
    with open(path, 'w', encoding=encoding,newline="") as fp:
        # encoding是读取时候的解码规则
        writer = csv.DictWriter(fp, headers)
        writer.writeheader()
        writer.writerows(arr)
def writeData_arrArr(path,header=[], datas='',encoding='utf-8'):
    """
    :param path:  str | 保存的文件路径
    :param header: [] | 表格的表头
    :param datas:  [[],[],...] | 表格的数据
    :param encoding: str | 编码形式
    :return: None
    """
    with open(path, 'w', encoding=encoding, newline="") as fp:
        # encoding是读取时候的解码规则
        writer = csv.writer(fp)
        writer.writerow(header)
        writer.writerows(datas)