#!python
print("content-type:text/html; charset=UTF-8\n")

import cgi
import os
files = os.listdir('data')
listStr = ''
for item in files:
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()
if 'id' in form:
    pageid = form.getvalue("id")
    description = open('data/'+pageid).read()
else:
    pageid = 'Welcome to World Wide Web!'
    description = 'WWW and The Web redirect here. For other uses of WWW, seeWWW (disambiguation). For uses of web, see Web (disambiguation). For the first web software, see WorldWideWeb. Not to be confused with the Internet.'
print('''
<!doctype html>
<html>
<head>
  <title>ALL ABOUT WEB_welcome!</title>
  <meta charset="utf-8">
  <link rel="stylesheet" href="style.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="color.js"></script>

</head>

<body>
  <input type="button" value="NIGHT" onclick="
  night_dayHandller(this);
    ">
<h1><a href="index.py">WEB</a></h1>

<div id="grid">
  <ul>
    {listStr}
  </ul>
<div id="article">
<h2>{title}</h2>
<p>{desc}</p>
  </div>
  </div>
  </body>
</html>
'''.format(title=pageid, desc=description, listStr=listStr))
