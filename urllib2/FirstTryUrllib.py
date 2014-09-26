#!/usr/bin/env python
# coding=utf-8
__author__ = 'rhain'

import urllib2
import urllib

# 简单请求一个页面
url = r'http://www.xunlei.com'
html = urllib2.urlopen(url).read()
#print html

#构造一个request请求
request = urllib2.Request(url)
html = urllib2.urlopen(request).read()
#print html

#传参数
burl = "http://www.baidu.com"
#values = {"wd":"rhain"}
#data = urllib.urlencode(values)
#print data
#burl2 = burl+"?"+data
response = urllib2.urlopen(burl)
page = response.read()
#print page

#使用cookie，登陆
request = urllib2.Request(burl)
request.add_header('Referer', 'http://www.python.org')
request.add_header('Cookie', 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
request.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')
try:
    response = urllib2.urlopen(request)
except urllib2.HTTPError, e:
    pass
    #print e.code
    #print e.reason
except urllib2.URLError, e:
    pass
    #print e.reason
    #print e.reason[0]
else:
    pass
    #print response.read()
    #print response.geturl()
    #print response.info()
    #print response.getcode()


#使用代理
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({'http': '211.138.121.37:83'});
null_proxy_handler = urllib2.ProxyHandler({});
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
response = opener.open(burl)
page = response.read()
info = response.info()
#print info
#print response.getcode()

#获取cookie
import cookielib

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(burl)
for item in cookie:
    print   item.name + ":" + item.value


#debug log
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler,httpsHandler)
#print opener.open(burl).read()


#表单处理
postData = urllib.urlencode({
    'username':'rhain',
    'age':18,
})
headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
request = urllib2.Request(burl,postData,headers)
response = urllib2.urlopen(request)
print response.read()





