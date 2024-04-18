appInfo = {
    'active': True,
}


def getAppInfo():
    return appInfo


def getUsersInfo():
    return {
        'email': [
            { 'id': 1, 'username': 'example1@example.com', 'active': True, },
            { 'id': 2, 'username': 'example2@example.com', 'active': False, },
            { 'id': 3, 'username': 'example3@example.com', 'active': True, },
        ],
    }


def activateMonitoring():
    appInfo['active'] = True
    print(f'Activate Monitoring')


def deactivateMonitoring():
    appInfo['active'] = False
    print(f'Deactivate Monitoring')


def activateUser(mode, id):
    print(f'Activate User: {id}')


def deactivateUser(mode, id):
    print(f'Deactivate User: {id}')


def addUser(mode, username, password):
    print(mode, username, password)


def deleteUser(mode, id):
    print(f'Delete User: {id}')
