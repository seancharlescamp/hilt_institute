import os
from bottle import route, run, template, static_file

@route('/static/<filepath:path>')
def server_static(filepath):
    static_path = os.getcwd() + '/static/'
    return static_file(filepath, root=static_path)

@route('/')
def index():
    return template('templates/layout.tpl')

run(host='0.0.0.0', port=8080, debug=True)
