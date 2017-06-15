# -*- coding:utf-8 -*-
#下载coci首页当前season数据，不直接下载，生成下载链接文件，uget工具下载

index_url="http://www.hsin.hr/coci/"
DIR='archives/'
import urllib2  
import bs4
from bs4 import BeautifulSoup  
import re
import time
import os

#获取html页面内容
def getHtml(url):
	print "download:"+url
	return urllib2.urlopen(url).read()
#bs化Html
def bsHtml(html):
	return BeautifulSoup(html,"lxml")

#输出内容到文件
def outputToFile(filename,content):
	if not os.path.exists(filename):
		f=open(filename,"wb")
		f.write(content)
		f.close()
	else:
		print filename+" already exist!"

#获取下载链接	
def getlinks(content):
	links=[]
	tbls=content.select('table')
	for tbl in tbls:
		tds=tbl.find_all('td')
		for td in tds:
			contest=td.find('div')
			for a in td.find_all('a')[1:-1]:
				link=a['href']
				links.append(index_url+link)
	return links	
				
def main():
	#season_pages=getSeasons();
	indexHtml=getHtml(index_url)
	indexBs=bsHtml(indexHtml)
	links=getlinks(indexBs)
	txt="\n".join(links)
	outputToFile('downlist.txt',txt)

if __name__ == '__main__':
    main()