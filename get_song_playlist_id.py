#/usr/bin/python
# encoding:utf-8
# __Author__ = Slwhy

import requests
import os
import json
from Crypto.Cipher import AES
import base64
from bs4 import BeautifulSoup
import string
import csv
from mysql import mysql_db

db = mysql_db('user','password','mysql')

def write_song_list(song_list):

    # cur.execute(    # 创建一张 table
    #     'create table song_id_list('
    #     'id int not null auto_increment primary key,'
    #     # 'title varchar(20),'
    #     'song_id int)'
    # )
    len_song_list = song_list.__len__()
    for i in range(0,len_song_list):
        id = song_list[i][0]
        id = string.atoi(id)
        print id
        title = song_list[i][1]
        print title
        db.cur.execute('insert into songs_playlist_id(playlist_id) values (%s)' %id)
        # cur.execute('insert into song_id_list(song_id,title) values (%s,%s)',(id,title))
    db.con.commit()


def write_song_playlist_id(song_list):
    path = os.getcwd()
    path = path + '/db/playlist_id.csv'
    with open(path,'wb') as f:
    # f = open(path,'wb')


        write = csv.writer(f,dialect='excel')
        len = song_list.__len__()

        # csv 写入时必须要以列表的形式写入，要不然，ta 会将你的字符串当成一个列表写进去
        for i in range(0,len):
            write.writerow([song_list[i][0],])





class wangyi_encry(object):

    def __init__(self):
        pass
    # 产生一个 aes 的秘钥
    def createSecretKey(self,size):
        return (''.join(map(lambda xx: (hex(ord(xx))[2:]), os.urandom(size))))[0:16]

    # rsa 加密算法
    def rsaEncrypt(self,text, pubKey, modulus):
        text = text[::-1]
        rs = int(text.encode('hex'), 16)**int(pubKey, 16)%int(modulus, 16)
        return format(rs, 'x').zfill(256)

    # aes 加密算法
    def aesEncrypt(self,text, secKey):
        pad = 16 - len(text) % 16
        text = text + pad * chr(pad)
        encryptor = AES.new(secKey, 2, '0102030405060708')
        ciphertext = encryptor.encrypt(text)
        ciphertext = base64.b64encode(ciphertext)
        return ciphertext


class from_data(object):


    def __init__(self):
        pass

    def create_text(self,num):
        text = {
            "rid": "A_PL_0_430509126",
            "offset": str(num*40),
            "total": "false",
            "limit": "40",
            "csrf_token": ""}

        return text

    def create_data(self,num):  #num用于获取多条评论，40一次
        modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        nonce = '0CoJUm6Qyw8W8jud'
        pubKey = '010001'
        text = json.dumps(self.create_text(num))
        wangy_en = wangyi_encry()
        secKey = wangy_en.createSecretKey(16)
        encText = wangy_en.aesEncrypt(wangy_en.aesEncrypt(text, nonce), secKey)
        encSecKey = wangy_en.rsaEncrypt(secKey, pubKey, modulus)

        data = {
            'params': encText,
            'encSecKey': encSecKey
        }

        return data

def get_song_list(song_list,page):

    '''
        http://music.163.com/discover/playlist/?order=hot&limit=35&offset=70
        http://music.163.com/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=35
        http://music.163.com/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=70
    '''

    url_play_root = 'http://music.163.com/discover/playlist/'
    for i in range(page):
        url_play = url_play_root + '?order=hot&limit=35&offset=' +str(page*i)
        r = requests.get(url_play)
        soup = BeautifulSoup(r.text, 'html.parser')
        tag_li = soup.find(class_="m-cvrlst f-cb")
        try:
            for i in tag_li.find_all('a'):
                try:
                    id = i.get('href')
                    id = str(id).split('id=')
                    title = i.get('title')
                    print type(title)
                    song_list.append((id[1], i.get('title')))
                except IndexError:
                    print IndexError.message

        except AttributeError:
            print AttributeError.message


if __name__ == '__main__':

    url_play = 'http://music.163.com/discover/playlist/'
    song_list = []
    get_song_list(song_list,37)
    write_song_list(song_list)
    # write_song_playlist_id(song_list)


