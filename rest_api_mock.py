from bottle import run, get, post, delete, request, default_app

guitars = [{'id': "0", 'name': 'Gibson', 'model': 'SG'},
           {'id': "1",'name': 'Gibson', 'model': 'Les Paul'},
           {'id': "2",'name': 'Schecter', 'model': 'C-7'},
           {'id': "3",'name': 'Ibanez', 'model': 'Iceman'}, ]

amplifiers = [{'id': "0", 'name': 'Orange', 'model': 'Tiny Terror'},
              {'id': "1", 'name': 'Marshall', 'model': 'JCM900'},
              {'id': "2", 'name': 'Mesa Boogie', 'model': 'Dual Rectifier'},
              {'id': "3", 'name': 'Yamaha', 'model': 'THR10'}, ]

rest_api_mock = default_app()  # for gunicorn server startup


@get('/get_guitars')
def get_guitars():
    return {'guitars': guitars}


@get('/get_amplifiers')
def get_amplifiers():
    return {'amplifiers': amplifiers}


@get('/get_guitar/<id>')
def get_guitar_by_id(id):
    the_guitar = [guitar for guitar in guitars if guitar['id'] == id]
    return {'guitar': the_guitar[0]}


@get('/get_amplifier/<id>')
def get_amplifier_by_id(id):
    the_amplifier = [amplifier for amplifier in amplifiers if amplifier['id'] == id]
    return {'amplifier': the_amplifier[0]}


@post('/add_guitar')
def add_guitar():
    new_guitar = {'id': request.json.get('id'),
                  'name': request.json.get('name'),
                  'model': request.json.get('model')}
    guitars.append(new_guitar)
    return {'guitars': guitars}


@post('/add_amplifier')
def add_amplifier():
    new_amplifier = {'id': request.json.get('id'),
                  'name': request.json.get('name'),
                  'model': request.json.get('model')}
    amplifiers.append(new_amplifier)
    return {'guitars': amplifiers}


@delete('/delete_guitar/<id>')
def delete_guitar_by_id(id):
    the_guitar = [guitar for guitar in guitars if guitar['id'] == id]
    guitars.remove(the_guitar[0])
    return {'guitars': guitars}


@delete('/delete_amplifier/<id>')
def delete_amplifier_by_id(id):
    the_amplifier = [amplifier for amplifier in amplifiers if amplifier['id'] == id]
    amplifiers.remove(the_amplifier[0])
    return {'guitars': amplifiers}


if __name__ == '__main__':
    run(host='192.168.1.1', port=8001)
