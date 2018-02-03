#/usr/bin/python
# encoding:utf-8
# __Author__ = Slwhy

import requests
import os
import json
from Crypto.Cipher import AES
import base64
import re
from mysql import mysql_db



db = mysql_db('root','1002','wangyiyun')



head = {
#

        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'

}
#
# # head['Cookie'] = 'JSESSIONID-WYYY=Jgi1ax6XAkd6cNwfV6qxBbhya5s4SW00PtEcYPNYUgdOeQO%5Cf%2FyFUQo%2FAVRlqDhDV8d7D%5CSGCtdu0NYgBxn9YdoZ0WuTb9VH0Nydug%2BZ4SUn74vDPG%2F%5CD6slP%2FmuljYfIVf%2F2X%5CxlrXuCvJjw8ER4amzfEPao6x5elWf%2B2OkzmGPJ%2Bvz%3A1515500969576; _iuqxldmzr_=32; _ntes_nnid=099805196f22bf7617cf11b5a67feeff,1515499169604; _ntes_nuid=099805196f22bf7617cf11b5a67feeff; __utma=94650624.1398381638.1515499170.1515499170.1515499170.1; __utmc=94650624; __utmz=94650624.1515499170.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmb=94650624.6.10.1515499170'


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

class analy_comments_json(object):

# data = {
#         'params':'VTR9VH3d/ourPcEVgzKHba+sLegQNw9bJiqltYz2T0NcJifrsrSlOh1BfqQt2wZsZo5okKVeluhBQ0TNhrQChbDoq9FfyJo6BvTkKVQN6e13ytcwo+9voHSQmhbDSn71zv9/v3axqK5p8PhajmA8+1/BKowmhlOP2Ohjcf4MYjnBRpbTcirXVwGf7k5ZaNIA',
#         'encSecKey':'cc6d7e14ac1408c39a7c172b70fb1005e199f298abfb5db75919d8b17e574c95ed400947e6e0213a3f4a03e3e568bb54841bafb736906d4d6fe118097afb413ec27ad514c41d92a6f6e2fe8d97febf600651726023071d62236445d2c5bc667888e30f03000f09fefd76f28613abd90f680603cfd7a624370c736b8805225b16'
#     }


    def __init__(self):
        pass

    def analy_cont(self,retur_json,song_id):
        # count = 0
        try:
            comments = retur_json['comments']
            for i in comments:
                # count = count+1
                try:
                    user = i['user']
                    user_nickname = user['nickname']
                    content = i['content']
                    commentId = i['commentId']
                    print 'user_nikname:',user_nickname
                    print 'content:',content
                    print 'commentId:',commentId
                    # print count
                    print '\n----------------------------\n'
                    cur = db.cur
                    cur.execute('insert into  comments (content,song_id,comment_id,comment_ower_name) value (\'%s\',\'%s\',\'%s\',\'%s\')' % (content,song_id,commentId,user_nickname))
                    # db.con.commit()
                except:
                    print 'error'

        except:
            print "KeyError"


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

class comm_songs(object):

    def __init__(self):
        pass



if __name__ == '__main__':

    root_url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_'
    # url = 'http://music.163.com/weapi/v1/resource/comments/A_PL_0_2015321897?csrf_token='
    # url = 'http://music.163.com/weapi/v1/resource/comments/A_PL_0_973757368?csrf_token='
    song_id_list = db.read('song_id','song_id_list')
    s = requests.session()
    f_data = from_data()
    count = 0     # 用于控制爬取的歌曲数量
    while True:
        try:
            song_id = song_id_list[count]
            url = root_url + str(song_id) + '?csrf_token='
            count = count + 1
            for i in range(10):
                r = s.post(url, data=f_data.create_data(i), headers=head)
                conte = r.text
                conte = json.loads(conte)
                anay = analy_comments_json()
                anay.analy_cont(conte,song_id)

        except:
            print 'requests.exceptions.ConnectionError'
        db.con.commit()
        if count == 3000:
            break

