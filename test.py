#/usr/bin/python 
# encoding:utf-8
# __Author__ = Slwhy


# request
# bs4
# Cryptopip


from mysql import mysql_db

if __name__ == '__main__':
    db = mysql_db('user','password','wangyiyun')
    # list = db.read('playlist_id','songs_playlist_id')
    # db.remov_dupli('song_id_list','song_id')
    # min_1 = db.cur.execute('select min(id) from song_id_list')
    # print min_1 == 1
    # db.arrange_id('song','id')

