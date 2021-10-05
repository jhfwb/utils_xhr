import threading
import time
class TheadingXHR(threading.Thread):
    """
    继承了theading的方法。里面定义了一个方法能关闭掉该线程。
    """
    def __init__(self,target=None,kwargs={},args=[]):
        self.__sign=0
        self.__target=target
        self.__kwargs=kwargs
        self.__args=args
        super().__init__(target=target,kwargs=kwargs,args=args)
    def run(self):
        t = threading.Thread(target=self.__target, kwargs=self.__kwargs, args=self.__args)
        t.setDaemon(True)
        t.start()
        while self.__sign==0:
            pass
    def killThread(self):
        """
        关闭掉自己
        """
        self.__sign=1

if __name__ == '__main__':
    def haha():
        while True:
            print(1)
    t主 = TheadingXHR(target=haha)
    t主.start()
    time.sleep(5)
    t主.killThread()