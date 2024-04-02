import csv

# 数据行列表，每行是一个列表
data = [
    ["姓名", "年龄", "城市"],
    ["Alice", "28", "纽约"],
    ["Bob", "34", "洛杉矶"],
    ["Charlie", "45", "芝加哥"],
]

# 指定要写入的CSV文件名称
filename = "example.csv"

# 使用 'with' 用于自动关闭文件
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # 写入数据
    for row in data:
        writer.writerow(row)

# 文件现在已经保存了

import csv

# 需要插入的数据，假设数据是一个列表形式，字段匹配CSV的列
data_to_insert = ['value1', 'value2', 'value3']

# CSV文件的路径
csv_file_path = 'example.csv'

# 打开文件
with open(csv_file_path, mode='a', newline='') as file:  # 模式'a'用于向文件追加内容
    writer = csv.writer(file)
    # 插入数据，data_to_insert是一个列表，其中包含所有你需要按顺序插入的值
    writer.writerow(data_to_insert)