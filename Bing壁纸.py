# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Bing壁纸.py
# Time       ：2023-02-19 17:02
# Author     ：Kylin
# version    ：python 3.6
# Description：
"""
import requests
from bs4 import BeautifulSoup

search_query = '小清新插画'
url = f'https://www.bing.com/images/search?q={search_query}&size=1920x1200'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

images = soup.findAll('img', {'class': 'mimg'})

for img in images:
    img_url = img['src']
    img_response = requests.get(img_url)
    file_size = int(img_response.headers.get('Content-Length', 0))
    with open(f'{search_query}_{file_size}.jpg', 'wb') as f:
        f.write(img_response.content)
