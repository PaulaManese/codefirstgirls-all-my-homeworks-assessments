users = ['user1', 'user2', 'user3', 'user4']
pins = ['1234', '4321', '0000', '1212']
amounts = [100, 200, 300]
count = 0


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
        break
    else:
        print('****************')
        print('INVALID USERNAME')
        print('****************')


while count < 3:
    print('******************')
    pin = input('PLEASE ENTER PIN NUMBER: ')
    print('******************')

    if pin.isdigit():
        if user == 'user1':
            if pin == pins[0]:
                break
            else:
                count += 1
                print('***********')
                print('INVALID PIN')
                print('***********')
                print()

        if user == 'user2':
            if pin == pins[1]:
                break
            else:
                count += 1
                print('***********')
                print('INVALID PIN')
                print('***********')
                print()

        if user == 'user3':
            if pin == pins[2]:
                break
            else:
                count += 1
                print('***********')
                print('INVALID PIN')
                print('***********')
                print()

        if user == 'user4':
            if pin == pins[2]:
                break
            else:
                 count += 1

                 print('***********')
                 print('INVALID PIN')
                 print('***********')
                 print()
    else:

        print('************************')
        print('PIN CONSISTS OF 4 DIGITS')
        print('************************')
        count += 1



    raise ValueError

    print('***********************************')
    print('3 UNSUCCESSFUL PIN ATTEMPTS, EXITING')
    print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
    print('***********************************')


    exit()