#!/usr/bin/python3
""" Import request module """
import requests
from sys import argv


def userTodo():
    """ returns information about his/her TODO list progress. """
    api = "https://jsonplaceholder.typicode.com/"
    if (len(argv) > 1):
        id = int(argv[1])
        reqUser = requests.get('{}users/{:d}'.format(api, id)).json()
        reqTodo = requests.get('{}todos'.format(api)).json()
        filtered = list(filter(lambda x: x.get('userId') == id, reqTodo))
        todoComplete = list(filter(lambda x: x.get('completed'), filtered))

        name = reqUser.get('name')
        print('Employee {} is done with tasks({:d}/{:d}):'
              .format(name, len(todoComplete), len(filtered)))
        for i in todoComplete:
            print('\t {}'.format(i.get('title')))


if __name__ == "__main__":
    userTodo()
