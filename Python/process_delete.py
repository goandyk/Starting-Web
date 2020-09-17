#!C:\Users\66655\AppData\Local\Programs\Python\Python38-32\python.exe

import cgi, os

form = cgi.FieldStorage()
pageid = form.getvalue("pageid")

os.remove('data/'+pageid)
#Redirection
print("Location: index.py")
print()
