# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : youdao.py
# Time       ：2023-02-25 12:56
# Author     ：Kylin
# Description：
"""
import json
from Crypto.Cipher import AES
import time
from Crypto.Hash import MD5
import requests
import hashlib
import base64
import os

t = str(int(time.time() * 1000))

def clear_input():
    """清除输入缓存"""
    try:
        # for Windows
        os.system('cls')
    except:
        # for other systems
        os.system('clear')

def clear_screen():
    os.system('cls')

def md5(s):
    h = hashlib.md5()
    h.update(s.encode('utf-8'))
    return h.hexdigest()

def get_sign(r, i, e, t):
    s = f'client={r}&mysticTime={t}&product={i}&key={e}'
    return md5(s)

def decrypt(t, key, iv):
    a = key
    r = iv
    cipher = AES.new(a, AES.MODE_CBC, r)
    res = cipher.decrypt(base64.urlsafe_b64decode(t))
    txt = res.decode("utf-8")
    return json.loads(txt[: txt.rindex("}") + 1])

def main():
    while True:
        key = input("请输入中文（输入 EXIT 退出, 输入 REFRESH刷新）：").strip()
        if key == "EXIT":
            return
        elif not key:
            continue
        elif key == 'REFRESH':  # 如果输入为fresh，则清空屏幕
            clear_input()
            continue
        else:
            # 密码参数常量
            e = "fsdsogkndfokasodnaso"
            r = "fanyideskweb"
            i = "webfanyi"

            decode_key = b"ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl"
            decode_iv = b"ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4"

            key_bytes = MD5.new(decode_key).digest()[:16]
            iv_bytes = MD5.new(decode_iv).digest()[:16]

            sign = get_sign(r, i, e, t)

            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50',
                'Cookie': 'OUTFOX_SEARCH_USER_ID=-1319948723@10.105.137.202; OUTFOX_SEARCH_USER_ID_NCOO=1992916785.0866556',
                'Host': 'dict.youdao.com',
                'Origin': 'https://fanyi.youdao.com',
                'Referer': 'https://fanyi.youdao.com/'
            }
            data = {
                'i': key,
                'from': 'auto',
                'to': 'auto',
                'dictResult': 'true',
                'keyid': 'webfanyi',
                # 已加密
                'sign': sign,
                'client': 'fanyideskweb',
                'product': 'webfanyi',
                'appVersion': '1.0.0',
                'vendor': 'web',
                'pointParam': 'client,mysticTime,product',
                # 时间戳
                'mysticTime': t,
                'keyfrom': "fanyi.web"
            }
            url = 'https://dict.youdao.com/webtranslate'
            response = requests.post(url, headers=headers, data=data)

            data = decrypt(response.text, key_bytes, iv_bytes)
            result = data['translateResult']
            print(result[0][0]['tgt'])

if __name__ == "__main__":
    main()
