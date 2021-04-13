from py2neo import Graph, Node, Relationship
import pandas as pd
import csv
# 连接neo4j数据库，输入地址、用户名、密码
graph = Graph("http://localhost:7474", username="neo4j", password='123456')
graph.delete_all()

with open('D:/知识图谱代码实现/知识图谱/燃气事故.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
# print(data[1][1])
def deleteDuplicatedElementFromList2(list):
    resultList = []
    for item in list:
        if not item in resultList:
            resultList.append(item)
    return resultList
alist=[]
for i  in  range(1,len(data)):
        alist.append(data[i][3])
# print(alist)
resultList=deleteDuplicatedElementFromList2(alist)
# print(resultList)
for j in resultList:
    node_location = Node('region',name = j)
    graph.create(node_location)
    print(node_location)

for i  in  range(1,len(data)):
    node1 = Node('person',name = data[i][1],id = data[i][0],gender= data[i][2])
    # if data[i][3] in resultList:
    #     node_location = data[i][3]
    #     print(node_location)
    node2 = Node('region',name = data[i][3])
    # print(node2)
    node3 = Node('concerns',name = data[i][4])
    node4 = Node('fans',name = data[i][5])
    node5 = Node('text',name = data[i][6])
    node6 = Node('time',name = data[i][7])
    node7 = Node('tool',name = data[i][8])
    graph.create(node1)
    graph.create(node3)
    graph.create(node4)
    graph.create(node5)
    graph.create(node6)
    graph.create(node7)

    region  = Relationship(node1,'发布地区',node_location)
    concerns = Relationship(node1,'关注数',node3)
    fans    = Relationship(node1,'粉丝数',node4)
    text    = Relationship(node1,'发布内容',node5)
    time    = Relationship(node1,'发布时间',node6)
    tool    = Relationship(node1,'发布工具',node7)
    graph.create(region)
    graph.create(concerns)
    graph.create(fans)
    graph.create(text)
    graph.create(time)
    graph.create(tool)