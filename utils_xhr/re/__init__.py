import re
# re.match(r'','年后\"\"\"\年后"\"\"哈哈')
s="""
class ReflexUtils:
    
    def __init__(self):


    def hahfa():
        j
        ff
"""
# print(s.replace('\n','@'))
s=re.sub('\n\s+\n','\n',s)

# print(s.replace('\n','@'))
print(s)