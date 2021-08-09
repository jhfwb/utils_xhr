"""
时间工具包。用于处理时间
"""
import time

__all__=['currentTime']

def currentTime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
