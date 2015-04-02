'''
Created on Oct 9, 2011

@author: Meredith
'''
grade = int(input('Test Score: '))
if grade >= 90:
    print('HAPPY DANCE!!!, Your Grade is an A!!')
elif grade >= 80:
    print('Almost there, Your Grade is a B')
elif grade >= 70:
    print('You can do better, Your Grade is a C')
elif grade >= 60:
    print(':O, Your Grade is a D')
else:
    print('MORE EFFORT, Your Grade is a F')