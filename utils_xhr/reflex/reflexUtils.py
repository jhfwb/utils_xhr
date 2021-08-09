import inspect
import re
import threading
import sys
from annotate_xhr import threadingRun
class  ReflexUtils:
    "最好不要使用单例模式，否则会对服务器造成负担"
    def __init__(self):
        pass
    def excuteAllDecorator(self, obj={}, decoratorName="", args=[]):
        funcs = self.getFuncByDecoratorName(className=obj.__class__, decoratorName=decoratorName)
        results=None
        for func in funcs:
            results = func(obj, *args)
        return results
    def excuteDecorator(self,obj={},decoratorName="",args=[]):
        func=self.getFuncByDecoratorName(className=obj.__class__,decoratorName=decoratorName)[0]
        try:
            result=func(obj,*args)
        except TypeError:
            raise SyntaxError('语法错误:该类:' + str(obj.__class__) + ':的方法中缺少' + decoratorName + '注解,无法指'
             '定执行' + decoratorName + '下的方法。建议在该类中创建一个方法，该方法需要被装饰器' + decoratorName + '注解')
        return result
    def getSource(self,any):
        """获得对象的源数据
        :param object any: 此处存放module, class, method, function, traceback, frame, or code object.
        """
        return inspect.getsource(any)
    def getSourceRemoveNotes(self,any):
        """
        获得文件源数据。该源数据会剔除掉所有注释
        :param object any: 此处存放module, class, method, function, traceback, frame, or code object.
        """
        s=self.getSource(any)
        s=self._removeNotes(s)
        return s
    def  _removeNotes(self,s):
        """
        (此方法有bug，难以修补。当比如字段名下方的注释无法删除。当注释与等号中的单词一样的时候会被误删除。)
        去除掉字符串中的所有注释。包括头部注释。类注释。方法注释
        e.g:
            s='
            @threadingRun # 我是注解
            def haha(self,s,dd):
                print('你好'+s)
                 # 我是注解
            '
            去除后:
            s='
            @threadingRun
            def haha(self,s,dd):
                print('你好'+s)
            '
        :param s: 字符串
        :return:
        """
        #去除为三个"的注释
        classNotes=re.findall(r'class\s+\w+:\n\s+(\"\"\"[\s\S]*?\"\"\")',s)#class下面的注释
        functionNotes=re.findall(r'def\s+\w+\(.*\):\n\s+(\"\"\"[\s\S]*?\"\"\")',s)#def下面的注释

        for classNote in classNotes:
            s=s.replace(classNote,'')
        for functionNote in functionNotes:
            s = s.replace(functionNote, '')
        # 去除为两个"的注释
        classNotes2 = re.findall(r'class\s+\w+:\n\s+(\"[\s\S]*?\")', s)  # class下面的注释
        functionNotes2 = re.findall(r'def\s+\w+\(.*\):\n\s+(\"[\s\S]*?\")', s)  # def下面的注释
        for classNote in classNotes2:
            s = s.replace(classNote, '')
        for functionNote in functionNotes2:
            s = s.replace(functionNote, '')

        # s=re.sub(r'class\s+\w+:\n+\s+(\"\"\"[\s\S]*?\"\"\")','',s)#替换掉class下面的注释
        # s=re.sub(r'class\s+\w+:\n\s+(\"\"\"[\s\S]*?\"\"\")','',s)#替换掉def下面的注释
        s=re.sub(r'#.*','',s) #去除掉#后面的注释
        s=s.strip()
        s = re.sub(r'^\"\"\"[\s\S]*?\"\"\"', '', s)  # 去除掉三个"头部注释
        s = re.sub(r'^\"[\s\S]*?\"', '', s)  # 去除掉两个"的头部注释
        s=re.sub('\n+(\s+)?\n+','\n',s) #删掉不必要的回车键
        return s

    # def excuate
    def getFuncByDecoratorName(self,className,decoratorName=""):
        """
        module, class, method, function, traceback, frame, or code object.
        根据装饰器名称，获得被该装饰器修饰的方法。
        注意！由于该方法内部使用到inspect.getsource()。为了避免装饰器修改了类。因此需要在方法中添加
        """
        try:
            if hasattr(self,'_'+str(className)+'_src'):
                pass
            else:
                # 将注释去除掉
                s=self.getSourceRemoveNotes(className)
                setattr(self, '_'+str(className) + '_src',s)
            s=getattr(self,'_'+str(className)+'_src')
        except TypeError:
            raise TypeError('类型错误:'+str(className)+"必须是类对象")
        arr=[]
        _index=0
        while(_index!=-1):
            _index=s.find(decoratorName,_index+1)
            if _index==-1:
                break
            defIndex_start=s.find('def',_index)+3
            defIndex_end=s.find('(',defIndex_start)
            line=s[defIndex_start:defIndex_end].strip()
            arr.append(getattr(className, line))
        return arr
class A:
    def haha(self,s,dd):
        print('你好'+s)

    def haha2(self):
        print('你好')

if __name__ == '__main__':
    pass
    ReflexUtils()
    # print(ReflexUtils().getFuncByDecoratorName(reflexUtils,'@threadingRun'))
    # print(ReflexUtils().getFuncByDecoratorName(A(),'@threadingRun','我不好','woow'))