# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 15:48:11 2015
获取实时股票与股票的历史数据
@author: lywen
"""
import urllib.request as request
from script.symbol import *
##获取实时数据
def getSymbol(symbol):
    url="http://hq.sinajs.cn/list="+symbol
    codes=['ASCII','UTF-8','GBK','GB2312']
    s=""
    if url_Exists(url):
       s=request.urlopen(url).read()
       for code in codes:
           try:
              s= s.decode(code).replace('"',"").split("=")[1].split(",")              
              break
           except:
               continue 
    da={}
    if len(s)>0:
       try:
           da['symbol']=symbol
           da['name']=da
           da['open']=float(s[1])
           da['current']=float(s[3])
           da['high']=float(s[4])
           da['low']=float(s[5])
           da['volume']=int(s[8])
           da['money']=float(s[9])
       except:None
    return da

