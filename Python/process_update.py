#!Python

import cgi, os

form = cgi.FieldStorage()
pageid =form.getvalue("pageid")
title = form.getvalue("title")
description = form.getvalue("description")

opened_file  = open('data/'+pageid, 'w')
opened_file.write(description)
opened_file.close()

os.rename('data/'+pageid, 'data/'+title)
#Redirection
print("Location: index.py?id="+title)
print()
