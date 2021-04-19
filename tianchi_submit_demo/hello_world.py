#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pandas import DataFrame as df
import pandas as pd
import numpy as np
import json

# 终端输出Hello world
print("Hello world")

# 对天池在基础镜像给出的基础数据列求和
data = pd.read_csv("/tcdata/num_list.csv", header=None)
total = 0
for i, num in enumerate(data[0]):
    total += num

# 对数据排序
data.sort_values(by=0, ascending=False, inplace=True)
sort_data = list(data[0][:10])

# 以json文件方式输出结果到本地文件
result = {
    "Q1": "Hello world",
    "Q2": total,
    "Q3": sort_data
        }

with open("result.json", "w") as f:
    json.dump(result, f)
