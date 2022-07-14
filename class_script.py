"""
RSL脚本解释器中要用到的类定义
"""

class Person:
    """记录每个用户的姓名，购票数和订购数"""
    name=""
    ticket=0
    order=0

    def __init__(self,name="",ticket=0,order=0):
        self.name=name
        self.ticket=ticket
        self.order=order

class Step:
    """记录每个step中的信息"""
    stepId=""
    output=list()#要说的一系列string数组
    branchTable=dict()#key是听取到的answer，value是stepid
    Silence='silenceProc'
    Default='defaultProc'
    isEnd=0#标识是否为终结步骤
    isDeal=0#标记是否为处理步骤

    def __init__(self,stepId):
        self.stepId=stepId
        self.output=list()
        self.branchTable=dict()
        self.Silence='silenceProc'
        self.Default='defaultProc'
        self.isEnd=0
        self.isDeal=0

class Script:
    """脚本的运行环境"""
    person=Person()
    stepNow=Step("") #当前step
   
    def __init__(self,entry=Step(""),person=Person()):
        self.entry=entry
        self.person=person

class Tree:
    """存储语法树的结构"""
    idNow=''
    stepTable=dict()

    def __init__(self,idNow='',stepTable={}):
        self.idNow=''
        self.stepTable=dict()

    def __eq__(self,other):#重定义判断相等方法便于测试
        return self.stepTable.values() == other.stepTable.values()


