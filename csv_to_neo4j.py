from py2neo import Graph, Node, Relationship
import pandas as pd
import csv
# 连接neo4j数据库，输入地址、用户名、密码
graph = Graph("http://localhost:7474", username="neo4j", password='123456')
graph.delete_all()

with open('D:/知识图谱代码实现/FireEventExtraction-master/data.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
print(data[1])

loc=[]
cau=[]
# acc_name = ['事故名称']
# node8 = Node('acc_name', name=acc_name)
# graph.create(node8)

# acc_loc = ['事故地点']
# node9 = Node('acc_location', name=acc_loc)
# graph.create(node9)

# acc_rescureorg = ['救援组织']
# node10 = Node('acc_rescureorg', name=acc_rescureorg)
# graph.create(node10)

# acc_cause = ['事故原因']
# node11 = Node('acc_cause', name=acc_cause)
# graph.create(node11)

# acc_loss = ['事故损失']
# node12 = Node('acc_loss', name=acc_loss)
# graph.create(node12)

# location  = Relationship(node9,'发生',node8)
# rescueorg  = Relationship(node10,'救援',node8)
# cause    = Relationship(node11,'导致',node8)
# loss    = Relationship(node8,'造成',node12)
# graph.create(location)
# graph.create(rescueorg)
# graph.create(cause)
# graph.create(loss)

locs=[]
caus=[]
acc_location =[]
for i in range(1,len(data)):
    loc.append(data[i][4])
    cau.append(data[i][6])

loc = list(set(loc))
cau = list(set(cau))

for i in range(0,len(loc)):
    node4 = Node('location', name=loc[i])
    locs.append(node4)
    graph.create(node4)
for i in range(0,len(cau)):
    node6 = Node('cause', name=cau[i])
    caus.append(node6)
    graph.create(node6)

for i  in  range(1,len(data)):
    node1 = Node('accident',name = data[i][0],time = data[i][3],events= data[i][2])
    node4 = data[i][4]
    node5 = Node('rescueorg',name = data[i][5])
    node6 = data[i][6]
    node7 = Node('loss',name = data[i][7])
    
    graph.create(node1)
    # graph.create(node4)
    graph.create(node5)
    # graph.create(node6)
    graph.create(node7)
    res_loc = loc.index(node4)
    res_cau = cau.index(node6)

    # location  = Relationship(node1,'事故地点',locs[res_loc])
    # rescueorg  = Relationship(node1,'救援组织',node5)
    # cause    = Relationship(node1,'事故原因',caus[res_cau])
    # loss    = Relationship(node1,'事故损失',node7)
    # acc_location = Relationship(locs[res_loc],'地点',node9)
    location  = Relationship(locs[res_loc],'发生',node1)
    rescueorg  = Relationship(node5,'救援',node1)
    cause    = Relationship(caus[res_cau],'导致',node1)
    loss    = Relationship(node1,'造成',node7)

    # acc_name = Relationship(node1,'type',node8)
    # acc_location = Relationship(locs[res_loc],'type',node9)
    # acc_rescureorg = Relationship(node5,'type',node10)
    # acc_cause = Relationship(caus[res_cau],'type',node11)
    # acc_loss = Relationship(node7,'type',node12)

    graph.create(location)
    graph.create(rescueorg)
    graph.create(cause)
    graph.create(loss)
    # graph.create(acc_name)
    # graph.create(acc_location)
    # graph.create(acc_rescureorg)
    # graph.create(acc_cause)
    # graph.create(acc_loss)