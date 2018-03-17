#-*- coding:utf-8 -*-
from urllib import request 
from bs4 import BeautifulSoup
import os
import re

def get_html(url):
    #user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    #headers={'User_Agent':user_agent}
    req=request.Request(url)
    response=request.urlopen(req)
    html=response.read().decode("UTF-8")
    return html

def get_title(html):
    soup=BeautifulSoup(html,"html.parser")
    this_title=soup.select('#wrapper .content_read .box_con .bookname h1')[0]
    #\s 匹配任意空白字符，等价于 [\t\n\r\f].
    
    for ss in this_title.select("script"):
        ss.decompose()
    this_title=re.sub(r'\s', '  ',this_title.text).strip()
    return this_title

def get_content(html):
    soup=BeautifulSoup(html,"html.parser")
    this_content=soup.select('#wrapper .content_read .box_con #content')[0]
    for ss in this_content.select("script"):
        ss.decompose()
    this_content=re.sub( '\s+', '\r\n\t',this_content.text).strip('\r\n')     
    return this_content

def write_to_file(this_title,this_content,chapter_num):
    path="E:\\novel"
    if not os.path.isdir(path):
        os.makedirs(path)
    print("正在保存--->%s"%(this_title))
    fo=open("E:\\novel\%s.txt"%this_title,'wb')        
    fo.write(this_title.encode("UTF-8"))
    fo.write(this_content.encode("UTF-8"))
    fo.close()

def begin(a,b):
    for page in range(a,b):
        this_page=page+3231889
        url='http://www.duquge.com/dqg61582/%d.html'%this_page
        html=get_html(url)
        write_to_file(get_title(html),get_content(html),page)
    print("本部小说下载完成 ")

begin(1,400)