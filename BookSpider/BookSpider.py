# -*- coding=utf-8 -*-
__author__ = "Jia Jiedong"

import urllib
# import urllib.request
# import urllib.parse
import re

url="http://www.quanxue.cn/CT_NanHuaiJin/LengYan/LengYan01.html"

# 根据正则表达式reg提取content中第一个匹配reg的字符串，
def splitMatch(content, reg):
    return re.search(reg, content).group(1)


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()  #.decode('utf-8')
    print html
    print '------------------------'

    pattern = re.compile(r'<p>[\s\S]*?(.*)</div>')
    pattern = re.compile(r'<p>?<=[(])[^()]+\.[^()]+(?=[>])')
    result = re.findall(pattern, html)
    # result = re.findall(r'hello', 'hello, re')
    # result = html
    return result


def writetoText(name, text):
    fp = open(name, "w")  # 打开一个文本文件
    fp.write(text)  # 写入数据
    fp.close()  # 关闭文件
    return


if __name__ == "__main__":
    text = getHtml(url)
    print (text)
    name = "d:\\BookSpider\\web.txt"

    # writetoText(name, text)

