#! /usr/bin/env python 
# encoding:utf-8


#网易云音乐增加了 UA 的判别，需要修改

head = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    #'Cookie': '_iuqxldmzr_=32; _ntes_nnid=8390001eb944938edd933ce80bafaee8,1515684802491; _ntes_nuid=8390001eb944938edd933ce80bafaee8; __utmz=94650624.1515941185.5.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=94650624; JSESSIONID-WYYY=3M1JFih9TuhjwyubKvESyb757Wx8l2pO8Raq5gGlBnBFVS%5ChFBGxAKcZugzAps6fDgoJhNN9SB9b6QOGqg94rkg18zgzSV8hB0XzVjQjTn6I%5Cs3DASN2wkxT1qDcAbYBqIJjRg%2BD%5CAYEz1%5Ck46sluHVCabDi9ItO2%2BlmJtSUU624hi1%2B%3A1517143718685; __utma=94650624.1122297636.1515684804.1517127998.1517142059.7; __utmb=94650624.10.10.1517142059',
    'Host': 'music.163.com',
    'Referer': 'http://music.163.com/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3311.4 Safari/537.36'
}