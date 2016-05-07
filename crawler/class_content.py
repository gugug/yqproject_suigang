#coding=utf-8
__author__ = 'yc'

from class_save_data import *

class Content(Database):
    def __init__(self):
        Database.__init__(self)

    def get_content(self,eid):

        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "SELECT blog_id,post_time FROM content WHERE event_id ='%s' ORDER BY post_time ASC LIMIT 1" % eid
            cur.execute(sql)
            rows = cur.fetchall()
        print "从数据库中提取event_id为",eid,"的记录",rows[0]['post_time']
        return rows[0]

    def save_event_rest(self, rows, tp, tpw, link,eid):
        ptime = rows['post_time']
        print 'post_time', ptime
        origin = rows['blog_id']
        print "正在更新event表"
        with self.conn:
            cur = self.conn.cursor(MySQLdb.cursors.DictCursor)
            sql = "UPDATE event SET post_time='%s',topic='%s',topic_words='%s',origin='%s',link='%s'" \
                  " WHERE event_id ='%s'" % (ptime, tp, tpw, origin, str(link), eid)
            print sql
            cur.execute(sql)

