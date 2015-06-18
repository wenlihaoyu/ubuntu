# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 14:37:02 2015
该模块用于获取股票的代码和股票名称
@author: lywen
"""
import urllib.request as request
import re
##判断网页是否存在
def url_Exists(url):
     try:
         request.urlopen(url)
         return True
     except:
         return False      
##获取网页的html 文档信息
def get_html(url):
    ##http://quote.eastmoney.com/stocklist.html
    codes=['ASCII','UTF-8','GBK','GB2312']
    if url_Exists(url):
       s=request.urlopen(url).read()
       for code in codes:
           try:
              return s.decode(code)
           except:
               continue  
    else:
         return None
## 对文档的内容进行提取        
def get_symbol(url='http://quote.eastmoney.com/stocklist.html'):
    S=get_html(url)
    if S==None:
        return
    s1='<li><a target="_blank" href="http://quote.eastmoney.com/'
    s2='</a></li>'
    str_symbol=re.findall(s1+'(.*)'+s2,S)
    symbol=[[i.split('.html')[0],(i.split('>')[1]).split('(')[0]] for i in str_symbol]
    symbol=[[i[0][2:]+'.'+i[0][0:2],i[1]] for i in symbol]    
    return symbol
def save(data):
    import pandas as pd
    try:
        df=pd.DataFrame(list(data),columns=["symbol","name"])
        df.to_csv("data/symbol.csv",index=False,encoding="utf-8")
    except:
        return
        
    