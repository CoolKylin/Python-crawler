# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 垃圾焚烧.py
# Time       ：2023-02-19 14:13
# Author     ：Kylin
# version    ：python 3.6
# Description：
"""
import requests
url = 'https://ljgk.envsc.cn/OutInterface/GetPSList.ashx?regionCode=0&psname=&SystemType=C16A882D480E678F&sgn=f1d10069369e0732c8cd0d92ec43c98a94c89d9e&ts=1676788277121&tc=11372987'

response = requests.get(url)
data = response.json()
print(type(data))
for i in data:
    # print(i)
    ps_name = i['ps_name']
    create_time = i['create_time']
    fullregion_name = i['fullregion_name']

    with open('垃圾焚烧站.csv', 'a+') as f:
        f.write('{},{},{}\n'.format(ps_name,create_time,fullregion_name))