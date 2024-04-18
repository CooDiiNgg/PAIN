import os
import sys
import time

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)

sys.path.append(parentdir)

from Server import pain

appInfo = {
    'active': True,
}


def getAppInfo():
    return appInfo


def getUsersInfo():
    pain.get_users.put(1)
    time.sleep(1)
    return pain.get_users.get()
    # return {
    #     'email': [
    #         { 'id': 1, 'username': 'example1@example.com', 'active': True, },
    #         { 'id': 2, 'username': 'example2@example.com', 'active': False, },
    #         { 'id': 3, 'username': 'example3@example.com', 'active': True, },
    #     ],
    # }


def activateMonitoring():
    appInfo['active'] = True
    print(f'Activate Monitoring')


def deactivateMonitoring():
    appInfo['active'] = False
    pain.end.put(1)
    print(f'Deactivate Monitoring')


def activateUser(mode, id):
    print(f'Activate User: {id}')


def deactivateUser(mode, id):
    print(f'Deactivate User: {id}')


def addUser(mode, username, password):
    print(mode, username, password)
    user = {"service": mode, "password": password, "email": username, "active": True}
    return None


def deleteUser(mode, id):
    print(f'Delete User: {id}')


def shutdownServer():
    pain.flag = False
    print('Shutdown Server')
