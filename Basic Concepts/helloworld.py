'''
Created on Oct 5, 2011

@author: Meredith
'''
first_name = input('Enter Your First Name: ')
last_name = input('Enter Your Last Name: ')
print('Hello ' + first_name + ' ' + last_name + ', I see you.')
namelen = len(first_name + last_name)
print('Your name has ' + str(namelen) + ' letters.')
if namelen > 8:
    print('Quite a long name you have there, very interesting.')
else:
    print('Your name does not contain that many letters, it is easy to type.')
    