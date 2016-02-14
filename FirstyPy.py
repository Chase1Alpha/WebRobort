# -*- coding: utf-8 -*-

__author__ = 'zcx'

# import urllib
import urllib2
import re


# 处理网页标签
class Tool:
    # 去除img标签,7位长空
    removeImg = re.compile('<img.*?>| {7}|')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    # 把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')

    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n    ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        # strip()将前后多余内容删除
        return x.strip()


# 天天美剧爬虫类
class TTMJ:
    # 初始化，传入基地址，是否只看楼主的参数
    def __init__(self, baseUrl):
        # base链接地址
        self.baseURL = baseUrl
        # HTML标签剔除工具类对象
        self.tool = Tool()
        # 全局file变量，文件写入操作对象
        self.file = None
        # 楼层标号，初始为1
        # self.floor = 1
        # 默认的标题，如果没有成功获取到标题的话则会用这个标题
        self.defaultTitle = u"天天美剧"

    # 获取网页的代码
    def getPage(self):
        try:
            # 构建URL
            url = self.baseURL
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            # 返回gbk格式编码内容
            return response.read().decode('gbk')
        # 无法连接，报错
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"连接天天美剧失败,错误原因", e.reason
                return None

                # 获取帖子一共有多少页

    def getPageNum(self, page):
        # 获取帖子页数的正则表达式
        pattern = re.compile('<a href="?page=10">(.*?)</a>', re.S)
        #print pattern
        result = re.search(pattern, page)
        #print result
        if result:
            return result.group(1).strip()
        else:
            return None

    # 获取电视剧标题
    def getTitle(self, page):
        # 得到标题的正则表达式
        pattern = re.compile('<td height="28" colspan="7" align="left"><h3>(.*?)</h3></td>', re.S)
        result = re.search(pattern, page)
        if result:
            # 如果存在，则返回标题
            return result.group(1).strip()
        else:
            return None

    # 获取网页的内容,传入页面内容
    def getContent(self, page):
        # 匹配所有的内容
        pattern = re.compile('<a href=\'(.*?)\'', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            # 将文本进行去除标签处理，同时在前后加入换行符
            content = "\n" + self.tool.replace(item) + "\n"
            contents.append(content.encode('gbk'))
        print contents
        return contents

    def setFileTitle(self, title):
        # 如果标题不是为None，即成功获取到标题
        if title is not None:
            self.file = open(title + ".txt", "w+")
        else:
            self.file = open(self.defaultTitle + ".txt", "w+")

    def writeData(self, contents):
        # 向文件写入magnet的信息
        for item in contents:
            self.file.write(item)
            #self.floor += 1

    def start(self):
        indexPage = self.getPage()
        #print indexPage
        pageNum = self.getPageNum(indexPage)
        #print pageNum
        title = self.getTitle(indexPage)
        #print title
        self.setFileTitle(title)
        #if pageNum == None:
            #print "URL已失效，请重试"
            #return
        try:
            #print "该帖子共有" + str(pageNum) + "页"
            #for i in range(1, int(pageNum) + 1):
                #print "正在写入第" + str(i) + "页数据"
                #page = self.getPage(i)
                contents = self.getContent(indexPage)
                self.writeData(contents)
        # 出现写入异常
        except IOError, e:
            print "写入异常，原因" + e.message
        finally:
            print "写入任务完成"

if __name__ == '__main__':

    print u"请输入网址"
    baseURL = 'http://www.ttmeiju.com/meiju/The.Big.Bang.Theory.html' + str(
        raw_input(u'http://www.ttmeiju.com/meiju/The.Big.Bang.Theory.html'))
    ttmj = TTMJ(baseURL)
    ttmj.start()
