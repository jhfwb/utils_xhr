import threading
import time
import threading
import time
import ctypes
import inspect
def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    try:
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if res == 0:
            # pass
            raise ValueError("invalid thread id")
        elif res != 1:
            # """if it returns a number greater than one, you're in trouble,
            # and you should call it again with exc=NULL to revert the effect"""
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")
    except Exception as err:
        print(err)
def stop_thread(thread):
    """终止线程"""
    _async_raise(thread.ident, SystemExit)
# class TheadingXHR(threading.Thread):
#     """
#     继承了theading的方法。里面定义了一个方法能关闭掉该线程。
#     """
#     def __init__(self,target=None,kwargs={},args=[]):
#         self.__sign=0
#         self.__target=target
#         self.__kwargs=kwargs
#         self.__args=args
#         super().__init__(target=target,kwargs=kwargs,args=args)
#     def run(self):
#         self.t = threading.Thread(target=self.__target, kwargs=self.__kwargs, args=self.__args)
#         self.t.setDaemon(True)
#         self.t.start()
#
#
#
#     def killThread(self):
#         """
#         关闭掉自己
#         """
#         stop_thread(self.t)
#         # self._async_raise(self.t.ident, SystemExit)

if __name__ == '__main__':
    def haha():
        while True:
            print(1)
    # t主 = TheadingXHR(target=haha)
    t主=threading.Thread(target=haha)
    t主.start()
    time.sleep(1)
    # t主.killThread()
    stop_thread(t主)
    print('结束')
