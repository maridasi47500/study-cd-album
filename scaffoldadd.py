import sys
table=sys.argv[1]
form=""

for x in sys.argv[1:]:
   form+="\n    def add"+x+"(self,search):"
   form+="\n        print(\"hello action\")"
   form+="\n        return self.render_figure.render_figure(\"welcome/"+x+".html\")"
for x in sys.argv[1:]:
   form+="\nfrom "+x+" import "+x.capitalize()
for x in sys.argv[1:]:
   form+="\n        self."+x.capitalize()+"="+x.capitalize()+"()"
for x in sys.argv[1:]:
   form+="\n<%=\"<a href=\\\"/add"+x+"\\\"> add "+x+"</a>\" if session['name'] != \"\" else \"\"%>"

print(form)
