from directory import Directory
from render_figure import RenderFigure
from user import User
from country import Country
from somehtml import Somehtml
from scriptpython import Scriptpython
from speak import Speak

from mymusic import Music

from mydb import Mydb
from mypic import Pic
from javascript import Js
from stylesheet import Css
import re
import traceback
import sys

class Route():
    def __init__(self):
        self.dbUsers=User()
        self.Speak=Speak

        self.Program=Directory("become 1 builder")
        self.Program.set_path("./")
        self.mysession={"notice":None,"email":None,"name":None}
        self.scriptpython=Scriptpython
        self.dbCountry=Country()
        self.db=Mydb()
        self.render_figure=RenderFigure(self.Program)
        self.getparams=("id",)
    def set_post_data(self,x):
        self.post_data=x
    def get_post_data(self):
        return self.post_data
    def set_my_session(self,x):
        print("set session",x)
        self.Program.set_my_session(x)
        self.render_figure.set_session(self.Program.get_session())
    def set_redirect(self,x):
        self.Program.set_redirect(x)
        self.render_figure.set_redirect(self.Program.get_redirect())
    def render_some_json(self,x):
        self.Program.set_json(True)
        return self.render_figure.render_some_json(x)
    def render_my_json(self,x):
        self.Program.set_json(True)
        return self.render_figure.render_my_json(x)
    def set_json(self,x):
        self.Program.set_json(x)
        self.render_figure.set_json(self.Program.get_json())
    def set_notice(self,x):
        print("set session",x)
        self.Program.set_session_params({"notice":x})
        self.render_figure.set_session(self.Program.get_session())
    def set_session(self,x):
          print("set session",x)
          self.Program.set_session(x)
          self.render_figure.set_session(self.Program.get_session())
    def get_this_get_param(self,x,params):
          print("set session",x)
          hey={}
          for a in x:
              hey[a]=params[a][0]
          return hey
          
    def get_this_route_param(self,x,params):
          print("set session",x)
          return dict(zip(x,params["routeparams"]))
          
    def logout(self,search):
        self.Program.logout()
        self.set_redirect("/")
        return self.render_figure.render_redirect()
    def addfourpointfield(self,search):
        print("hello action")
        return self.render_figure.render_figure("welcome/fourpointfield.html")
    def addsong(self,search):
        print("hello action")
        return self.render_figure.render_figure("welcome/addsong.html")
    def hello(self,search):
        print("hello action")

        return self.render_figure.render_figure("welcome/index.html")
    def delete_user(self,params={}):
        getparams=("id",)
        myparam=self.post_data(self.getparams)
        self.render_figure.set_param("user",User().deletebyid(myparam["id"]))
        self.set_redirect("/")
        return self.render_figure.render_redirect()
    def edit_user(self,params={}):
        getparams=("id",)

        myparam=self.get_this_route_param(getparams,params)
        print("route params")
        self.render_figure.set_param("user",User().getbyid(myparam["id"]))
        return self.render_figure.render_figure("user/edituser.html")
    def seesong(self,params={}):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        self.render_figure.set_param("song",self.db.Song.getbyid(myparam["id"]))
        return self.render_figure.render_figure("welcome/song.html")
    def seeuser(self,params={}):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        self.render_figure.set_param("user",User().getbyid(myparam["id"]))
        return self.render_figure.render_figure("voir/user.html")
    def update_user(self,params={}):
        myparam=self.post_data(self.getparams)
        self.user=self.dbUsers.update(params)
        self.set_session(self.user)
        self.set_redirect(("/seeuser/"+params["id"][0]))
    def login(self,s):
        search=self.get_post_data()(params=("email","password"))
        self.user=self.dbUsers.getbyemailpwsecurity(search["email"],search["password"])
        print("user trouve", self.user)
        if self.user["email"] != "":
            print("redirect carte didentite")
            self.set_session(self.user)
            self.set_json("{\"redirect\":\"/\"}")
        else:
            self.set_json("{\"redirect\":\"/sign_in\"}")
            print("session login",self.Program.get_session())
        return self.render_figure.render_json()

    def signup(self,search):
        return self.render_figure.render_figure("user/signup.html")
    def signin(self,search):
        return self.render_figure.render_figure("user/signin.html")

    def chat(self,params={}):
        myparam=self.get_post_data()(params=("user_id","text"))
        myparam["me"]="1"
        self.user=self.db.Chat.create(myparam)
        self.user= self.db.Mychat.gettextbyuserid(myparam["user_id"])
        if self.user["chat_id"]:
            self.set_notice("chat ajouté")
            self.render_figure.set_param("chats",self.db.Chat.getbyuserid(myparam["user_id"]))
            return self.render_some_json("welcome/chat.json")
        else:
            self.set_notice("erreur ; pas ok pour la creation de votre chat")
            self.render_figure.set_param("chats",[])
            return self.render_some_json("welcome/chat.json")
    def save_user(self,params={}):
        myparam=self.get_post_data()(params=("job_id","description","country_id","phone","email","gender","mypic","password","passwordconfirmation","nomcomplet"))
        print(myparam)
        self.user=self.dbUsers.create(myparam)
        if self.user["user_id"]:
            self.set_session(self.user)
            self.set_json("{\"redirect\":\"/\"}")
            return self.render_figure.render_json()
        else:
            self.set_session(self.user)
            self.set_json("{\"redirect\":\"/sign_up\"}")
            return self.render_figure.render_json()
    def newgoals(self,params={}):
        myparam=self.get_post_data()(params=("timeframe","logistics","execution","mission"))
        goals=self.db.Goals.create(myparam)
        if goals["goals_id"]:
            self.set_notice("votre goals a été créé(e)")
            self.set_json("{\"redirect\":\"/addgoals\"}")
            return self.render_figure.render_json()
        else:
            self.set_notice("erreur ; pas ok pour la creation de votre goals")
            self.set_json("{\"redirect\":\"/addgoals\"}")
            return self.render_figure.render_json()
    def newasif(self,params={}):
        myparam=self.get_post_data()(params=("speech","facial","body","accessories"))
        asif=self.db.Asif.create(myparam)
        if asif["asif_id"]:
            self.set_notice("votre asif a été créé(e)")
            self.set_json("{\"redirect\":\"/addasif\"}")
            return self.render_figure.render_json()
        else:
            self.set_notice("erreur ; pas ok pour la creation de votre asif")
            self.set_json("{\"redirect\":\"/addasif\"}")
            return self.render_figure.render_json()
    def newfourpointfield(self,params={}):
        myparam=self.get_post_data()(params=("mission","situation","execution","contingencies"))
        fourpointfield=self.db.Fourpointfield.create(myparam)
        if fourpointfield["fourpointfield_id"]:
            self.set_notice("votre fourpointfield a été créé(e)")
            self.set_json("{\"redirect\":\"/addfourpointfield\"}")
            return self.render_figure.render_json()
        else:
            self.set_notice("erreur ; pas ok pour la creation de votre fourpointfield")
            self.set_json("{\"redirect\":\"/addfourpointfield\"}")
            return self.render_figure.render_json()
    def newcouragelog(self,params={}):
        myparam=self.get_post_data()(params=("event","fear","action","result"))
        couragelog=self.db.Couragelog.create(myparam)
        if couragelog["couragelog_id"]:
            self.set_notice("votre couragelog a été créé(e)")
            self.set_json("{\"redirect\":\"/addcouragelog\"}")
            return self.render_figure.render_json()
        else:
            self.set_notice("erreur ; pas ok pour la creation de votre couragelog")
            self.set_json("{\"redirect\":\"/addcouragelog\"}")
            return self.render_figure.render_json()
    def newcouragejournal(self,params={}):
        myparam=self.get_post_data()(params=("event","fear","action","result"))
        couragejournal=self.db.Couragejournal.create(myparam)
        if couragejournal["couragejournal_id"]:
            self.set_notice("votre couragejournal a été créé(e)")
            self.set_json("{\"redirect\":\"/addcouragejournal\"}")
            return self.render_figure.render_json()
        else:
            self.set_notice("erreur ; pas ok pour la creation de votre couragejournal")
            self.set_json("{\"redirect\":\"/addcouragejournal\"}")
            return self.render_figure.render_json()
    def speak(self,params={}):
        myparam=self.get_post_data()(params=("speak",))
        self.Speak(myparam["speak"]).talk()
        self.set_json("{\"redirect\":\"/vrsong\"}")
        return self.render_figure.render_json()
    def newsong(self,params={}):
        myparam=self.get_post_data()(params=("filename","metronome","aegal","myspeed","satz","opus","speed","ton","number","name","composer","instrument_id","mytype"))
        song=self.db.Song.create(myparam)
        if song["song_id"]:
            self.set_notice("votre song a été créé(e)")
            self.set_json("{\"redirect\":\"/voirsong/"+song["song_id"]+"\"}")
            return self.render_figure.render_json()
        else:
            self.set_notice("erreur ; pas ok pour la creation de votre song")
            self.set_json("{\"redirect\":\"/addsong\"}")
            return self.render_figure.render_json()

    def lancerscript(self,search):
        myid=search["myid"][0]
        jobid=search["jobid"][0]
        namescr=self.db.Scriptjob.getbyuseridjobid(myid,jobid)
        a=self.scriptpython(namescr).lancer()
        return self.render_some_json("welcome/monscript.json")
    def ecoutermusic(self,search):
        return self.render_figure.render_figure("welcome/ecoutermusic.html")
    def run(self,redirect=False,redirect_path=False,path=False,session=False,params={},url=False,post_data=False):
        if post_data:
            print("post data")
            self.set_post_data(post_data)
            print("post data set",post_data)
        if url:
            print("url : ",url)
            self.Program.set_url(url)
        self.set_my_session(session)

        if redirect:
            self.redirect=redirect
        if redirect_path:
            self.redirect_path=redirect
        if not self.render_figure.partie_de_mes_mots(balise="section",text=self.Program.get_title()):
            self.render_figure.ajouter_a_mes_mots(balise="section",text=self.Program.get_title())
        if path and path.endswith("png"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith("mp3"):
            self.Program=Music(path)
            self.Program.set_path("./")
        elif path and path.endswith("html"):
            self.Program=Somehtml(path)
            self.Program.set_path("./")
        elif path and path.endswith("jpeg"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith("gif"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith("svg"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith("jpg"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith(".jfif"):
            self.Program=Pic(path)
        elif path and path.endswith(".css"):
            self.Program=Css(path)
        elif path and path.endswith(".js"):
            self.Program=Js(path)
        elif path:
            path=path.split("?")[0]
            print("link route ",path)
            ROUTES={
            '^/signin$': self.signin,
            '^/newsong$': self.newsong,
            '^/speak$': self.speak,
            '^/chat$': self.chat,
            '^/logmeout$':self.logout,

            '^/save_user$':self.save_user,
            '^/update_user$':self.update_user,
            "^/voirsong/([0-9]+)$":self.seesong,
            "^/seeuser/([0-9]+)$":self.seeuser,
            "^/edituser/([0-9]+)$":self.edit_user,
            "^/deleteuser/([0-9]+)$":self.delete_user,
            '^/login$':self.login,
            '^/sign_up$':self.signup,
            '^/sign_in$':self.signin,

                    '^/$': self.hello

                    }
            REDIRECT={"/save_user": "/welcome"}
            for route in ROUTES:
               print("pattern=",route)
               mycase=ROUTES[route]
               x=(re.match(route,path))
               print(True if x else False)
               #code bon pour les erreurs dans le code python
               if x:
                   params["routeparams"]=x.groups()
                   try:
                       html=mycase(params)
                   except Exception as e:
                       print("erreur"+str(e),traceback.format_exc())
                       html=("<p>une erreur s'est produite dans le code server  "+(traceback.format_exc())+"</p><a href=\"/\">retour à l'accueil</a>").encode("utf-8")
                       print(html)
                   self.Program.set_html(html=html)
                   self.Program.clear_notice()
                   #self.Program.redirect_if_not_logged_in()
                   return self.Program
               else:
                   self.Program.set_html(html="<p>la page n'a pas été trouvée</p><a href=\"/\">retour à l'accueil</a>")

        return self.Program
