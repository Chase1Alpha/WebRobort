import urllib
import urllib2
from bs4 import BeautifulSoup

url = 'http://www.ttmeiju.com/meiju/The.Big.Bang.Theory.html'
#user_agent = 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)'
#headers = {'User-Agent' : user_agent}
request = urllib2.Request(url)#, headers)
try:
    response = urllib2.urlopen(request)
except urllib2.URLError, e:
    print e.reason
print response.read()