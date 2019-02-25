#!/usr/bin/env python
from bottle import route, request, run, template # $ pip install bottle

temperature = None

@route('/')
def index():
    global temperature
    temperature = request.query.temperature or temperature
    return template('<b>Temperature: {{temperature}}</b>',
                    temperature=temperature)

run(host='192.168.0.198', port=8080)
