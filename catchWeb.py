# -*- coding: gbk -*-

import urllib2

# ����URL:
url = 'http://www.ttmeiju.com/meiju/The.Big.Bang.Theory.html'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
# ����gbk��ʽ��������
download = response.read()

file = open("download.txt", "w+")
file.write(str(download))
file.close()