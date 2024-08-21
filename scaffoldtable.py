import sys
table=sys.argv[1]
form="<table>"
form+="\n<tr>"

for x in sys.argv[2:]:

    form+="\n<td>"
    form+=x
    form+="\n</td>"
form+="\n</tr>"
form+="\n<%=render_collection(collection=db."+table.capitalize()+".getall(), partial='welcome/_"+table+".html', as_='"+table+"')%>"

form+="\n</table>"
form+="\n<tr>"
for x in sys.argv[2:]:

    form+="\n<td>"

    form+="\n<%="+table+"['"+x+"']%>"
    form+="\n</td>"
form+="\n</tr>"


form+="\n    def new"+table+"(self,params={}):"
paspremier=False
form+="\n        myparam=self.get_post_data()(params=("

for x in sys.argv[2:]:
    if paspremier:
       form+=","

    form+="\""+x+"\""
    paspremier=True
form+="))"
form+="\n        "+table+"=self.db."+table.capitalize()+".create(myparam)"
form+="\n        if "+table+"[\""+table+"_id\"]:"
form+="\n            self.set_notice(\"votre "+table+" a été créé(e)\")"
form+="\n            self.set_json(\"{\\\"redirect\\\":\\\"/add"+table+"\\\"}\")"
form+="\n            return self.render_figure.render_json()"
form+="\n        else:"
form+="\n            self.set_notice(\"erreur ; pas ok pour la creation de votre "+table+"\")"
form+="\n            self.set_json(\"{\\\"redirect\\\":\\\"/add"+table+"\\\"}\")"
form+="\n            return self.render_figure.render_json()"

print(form)
