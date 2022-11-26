#! python3
# coding: utf-8
# 测试pandas读取csv文件

import os
import pandas as pd

# csv_path = os.path.join('..','/original scripts/csv')
# os.chdir(csv_path)
path = os.getcwd()
# parent = os.path.join(path, os.pardir)
spath = os.path.join(path, r'OriginalScripts/csv/')
# os.chdir(spath)
test_file = pd.read_csv(os.path.join(path, r'Original Scripts/csv/AAPL.csv'))
# test_file = pd.read_csv('AAPL.csv')
print(test_file.head())
# print(os.getcwd())
