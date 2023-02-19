# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 网易新闻采集.py
# Time       ：2023-02-19 18:51
# Author     ：Kylin
# version    ：python 3.6
# Description：
"""
import os
import re
import requests
from bs4 import BeautifulSoup #用于解析HTML页面

url = 'https://c.m.163.com/news/hot/newsList'

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)

# 解析HTML页面
soup = BeautifulSoup(response.text, 'html.parser')

# 获取标题
title_divs = soup.find_all('div', class_='title')

# 遍历所有 <div> 元素，并获取 <a> 元素中的链接和文本信息
titles = []
for div in title_divs:
    a = div.find('a')
    title = a.text
    href = a['href']
    titles.append(href)
print(titles)

for tit in titles:
    # 使用requests模块获取页面内容
    headtit = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    response = requests.get(tit, headers=headtit)
    tmp_html = response.text
    # 使用BeautifulSoup模块解析HTML页面
    tmp_soup = BeautifulSoup(tmp_html, 'html.parser')
    # 获取标题和正文
    title = tmp_soup.title.string
    # 将非法字符替换为空格
    title = re.sub(r'[\\/:*?"<>|]+', ' ', title)
    content = tmp_soup.find_all('p')

    # 创建名为"output"的子目录，如果该子目录不存在
    if not os.path.exists("book"):
        os.makedirs("book")

    # 将标题和正文写入文件中
    with open(os.path.join("book", title + '.txt'), 'w', encoding='utf-8') as f:
        f.write(f'Title: {title}\n')
        for p in content:
            f.write(f'{p.text}\n')
        f.write('\n')
