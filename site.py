import os, pickle, argparse
from bottle import route, run, template, static_file

parser = argparse.ArgumentParser(description='A bottle server for the HILT Institute')
parser.add_argument('-p','--port', type=int, help="The port number the server will run on")
args = parser.parse_args()

port = args.port if args.port else 8080

@route('/static/<filepath:path>')
def server_static(filepath):
    static_path = os.getcwd() + '/static/'
    return static_file(filepath, root=static_path)


@route('/')
def index():
    return template('templates/index.tpl')


@route('/staff')
@route('/staff/<name>')
def staff(name=None):
    staff_dict = pickle.load(open('data/staff_info.dat', 'rb'))

    if not name:
        return template('templates/staffdir.tpl')
    return template('templates/staffmember.tpl', name=name,
                    full_name=staff_dict[name]['full_name'],
                    position=staff_dict[name]['position'],
                    description=staff_dict[name]['description'])


run(host='0.0.0.0', port=port)
