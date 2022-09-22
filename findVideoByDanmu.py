import re
import requests
from bs4 import BeautifulSoup as BS

def findVideoByDanmu(url_to_go, str_to_find):
    '''
    爬取视频所在合集内的所有视频（包括本身）的弹幕，并返回包含关键词的视频av号
    '''

    soup = BS(requests.get(url_to_go).text, 'lxml')
    cvid_list = set(re.findall('"aid":.........,"cid":.........',soup.prettify()))

    for cvid in cvid_list:
        url = 'http://comment.bilibili.com/' + cvid[22:] + '.xml'
        re_list = re.findall(str_to_find, str(BS(requests.get(url).content, 'xml')))
        if len(re_list):
            print(url + ' 中有弹幕关键词：' +  str_to_find + ' ' + str(len(re_list))+ '次 https://www.bilibili.com/video/av'+cvid[6:15])
        else:
            print(url)


url_to_go = 'https://www.bilibili.com/video/BV18e4y1f7iK/'
str_to_find = '电脑玩家卡比'

findVideoByDanmu(url_to_go, str_to_find)