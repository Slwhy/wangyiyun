#! /usr/bin/env python 
# encoding:utf-8
# primary function of MySQL

import MySQLdb


'''
readme: achieve some primary functon of mysql
params : 
    table  :  the name of table you want to operate 
    key    :  the name of column
    value  :  the value you want to select or insert 

function: 
    appoint_num_auto  :  
    remov_dupli       :
'''
class mysql_db(object):

    def __init__(self,user,passwd,db):
        self.user = user
        self.passwd = passwd
        self.db = db
        self.con = MySQLdb.connect(host='localhost', user=str(self.user), passwd=str(self.passwd), db=str(self.db), port=3306, charset='utf8')
        self.cur = self.con.cursor()

    def write(self,table,key,value):
        # 有待完善
        # key 以 tuple 形式传入 '( \'' + key + '\')'+ '
        # self.cur.execute('insert into '+ table + key + ' values (%s)' % value)
        # self.cur.execute('insert into ' + table + key + ' values' + tup  % value)
        self.cur.execute('insert into ' + table + key + ' values (%s)' % value)
        self.con.commit()

    def read(self,id,table):
        list = []
        self.cur.execute('select '+ id +' from ' + table)
        res = self.cur.fetchall()
        for line in res:
            list.append(line[0])
        return list



    def appoint_num_auto(self,table,num):
        # table is string
        self.cur.execute('alter table '+ table +' auto_increment = '+ str(num))


    # def remov_dupli(self,table,key):
    #     list = []   # 保存去重的字段，去重后的数据
    #     self.cur.execute('select distinct ' + key + ' from '+ table)
    #     res = self.cur.fetchall()
    #     for i in res:
    #         list.append(i)
    #
    #     return list

    def remov_dupli(self,table,key):
        # id is primary key

        sql = '''
        delete from table where key in(
            select t.key from(
                select key from table group by key having count(*)>1
            ) t
        )and id not in(
            select t.id from(
                select max(id) as id from table group by id having count(*)>1
            ) t
        )
        '''
        sql = sql.replace('table',table)
        sql = sql.replace('key',key)
        self.cur.execute(sql)
        self.con.commit()


    def arrange_id(self,table,key):
        count = 1

        #不管如何 返回值都是 1


        print self.cur.execute('select max(id) from song')
        # max_id = 0
        # sql_update = 'update table set id = count where id = min'
        # sql_update = sql_update.replace('table',table)
        # sql_update = sql_update.replace('id',key)
        #
        # sql_min = 'select min(id) from table'
        # sql_min = sql_min.replace('table',table)
        # sql_min = sql_min.replace('id',key)
        #
        # sql_max = sql_min.replace('min','max')
        # print sql_max
        #
        # print self.cur.execute(sql_max)
        # while True:
        #     sql_update = sql_update.replace('count',str(count))
        #     min_id = self.cur.execute(sql_min)
        #     sql_update = sql_update.replace('min',str(min_id))
        #     # print sql_update
        #     self.cur.execute(sql_update)
        #     print self.cur.execute('select min(id) from new_song_id')
        #     if count == self.cur.execute(sql_max):
        #         print self.cur.execute(sql_max)
        #         break
        #     self.cur.execute('')
        #     count = count + 1
        #
        # self.con.commit()