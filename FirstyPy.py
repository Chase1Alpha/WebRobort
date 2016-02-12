import urllib
import urllib2
from bs4 import BeautifulSoup
import re

url = 'http://www.ttmeiju.com/meiju/The.Big.Bang.Theory.html'

request = urllib2.Request(url)

try:
    response = urllib2.urlopen(request)
except urllib2.URLError, e:
    print e.reason

soup = BeautifulSoup(response)

#print soup.html.find_all(href=re.compile("magnet"))

download = soup.html.find_all(href=re.compile("magnet"))

def saveBrief(download):
    fileName = "download.txt"
    f = open(fileName, 'w+')
    f.write(download.encode('utf-8'))
