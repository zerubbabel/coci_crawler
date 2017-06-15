# -*- coding:utf-8 -*-

index_url="http://www.hsin.hr/coci/";
import urllib2  
import bs4
from bs4 import BeautifulSoup  
import re
import time
import sqlite3
import os

def insert(file_name,url):
	sql ="INSERT INTO files(file_name,url) values ('"+file_name+"','"+url+"')"
	try:
		conn.execute(sql)
		conn.commit()
		return True
	except:
		return False

def saveHtml(index_url,url):
	try:
		print "starting download:"+url
		response=urllib2.urlopen(index_url+url)
		html=response.read()		
		f=open('archives/'+url,"wb")
		f.write(html)
		f.close()
		#insert(file_name,url);
	except urllib2.URLError, e:
		if hasattr(e,"code"):
		    print e.code
		if hasattr(e,"reason"):
		    print e.reason 			

def main2():
	#global DB_FILE_PATH
	#DB_FILE_PATH='coci.db'
	#global conn
	#conn = sqlite3.connect(DB_FILE_PATH)
	global log_text
	log_text=''
	now=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))	
	log_text+=now+'\n=========\n'
	print log_text

	try:
		#首页
		response = urllib2.urlopen(index_url)
		html=response.read()
		
		f=open("index.html","wb")
		f.write(html)
		f.close()

		content = BeautifulSoup(html,"lxml")
		#file_name=content.select('div[class="naslov"]')
		tbls=content.select('table')
		for tbl in tbls:
			tds=tbl.find_all('td')
			for td in tds:
				contest=td.find('div')
				for a in td.find_all('a')[1:-1]:
					link=a['href']
					if not os.path.exists('archives/'+link):
						saveHtml(index_url,link)
						log_text+=link+"downloaded!\n"
			
	except urllib2.URLError, e:
	    if hasattr(e,"code"):
	        print e.code
	    if hasattr(e,"reason"):
	        print e.reason  

	#conn.close()  

	f=open(now+"log.txt","wb")
	f.write(log_text)
	f.close()  
	  

def getSeasons():
	response = urllib2.urlopen(index_url)
	html=response.read()
	content = BeautifulSoup(html,"lxml")
	season=content.select('table')[-1].find_next_sibling('div[class="naslov"]')
	while season:
		print season
		season=season..find_next_sibling('div[class="naslov"]')
		

def main():
	season_pages=getSeasons();
	
if __name__ == '__main__':
    main()