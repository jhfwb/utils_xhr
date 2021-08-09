class BaseException(Exception):
    """这是一个基础错误"""

class IOException(BaseException):
    """io模块的错误"""

class CsvToolException(IOException):
    """csv工具的错误"""

class ExcelToolException(IOException):
    """Excel工具的错误"""