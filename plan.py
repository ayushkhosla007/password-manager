from hash_maker import password
import subprocess 
from database^script import store_passwords, find_users, find_password 

def menu():
    print('-'*30)
    print(('-'*13) + 'Menu'+ ('-' *13))
    print('1. Create new password')
    print('2. Find all sites and apps connected to an email')
    print('3. Find a password for a site or app')
    print('Q. Exit')
    print('-'*30)
    return input(': ')

def create():
   print('proivide the name of the site or app')
   app_name = input()
   print('provide a simple password: ')
   plaintext = input()
   passw = password(plaintext, app_name, 12)
   subprocess.run('xclip', universal_newlines=True, input=passw)
   print('-'*30)
   print('')
   print('Your password has now been created and copied to your clipboard')
   print('')
   print('-' *30)
   user_email = input('provide a user email')
   username = input('Please provide a username for this app or site (if applicable)')
   if username == None:
       username = ''
   url = input('paste the url')
   store_passwords(passw, user_email, username, url, app_name)

def find():
   print('Please proivide the name of the site or app you want to find the password to')
   app_name = input()
   find_password(app_name)

def find_accounts():
   print('Please proivide the email that you want to find accounts for')
   user_email = input() 
   find_users(user_email)
