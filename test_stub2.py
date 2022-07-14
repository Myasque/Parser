""""
parser模块的自动测试脚本2
"""

from unittest import mock
from parser import ParserFile
from class_script import Person,Step,Tree

equal=1
tree=ParserFile("北京人艺.txt","Foo先生")#经由parser获得的语法树
tree_stan=Tree()#标准语法树

#开始储存正确语法树
stepnames={"welcome","purchaseProc","orderProc","complainProc","silenceProc","defaultProc","goodbye"}

tree_stan.idNow='goodbye'

for stepname in stepnames:
    tree_stan.stepTable[stepname]=Step(stepname)
    tree_stan.stepTable[stepname].stepId=stepname

tree_stan.stepTable["welcome"].output=['Foo先生','欢迎您致电北京人民艺术剧院，话剧《原野》和朗读会《李白》售票中，所有剧目一经售出不退不换。请问有什么可以帮您？请说：购买话剧、预定朗读会、投诉。']
tree_stan.stepTable["welcome"].branchTable={'购买话剧':'purchaseProc','预定朗读会':'orderProc','投诉':'complainProc'}
tree_stan.stepTable["welcome"].Silence='silenceProc'
tree_stan.stepTable["welcome"].Default='defaultProc'
tree_stan.stepTable["welcome"].isEnd=0
tree_stan.stepTable["welcome"].isDeal=0

tree_stan.stepTable["purchaseProc"].output=['您已成功购买此剧目，请在指定日期前来取票观看。']
tree_stan.stepTable["purchaseProc"].branchTable={}
tree_stan.stepTable["purchaseProc"].Silence='silenceProc'
tree_stan.stepTable["purchaseProc"].Default='defaultProc'
tree_stan.stepTable["purchaseProc"].isEnd=1
tree_stan.stepTable["purchaseProc"].isDeal=1

tree_stan.stepTable["orderProc"].output=['您已成功订购此剧目，请在指定日期前来参加。']
tree_stan.stepTable["orderProc"].branchTable={}
tree_stan.stepTable["orderProc"].Silence='silenceProc'
tree_stan.stepTable["orderProc"].Default='defaultProc'
tree_stan.stepTable["orderProc"].isEnd=1
tree_stan.stepTable["orderProc"].isDeal=3

tree_stan.stepTable["complainProc"].output=['感谢您的建议，您的反馈我们已经收到，请问您还有什么要补充的吗？']
tree_stan.stepTable["complainProc"].branchTable={}
tree_stan.stepTable["complainProc"].Silence='silenceProc'
tree_stan.stepTable["complainProc"].Default='goodbye'
tree_stan.stepTable["complainProc"].isEnd=0
tree_stan.stepTable["complainProc"].isDeal=0

tree_stan.stepTable["silenceProc"].output=['对不起我没有听到您的声音，可以请您重复一遍吗？']
tree_stan.stepTable["silenceProc"].branchTable={'购买话剧':'purchaseProc','预定朗读会':'orderProc','投诉':'complainProc'}
tree_stan.stepTable["silenceProc"].Silence='silenceProc'
tree_stan.stepTable["silenceProc"].Default='defaultProc'
tree_stan.stepTable["silenceProc"].isEnd=0
tree_stan.stepTable["silenceProc"].isDeal=0

tree_stan.stepTable["defaultProc"].output=['对不起我没有理解，您能换一种方式表达吗？请说：购买话剧、预定朗读会、投诉。']
tree_stan.stepTable["defaultProc"].branchTable={'购买话剧':'purchaseProc','预定朗读会':'orderProc','投诉':'complainProc'}
tree_stan.stepTable["defaultProc"].Silence='silenceProc'
tree_stan.stepTable["defaultProc"].Default='defaultProc'
tree_stan.stepTable["defaultProc"].isEnd=0
tree_stan.stepTable["defaultProc"].isDeal=0

tree_stan.stepTable["goodbye"].output=['感谢您的来电，再见！']
tree_stan.stepTable["goodbye"].branchTable={}
tree_stan.stepTable["goodbye"].Silence='silenceProc'
tree_stan.stepTable["goodbye"].Default='defaultProc'
tree_stan.stepTable["goodbye"].isEnd=1
tree_stan.stepTable["goodbye"].isDeal=0

print(tree.idNow)
print(tree_stan.idNow)

#将得到的语法树与标准正确语法树进行对比
for stepname in stepnames:
    #print(tree.stepTable[stepname].__dict__)
    #print(tree_stan.stepTable[stepname].__dict__)
    #print("\n")
    if(tree.idNow!=tree_stan.idNow):equal=0
    else:
        if(tree.stepTable[stepname].__dict__!=tree_stan.stepTable[stepname].__dict__):equal=0
    
if(equal):print('Equal!')
else:print('Not Equal!')