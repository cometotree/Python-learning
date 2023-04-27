import pandas as pd
import json

# 读取Excel文件
df = pd.read_excel('data_dc_level_sort.xlsx')

# 转换为JSON格式
json_data = df.to_json(orient='records')

# 保存JSON文件
with open('data_dc_level_sort_1.json', 'w') as f:
    json.dump(json.loads(json_data), f)

#======================================================================
# 读取Excel文件
df = pd.read_excel('data_dc_level_sort.xlsx', sheet_name=0)

# 将DataFrame转换为字典
data_dict = df.to_dict(orient='records')

# 将字典转换为JSON格式
sheet_name = df.columns[0]  # 获取第一列的列名，即sheet的名称
json_data = {sheet_name: data_dict}

# 保存JSON文件
with open('data_dc_level_sort_2.json', 'w') as f:
    json.dump(json_data, f)


#======================================================================
# 读取Excel文件
excel_file = pd.read_excel('data_dc_level_sort.xlsx', sheet_name=None)

# 遍历每个sheet，将其转换为JSON格式
json_data = {}
for sheet_name, df in excel_file.items():
    data_dict = df.to_dict(orient='records')
    json_data[sheet_name] = data_dict

# 保存JSON文件
with open('data_dc_level_sort.json', 'w') as f:
    json.dump(json_data, f)

#======================================================================
def find_median(arr):
    """
    计算数值类型数组的中位数
    :param arr: 数值类型数组
    :return: 数组所有数字的中位数
    """
    n = len(arr)
    if n % 2 == 0:
        # 如果数组长度为偶数，则中位数为中间两个数的平均值
        return (sorted(arr)[n // 2 - 1] + sorted(arr)[n // 2]) / 2
    else:
        # 如果数组长度为奇数，则中位数为中间的数
        return sorted(arr)[n // 2]

find_median([99,28,30,40,77,20,31,888,53.4])

#======================================================================

# 导入需要的模块
import pandas as pd
import json

# 读取excel文件中的所有sheet
sheets = pd.read_excel("events_lv_data_1.xlsx", sheet_name=None)

# 创建一个空字典用于存储数据
data = {}

# 遍历每个sheet
for sheet_name, sheet_data in sheets.items():
    # 将指定的列转换为相应的类型
    sheet_data["level_id"] = sheet_data["level_id"].astype(int)
    sheet_data["target"] = sheet_data["target"].astype(str)
    sheet_data["target_type"] = sheet_data["target_type"].astype(str)
    sheet_data["category"] = sheet_data["category"].astype(str)
    sheet_data["map_above"] = sheet_data["map_above"].astype(str)
    sheet_data["map_below"] = sheet_data["map_below"].astype(str)

    # 将数据框转换为字典列表
    sheet_dict = sheet_data.to_dict(orient="records")

    # 将sheet名称作为键，字典列表作为值，添加到数据字典中
    data[sheet_name] = sheet_dict

# 将数据字典转换为json格式
json_data = json.dumps(data, indent=4)

# 写入json文件
with open("events_lv_data_1.json", "w") as f:
    f.write(json_data)

#======================================================================

# 导入需要的模块
import os
import json
import pandas as pd

# 获取当前文件夹内的所有excel文件
excel_files = [f for f in os.listdir() if f.endswith('.xlsx')]

# 遍历每个excel文件
for excel_file in excel_files:
    # 读取excel文件中的所有sheet
    sheets = pd.read_excel(excel_file, sheet_name=None)
    # 创建一个空字典用于存储json数据
    json_data = {}
    # 遍历每个sheet
    for sheet_name, sheet_data in sheets.items():
        # 将sheet数据转换成字典格式，并以sheet名称作为父级名称
        json_data[sheet_name] = sheet_data.to_dict(orient='records')
    # 将json数据格式化并编码为utf-8
    json_data = json.dumps(json_data, ensure_ascii=False, indent=4).encode('utf-8')
    # 生成输出的json文件名，与excel文件名相同，只是后缀不同
    json_file = excel_file.replace('.xlsx', '.json')
    # 打开输出的json文件，并写入json数据
    with open(json_file, 'wb') as f:
        f.write(json_data)

#======================================================================

# 导入所需的模块
import pandas as pd
import json

# 定义一个函数来转换数据类型
def convert_dtype(value, dtype):
    if dtype == "int":
        return int(value)
    elif dtype == "float":
        return float(value)
    elif dtype == "bool":
        return bool(value)
    else:
        return str(value)

# 读取excel文件"events_lv_data_1.xlsx"
df = pd.read_excel("events_lv_data_1.xlsx", sheet_name=None)
# 遍历excel文件的每一个sheet
for sheet_name, sheet_data in df.items():
    # 获取第一行的数据类型列表
    dtypes = sheet_data.iloc[0].tolist()
    # 获取第二行的输出标志列表
    flags = sheet_data.iloc[1].tolist()
    # 获取第三行的字段名称列表，并作为列名
    columns = sheet_data.iloc[2].tolist()
    sheet_data.columns = columns
    # 创建一个空列表来存储json数据
    json_data = []
    # 遍历sheet的每一行（从第四行开始）
    for index, row in sheet_data.iterrows():
        if index > 2:
            # 创建一个空字典来存储每一行的数据
            row_data = {}
            # 遍历每一列（从第一列开始）
            for i in range(len(row)):
                # 如果输出标志为TRUE，则将该列的数据添加到字典中，并转换为相应的数据类型
                if flags[i] == "TRUE":
                    row_data[columns[i]] = convert_dtype(row[i], dtypes[i])
            # 将字典添加到列表中
            json_data.append(row_data)
    # 将列表转换为json格式，并以sheet名称作为父级名称，以excel文件名作为输出文件名
    with open("events_lv_data_1.json", "w") as f:
        json.dump({sheet_name: json_data}, f, indent=4)




# 导入所需的模块
import pandas as pd
import json

# 定义一个函数来转换数据类型
def convert_dtype(value, dtype):
    if dtype == "int":
        return int(value)
    elif dtype == "float":
        return float(value)
    elif dtype == "bool":
        return bool(value)
    else:
        return str(value)

# 读取excel文件"events_lv_data_1.xlsx"
df = pd.read_excel("events_lv_data_1.xlsx", sheet_name=None)
# 遍历excel文件的每一个sheet
for sheet_name, sheet_data in df.items():
    # 获取第二行的数据类型列表
    dtypes = sheet_data.iloc[1].tolist()
    # 创建一个空列表来存储json数据
    json_data = []
    # 遍历sheet的每一行（从第三行开始）
    for index, row in sheet_data.iterrows():
        #if index > 1:
            # 创建一个空字典来存储每一行的数据
            row_data = {}
            # 遍历每一列（从第一列开始）
            for i in range(len(row)):
                # 将该列的数据添加到字典中，并转换为相应的数据类型
                row_data[sheet_data.columns[i]] = convert_dtype(row[i], dtypes[i])
            # 将字典添加到列表中
            json_data.append(row_data)
    # 将列表转换为json格式，并以sheet名称作为父级名称，以excel文件名作为输出文件名
    with open("events_lv_data_1.json", "w") as f:
        json.dump({sheet_name: json_data}, f, indent=4)
