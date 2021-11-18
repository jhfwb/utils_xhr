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
        self.__target(*self.__args,**self.__kwargs)
    def killThread(self):
        """
        关闭掉自己
        """
        self.__sign = 1




if __name__ == '__main__':
    class a:
        def haha(self):
            while True:
                time.sleep(1)
                print(1)
    t主 = TheadingXHR(target=a().haha)
    t主.start()

    # t主.t.join()
    # print(t主.is_alive())
    # print(2)
