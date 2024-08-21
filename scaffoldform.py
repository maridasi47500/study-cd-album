import sys

form="<form action=\"\" method=\"post\">"

for x in sys.argv:
    form+="\n<div class=\"field\">"
    form+="\n<label for=\"user_"+x+"\">"
    form+=x
    form+="\n</label>"
    form+="\n<input type=\"text\" name=\""+x+"\" id=\"user_"+x+"\" />"
    form+="\n</div>"
form+="\n<div class=\"actions\">"
form+="\n<input type=\"submit\" name=\"submit\" value=\"envoyer\" id=\"user_submit\" />"
form+="\n</div>"
form+="\n</form>"

print(form)
