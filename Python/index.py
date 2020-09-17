#!C:\Users\66655\AppData\Local\Programs\Python\Python38-32\python.exe
print("content-type: texthtml; charset=utf-8\n")

import cgi, os

files = os.listdir('data')
listStr = ''
for item in files:
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()
if 'id' in form:
    pageid = form.getvalue('id')
    description = open('data/'+pageid, 'r').read()
    update_link = '<a href = "update.py?id={}">UPDATE</a>'.format(pageid)
    delete_action = '''
<form action = "process_delete.py" method = "post">
    <input type = "hidden" name = "pageid" value="{}">
    <input type  = "submit" value = "DELETE">
    '''.format(pageid)
else:
    pageid = 'Welcome to the WE!'
    description = 'Hello Web'
    update_link = ''
    delete_action = ''

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

    <p><h1><a href="index.py">WEB</a></h1></p>

        <div id="grid">
        <ol>
        {listStr}
        </ol>
    <a href = "create.py">CREATE</a>
    {update_link}
    {delete_action}
        <div id="article">

    <h2>{title}</h2>
        <p>{desc}</p>
        </div>
        </div>
</body>
</html>
'''.format(title=pageid, desc=description, listStr=listStr, update_link=update_link, delete_action=delete_action))
