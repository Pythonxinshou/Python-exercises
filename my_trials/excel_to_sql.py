import xlrd


# 设置路径
path = 'C:/Users/zsj/PycharmProjects/Python-exercises/my_trials/sql.xlsx'
# 打开文件
workbook = xlrd.open_workbook(path)

# 输出Excel文件中所有sheet的名字
# print(workbook.sheet_names())

# 根据sheet索引或者名称获取sheet内容
data_sheet = workbook.sheets()[0]       # 通过索引获取
# data_sheet = workbook.sheet_by_index(0)     # 通过索引获取
# data_sheet = workbook.sheet_by_name(u'名称')      # 通过名称获取


# 获取sheet的名称、行数和列数
# print(data_sheet.name)
rowNum = data_sheet.nrows
colNum = data_sheet.ncols

# 获取所有单元格的内容
list = []
for i in range(rowNum):
    rowlist = []
    for j in range(colNum):
        rowlist.append(data_sheet.cell_value(i, j))
    list.append(rowlist)
# 输出所有单元格的内容
# for i in range(rowNum):
#     for j in range(colNum):
#         print(list[i][j], '\t\t', end="")
#     print()

# 创建三个列表包含字段名、值以及值为空的索引位列表
keylst, valuelst, numlst = [], [], []
for i in range(rowNum):
    keylst.append(data_sheet.cell_value(i, 0))
for j in range(rowNum):
    if data_sheet.cell_value(j, 1) == '':
        numlst.append(j)
    else:
        valuelst.append(data_sheet.cell_value(j, 1))

# 提出值为空的字段
for i in range(-1, -len(numlst)-1, -1):
    del keylst[numlst[i]]
a, b = '', ''
for i in range(len(keylst)):
    if i != len(keylst)-1:
        a += "'{}',".format(keylst[i])
        b += "'{}',".format(valuelst[i])
    else:
        a += "'{}'".format(keylst[i])
        b += "'{}'".format(valuelst[i])
print(a, b)

c = "INSERT INTO table_name (" + a + ") VALUES (" + b + ")"

# with open('C:/insert1.sql', 'w') as f:
#     f.write(c)
