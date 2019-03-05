# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 22:47:30 2019

@author: Administrator
"""

import re

s = input("请输入身份证号码：") 

res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})',s)
print(res.groupdict())