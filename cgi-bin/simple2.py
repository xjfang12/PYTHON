#!D:\Python\Python37\python.exe

import cgi
form = cgi.FieldStorage()

name = form.getvalue('name','world')

print('Content-type: text/plain\n')

print('Hello, {}!'.format(name))