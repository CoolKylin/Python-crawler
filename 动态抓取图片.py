# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 动态美女.py
# Time       ：2023-02-19 15:33
# Author     ：Kylin
# version    ：python 3.6
# Description：
"""
import requests
# url = 'https://api.bilibili.com/x/web-interface/wbi/search/type?__refresh__=true&_extra=&context=&page=2&page_size=42&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword=美女&qv_id=WUyTCXoxIMhY5wxg5XJAUiXeNpbZ0hlW&ad_resource=5654&source_tag=3&category_id=&search_type=video&dynamic_offset=36&preload=true&com2co=true'
url = 'https://api.bilibili.com/x/web-interface/wbi/search/type?__refresh__=true&_extra=&context=&page=2&page_size=42&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword=美女&qv_id=Q4UAuZYEz7j8cjLHCAOt0kHtr3cjhQkq&ad_resource=5654&source_tag=3&category_id=&search_type=video&dynamic_offset=36&w_rid=68b0140504bf4bed7e8cd917c50bb4f8&wts=1676793817'
response = requests.get(url)
data = response.json()['data']['result']
num = 0
for info in data:
    author = info['author']
    pic = info['pic']
    filename = 'http:' + pic
    print(filename)
    description = info['description']
    arcurl = info['arcurl']

    with open('B站美女.csv','a+') as f:
        f.write('{},{},{},{}\n'.format(num,author,arcurl,pic))

    a = requests.get(filename)
    with open(r'.\photo\{}.jpg'.format(num), 'wb') as f1:
        f1.write(a.content)  # 二进制
    num += 1
