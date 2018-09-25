import requests
import random

host = 'localhost'
port = '28080'
post = requests.post
names = {
    'firstnames':
             ['John', 'Alex', 'Joshua', 'Chandler', 'Joey', 'Rachel', 'Monica', 'Phoebe', 'Ross', 'Paul', 'George'],
    'lastnames': ['Johnson', 'Jordan', 'James', 'Curry', 'Jackson', 'Bing', 'Geller', 'Buffay', 'Green', 'Tribbiani']}


def generate(num):

    for n in range(num):
        firsname = random.choice(names['firstnames'])
        lastname = random.choice(names['lastnames'])
        post('http://' + host + ':' + port + '/rs/users/',
             headers={'Content-Type': 'application/json',
                      'firstName': firsname,
                      'lastName': lastname})
        print firsname, lastname


generate(100)