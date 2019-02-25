#!/usr/bin/env python3
# coding: utf8

import cgi
import html

form = cgi.FieldStorage()
field1 = form.getfirst("field1", "не задано")

field1 = html.escape(field1)



print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм</h1>")
print("<p>TEXT_1: {}</p>".format(field1))


print("""</body>
        </html>""")
