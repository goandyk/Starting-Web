#!C:\Users\66655\AppData\Local\Programs\Python\Python38-32\python.exe
print("content-type:text/html; charset=UTF-8\n")

import cgi, os, view

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
<a href = "create.py">CREATE</a>
<form enctype="multipart/form-data" action="process_create.py" method="post">
    <p><input type = "text" name = "title" placeholder = "title"></p>
    <p><textarea rows = "4" name = "description" placeholder = "description"></textarea></p>
    <p><input type = "submit"></p>
</form>
  </div>
  </div>
  </body>
</html>
'''.format(title=pageid, desc=description, listStr=view.getList()))
