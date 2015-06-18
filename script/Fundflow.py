# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 22:45:17 2015
资金流向：分为：地域／大盘／个股／板块／行业资金流／概念股资金流

@author: lywen
"""
import urllib.request as request
import re
import pandas as pd
##判断网页是否存在
def url_Exists(url):
     try:
         request.urlopen(url)
         return True
     except:
         return False 
### 地地域板块数据
def get_Regional():
    url='http://data.eastmoney.com/bkzj/dy.html'
    codes=['ASCII','UTF-8','GBK','GB2312']
    header=['编码','名称','今日涨跌幅' ,'主力净流入净额','主力净流入净占比','今日超大单净流入净额','今日超大单净流入占比','今日大单净流入净额','今日大单净流入占比','今日中单净流入净额','今日中单净流入占比','今日小单净流入净额','今日小单净流入占比']
    s=""
    if url_Exists(url):
       s=request.urlopen(url).read()
       for code in codes:
           try:
              s= s.decode(code)              
              break
           except:
               continue 
    s1='defjson:{pages:1,data:'
    s2='},\r\n'
    s=re.findall(s1+'(.*)'+s2,s)
    if len(s)!=0:
        s=s[0]
        s=s.replace('[',"").replace(']',"").replace('","','"').split('"')
        if len(s)>1:
           s=map(lambda x:x.split(","),s[1:len(s)-1])
           s=list(map(lambda x:[[x[1]],[x[2]],list(map(lambda x:float(x),x[3:len(x)-2]))],s))
           return pd.DataFrame(list(map(lambda x:sum(x,[]),s)),columns=header)
    else:
        return
##个股资金流
def get_single():
    url='http://data.eastmoney.com/bkzj/dy.html'
    codes=['ASCII','UTF-8','GBK','GB2312']
    header=['编码','名称','今日涨跌幅' ,'主力净流入净额','主力净流入净占比','今日超大单净流入净额','今日超大单净流入占比','今日大单净流入净额','今日大单净流入占比','今日中单净流入净额','今日中单净流入占比','今日小单净流入净额','今日小单净流入占比']
    s=""
    if url_Exists(url):
       s=request.urlopen(url).read()
       for code in codes:
           try:
              s= s.decode(code)              
              break
           except:
               continue 
    s1='defjson:{pages:1,data:'
    s2='},\r\n'
    s=re.findall(s1+'(.*)'+s2,s)
    if len(s)!=0:
        s=s[0]
        s=s.replace('[',"").replace(']',"").replace('","','"').split('"')
        if len(s)>1:
           s=map(lambda x:x.split(","),s[1:len(s)-1])
           s=list(map(lambda x:[[x[1]],[x[2]],list(map(lambda x:float(x),x[3:len(x)-2]))],s))
           return pd.DataFrame(list(map(lambda x:sum(x,[]),s)),columns=header)
    else:
        return
def save():
    pass
        
