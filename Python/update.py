#!Python
print("content-type: texthtml; charset=utf-8\n")

import cgi, os, view
'''
files = os.listdir('data')
listStr = ''
for item in files:
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form.getvalue('id')
    description = open('data/'+pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello, web'
'''

form = cgi.FieldStorage()
if 'id' in form:
    pageid = form.getvalue('id')
    description = open('data/'+pageid, 'r').read()
else:
    pageid = 'Welcome to the WEB!'
    description = 'Hello Web'

print('''<!doctype html>
<html>
<head>
  <title>ALL ABOUT WEB_welcome!</title>
  <meta charset="utf-8">
  <link rel="stylesheet" href="style.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src= "color.js"></script>
</head>
<body>
  <input id="Night_Day" type= "button" value ="Night" onclick="nightDayHandler(this);">
    <h1><a href="index.py">WEB</a></h1>
        <div id="grid">
        <ol>
        {listStr}
        </ol>
        <div id="article">
    <h2><a href = "create.py?id=">CREATE</a></h2>
    <form action = "process_update.py" method = "post">
        <input = type ="hidden" name = "pageid" value = "{form_default_title}">
        <p><input type = "text"  name = "title" placeholder = "title" value = "{form_default_title}"></p>
        <p><textarea rows = "4"  name = "description" placeholder = "description">{form_default_description}</textarea></p>
        <p><input type = "submit"></p>
    </form>
        </div>
        </div>
</body>
</html>
'''.format(title=pageid, desc=description, listStr=view.getList(), form_default_title=pageid, form_default_description=description))
