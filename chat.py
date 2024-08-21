# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Chat(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists chat(
        id integer primary key autoincrement,
        user_id text,
            me text,
            text text
    ,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP                );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from chat")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from chat where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyuserid(self,myid):
        self.cur.execute("select * from chat where user_id = ?",(myid,))
        job=self.cur.fetchall()
        return job
    def getbyid(self,myid):
        self.cur.execute("select * from chat where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def create(self,params):
        print("ok")
        myhash={}
        for x in params:
            if 'confirmation' in x:
                continue
            if 'envoyer' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                #print("my params",x,params[x])
                try:
                  myhash[x]=str(params[x].decode())
                except:
                  myhash[x]=str(params[x])
        print("M Y H A S H")
        print(myhash,myhash.keys())
        myid=None
        try:
          self.cur.execute("insert into chat (user_id,me,text) values (:user_id,:me,:text)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["chat_id"]=myid
        azerty["notice"]="votre chat a été ajouté"
        return azerty




