
from secret import get_secret_key
from plan import plan, create, find, find_accounts


secret = get_secret_key()

passw = input('provide the master password: ')

if passw == secret:
    print('You\'re in')

else:
    print('no luck')
    exit() 

choice = menu()
while choice != 'Q':
    if choice == '1':
        create()
    if choice == '2':
        find_accounts()
    if choice == '3':
        find()
    else:
        choice = menu()
exit()
