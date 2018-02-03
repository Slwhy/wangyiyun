#/usr/bin/python 
# encoding:utf-8
# __Author__ = Slwhy
# get the url of song

import requests
from mysql import mysql_db
from bs4 import BeautifulSoup
from header import head


db = mysql_db('root', '1002', 'wangyiyun')


def get_html(url):
    try:
        r = requests.get(url,headers = head,timeout = 20)
        print r.status_code
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print 'get_html error'
        return ''


def get_song_id(playlist_id_list):
    # url = 'http://music.163.com/playlist?id=2074306523'
    root_url = 'http://music.163.com/playlist?id='
    lent = playlist_id_list.__len__()
    count = 1
    for i in range(0, lent):
        db.appoint_num_auto('song_id_list',count)
        playlist_id = playlist_id_list[i]
        url = root_url + playlist_id
        html = get_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.find('ul')
        try:
            for tag in ul.children:
                a = tag.a
                song_href = a.get('href')
                song_id = song_href.split('=')[1]
                song_name = tag.get_text()
                cur = db.cur

                # 在插入字符是需要对加入 '' 要不然会报 _mysql_exceptions.OperationalError: (1054, "Unknown column 'Collide' in 'field list'")
                # cur.execute('insert into song_id_list (song_id,name) values (%s,%s)' % (song_id, song_name))
                try:
                    cur.execute('insert into song_id_list (song_id,name) values (\'%s\',\'%s\')' % (song_id, song_name))
                    count = count + 1
                except:
                    print 'mysql error'
                    print song_id,song_name

        except AttributeError:
            print ArithmeticError.message
        db.con.commit()

if __name__ == '__main__':
    playlist_id_list = []
    playlist_id_list = db.read('playlist_id','songs_playlist_id')
    # print playlist_id_list
    # get_song_id(playlist_id_list)
    song_id_list = db.remov_dupli('song_id_list','song_id')
    lent = song_id_list.__len__()
    print lent
    for i in range(1,lent):
        print song_id_list[i]





