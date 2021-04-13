# -*- coding: utf-8 -*-

import json
import pandas as pd
import xlrd
from xlutils.copy import copy

colume_name = ['trigger', 'events','time', 'location', 'rescue_org', 'cause', 'loss']
data_path = 'data.xls' #先读取已经保存的excel文件的路径
data = pd.read_excel('data.xls')
# data.to_excel(data_path, index=None)
row = data.shape[0]#读取excel文件的行数

xls=xlrd.open_workbook(r'data.xls',formatting_info=True)#使用xlrd包读取excel数据
xlsx=copy(xls)#拷贝读取到的excel内容
shtc=xlsx.get_sheet(0)#选取sheet0中的内容
data = []
data.append({'trigger': '火灾', 'events': '燃气事故', 'time': '1月30日5', 'location': ['长春市'], 'rescue_org': ['公用局', '青林路交会处'], 'cause': '居民使用燃气不当造成', 'loss': ['8人死亡', '3人受伤']})

# df = pd.DataFrame() # 最后转换得到的结果
a = []
for i in data:
    if type(i)==dict:
        for k,v in i.items():#将事件抽取结果json格式数据的value值取出
            v= str(v)
            v=v.split()
            vs = ','.join(v)
            a.append(vs) #变量a为合并后的结果
    row += 1 #将数据插入到当前文件的新行
    for item in range(7):
        shtc.write(row,item, a[item])
        xlsx.save(r'data.xls')


# colume_name = ['trigger', 'events','time', 'location', 'rescue_org', 'cause', 'loss']
# data = []
# data.append({'trigger': '爆炸', 'events': '燃气事故', 'time': '10月13日上午11', 'location': ['无锡市'], 'rescue_org': ['新华网'], 'cause': '', 'loss': ['9人死亡', '10人受伤']})
# people=['peopleinfo1',{"name":"zhou",' age':26,' sex':'female'}, 
#         'peQpleinfo2',{'name':'liu','age':17,'sex':'male'}]
# # print(peopLe)
# for p in data:
#     if type(p)==dict:
#         for k,v in p.items():
#             print(v)



# data = [] # 用于存储每一行的Json数据
# event = {'trigger': '爆炸', 'events': '燃气事故', 'time': '10月13日上午11', 'location': ['无锡市'], 'rescue_org': ['新华网'], 'cause': '', 'loss': ['9人死亡', '10人受伤']}
# # with open('./data/temp2.txt','r', encoding = 'UTF-8') as fr:

# data.append(event)

# # data.append({'trigger': '爆炸', 'events': '燃气事故', 'time': '10月13日上午11', 'location': ['无锡市'], 'rescue_org': ['新华网'], 'cause': '', 'loss': ['9人死亡', '10人受伤']})
# print(data)
# df = pd.DataFrame() # 最后转换得到的结果
# # for line in data:
# #     for i in line:
# #         df1 = pd.DataFrame([i])
# #         df = df.append(df1)
# for i in data:
#     df1 = pd.DataFrame([i])
#     df = df.append(df1)
# # 在excel表格的第1列写入, 不写入index
# df.to_excel('data.xlsx', sheet_name='Data', startcol=0, index=False)