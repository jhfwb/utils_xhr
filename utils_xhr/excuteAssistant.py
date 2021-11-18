import threading
import time
import os
class ExcuteAssistant:
    def __init__(self):
        self.state=0
    def cycleExcute(self,func=None,path=None):
        self.state = 1
        if func==None and path !=None:
            func=lambda :os.system('python '+path)
        while True:
            if self.state == 0:
                break
            t = threading.Thread(target=func)
            t.start()
            while True:
                time.sleep(1)
                if self.state==0:
                    break
                if not t.is_alive():
                    break
    def close(self):
        self.state==0

