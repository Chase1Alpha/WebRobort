# -*- coding: gbk -*-

import urllib2

# 构建URL:
url = 'http://www.ttmeiju.com/meiju/The.Big.Bang.Theory.html'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
# 返回gbk格式编码内容
download = response.read()

file = open("download.txt", "w+")
file.write(str(download))
file.close()