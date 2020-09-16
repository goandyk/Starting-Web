#!C:\Users\66655\AppData\Local\Programs\Python\Python38-32\python.exe

import cgi
form = cgi.FieldStorage()
title = form.getvalue("title")
description = form.getvalue("description")

opened_file  = open('data/'+title, 'w')
opened_file.write(description)
opened_file.close()

#Redirection
print("Location: index.py?id="+title)
print()
