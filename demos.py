from utils_xhr.io import replaceFileSign
from utils_xhr.reflex.reflexUtils import ReflexUtils
from utils_xhr.reflex import reflexUtils as aaa

# ReflexUtils().getFuncByDecoratorName(aaa,'@threadingRun')[0]()

replaceFileSign(path='test.py',signs=[('@a@','你好')])