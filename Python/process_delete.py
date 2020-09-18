#!Python
import cgi, os

form = cgi.FieldStorage()
pageid = form.getvalue("pageid")

os.remove('data/'+pageid)
#Redirection
print("Location: index.py")
print()
