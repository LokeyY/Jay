#coding=gbk
import requests
from bs4 import BeautifulSoup
import json
import csv
def getHtmlText(url):
    try:
        kv={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0",
            "Referer":r"https://y.qq.com/n/yqq/album/003dAEX43IElBh.html"}
        r=requests.get(url,headers=kv)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.content
    except:
        print("页面爬取失败！")

def loadText(html,info):
    jsText=json.loads(html)
    commonData = jsText["comment"]["commentlist"]
    for eachComment in commonData:
        info.append([eachComment["commentid"], eachComment["nick"], eachComment["rootcommentcontent"]])

def  writeInfo(info):
    with open(r"C:\Users\john\Desktop\jay.txt","a",encoding="utf-8") as f:
        for item in info:
            f.write(item[2])
            f.write("\n")
    with open(r"C:\Users\john\Desktop\python_seeNumber\jay.csv","a",newline="",encoding="utf-8") as f:
        csvWriter=csv.writer(f)
        for row in info:
            csvWriter.writerow(row)

def main():
    info = []
    for i in range(5):
        url=r"https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk=5381&jsonpCallback=jsoncallback002420684550357821&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq&needNewCode=0&cid=205360772&reqtype=2&biztype=2&topid=60736&cmd=8&needmusiccrit=0&pagenum=%d&pagesize=25&domain=qq.com&ct=24&cv=101010"%i
        html=getHtmlText(url)
        loadText(html,info)
    writeInfo(info)

if __name__ == "__main__":
    main()



