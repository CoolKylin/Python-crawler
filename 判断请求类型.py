# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 判断请求类型.py
# Time       ：2023-02-19 19:23
# Author     ：Kylin
# version    ：python 3.6
# Description：
"""
import requests
url = 'https://c.m.163.com/news/hot/newsList'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)
content_type = response.headers.get('Content-Type')
if 'application/json' in content_type:
    print('返回的是JSON数据')
elif 'text/html' in content_type:
    print('返回的是HTML页面')
else:
    print('未知的响应类型')