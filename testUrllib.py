# -*- codeing = utf-8 -*-
# @Time : 2022-07-25 下午 4:38
# @Author : fengzhanwei
# @File : testUrllib.py
# @Software : PyCharm

import urllib.request

# 获取一个get请求
# response=urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8')) #对获取到的网页源码进行utf-8解码 会解析出一个html网页，不用decode解码的话，会乱码

#获取一个post请求 模拟用户网站登录的时候用
import urllib.parse
# data=bytes(urllib.parse.urlencode({'hello':'world'}),encoding="utf-8")
# response=urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode('utf-8'))

# 超时处理
# try:
#     response=urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("time out!")

#获取网站的各个信息
# response=urllib.request.urlopen("http://httpbin.org/get")
# print(response.status) #获取状态码
# print(response.getheaders()) #获取请求头
# print(response.getheader('Date')) #获取请求头的单个信息

# headers里面把User-Agent设为浏览器，不然会被网站识别出来是爬虫
url="http://douban.com"
headers={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71"

}
data=bytes(urllib.parse.urlencode({'name':'eric'}),encoding="utf-8")
req=urllib.request.Request(url=url,data=data,headers=headers)
response=urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
