"""
*********************************************
@author:张明昱
@class:2019211310
@number:2019211590
@name:parser
@function:按照TSL语法规则构造语法树
@date:2021/12/20
@version:4.0
*********************************************
"""
from class_script import Person,Step,Script,Tree

tree=Tree() #用于储存语法树的全局变量

def ParserFile(FileName,name):
    """从文件中逐行读取"""
    global tree
    with open(FileName,"r+",encoding="utf-8") as f:
        for line in f.readlines():     
            line=line.strip()#去除行空白
            if(line.startswith("#")):continue#处理注释
            ParserLine(line,name)
        f.close()
    return tree

def ParserLine(Line,name):
    """将一行语句分解成tokens数组"""
    tokens=Line.split(" ")
    for token in tokens:
        if(token.startswith("#")):
            tokens.remove(token)
    ProcessTokens(tokens,name)

def ProcessTokens(tokens,name):
    """按照行首token进行分支处理"""
    if(tokens[0]=="step"):ProcessStep(tokens[1])
    elif(tokens[0]=="output"):ProcessOutput(tokens,name)
    elif(tokens[0]=="listen"):pass
    elif(tokens[0]=="branch"):ProcessBranch(tokens[1],tokens[-1])
    elif(tokens[0]=="silence"):ProcessSilence(tokens[1])
    elif(tokens[0]=="default"):ProcessDefault(tokens[1])
    elif(tokens[0]=="exit"):ProcessExit()
    elif(tokens[0].startswith("$ticket")):ProcessTicket(tokens[0])
    elif(tokens[0].startswith("$order")):ProcessOrder(tokens[0])
    else:ProcessError()#都不是，进入错误控制

def ProcessStep(StepId):
    """如果是step行的处理"""
    global tree
    tree.idNow=StepId
    tree.stepTable.update({tree.idNow:Step(tree.idNow)})
    
def ProcessOutput(tokens,name):
    """如果是output行的处理"""
    global tree
    idNow=tree.idNow
    for token in tokens:
        if(token=="+"or token=="output" ):
            continue
        if(token.startswith("$")):
            tree.stepTable[idNow].output.append(name)#存入当前step的output列表中
            continue
        tree.stepTable[idNow].output.append(token)

def ProcessBranch(answer,nextStepId):
    """如果是branch行的处理"""
    global tree
    idNow=tree.idNow
    tree.stepTable[idNow].branchTable.update({answer:nextStepId})

def ProcessSilence(nextStepId):
    """如果是silence行的处理"""
    global tree
    idNow=tree.idNow
    tree.stepTable[idNow].Silence=nextStepId

def ProcessDefault(nextStepId):
    """如果是default行的处理"""
    global tree
    idNow=tree.idNow
    tree.stepTable[idNow].Default=nextStepId

def ProcessExit():
    """如果是exit退出行的处理"""
    global tree
    idNow=tree.idNow
    tree.stepTable[idNow].isEnd=1#当前step设置为终结step

def ProcessTicket(move):
    """如果是购票行的处理"""
    global tree
    idNow=tree.idNow
    if(move=="$ticket++"):tree.stepTable[idNow].isDeal=1
    if(move=="$ticket--"):tree.stepTable[idNow].isDeal=2
    
def ProcessOrder(move):
    """如果是预定行的处理"""
    global tree
    idNow=tree.idNow
    if(move=="$order++"):tree.stepTable[idNow].isDeal=3
    if(move=="$order--"):tree.stepTable[idNow].isDeal=4

def ProcessError():
    """错误处理"""
    print("Error!输入不符合语法规范\n")



    