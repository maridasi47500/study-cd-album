# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Song(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists song(
        id integer primary key autoincrement,
        opus text,
        filename text,
            speed text,
            ton text,
            number text,
            name text,
            satz text,
            mouvement text,
            metronome text,
            aegal text,
            myspeed text,
            composer text,
            instrument_id text,
            mytype text
    ,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP                );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from song")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from song where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from song where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def track_list(self,myid):
        self.cur.execute("select * from song where id = ?",(myid,))
        malist=[]

        row=self.cur.fetchall()
        for x in row:
            malist.append({
            "id": x["id"],
            "name": x["name"]+" "+x["number"],
            "artist": x["composer"],
            "image": ("https://source.unsplash.com/Qrspubmx6kE/640x360"),
            "path": "/uploads/"+x["filename"]
            })
        return malist
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
          self.cur.execute("insert into song (mouvement, filename,myspeed,metronome,aegal,satz,opus,speed,ton,number,name,composer,instrument_id,mytype) values (:mouvement,:filename,:myspeed,:metronome,:aegal,:satz,:opus,:speed,:ton,:number,:name,:composer,:instrument_id,:mytype)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["song_id"]=myid
        azerty["notice"]="votre song a été ajouté"
        return azerty




