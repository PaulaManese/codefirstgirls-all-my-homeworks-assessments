import sys

users = ['user1', 'user2', 'user3', 'user4']

def valid_user():
    counter = 0
    while True:
        user = input('\nENTER USERNAME: ')
        user = user.lower()
        if user in users:
            if user == users[0]:
                n = 0
            elif user == users[1]:
                n = 1
            else:
                n = 2
            return n
        else:
            counter += 1
            print('****************')
            print('INVALID USERNAME')
            print('****************')
            if counter >= 3:
                sys.exit(999)

