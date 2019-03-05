# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 00:26:27 2019

@author: Administrator
"""

import re

pattern = r"([\w\.-]+)@([\w\.+]+)(\.[\w\.]+)"
str = "please contant mazhenyuan002@gmail.com for assistance"

match = re.search(pattern,str)
if match:
    print(match.group())