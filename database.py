import sqlite3
import time

class UserPost():
    def creatDatabase(self):
        self.curosr=sqlite3.Connection("User_Post.db",check_same_thread=False)
        self.pointer=self.curosr.cursor()
    def userPostTable(self):
        table="CREATE TABLE IF NOT EXISTS userPostTable( user_post_text varchar(140),user_post_time varchar(30));"
        self.pointer.execute(table)
        self.curosr.commit()

    def userPost(self,post,t=time.asctime()):
        self.pointer.execute("insert into userPostTable(user_post_text,user_post_time) values(?,?)",(post,t,))
        self.curosr.commit()

    def seeUserPost(self):
        self.pointer.execute("select * from userPostTable;")
        self.result=self.pointer.fetchall()
        self.lst=[]
        for i in self.result:
            self.lst.append(i[0])
        self.lst.reverse()
        return self.lst
    







